# Day10

## Don't be sElfish!

Deploy the machine and read the dossier. Then let’s start answering the questions!

We'll start this challenge by running ***enum4linux*** on the machine!

`enum4linux -a 10.10.237.138`

First and second question can be easily answered by the result of this command:


![52](https://user-images.githubusercontent.com/83836972/122341831-89773380-cf61-11eb-8102-2b3dbb3d9955.PNG)

![53](https://user-images.githubusercontent.com/83836972/122341895-9d229a00-cf61-11eb-9a12-ca03e3d68cf0.PNG)

Next, let’s try to connect to the share. 

**One of them doesn’t require a password.**

So we'll try logging in using all of them and press enter for the password, the one which allows this is meant for the further working!

For logging in, the command is:
`smbclient //<machine_ip>/<share_name>`

For my CTF the share that allowed me to log in is ***tbfc-santa***
`smbclient //10.10.237.138/tbfc-santa`

Once connected, run ***ls*** to get the final answer!

![54](https://user-images.githubusercontent.com/83836972/122341948-ac094c80-cf61-11eb-8350-f9a0d871eb48.PNG)

Hope you gained a little bit knowledge of ***enum*** tool, note this down in your notes, it'll be very helpful in next CTFs as well!
