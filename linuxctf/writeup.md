# LinuxCTF

## Task 1 - Linux Challenges Introductions

### 1:
- Getting your machine deployed
- Getting yourself connected and logged in as garry
- Find out how many files are visible in garry's home directory

This task just ensures everything is set up correctly. 
Ensure you're connected via  vpn (through the access page), then ssh in.

`ssh -l garry <ip address>`
The -l flag indicates login name. `man ssh`
After this, enter the password 'letmein' and you should connect.
You're already in the home directory, so you can just use `ls` to list the contents, and count the files.
An alternative for the lazy or counting-impaired:
`ls | wc -w`
This will list the contents, then pipe the result directly into linux's wordcount. The -w flag only lists the words, instead of lines, words and characters.
Type in your result and you're done, challenge 1 complete.


## Task 2 - The Basics

### 1:
'What is flag 1?'
As you already saw when listing files, one of these was called flag1.txt,
we need to read this file to get the flag. You can use whatever reader or command you like to accomplish this, for example:
`cat flag1.txt`
This will show you the contents of the file, where you'll find a flag, and account credentials for another account, bob.

### 2: 
'Log into bob's account using the credentials shown in fla 1. What is flag 2?'
We've got the account credentials above, so we just need to switch to that user.
You can accomplish this by exiting your ssh and logging in again, or `su bob`
input the password, then use `cd` to get back to bob's home directory and repeat steps for flag 1.

### 3:
'Flag 3 is located where bob's bash history gets stored.'
Our bash history is just a list of commands we've executed (in bash, naturaly.)
This history is stored in a hidden, .bash_history file in the home directory. To find it, we would need to use `ls -a` to list all files.
We can either view that file, with `cat .bash_history` or just use the `history` command. The top command in either case, is our flag 3.

### 4: 
'Flag 4 is located where cron jobs are created.'
Cron jobs are a way of automating tasks on a machine. 
Haven't used these much, so googling cron jobs on linux leads me to a howto guide on crontab. 
I see that using `crontab -e` lets me edit the crontab file. 
Using this command, I find that bottom line on the file contains my flag4.

### 5:
'Find and retrieve flag 5.'
The wording makes me think we're using the 'find' command, and the hint confirms this.
Using `man find` I figure I can use find the -n flag to search by name.
`find / -name "flag5*"`
This command searches for our flag5 with a wildcard end for the extension, but fills our terminal with permission denied messages for areas we don't really care about.
Googling this shows me we can instead use:
`find / -name "flag5* -print 2>/dev/null"`
This will redirect stderr to /dev/null, so we don't have to see the error messages.
Now we're left with just the path to our flag5.txt file, `cat` it and we move on.

### 6:
'"Grep" through flag 6 and find the flag. The first 2 characters  of the flag is c9.'
We can use above find command to track down flag6, in the home directory.
Reading the file shows it's tons of lorem ipsum text so we'll need a more targetted search.
Using grep on the file, we can search for the text we want, in this case c9. `man grep` or `grep --help` to look up the syntax, and 
`grep c9 /home/flag6.txt` highlights the beginning of our flag.

### 7:
'Look at the systems processes. What is flag 7.'
we can use `ps` to list system processes. Using the -e flag to list every process, and the -f flag to show full format listing we can see all processes, with all info.
So `ps -ef` gives us a list. Our flag7 is in there but if we're feeling lazy (we are):
We can pipe the result into a grep: `ps -ef | grep flag7`.

### 8:
'De-compress and get flag 8.'
If we `cd` back to bob's home directory and `ls` (`cd && ls` if ya nasty) we see that flag8 is in a .tar.gz file.
We can't read this with cat, as it's compressed.
`tar` is the utility for decompressing this file, so `man tar` to look up our syntax.
We can use the -x (or --extract/--get if we were writing a nicer script) to extract, and -f to specify our file.
`tar -xf flag8.txt` then `cat flag8.txt`. Not necessary, but I decided to rm this file afterwards, to feel more sneaky. `rm flag8.txt`.

### 9:
'By look in your hosts file, locate and retrieve flag 9.'
The hosts file is in /etc/. We want to find our flag in here, so `cat /etc/hosts`.
The entry for 127.0.0.1 (our ipv4 loopback/localhost) is what looks suspiciously like a flag.com. 

### 10:
'Find all other uses on the system. What is flag 10.'
We can find a list of all users in /etc/passwd. 
Using `cat /etc/passwd` to read this file and looking through the list (sadly not greppable as the entry is just a flag, and we have to visually find it ¬_¬)
We find our flag, and we move on, finishing task 2.

## Task 3 - Linux Functionality
Note: don't be confused by the task introducing you to our user alice, we're not using that account just yet.
### 1:
'Run the command flag11. Locate where your command alias are stored and get flag11.'
`flag11` Not the most helpful command, we don't really learn anything that wasn't in the clue.
Where are command aliases created for bash? .bashrc, in the user's home directory.
We can manually read this file and track down our alias, or we can grep it.
`grep flag11 .bashrc` shows us our command alias, and a commented out flag.

