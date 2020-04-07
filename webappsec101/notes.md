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
Can't see a flash form here with firefox



