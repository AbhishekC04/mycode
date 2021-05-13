#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import urllib.request
import crayons
import yaml

# function to push commands
def commandpush(work): # devicecmd==list
    for task in work['todo']:
        print ('Handshaking. .. ... connecting with ' + task['ipaddr'] )
        # we'll learn to write code that connects to devices here
        print(crayons.yellow('Attempting to sending command --> ' + task['name'] + " " +  task['state'] ))
        # we'll learn to write code that sends cmds to device here

def get_yaml(ymlurl):
    with urllib.request.urlopen(ymlurl) as response:
        return yaml.load(response.read())
        # download yaml file using http

def addnumbers (a,b):
    return a+b

# start our main script
def main():
    thisurl = "http://localhost:8080/work2do-two"
        work2do = get_yaml (thisurl)
        print ("This url is downloaded from :", thisurl)
        print (crayons.green(yaml.dump(work2do)))
        print (crayons.red("Welcome to the network device command pusher", bold=True)) # welcome message
        
        ## run
        commandpush(work2do) # call function to push commands to devices
        print ("===>>", addnumbers(10,2))
# call our main function
main()
