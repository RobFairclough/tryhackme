# Red Primer: NMap

## Quiz (summarised)
help menu is accessed with flags -h, --help, or man nmap
stealth/syn scan flag is -sS
udp scan flag is -sU
os detection flag is -O
service version detection is -sV
default verbosity -v, very verbose -vv
output in xml = -oX
aggressive scan -A
max timing -T5
specific port -p, all ports -p-
use scripts with ==script= e.g. ==script=vuln
to prevent host pinging, -pN

## Scan 
syn scan:
sudo nmap -sS -vv -oG synscan.txt 10.10.66.40
aggressive scan:
sudo nmap -A -vv -oG aggressivescan.txt 10.10.66.40
vulnerability scan:
sudo nmap --script=vuln -vv -oG scriptscan.txt 10.10.66.40

