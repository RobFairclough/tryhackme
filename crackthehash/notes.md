# Crack the hash

## 1 - 48bb6e862e54f2a795ffc4e541caed4d
Top results for hashid are MD2, MD5
Trying MD5 first
MD5 hashcat num is 0, output to found1.txt, use oneruletorulethemall, input hash1.hash, using rockyou.txt as wordlist
`hashcat --force -m 0 -o found1.txt -r {pathtorule} hash1.hash {pathtowordlist}`
found th eresult pretty quick, 'easy'

## 2 - CBFDAC6008F9CAB4083784CBD1874F76618D2A97
Top results for hashid: SHA-1, double SHA-1
let's go with SHA-1
same command as above, swapping found/hash1 for 2 and -m 0 for -m 100, the sha-1 code
found almost immediately - 'password123'

## 3 - 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
Top results fo rhashid - Snefru-256, SHA-256
No result for man hashcat | grep snefru, so gonna try sha-256 before I jump in that rabbit hole.
sha-256 num is 1410 for $pass.$salt, 1420 for $salt.$pass
can't see a seperator for pass/salt
using grep for this is a pain for case sensitive / hyphen seperated. 
Either learn grep or manually look for your hash type.
1400 is the SHA256 num.
Cracked almost imedaitely again (11.06ms) - guessing they're pretty high up on the wordlist
'letmein'

## 4 - $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
top results: blowfish, woltlab burning board, bcrypt
Going to try the one i've actually heard of before, bcrypt
bcrypt code 3200
taking the rule off this one since it was estimated at 800 years.
still estimated at 6 days.. might see how the pc gpu handles this

