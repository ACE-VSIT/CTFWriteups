# Day2
## The Elf Strikes Back

Deploy the machine and go through what all has been given there.

Let's navigate to the IP in the browser  of the attack machine where we should see a homepage somewhat like the given below:
![5](https://user-images.githubusercontent.com/83836972/121180532-966b9700-c87e-11eb-8162-6080a22b943a.png)

It looks like we are not signed in but at the same time this homepage is giving us the hint of logging using a ***get*** parameter. 

When we use ***get*** request we pass a query parameter that follow a ***?*** character. Here we'll be passing a parameter called ***id*** bcs that is what needed to login anywhere. 

At the bottom of the dossier there is a note for all, having an id number to use for login. And the id is ***ODIzODI5MTNiYmYw***.  Let’s try to add this to our URL and sign in by writing ***?id=ODIzODI5MTNiYmYw*** to our URL. When we hit enter we see that it works and we are redirected to a file upload page!

Also, you must have got the answer to your 1st question till now!

![6](https://user-images.githubusercontent.com/83836972/121180558-9e2b3b80-c87e-11eb-86d4-349aae23f5b7.PNG)
If we try to upload any file we get an error telling us that it is not a support file type! Bad news!

But we might be able to get some information about what types of files we are able to upload. We can do this simply by going to the page source (Right Click > View Page Source)

![7](https://user-images.githubusercontent.com/83836972/121180586-a4211c80-c87e-11eb-9558-0be1b9a47364.PNG)

In here, you can easily spot the ***accept*** parameter having the supported file types. These are all image file types so it seems we are only able to upload image files through this.

So the supported file type has to be ***image***!

If the file uploader only accepts image uploads, how can we possibly upload our PHP script and run the reverse shell? 

Well, we can just try it out by renaming our file type with the extension of what supported file type is there in the question! This is because many poorly coded file uploads will simply look for the first .  and then take whatever is after it as the upload type.

So we'll just rename the file by the following command:

***mv shell.php.jpeg  shell.jpg.php***

If we try to upload the file now we can see that it has been uploaded successfully! Now we need to find the script and run it.

The next question asks us to find the directory where the uploaded files are kept. We can use a tool like ***gobuster*** in order to find some directories. However, the challenge here gives us some locations where file uploads might be found. Maybe we can start there and see if we find our file.

We find some immediate success. Navigating to the ***/uploads/*** directory reveals our file and also the answer to our 3rd question.

For the next question we first need to get a reverse shell script ready. 

If you are using a THM AttackBox, there will already be a copy of a script made available for you in /root/Desktop/AoC-2020/Day-2

If you are using Kali instead, you can find a copy of this script in usr/share/webshells/php 

To use this script, copy it to your home directory with the command:

***cp /usr/share/webshells/php/php-reverse-shell.php ./***

There are a few steps we need to follow first before deploying the script. First, let's edit the script in nano and make some changes to prepare it.

To edit the script, just type:

nano <name_of_the_file>

There are two lines of code with comments //CHANGE THIS after them, we'll be editing only them!

The IP address is the IP of your machine or AttackBox and the port is the port we want the shell to open on.

![8](https://user-images.githubusercontent.com/83836972/121180635-af744800-c87e-11eb-9580-652d8f1c278e.PNG)

Save the file.

Now we need to start our netcat listener in order to receive the shell when we execute the file, using the command: 

***nc -nvlp 1234***

**NOTE: Make sure the port matches the port you put into the uploaded file!**

If everything is successful we should see the reverse shell prompt appear!

![9](https://user-images.githubusercontent.com/83836972/121180696-c1ee8180-c87e-11eb-8431-394c8f14ba80.PNG)

In the last question we need to find the flag in the file ***/var/www/flag.txt***. 

We can simply use ***cat***  to read the contents of the file and reveal the flag! Run ***cat /var/www/flag.txt*** and there you get your flag!
