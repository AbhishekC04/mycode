#!/usr/bin/env python3

# define a function to verify the IP checks
def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    if parts[3]=="1":
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

ipchk = input("Apply an IP address: ")
if validIP(ipchk):
    print("The IP is valid",ipchk)
    parts = address.split(".")
    int(parts[0]),int(parts[1]),int(parts[2],int(parts[3]),sep=".")
else:
    print("The IP is invalid",ipchk)


