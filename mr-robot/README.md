#Mr Robot

#1	
What is key 1?

Found in /robots.txt
    User-agent: *
    fsocity.dic
    key-1-of-3.txt

fsocity.dic leads to a large wordlist which i downloaded to directory.

The flag was found by simply going to IP/key-1-of-3.txt. It took me way to long to figure this out and I swear it didn't work the first time I tried.

'''
073403c8a58a1f80d943455fb30724b9
'''


#2	
What is key 2?

Ran a nikto scan that gave me mostly nothing. Tossed about some uncommon headers and found robots.txt again. 

Nikto seemed to kill the box every time I ran it, so that is a no go unfortunately.

Running gobuster worked for a while but also seems to kill the box. 

Going to /dashboard brings us to a wordpress login page within the domain.

Running any type of enumeration on it just crashes the box so I went ahead and looked up something to get me past this part. I had previously found the WP login page which is where we need to go.

I decided to take my first dive into Hydra to try and crack this. May try to create a Python script to do the same some other time.

Hydra came back with the Username: Elliot and password:GNU. However the password was not correct.

The correct password is ER28-0652 found in a write-up in case Hydra doesn't come back correct a second time. Hydra did not pull the correct password after multiple attempts.

We then find ourselves at a wordpress landing page. We need to get a reverse shell going now, so I copy my reverse shell to the directory, change the ip to mine and setup netcat to listen on the given port.

We then have to copy our reverse shell script into the website itself. From the walkthrough we can do this by using a file called archive.php in the theme editor. We simply replace that code with our reverse shell and then visit the page while our netcat is listening and we get a shell.

I cannot find a good way to stabilize the shell unfortunately so I'm working on a very rudimentary shell. I CD into the home/robot folder and find key #2. Except I am not allowed access to it. I need to find a way into the robot user first.

The same folder has a password.raw-md5 file which we can read. I simply copy the hash and use crackstation.net to get the password for robot.

User:robot
Password: abcdefghijklmnopqrstuvwxyz

To switch users I need to find a way to spawn a shell. I couldn't get the python shell command to work until I ran it in the root folder instead of in the robot users folder. This allows me to run su robot and provide the password above. I can now cat out flag2

'''
822c73956184f694993bede3eb39f959
'''


#3	
What is key 3?


Now I need to escalate my priveleges to that of root to find the final flag. I will do this by first searching to see if I have any SUID binaries I can abuse.

I do so using this command: find / -perm -u=s -type f 2>/dev/null

I find a few SUID binary's using this. The one that stood out (was also in the hint) was /usr/local/bin/nmap.

I went to GTFObins to see how we could attack this. I first attempted to run the limited SUID code, but that proved ineffective. Because it has a setuid allowing nmap to run as root we may be able to use the interactive mode if we have an older version. Checking nmap - version did indeed show us that we were in version 3.81 which is the correct set of versions to do this.

We simply run nmap --interactive and follow that with !sh. Doing that gives us root. 

I can then cd to /root and cat out the final key!!

'''
04787ddef27c3dee1ee161b21670b4e4
'''
