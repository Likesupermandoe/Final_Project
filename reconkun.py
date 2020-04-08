#!/usr/bin/env python3
import sys
import subprocess #interacting with OS



def main():
  print("\n\n\n##### Reconkun is an interactive script that aims to guide beginner red-teamers through the active recon process by explaining#####\n##### the thought process as well useful tools to use to start gathering information. This is for ethical hackers who#####\n##### want to learn. Ethical hacking is performed by a company to help identify potential threats on a machine or network.#####\n\n ")
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
    print("- - - Who is your target? - - -")
    print("1 - Go to Scan Menu - I already have an IP")
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
        sys.exit(1) #exit program; same error

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
    print("1: nmap -A")
    print("2: nmap -O") # need to input subnet here
    print("3: nmap -sV")
    print("4: Exit")

    choice = input ("Please make a choice: ")

    if choice == "1":
        print("Aggressive Scan") #Explaination
        subprocess.call(['nmap', '-A'] + [input()])
        #subprocess.call(pingsweep.sh )
    elif choice == "2":
        print("Operating System Scan")
        subprocess.call(['nmap', '-O'] + [input()])
    elif choice == "2":
        print("Service Version Scan")
        subprocess.call(['nmap', '-sV'] + [input()])
    elif choice == "4":
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

main()