### 2:
'Flag12 is located where MOTD's are usually found on an ubuntu OS. What is flag12?'
I used locate for this one, `locate motd` pointed me to /etc/update-motd.d 
In this folder were a few files, I read the first one, and find the flag at the bottom.

### 3:
'Find the difference between two script files to find flag 13'
diff is the tool for finding the difference between two files, so we'll use that.
`locate flag13` shows us that these scripts are in a folder inside bob's home directory.
We'll cd into that folder, and diff the files. `cd /home/bob/flag13`, then:
`diff script1 script2` shows us a flag in one file, but not the other.

### 4:
'Where on the file system are logs usually stored? Find flag 14'
logs are often stored in /var/log. We'll go here, and `ls` the files.
We can now see the craftily named 'flagtourteen.txt' - guess this would stop us from seaching for it.
If we read this file, we see the final line is a flag.

### 5:
'Can you find information about the system, such as the kernel version etc'
My first instinct here is to use `uname` so I use `man uname`, find the -a/--all flag shoud list all informtation, and try that.
Using that, doesn't seem to be a flag in there. 
Googling suggests we can find system info in /proc/version, but reading this doesn't seem  to show a flag.
`lshw` lists hardware, but also doesn't seem to have a flag.
Some further research finds a program lsb-release, which lists system info. but using `lsb_release -a` doesn't seem to show a flag.
After cheating and looking at a walkthrough, it appears that the flag is within the file /etc/lsb-release.
I'm not sure if I was misusing the command for lsb-release, or it was setup incorrectly. Either way, `cat /etc/lsb-release` finds our flag15

### 6:
'Flag 16 lies within another system mount'
From a stackoverflow answer, I find that /media is 'for the system to mount its stuff'. Lets check that dir out.
`ls /media` shows us 1 folder, 'f'. I've got an idea where this is heading, so lets `ls /media/` and let tab completion show us where it ends.
Looks like at the end of the tabs, is our flag.

### 7:
'Log in to Alice's account using her private key and get flag 17'
The notes at the top tell us Alice's private key doesn't work, so lets just `su alice` and use the password provided.
We find flag17 in her home dir, so `cat` that and let's move on.

### 8:
'Find the hidden flag 18'
Let's take a wild leap and assume flag 18  is a hidden file. `ls -a` will list files, including hidden ones.
so `ls -a` and wouldn't you know it, .flag18 - `cat .flag18` and onwards

### 9:
'Read the 2345th line of the file that contains flag 19'
If we `cat flag19` we'll see it's a long file which we don't want to manually comb through.
We can list the top x lines of a file using head, and the bottom y lines using tail. Let's pipe this up.
`cat flag19  | head -2345 | tail -1` finds us our key, completing task 3. Congrats.

## Task 4 - Data Representation, Strings and Permissions 

### 1:
'Find and retrieve flag 20'
Again, looks like a find one.
`locate flag20` shows that it's actually just in alice's home dir, so let's `cat flag20`.
Doesn't seem to work, and there's a distinct '=' at the end, despite all the other flags being alphanumerics only.
The hint gives it away, the flag is base64 encoded. Let's decode and solve. `man base64` shows us the syntax for decode, so
`base64 -d flag20` gives us our flag.

### 2:
'Inspect the flag21.php file. Find the flag.'
`locate flag21.php` shows us this file is in bob's home dir, lets check it out.
`cat /home/bob/flag21.php` gives us a clue, that there's more to it than we think.
`man more` tells us that `less` actually gives more emulation plus enhancements. `more flag21.php` doesn't seem to give us any more. (without delving into the options) let's try less.
`less flag21.php` shows us our shortest flag yet, and a little praise.

### 3:
'Locate and read flag22. It's represented as hex.'
`locate flag22` shows us this flag is in alice's home dir, lets read it. Unsurprisingly, this appears to be in hex representation.
We can use xxd to decode this, so `man xxd`
From this, it looks like -r/-revert will reverse the operation. `xxd -r flag22` gives us our decoded flag. Hooray

### 4:
'Locate, read and reverse flag 23'
Seems easy enough, just need to reverse it. We could manually type this in after a `cat` but let's obviously not.
rev is a utility which serves this exact purpose, so let's use it. `rev flag23` gives us our reversed and correct flag.

### 5: 
'Analyse the flag 24 compiled C program. Find a command that might reveal human readable strings when looking in the source code.'
The compiled flag 24 program is naturally not human readable, but there's a nice command that can find strings within a compiled file, aptly named 'strings'.
`locate flag24` shows us it's in garry's home directory. let's go there and run 
`strings flag24` will show us our compiled flag.

### 6: 

 

