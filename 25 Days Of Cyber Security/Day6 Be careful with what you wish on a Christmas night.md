# Day6

## Be careful with what you wish on a Christmas night

Deploy your machine and go through the information provided.

For the first question, we need to find out the ***type of vulnerability the attacker used***. If you've read through the text, you should be able to answer this. If not, I recommend reading through the text again, and then specifically about each type of vulnerability again over there.

Now, since it is mentioned that you've to ***open the ip on port 5000***, then do as per what is said!

`http://MACHINE_IP:5000`

Once you navigate to the site, it'll show something like:

![34](https://user-images.githubusercontent.com/83836972/121776391-422c2400-cbaa-11eb-8a7f-9480762117bd.PNG)

Test the normal functionality of the site. If you type in a wish, you can see that it shows up when you search for it. This help us answer our second question. 

![35](https://user-images.githubusercontent.com/83836972/121776394-48ba9b80-cbaa-11eb-865c-74d3aa3f80ad.PNG)

Now we'll use the OWASP Zap.

Though it has been given in the dossier about how to use OWASP, but you can still read this writeup further to know how to run the OWASP.

### Using OWASP Zap

- Open OWASP from the applications. It'll look somewhat like this:

![36](https://user-images.githubusercontent.com/83836972/121776401-4fe1a980-cbaa-11eb-8172-a6a4d1fe11eb.PNG)

- Over there in the right, click on  ***Automated Scan*** and it'll take you to the page that will look like 

![37](https://user-images.githubusercontent.com/83836972/121776405-54a65d80-cbaa-11eb-8177-5c4a28bcceba.PNG)

- Now, simply put the target URL in the 'URL to attack' field (with port 5000) and choose Attack.
- Once the scan gets completed, look at the ***Alert*** tab in your left.

![38](https://user-images.githubusercontent.com/83836972/121776410-5a03a800-cbaa-11eb-828b-d15b7d8796f1.PNG)

- It will be showing something like this!
- Hope it will help you answer the next question.
- In order to make an alert, you've to use 
`reflected?keyword=<script>alert(stopppp)</script>`
- Once you press ***Enter*** , the XSS will successfully get exploited and you can even see that on your screen instantly.
