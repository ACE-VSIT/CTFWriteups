# Day1
## A Christmas Crisis

- Deploy the attack machine and the challenge by clicking the green buttons on your screen.
- Then open the browser and enter the IP of the deployed challenge box. Just in case it takes time, don't hurry, sometimes it takes more time than usual but not more than 5mins.
- It will open the web page somewhat like the given below:
![1](https://user-images.githubusercontent.com/83836972/120929169-9bf1a180-c705-11eb-9471-8d1c4e015c22.png)
- Now create a user by typing in a ***username*** & a ***password*** then click on the ***register button***. Right after registering, click on the ***login button*** and you are done with setting up an account.
- Toggle on the developer tools of the browser ***(ctrl+shift+I or fn+f12***). And navigate to the ***data panel***. Here you can see the ***cookie name*** and ***value***(usually found in the storage section).
![2](https://user-images.githubusercontent.com/83836972/120929304-2f2ad700-c706-11eb-85a0-e12f0f3cb385.png)
- Here you can see all the information regarding that cookie along with the name, i.e. auth. Looking at the value you can either know by experience what kind of encoding is used. Or, if you have no idea you can pull up ***cyberchef***, paste in the value and get the output. However the format is of ***Hexadecimal***.
- For my username of errorrrr404 the cookie decodes to:***{"company":"The Best Festival Company", "username":"errorrrr404"}***
- This is the ***JSON*** format (Java Script Object Notation) for further information regarding JSON you can head straight onto google.
- In order to get Santa’s cookie, we now need to ***change*** the ***username*** ***in the JSON to santa*** and ***encode that JSON into Hex again***. You can do that in CyberChef as well. Make sure to select the ***delimiter at none***.
![3](https://user-images.githubusercontent.com/83836972/120929315-3ce05c80-c706-11eb-9217-f8b898c00e35.png)
- Now we go back to the website and out developer tools. We replace the ***value of the auth*** cookie with what we just calculated, then ***reload*** the page.
- All the switches are flipped on, and the final flag is revealed.(it will reveal over the last switch, you can easily spot that)
![4](https://user-images.githubusercontent.com/83836972/120929323-45d12e00-c706-11eb-96b3-75b60554c741.png)

