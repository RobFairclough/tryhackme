# Crack the hash
## level 1
### 1 - 48bb6e862e54f2a795ffc4e541caed4d
Top results for hashid are MD2, MD5
Trying MD5 first
MD5 hashcat num is 0, output to found1.txt, use oneruletorulethemall, input hash1.hash, using rockyou.txt as wordlist
`hashcat --force -m 0 -o found1.txt -r {pathtorule} hash1.hash {pathtowordlist}`
found th eresult pretty quick, 'easy'

### 2 - CBFDAC6008F9CAB4083784CBD1874F76618D2A97
Top results for hashid: SHA-1, double SHA-1
let's go with SHA-1
same command as above, swapping found/hash1 for 2 and -m 0 for -m 100, the sha-1 code
found almost immediately - 'password123'

### 3 - 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
Top results fo rhashid - Snefru-256, SHA-256
No result for man hashcat | grep snefru, so gonna try sha-256 before I jump in that rabbit hole.
sha-256 num is 1410 for $pass.$salt, 1420 for $salt.$pass
can't see a seperator for pass/salt
using grep for this is a pain for case sensitive / hyphen seperated. 
Either learn grep or manually look for your hash type.
1400 is the SHA256 num.
Cracked almost imedaitely again (11.06ms) - guessing they're pretty high up on the wordlist
'letmein'

### 4 - $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
top results: blowfish, woltlab burning board, bcrypt
Going to try the one i've actually heard of before, bcrypt
bcrypt code 3200
taking the rule off this one since it was estimated at 800 years.
still estimated at 6 days.. might see how the pc gpu handles this
needs drivers etc. I'm not gonna set this up, doubtful that the challenge intends me to use a powerful gpu to crack it.
i'm gonna make a filtered rockyou with only words under 5 chars (pattern on the answer box)
cracked pretty fast with a list of only 21k instead of 14million
`hashcat --force -m 3200 -o found4.txt hash4.hash  /usr/share/wordlists/rockyouunder5.txt`
'bleh'

### 5 - 279412f945939ba78ce0758d3fd83daa
top result suggests md2, md5 or md4 - probably not md5 so let's try md2
md2 doesn't seem to be an option in hashcat, i'll try md4
didn't crack without the rule list, cracked very quickly with
'Eternity22'
hashcat --force -m 900 -r ../../tools/password_cracking_rules/OneRuleToRuleThemAll.rule -o found5.txt hash5.hash /usr/share/wordlists/rockyou.txt

## level 2

### 1 - F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85
top results in hashid - snefru and SHA-256
sha 256 cracks very fast
'paule'

### 2 - 1DFECA0C002AE40B8619ECF94819CC1B
hashid : md2,md5,md4 - hint says it's an NTLM, which was way near the bottom of the list lol
md5: exhausted
md4: exhausted 
ntlm: cracked in 0.22ms
'n63umy8lkf4i' - what the hell is this

### 3 - $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02 :aReallyHardSalt
sha512 from the $6$. this took me a long trime from not pasting the . in there
can I plug the salt/rounds in? apparently $rounds=5 after the signature does it?
that came out as exhausted
estimated at 1h20 - probably want a gpu to do this, might set up a non-live kali machine on my desktop..
cracked in about 17.5mins
'waka99'

### 4 - e5d8870e5bdd26602cab8dbe07a942c8669e56d6 salt: tryhackme
hashid: sha-1
has a salt, so based on the results of man hashcat | grep SHA, assuming 160:
HMAC-SHA1 (key = $salt)
hashfile like hash:salt
`hashcat --force -m 160 -o found9.txt hash9.hash /usr/share/wordlists/rockyou.txt`
'481616481616'


