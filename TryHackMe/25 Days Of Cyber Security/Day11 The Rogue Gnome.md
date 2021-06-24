# Day11

## The Rogue Gnome

Deploy your machine and read through the provided information, then let’s move on to the questions!

The first two questions can be found in the information provided and you can answer them easily.

Then we'll ***SSH*** into the box with the provided credentials:

`ssh cmnatic@10.10.55.73` 

On the first connect, you will have to confirm the servers fingerprint.

Then with `find / -perm -u=s -type f 2>/dev/null`  we'll search for binaries that have the ***SUID bit set*** which ***means that they can be executed with the permission of a different user.***

![55](https://user-images.githubusercontent.com/83836972/122553371-354d7b80-d055-11eb-9a43-e83db925c4c7.PNG)

***/bin/bash*** seems to be a very important one. So let's just go check the permissions of that:

`ls -la /bin/bash`

With what we've got as an output, it seems as if it ***can be just run as root***, so:

`bash -p`

This will ***escalate the priveledges to root***, then all that is left is to get the ***root flag***:

`cat /root/flag.txt`

![56](https://user-images.githubusercontent.com/83836972/122553389-3b435c80-d055-11eb-8399-e20eeb63a026.PNG)

And we're done for the day!

