# Gaming Server

We start as always by running some enumeration. So I ran a quick rustscan and found out that we have 2 ports open. Port 22 for ssh and port 80.

Since we have a webserver I go and check it out. It contains some links that we can go to and one of them leads to an upload page that gives us a dictionary list as well as the hacker manifesto and a meme.

I downloaded this dict list as it looked like a possible password list. I also checked the source code of the main page and found a comment that gave me a possible username

```
john
```

I ran a gobuster scan after I hit a wall with no way to login or anything. It found a /secret page. When I visit this page we find a private RSA Key. Presumably for the user john.