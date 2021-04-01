#!/usr/bin/python3

import requests

WEEKLUCK = "http://horoscope-api.herokuapp.com/horoscope/week/"



def SUNSIGN():
    print('Your Weekly Horoscope')
    SIGN = input("Please enter you horoscope sign--> ")
    SIGN = SIGN.lower()
    return SIGN


def main():
     SIGN = SUNSIGN()
#     r = requests.get(WEEKLUCK + "Libra")
     r = requests.get(WEEKLUCK + SIGN)
     
     if r.status_code != 200:
        print(r.status_code)
        print(r.json())
        exit()

     r = r.json()

     with open("WEEKLUCK.data", "w") as f:
        # write out title
        f.write("SUNSign: " + r.get("sunsign") + "\n\n")

        # write out week
        f.write("Week: " + r.get("week") + "\n\n")
    
        # write out Horoscope
        f.write("Your Horoscope: " + r.get("horoscope") + "\n\n")

        # two blank ines
 #       f.write("\n\n")

     f = open('WEEKLUCK.data', 'r')
     file_contents = f.read()
     print (file_contents)
     f.close()
if __name__ == "__main__":
    main()
