#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input
#ipchk = ipchk.split(".")
print(ipchk)
print(len(ipchk)
if (len(ipchk)) != 4:
    print("Not an IP address")
# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: # if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else

