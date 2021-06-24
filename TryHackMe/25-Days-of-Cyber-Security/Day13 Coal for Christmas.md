# Day13

## Coal for Christmas

As always, hit the deploy buttons. Once everything is ready, run a quick nmap scan.

As you can see from the result of nmap scan, ***telnet*** is also there, which is the old, deprecated protocol. So lets connect with `telnet 10.10.142.128`. Luckily for us, we are provided with the ***credentials in the greeting text***.

![60](https://user-images.githubusercontent.com/83836972/123261975-06cc1680-d515-11eb-863a-e2ee09c279ca.PNG)

To answer the next question, the above information is more than enough, so submit your answer first and then let's move onto the next one!

If you're going through the information that is provided then you very well know what command to run next in order to get the distribution and version!

So let's run the command `cat /etc/*release`:

![61](https://user-images.githubusercontent.com/83836972/123261990-0b90ca80-d515-11eb-8ec5-9aa84b014344.PNG)

Now with `ls` we'll have a look at what files we have in our home folder. ***christmas.sh ,  cookies_and_milk.txt***.

Let's have a look at the txt file by `cat cookies_and_milk.txt` :

The message will look somewhat like 

![62](https://user-images.githubusercontent.com/83836972/123262015-121f4200-d515-11eb-9d4f-e8ef4ba4282a.PNG)

This will answer the question about who got there first!!


The challenge asks us to learn about ***DirtyCow***. Let’s do that.

On the site you can find a link to the code of the Dirty Cow exploit. To get the code of the box, let's create a new file with `nano dirty.c` and copy paste the source. `CTRL+O` saves the file, `CTRL+X` closes the editor.

![63](https://user-images.githubusercontent.com/83836972/123262075-1cd9d700-d515-11eb-930d-5091e53cfa52.PNG)

After saving the file, check if this is shown there or not by `ls`, so we got the file there!

Also to answer the next question just read that source carefully, however the answer will be: `gcc -pthread dirty.c -o dirty -lcrypt`.

Now let's run the exploit using `./dirty` afterwards it'll ask for a password so use any password!

Also don't forget to submit the username you got i.e. ***firefart***.

With `su firefart` we change what user we are running. 
`cd ~` brings us to the home directory of firefart:

![64](https://user-images.githubusercontent.com/83836972/123262087-22cfb800-d515-11eb-88c9-dfc72333541e.PNG)

In the above message, it is asked to leave the file ***coal*** there so we'll just create a file using `touch coal` and leave it here.

Now run the command `tree` an you'll see the following output:

![65](https://user-images.githubusercontent.com/83836972/123262114-295e2f80-d515-11eb-806a-7483bc82ca55.PNG)

Now as per the information given in the task, we'll have to run the command `tree | md5sum` and press enter.

And there is our answer to the last question, ***the output of MD5 Hash***.

Cheers!!!!!!


