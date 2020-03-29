# OWASP Juice Shop

## Initial Website Recon
Features: 
- Shopping Cart
- User accounts
- register
- login
- forgot password
- 'remember me'
- search
- contact us - anonymous allowed but (self implemented?) captcha 
- terms of use markdown file in /about
- social links inc. slack
- images in customer feedback
- language select
- modals for products with review submissions
- track order
- recycle
- transactions


## Potential attack vectors
- Review on apple juice shows 'admin@juice-sh.op' email address. Login potential
- Review on banana juice shows 'bender@juice-sh.op' email
- Review on green smoothie shows 'jim@juice-sh.op' email
- Review on temp tattoos shows 'mc.safesearch@juice-sh.op'
probably more too
- Registration / login injection
- no validation & anonymousallowed on review submission
- forgot password: get request on type, searches email and shows reset question when one is recognised.
- security questions sent down with id, injection potential for getting someone's reset question
 (nevermind, question id is for security question as shown in registration)
- all http
- sequential ids
- Gravatar for getting email hash
- file uploader in user profile
- creating an order leads us to /ftp/order_{guid} - potential ftp vulnerability
- /ftp folder is accessible - only .pdf/.md files are viewable directly


## Notes:
- Looks like security answers are hashed. quinn -> a628f3b93f22e452926704af1810cfd8d65812b1cdf80992d39a31fc775a28e9
- whoami requests on either side of login - token confirmation? decode jwt and check
- hashed password are stored in jwt, as is isAdmin flag & lastloginip

## How is the site built?
- 'X-Powered-By: Express' - node/express server
  visit page /rest identifies version ~4.16.4
- /rest page shows file structure, /home/ubuntu/juice0shop - shows we're on a linux ubuntu server
- 'ng-version: 7.1.1' - Angular app version 7.1.1
- 4 scripts loaded in, runtime.js, polyfills.js, vendor.js, main.js
Angular v7.1.1 / Express v~4.16.4
 

### Logging in as administrator using SQL Injection
Found email address higher up, let's use that differently.
At login - 
email: "x' OR Email='admin@juice-sh.op' AND 1=1; --"
Using email to specify which user we successfully log in as, semi colon to end statement and -- to comment out the rest of the sql regarding password etc.

### Logging in as Jim using Forgot Password mechanism
again, email was found in recon: jim@juice-sh.op
Gonna try a word list with burp 
hint: 'try to look for more information on jim'
clues show that it's jim from Star Trek (had to cheat here, hadn't assumed the users would be fictional characters)
james kirk's cousin's middle name is Samuel

### What is the administrator password? 
hint is 'sometimes admins use very easy and common passwords - do you think you can guess any of them?'
Using the rockyou-20 wordlist from a previous task, going to try to bruteforce the login.
While that's running, jwt contains the hashed password - 0192023a7bbd73250516f069df18b500
A hash analyser suggests the password is md5. A rainbow table might solve this.
Crackstation's wordlist gives us a positive match - password is admin123
Cancelling the bruteforce, our rockyou-20 shortened wordlist wouldn't have cracked it, but the full rockyou.txt would have.

## Sensitive data exposure

### Protecting sensitive data. We're looking for a markdown file after we 'access a confidential document'
Could be in our /ftp folder we found during initial recon?
acquisitions.md looks pretty confidential!
noice

## Broken Access Control

### Access the administration section of the store
First off, we're just getting the name of the page. Hint tells us to look in the custom js
There's a file in there called 'administration' (who could've guessed) - how we get to this page is another story
No it isn't, it is just /administration. Thought this was gonna be trickier but I'd just misspelled it
This area shows us recycling requests, which could've helped us identify our captain kirk earlier.
Also lists out users and comments.
Can we access this as a non-admin? We can!

### Access someone else's basket
Looking at how the baskets are identified/stored, it looks as though we're using a GET on a basket id of 4 to get our basket.
Also looks like we're using a locally stored session variable to send up our basket id of 4. 
Can we switch this to get their basket? YEP switching to 3 shows us someone else's basket of lemon juice


### Get rid of all 5 star feedback
This seemed to be as simple as just deleting the feedback from the admin section. rip high avg feedbak
looking at the hint, they tell us to do exactly that.

## Cross Site Scripting
Should be interesting, never looked into this before now but used js a lot

### Carry out reflected XSS using Tracking Orders
Hint says 'what about using the iframe tag?'

### Carry out XSS using the Search Field

