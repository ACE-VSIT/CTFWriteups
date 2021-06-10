# Day4

## Santa's Watching

Deploy the machine and then go through the provided information.

Then just enter the IP of that challenge to the browser and you'll see a site as below:

![24](https://user-images.githubusercontent.com/83836972/121534180-9d311000-ca1e-11eb-9a88-6ada646b49f0.PNG)

And with this we completed our first question, wow!

The next step is to figure out what the wfuzz command would look like for the provided URL.

If you've gone through the dossier carefully you can easily answer this question, however the answer is as mentioned below:

`***wfuzz -c -z file,big.txt http://shibes.xyz/api.php?breed=FUZZ***`

Now we'll try to find the ***API with gobuster***. 

As suggested, we use ***-w*** to ***specify the dirbuster big word list***. We add the ***.php extension with -x***. This is not needed to solve the challenge, it just put it in there because most forum software is written in php and so have been the previous challenges. By the code is:

`***gobuster dir -u http://10.10.79.210/ -w /usr/share/wordlists/dirb/big.txt -x .php***`

And you'll get something like below:

![25](https://user-images.githubusercontent.com/83836972/121534200-a326f100-ca1e-11eb-98e9-8483edd575d0.PNG)

In the output we find ***/api*** with a ***301 http code***, indicating it has permanently moved. We pull the url up in the browser and

![26](https://user-images.githubusercontent.com/83836972/121534222-a7530e80-ca1e-11eb-93ae-0eb52e7d0226.PNG)

It redirects to /api/ , a folder on the server. It looks like the API is only having one directory, ***site-log.php***

The challenge tells us that the parameter for that directory is date. 

So we find that out by ***wfuzz***.

`***wfuzz -c -z file,/home/kali/Downloads/wordlist  -u http://10.10.106.143/api/site-log.php?date=FUZZ***`

![27](https://user-images.githubusercontent.com/83836972/121534239-ad48ef80-ca1e-11eb-85be-c9238cf7c9d1.PNG)

Here, we see one of the results to have a different length. So we'll just pull up the url with that parameter by:

`***http://10.10.79.210/api/site-log.php?date=20201125***`

where, 20201125 is the payload of that!

Now, just by pressing enter, the flag will be available to us! And here the Day4 is completed! 
