#!/usr/bin/env python3
import sys
import nmap
import subprocess #interacting with OS
from colorama import Fore, Back, Style 


def main():
  print(Fore.GREEN + "\n\n\n##### Reconkun is an interactive script that aims to guide beginner red-teamers through the active recon process by explaining \n##### the thought process as well useful tools to use to start gathering information. This is for ethical hackers who \n##### want to learn. Ethical hacking is performed by a company to help identify potential threats on a machine or network.\n\n ")
  print(Style.RESET_ALL)
  print(r"""\

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   • •. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)


  choice ='0'
  while choice =='0':
    print(Fore.BLUE +"- - - Who is your target? - - -")
    print(Style.RESET_ALL)
    print("1 - I have a target IP - take me to the Scan Menu")
    print("2 - Subnet")
    print("3 - My target?! Subnet!?  What's that?")
    print("4 - Exit")

    choice = input ("Please make a choice (Use numbers): ")

    if choice == "1":
        #print(". . . . .") #input ip here
        #usrchoice = input()
        #usrchoice = subprocess.call(['nmap'] +  [input()])
        scan_menu()
    elif choice == "2":
        print("Input Subnet here:") #input subnet here
        subprocess.call(['nmap', '-sn'] +  [input()])
        scan_menu()
    elif choice == "3":
        print("Target info here")
        target_info()
    elif choice == "4":
        print("Exiting program")
        sys.exit(1) #exit program
        #repl process died unexpectedly: exit status 1 *ask someone!
    else:
        print("I don't understand your choice.")
        main() #invalid choice... go back to main()

def scan_menu(): #scan_MENU
  print("- - - - - - - - - - - - - - - - - - - - - -\n")
  choice ='0'
  while choice =='0':
    print(" :: What scans do you want to do? ::")
    print("1: NMAP") # need to input IP here
    print("2: Nikto")
    print("3: Exit")

    choice = input ("Please make a choice: ")
    #usrchoice = raw_input(" ")

    if choice == "1":
        print("NMAP scan choices") #input ip here
        nmap_menu()
    elif choice == "2":
      print("Going back!")
      main() 
    elif choice == "3":
      print("Exiting program. Byebye!")
      sys.exit(1) #exit program     
    else:
        print("I don't understand your choice.")

def nmap_menu(): #NMAP_menu
  print("- - - - - - - - - - - - - - - - - - - - - -\n")
  choice ='0'
  while choice =='0':
    print("1: nmap -sV")
    print("2: nmap -O")
    print("3: nmap -A")
    print("4: What is NMAP and why should I love it?")
    print("5: Exit")

    choice = input ("Please make a choice: ")
    if choice == "4":
        nmap_expl() #Takes to NMAP explanation menu
    elif choice == "3":
        print("Aggressive Scan") #Explaination
        print(Fore.BLUE + '''\t\t The syntax on the command line is: nmap -A <target>. 
                 This special scan enables OS detection, Service Version detection, and 
                 default nmap script scans among many other probing functions all in one setting.''')
        print('''\t\t Cons: Sending so many probes to your target machine creates a lot of traffic. 
                 In a real-world setting where data traffic is closely monitored, this scan will draw unwanted attention to your reconnaissance. 
                 It is important to keep in mind that we want to remain undetected as we gather information to eventually compromise a target machine.''') 
        print(Style.RESET_ALL)
        print(Fore.RED + "Enter Target IP")
        print(Style.RESET_ALL)
        nm = nmap.PortScanner()
        host = input() 
        nm.scan(host, '1-1024', '-A')
        nm.command_line()
        nm.scaninfo()

        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------')
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

        lport = nm[host]['tcp'].keys()   #<------ This 'proto' was changed from the [proto] to the ['tcp'].
#            lport.sort()
        for port in lport:
            print('----------------------------------------------------')
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
            print('port : %s\tService : %s' % (port, nm[host][proto][port]['name']))
            print('port : %s\tVersion : %s' % (port, nm[host][proto][port]['version']))
            print('port : %s\tProduct : %s' % (port, nm[host][proto][port]['product']))
            print('----------------------------------------------------') 

        if 'osmatch' in nm[host]:
            for osmatch in nm[host]['osmatch']:
                print('OsMatch.name : {0}'.format(osmatch['name']))
                print('OsMatch.accuracy : {0}'.format(osmatch['accuracy']))
                print('OsMatch.line : {0}'.format(osmatch['line']))
                print('')
        if 'osclass' in osmatch:
            for osclass in osmatch['osclass']:
                print('OsClass.type : {0}'.format(osclass['type']))
                print('OsClass.vendor : {0}'.format(osclass['vendor']))
                print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                print('OsClass.osgen : {0}'.format(osclass['osgen']))
                print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
                print('')

        #subprocess.call(['nmap', '-A', input(), '-oX', 'NMAP_A_Scan.txt'])        
        scan_menu() # takes us back to scan menu
        #subprocess.call(['nmap', '-A'] + [input()])
        #subprocess.call(pingsweep.sh )
    elif choice == "2":
        print("Operating System Scan")
        print(Fore.BLUE +'''\t\t This nmap flag calls for ‘Operating System discovery’ 
                 The syntax for this command line is: nmap -O <target>. 
                 Nmap sends a series of tcp/ip packets to the targetted machine, examines all the responses 
                 and compares those responses to its database of OS fingerprints to identify the most probable Operating System that target is running on. 
                 For indepth info visit: https://nmap.org/book/man-os-detection.html''')
        print(Style.RESET_ALL)
        print(Fore.RED +"Enter Target IP")
        print(Style.RESET_ALL)
#        subprocess.call(['nmap', '-O', input(), '-oX', 'NMAP_O_Scan.txt'])  
        nm = nmap.PortScanner()
        host = input()
        nm.scan(host, arguments="-O")
        if 'osmatch' in nm[host]:
            for osmatch in nm[host]['osmatch']:
                print('OsMatch.name : {0}'.format(osmatch['name']))
                print('OsMatch.accuracy : {0}'.format(osmatch['accuracy']))
                print('OsMatch.line : {0}'.format(osmatch['line']))
                print('')
        if 'osclass' in osmatch:
            for osclass in osmatch['osclass']:
                print('OsClass.type : {0}'.format(osclass['type']))
                print('OsClass.vendor : {0}'.format(osclass['vendor']))
                print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                print('OsClass.osgen : {0}'.format(osclass['osgen']))
                print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
                print('')
       
        scan_menu() # takes us back to scan menu
        #subprocess.call(['nmap', '-O'] + [input()])
    elif choice == "1":
        print("Service Version Scan")
        print(Fore.BLUE + '''\t\t This nmap flag calls for ‘Version Detection’ 
                 The syntax for this on the command line is: nmap -sV <target>. 
                 Nmap will discover ports and use probes from its data base to query the ports and examine their responses 
                 and returns to you the services that are running on those ports as well other pertinent info about those services 
                 such as protocol name, application name, service version, device type, etc.
                 For indepth info visit: https://nmap.org/book/man-version-detection.html''')
        print(Style.RESET_ALL)
        print(Fore.RED + "Enter Target IP")
        print(Style.RESET_ALL)
        nm = nmap.PortScanner()
        host = input()
        nm.scan(host, '1-1024', '-sV')
        nm.command_line()
        nm.scaninfo()

        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------')
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host]['tcp'].keys()   #<------ This 'proto' was changed from the [proto] to the ['tcp'].
#            lport.sort()
        for port in lport:
            print('----------------------------------------------------')
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
            print('port : %s\tService : %s' % (port, nm[host][proto][port]['name']))
            print('port : %s\tVersion : %s' % (port, nm[host][proto][port]['version']))
            print('port : %s\tProduct : %s' % (port, nm[host][proto][port]['product']))

#        subprocess.call(['nmap', '-sV', input(), '-oX', 'NMAP_sV_Scan.txt'])  
        scan_menu() # takes us back to scan menu
        #subprocess.call(['nmap', '-sV'] + [input()])
    elif choice == "5":
        print(" Exiting")
        sys.exit(1) #exit program 
    else:
        print("I don't understand your choice.")


def target_info(): #Target Information & How to find it!
    print("- - - - - - - - - - - - - - - - - - - - - -\n")
    print("What's a target?\n\n")
    print("Your target is the machine or network you are performing active recon on.\nThis is where you are actively engaging the target machine or network\nto gather more information.\n\n")
    print("- - - - - - - - - - - - - - - - - - - - - -\n")
    print("\nA Subnet is a smaller network in which all the devices on THAT network share IP addresses with the same prefix. Like 192.168.2.0, 192.168.3.0, 192.168.4.0 are on the same subnet. ")
    print("\nSometimes your subnet may be a /24 or /16. To scan a subnet you might want to input something like 192.168.2.0/24 to see all the machines there! :)\n\n")
    choice = '0'
    while choice == '0':
        print ("1: Sounds good. Take me back!")
        print ("2: Exit")

        choice = input ("Please make a choice: ")

        if choice == "1":
            print ("Going back!")
            main() #takes back to main menu
        elif choice == "2":
            print ("Exiting program. Bye!")
            sys.exit(1) #exit program
        else:
            print ("I don't understand your choice.")

def nmap_expl(): #Explanation on Nmap!
    print("- - - - - - - - - - - - - - - - - - - - - -\n")
    print("What is Nmap? \n\n")
    print("Nmap is an open source port scanning tool. It can be used to find different machines on a network,\nopen ports on a machine and the services they run, the operating system they're running on.")
    print("\nHowever, it doesn't have to be just that. You can customize your Nmap scan to do different things. It can scan for vulnerabilities as well.")
    print("\nA basic scan on a machine looking for all ports would look something like this: nmap -p- 192.168.2.0 \nThe '-p-' means to scan for all open ports on the machines 192.168.2.0 ")
    nmap_menu()
main()
