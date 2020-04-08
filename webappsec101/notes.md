# WebApp Security 101 - tryhackme

Encountering a lot of disconnects and general trouble with this machine.

## Task 2 - walking through the application
All of these answers found by visiting the ip in browser, looking at response headers
### What version of apache is being used?
2.4.7 (server header)
### What language was used to create the website?
php (x-powered-by)
### What version of this language is being used?
5.5.9 (x-powered-by)

## Task 3 - Establishing a methodology
just reading here, might summarise later idk

## Task 4 - Authentication
Fairly basic auth
### What is the admin username?
let's make a guess: admin 
### What is the admin password? 
hmmm, admin?
### What is the name of the cookie that can be manipulated?
Used the network tab, checked out the cookies and found a session one with a few nice things we can change
### What is the username of a logged on user?
Hint for this was a link to a list of names, so I'm assuming there was some enumeration to be done here.
I solved by using the sample user page and cycling through ids. May revisit after
### What is the corresponding password to the username?
Swing in the dark and used the same password here

## Task 5 - Cross Site Scripting (XSS)
Learned most of this in the juiceshop challenge 
### Test for XSS on the search bar
plugged in <iframe src="javascript:alert`xss`"> as my standard example.
This becomes a query string that is executed on page load, w/potential for redirect, stealing data or making requests with the user's auth
### Test for XSS on the guestbook page
Same attack, but persisted here so any user visiting the guestbook would receive my alert. 
Much more dangerous as there's no telltale query string for this one.
### Test for XSS behind the flash form on the home page
Can't see a flash form here with firefox and chromiom just shows this plugin is not supported.
Don't want to jump throughb hoops for this so skipping it.

## Task 6 - Injection
### Perform command injection on the check password field
The passcheck runs a command (and tell us about it) to exploit this we can pipe into any command of our choice.
in this case we don't seem to receive a response so can't return data, but potentially could add a user to the system, remove files
x | chmod /etc/passwd 777 # seems to have broken the site completely
x | rm -rf ~/ # should wipe the whole site from the server
potential to use curl to send files to a remote server? hijack the server's resource for mining? other nefarious purposes?
give ourselves a shell into the machine maybe? this would be a fun avenue to check out
### Check for sqli on the application
Couple of vulnerabilities here:
registration -> similar usernames, using 1' or 1=1 #-- as all fields seems to list out all users.
Login: same vulnerability above logs us in as a sample user, 1' OR {username col name} = {username}
would log us in as anyone, couldn't seem to crack the username column name with a few guesses but enumerating this would get it.

## Task 7 - Miscellaneous and logic flaws
### Find a parameter manipulation vulnerability
We used this to find bryce, the sample user with ?id={id} combined with sequential ids allowed us to check out every user.

### Find a directory traversal vulnerability
Had to look for some help with this one - was just trying to exploit the url bar.
File upload is vulnerable to this via the tag function - we can upload a file to replace existing files on the server.
This means we can, for example, use the path to the index, ../index.php and replace it with our own hostile index.php to phish/watering hole attack users.

### Find a forceful browsing vulnerability
Hint was 'try to access a restricted image' 
We were able to do this just by going through steps to purchase, where we're given the high quality link before we actually pay.
Also ran a dirbuster to find other paths, which seems to find all the file directories and via the /upload directory we can view any image in high quality. 

### Logic flaw: try to get an item for free
options for a logic attack - set our own price? reduce price of item? discount codes?
hint tells us to use discount codes so let's try that first
After the dirbuster scan, came across the /calendar route, which on a few days showed a discount code:
SUPERYOU21 
going to the checkout and using this code we find that we can just add it again and again.
as a result, we can just spam the http request for adding that coupon. After a certain number the request was 'blocked' maybe ddos protection?
So we've not got it free, but down to 0.4639... down from 15

