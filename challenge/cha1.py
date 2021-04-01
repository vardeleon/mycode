#!/usr/bin/env python3


import subprocess
call(["ip", "link", "show", "up"])
def main():
    counter = 0
    while(True):        # sets up an infinite loop condition
         print("What is the IPv4 address used to broadcast on a local network? ")
         answer = str(input())    # string answer collected from user
         counter = counter + 1     # increase the round counter
         if (answer == "255.255.255.255"): # logic to check if user gave correct answer
            print("Correct!")
            break             # break statement escapes the while loop
         elif (counter == 3):    # logic to ensure round has not yet reached 3
            print('Sorry, the answer was 255.255.255.255')
            break             # break statement escapes the while loop
         else:                 # if answer was wrong, and round is not yet equal to 3
            print('Sorry. Try again!')

if __name__ == "__main__":
    main()
