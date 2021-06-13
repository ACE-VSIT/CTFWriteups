# Day7

## The Grinch Really Did Steal Christmas

Read through the task and download the .pcap files!

Extract them.

Open pcap1.pcap in wireshark.

For the first question, apply the filter ***icmp*** and ***go through the first entry*** in order to find the IP address that initiates an ICMP/ping.

![39](https://user-images.githubusercontent.com/83836972/121806633-4883d400-cc6e-11eb-9e44-7a93efb25e6c.PNG)

The next question can be answered if you've read the given information in the task carefully! 
However, the answer would be, `http.request.method == GET`

In the next question, it is clearly written to use the above filter in Wireshark, so we'll be doing as per what is told along with ip.src==10.10.67.199: `ip.addr == 10.10.67.199 && <answer_from_previous_question>` to find the article name.

![40](https://user-images.githubusercontent.com/83836972/121806641-4de11e80-cc6e-11eb-9444-d6e76d9fd86c.PNG)

For the next question, use the filter `ftp` and follow the one saying ***please specify the password and got the above password*** by right click and then select follow!

![41](https://user-images.githubusercontent.com/83836972/121806649-52a5d280-cc6e-11eb-8d3c-6480b9612f93.PNG)

For the next question, the name of protocol that has been encrypted is `ssh`.

Now, let’s ***open pcap3.pcap*** for the final question. 

Then go to File > Export Objects > HTTP. 

![42](https://user-images.githubusercontent.com/83836972/121806651-576a8680-cc6e-11eb-932c-745245c851c4.PNG)

Select the file and save it. 

Then extract the wishlist and you'll get the following files:

![43](https://user-images.githubusercontent.com/83836972/121806657-5c2f3a80-cc6e-11eb-907e-85f66f70425f.PNG)

Try opening all the files only to explore things but you'll get the flag in ***elf_mcskidy_wishlist.txt***

![44](https://user-images.githubusercontent.com/83836972/121806662-60f3ee80-cc6e-11eb-9473-3a39a5f54552.PNG)

Submit your answers and you're done with Day7!

