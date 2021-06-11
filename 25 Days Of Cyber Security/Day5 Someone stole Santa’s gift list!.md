# Day5

## Someone stole Santa’s gift list!

Deploy the machine and read through the dossier. First thing we need to do is ***look for Santa’s secret login panel***. 

The answer is using the 2 words from the question itself. Use hint if you want to!

For further questions, first visit your machine_ip and you'll see a login panel like below:

![28](https://user-images.githubusercontent.com/83836972/121699836-ecde0d00-caec-11eb-8e1c-e3afcebdf5e4.PNG)

Now we need to ***bypass the login***. If you've read the dossier carefully, you can go ahead, but if not, we're here to help!!

So, we'll be using  `' or true--` because ***--*** ***will comment out the password checking part***, i.e. It won't ask us for the password now and will directly let us log in.

![29](https://user-images.githubusercontent.com/83836972/121699864-f36c8480-caec-11eb-8515-8912996ab563.PNG)

In the search area, we can again use that same command `' or true--` because ***this is also a default true condition***. 

![30](https://user-images.githubusercontent.com/83836972/121699910-fd8e8300-caec-11eb-97a1-ace46ab77893.PNG)

Once you enter, you'll be getting the following as a result of your search:

![31](https://user-images.githubusercontent.com/83836972/121699931-05e6be00-caed-11eb-8af8-60d845fc97a0.PNG)

Have a count and you can easily answer about the total number of entries over there.

The next question is about ***what has Paul wished for***, and for this you just have to ***go through the list of wishes and look for Paul's wish***.

For getting the flag, we will need to utilize BurpSuite and SQLMap. 

First, open up BurpSuite and make sure your proxy is turned on.***(In day3, we've already done Burpsuite, so if you're still getting any issue just step over to our writeup of Day3:  https://github.com/ACE-VSIT/CTFWriteups/blob/main/25%20Days%20Of%20Cyber%20Security/Day3%20Christmas%20Chaos.md)*** 

Then capture a request from the website.

Right Click > Sent to Repeater on the request.

![32](https://user-images.githubusercontent.com/83836972/121699965-0f702600-caed-11eb-8ba6-87d726170b0c.PNG)

Right Click > Save Item to save the request in a folder. Name it anything, like `SantaPanel`.

We can now use that request in SQLMap.

`sqlmap -r SantaPanel --dbms=sqlite --dump-all --batch`

							or
							
`sudo sqlmap -r SantaPanel --tamper=space2comment --dump-all --dbms sqlite`

When you run that command, you receive a dump of all the data in the database! 


![33](https://user-images.githubusercontent.com/83836972/121699995-15fe9d80-caed-11eb-827d-0a500679fd14.PNG)

And we can now finish the task by giving answer to the next two questions using the above information!
