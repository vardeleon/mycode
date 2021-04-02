#!/usr/bin/env python3
import urllib.request
import re

while(True):
    print("Where should we search? or q to quit")
    url = input()
    if (url.lower() == 'q'):
      break
    print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
    searchFor = input()
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

#    if (url.lower() == 'q'):
##      break
    if re.search(searchFor, searchMe):
      print("Found a match!")
    else:
      print("No match!")
