#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())

## function to return IP Address

def ip_addr(netifaces.interfaces()):
    ips = set()
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        ip_return_addr = netifaces.ifaddresses(ip_addr)[netifaces.AF_INET][0]['addr']
        print(ip_return_addr)
        return (ips)
    
def main():
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:    
            print('MAC Address: ', end='') # This print statement will always print MAC without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #Prints the MAC Addr
            print('IP Address: ', end='') # This print statement will always print MAC without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #Prints the IP Addr
        except:
            print('Could not collect adapter information')
        
            ip_addr(netifaces.interfaces())
main()

        
