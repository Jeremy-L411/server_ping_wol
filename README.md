# server_ping_wol
ping a server and if off send wol packets

This is a simple script I created because a server was intermittently shutting 
down, and I was not always around to restart it. Using a small 
linux machine and set to run this script every hour it will ping the 
ip address, if it returns True the loop is broken, if False it 
sends three packets with 5.5 seconds delay. I have found that WOL 
packets need two or three times to succeed and added a delay so 
it does not overload it. 

# Import packages  
###### platform
###### subprocess
###### time
###### wakeonlan