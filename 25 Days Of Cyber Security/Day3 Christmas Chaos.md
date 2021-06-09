# Day3

## Christmas Chaos

This task is very easy, we'll be using ***Burpsuite*** to complete the task but before that, deploy your machine and go through the ***dossier*** as it'll give you a brief about how to use burp.

Moving straight onto the task, head over to the ip provided, and you'll see a webpage as below:

![10](https://user-images.githubusercontent.com/83836972/121354718-c71a0200-c94c-11eb-94b5-71185e697028.PNG)
Try those id and passwords that are provided to you.
I did, but all of them were wrong, so let's use Burp!

Don't forget to setup burpsuite to intercept the request coming from this webpage.

### Setting up Burp

Setting up the burp is already explained in the dossier but hey, there's an easy way to use that!

Download the foxy proxy from the browser and just bookmark it bcss it'll be going to help us in other CTFs as well.

Link to download the foxy proxy is here: https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/

After doing all that, just follow the following steps:

- Click on proxy, go on options.
- Click on add. 

![11](https://user-images.githubusercontent.com/83836972/121354740-ced9a680-c94c-11eb-9397-595b2ec8a82d.PNG)
- Give the title ***Burp Proxy*** and set the ip address to ***127.0.0.1*** which is default and port number as ***8080***.

![12](https://user-images.githubusercontent.com/83836972/121354762-d4cf8780-c94c-11eb-9d93-e84147b21da5.PNG)
- Save those and just turn it on.

![13](https://user-images.githubusercontent.com/83836972/121354790-db5dff00-c94c-11eb-8192-cc31352f77c9.PNG)
- Now, open burpsuite from your applications, you can just search it there.
- After opening, it might show the screen as below, all you have to do is click on ***next***.

![14](https://user-images.githubusercontent.com/83836972/121354808-e022b300-c94c-11eb-9e86-25c5306bb806.PNG)
- And then an option will be there, ***start burp***, just click on it and you'll hop to the below screen:

![15](https://user-images.githubusercontent.com/83836972/121354822-e44ed080-c94c-11eb-8bb2-2a1141e9a922.PNG)
- When you get to this screen, you'll by default be on ***Dashboard***, from there you just have to click on ***Proxy*** and then turn the ***intercept on***.
- After that just go back to that webpage and reload it.
- Then get back to the burp proxy and you'll be seeing some requests:

![16](https://user-images.githubusercontent.com/83836972/121354836-e7e25780-c94c-11eb-9466-33753a29259c.PNG)
- Now send this request to the Intruder tab ***(by just right click and send to intruder)*** and ***select the attack type to be a “Cluster Bomb”***. 

![17](https://user-images.githubusercontent.com/83836972/121354853-eca70b80-c94c-11eb-86e7-031a2052bb24.PNG)
- Add the list of usernames in payload section.

![18](https://user-images.githubusercontent.com/83836972/121354879-f29cec80-c94c-11eb-850c-3ec3f57d1036.PNG)
![19](https://user-images.githubusercontent.com/83836972/121354899-f7fa3700-c94c-11eb-9f38-afe5fa89f52a.PNG)
- Add the list of passwords in payload section.

![20](https://user-images.githubusercontent.com/83836972/121354921-fcbeeb00-c94c-11eb-85e2-0855f4eed5d3.PNG)
![21](https://user-images.githubusercontent.com/83836972/121354939-01839f00-c94d-11eb-98ee-aae3096c9a5d.PNG)
- Launch the attack.
- Once the attack gets completed, you will see something like this.

![22](https://user-images.githubusercontent.com/83836972/121354970-08aaad00-c94d-11eb-9428-bdfcc79ca308.PNG)
- Here, the one with the varying length looks suspicious. And yes now we can manually try logging in using username as “admin” and password as “12345”.
- After logging in, you'll get to this

![23](https://user-images.githubusercontent.com/83836972/121354992-0ea08e00-c94d-11eb-9508-b6ea4477e7e6.PNG)

And there is the flag!
