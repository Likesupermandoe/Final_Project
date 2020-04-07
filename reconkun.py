#!/usr/bin/env python3
import sys
import subprocess #interacting with OS
def main():
  choice ='0'
  while choice =='0':
    print("Who is your target?")
    print("1 - IP")
    print("2 - Subnet")
    print("3 - Exit")

    choice = input ("Please make a choice (Use numbers): ")

    if choice == "1":
        print("Input IP here") #input ip here
        #usrchoice = input()
        usrchoice = subprocess.call(['nmap'] +  [input()])
        scan_menu()
    elif choice == "2":
        print("Input Subnet here:") #input subnet here
        subprocess.call(['nmap', '-sn'] +  [input()])
        scan_menu()
    elif choice == "3":
        print("Exiting program")
        sys.exit(1) #exit program
        #repl process died unexpectedly: exit status 1 *ask someone!
    else:
        print("I don't understand your choice.")
        sys.exit(1) #exit program; same error

def scan_menu(): #scan_MENU
  print("- - - - - - - - - - - - - - - - - - - - - -")
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
  print("- - - - - - - - - - - - - - - - - - - - - -")
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
main()

