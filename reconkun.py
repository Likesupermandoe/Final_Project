#!/usr/bin/env python3
import sys
import subprocess #interacting with OS
def main():
  choice ='0'
  while choice =='0':
    print("Do you have a target?")
    print("1: Yes")
    print("2: No")
    print("Exit")
    print("Choose 5 to go to another menu")

    choice = input ("Please make a choice: ")

    if choice == "1":
        print("⋆ -- Taking you to IP menu -- ⋆")
        second_menu()
    elif choice == "2":
        print("⋆ -- Taking you to Subnet menu -- ⋆")
        third_menu()
    elif choice == "exit":
        print("Exiting program")
        sys.exit(1) #exit program
        #repl process died unexpectedly: exit status 1 *ask someone!
    else:
        print("I don't understand your choice.")
        sys.exit(1) #exit program; same error

def second_menu(): #ip menu
  print("This is the IP menu")
  print("- - - - - - - - - - - - - - - - - - - - - -")
  choice ='0'
  while choice =='0':
    print(" :: What is the IP you are targeting? ::")
    print("1: IP") # need to input IP here
    print("2: Go Back")
    print("3: Exit")

    choice = input ("Please make a choice: ")
    #usrchoice = raw_input(" ")

    if choice == "1":
        print("Input IP here") #input ip here
        #usrchoice = input()
        usrchoice = subprocess.call(['nmap'] +  [input()])
    elif choice == "2":
      print("Going back!")
      main() 
    elif choice == "3":
      print("Exiting program. Byebye!")
      sys.exit(1) #exit program     
    else:
        print("I don't understand your choice.")

def third_menu(): #subnet menu
  print("This is the Subnet menu")
  print("- - - - - - - - - - - - - - - - - - - - - -")
  choice ='0'
  while choice =='0':
    print(" :: What is the Subnet you are targeting? ::")
    print("1: Subnet") # need to input subnet here
    print("2: Go Back")
    print("3: Exit")

    choice = input ("Please make a choice: ")

    if choice == "1":
        print("Input Subnet here:") #input subnet here
        subprocess.call(['nmap', '-sn'] +  [input()])
        #subprocess.call(pingsweep.sh )
    elif choice == "2":
        print("Going back!")
        main()
    elif choice == "3":
        print("Exiting program. Byeybye!")
        sys.exit(1) #exit program 
    else:
        print("I don't understand your choice.")

main()