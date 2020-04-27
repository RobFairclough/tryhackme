# Pickle Rick
This Rick and Morty themed challenge requires you to exploit a webserver to find 3 ingredients that will help Rick make his potion to transform himself back into a human from a pickle.

## Credentials
Username: R1ckRul3s
Password: Wubbalubbadubdub

decoded base64 comment: 'rabbit hole'
Sup3rS3cretPickl3Ingred.txt: 'mr. meeseeks hair'
clue.txt: 'look around the file system for the other ingredient'
second ingredients: '1 jerry tear'
3rd.txt: '3rd ingredients: fleeb juice'

machine username: rick

machine username: ubuntu

## Recon
Visiting the webpage on the ip shows this text:
'Listen Morty... I need your help, I've turned myself into a pickle again and this time I can't change back!

I need you to *BURRRP*....Morty, logon to my computer and find the last three secret ingredients to finish my pickle-reverse potion. The only problem is, I have no idea what the *BURRRRRRRRP*, password was! Help Morty, Help!'

Html inspector shows this:
'

    Note to self, remember username!

    Username: R1ckRul3s
'
### Nmap
2 open ports, 22 and 80 - SSH and HTTP
### GoBuster
/assets accessible, can't see anything of use just images, bootstrap and jquery
/server-status - exists but forbidden
### Dirbuster
doing better here - maybe because of a better list? maybe because it default checked php extensions

/login.php - bruteforce opportunity? we have username already
/assets - nothing of use
/portal.php - redirect to login
/icons/ - forbidden?
/denied.php - redirect to login

worth adding multiple extensions here?
added robots to my dirbuster-common wordlist as I was able to manually visit, but dirbuster didn't find.

### Hydra
No success

### Robots.txt
shows only 'Wubbalubbadubdub' instead of usual content. Potential password?
yep!

## Exploring inside
We have a command panel, and a bunch of links that just lead to denied.php 
Html inspector has a comment with this:
'Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0=='
looks like base64
couldn't get the base64 cli to decode this properly so probably need to look into that, using an online base64 decoder
decoding seemed to give us another base64 string so followed this trail down to:
'rabbit hole' - potential flag? or just an easter egg? maybe a command?
doesn't match the pattern for any of the 'ingredient' flags
doesn't seem to have an effect in command panel, nor does inputting the base64

used `echo hi` into the command panel and the result shows, so looks like it's a shell
`echo $SHELL` has no result
`ls` shows a few files, interesting ones:
- Sup3rS3cretPickl3Ingred.txt
- clue.txt

`whoami` shows 'www-data' - we're not root
`cd home && ls` shows we have at least two other users: rick and ubuntu
`cd /home/rick && ls` shows a second ingredient file, but
`cat /home/rick/second ingredients` shows:
'command isabled to make it hard for future pickle rick - no other visible clues
`cp` the file and read that doesn't work either, doesn't seem to move the file where i want it either.
seems that the `cat` command in general is disabled now? same with head/tail
think that was disabled before too, but got the flag by visiting the file..
awk isn't disabled, so
`awk '{ print $0}' /home/rick/second\ ingredients` gets us: 1 jerry tear

`sudo -l` shows:
'Matching Defaults entries for www-data on ip-10-10-155-211.eu-west-1.compute.internal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-10-10-155-211.eu-west-1.compute.internal:
    (ALL) NOPASSWD: ALL
'

nopasswd: all looks very nice, means we can sudo anything 
 including the /home/ubuntu/.ssh dir
how to use this though? maybe not important
`sudo ls -al /root` shows there's a text file in there called 3rd.txt
`sudo awk '{ print$0}' /root/3rd.txt` shows : '3rd ingredients: fleeb juice'


## summary
a little manual investigatino to find username,
 dirbuster to find robots.txt for the password
some linux commands to get the rest
