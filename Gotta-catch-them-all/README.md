# Gotta catch em all!

Machine IP = 10.10.125.57

THM IP = 10.2.38.112

This room is based around finding flags but it's essentially like catching pokemon! How awesome!

I will start as always with a simple rustscan to see any open ports and also enumerate some of the versions etc.

*insert rustscan and rustscan-command*

We immediately find that there are 2 ports open. SSH on port 22 and a webserver on 80. 

When we check the website ip we are given the stock Apache2 welcome page.

*insert welcome page*

Now that we know there is a webpage I will go ahead and run a gobuster to see if I can find any hidden directories.

*insert gobuster command*

While waiting on gobuster I will also do some simple enumerations myself such as checking for robots.txt. Sadly gobuster never comes back with anything so I continue doing manual enumeration.

After finding nothing I finally find a small nugget to go on after checking the source code. At the bottom of the page is a comment and also something that looks like a possible username:password combo.

*insert source comment*

I will look at the console first before we test out our possible username and password on the ssh port.

We are greeted with this message when we reload the page with the console open. Sadly this doesn't give us the full flag quite yet but if you know your pokemon you simply need to find the beginning of the flag.

*insert console*

This gives us our first flag. I will not be putting the flags here as I don't want to give away the answers for free. I was also only able to get the flag here because THM has the flag format in the answer box. So i was able to see what it should look like. I probably shouldn't have gotten it but it worked.

Now we will attempt to ssh into the box with the username:password combo that we found.

*insert ssh.png*

This gets us into the box. I run an id and whoami command immediately to see what I might be able to see.

*insert commands.png*

I also manually go through the file system and see if I can find anything. I always see if i'm able to see /etc/passwd and /etc/shadow when I get access to a machine. Going through I find a file on ~/Desktop.

*insert desktop.png*

Since it's a zip file we have to unzip it. Doing so gives us a new folder with a text file inside. 

*insert flag1.png*

This flag is in a hex format so I simply copy and paste it into a hex to ascii converter. It spits out the flag that I had already figured out from before unfortunately.

After some more manual enumeration I finally find a set of folders inside pokemons Video folder. We find a .cplusplus file inside of them with another set of credentials.

*insert Videos.png*

This is what we find after logging into the ash user and running a couple of commands. 

*insert ash.png*

We can run everything as sudo!! That is very good for us!

First I check the home folder and find roots favorite pokemon!

*insert roots pokemon*

After that I decided to run a simple find command to find both the final flags.

*insert fire.png*

*insert firetxt.png*

I then cat out the file and find that is is a base64 encoded string. I simply paste that into a terminal and pipe it to base64 -d to find the flag.

The final flag was found in the same way, but by passing water instead of fire to the find command. This string was found to be what looked like a rot13, but when you use rot13 on it you still get nothing.

*insert rot13.png*

I decided to toss it into a website called Cyber Chef and play with the rot settings to see if it was a different rotation encoding. Turns out it was the first one that I tried, rot14. That is the final flag of this room! 

Congratulations!