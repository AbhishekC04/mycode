#!/usr/bin/env python3
import crayons

"""Alta3 Research || Author: RZFeeser@alta3.com"""

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print (crayons.yellow('Handshaking. .. ... connecting with ' + coffeetime ))
        # we'll learn to write code that connects to devices here
        print (devicecmd.keys())
        print (coffeetime)
        print (devicecmd[coffeetime])
        for mycmds in devicecmd[coffeetime]:
            print (crayons.magenta('Attempting to sending command --> ' + mycmds ))
            # we'll learn to write code that sends cmds to device here

# function to iterate thru the list of IPs
def devicereboot(ipcmd):
    for ip in ipcmd.keys():
        print ("Connecting to..", ip)
        print ("REBOOTING NOW!")

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print (crayons.green("Welcome to the network device command pusher")) # welcome message

    ## get data set
    print (crayons.white("\nData set found\n")) # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices
    devicereboot(work2do) # call the second device reboot function

# call our main function
main()

