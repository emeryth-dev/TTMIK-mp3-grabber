#!/usr/bin/python3

#this is only for getting the mp3 files from TTMIK.com

from bs4 import BeautifulSoup
import requests
import re

loginurl = 'https://talktomeinkorean.com/sign-in/?redirect_to=https%3A%2F%2Ftalktomeinkorean.com%2Fcurriculum%2Flevel-1-korean-grammar%2Flessons%2Flevel-1-lesson-2%2F'
logininfo = {"log":"PUT USERNAME HERE", "pwd":"PUT PASSWORD HERE"}

#set up the session and save login cookies. yum.
s = requests.Session()
r = s.post(loginurl, data=logininfo)
#loop for each level
for level in range(1,11):
    #starts with the Level top page and creates a list of all the lesson sub-pages
    urlstart = 'https://talktomeinkorean.com/curriculum/level-{}-korean-grammar/'.format(level)
    starterhtml = s.get(urlstart).text
    soup = BeautifulSoup(starterhtml, 'lxml')
    global listofurls
    listofurls = [] #this resets our list after every loop
    for tag in soup.find_all('a'): #grabs all the links on top page
        templist = re.split('\"', str(tag)) #split for parsing
        for entry in templist:
            if re.compile('vel-{0}-kor'.format(level)).search(entry): #checks to verify it's a lesson
                listofurls.append(entry)

            
        #grab the http crap from the second page
    for url2 in listofurls:
        tst = s.get(url2).text
        newsoup = BeautifulSoup(tst, 'lxml')

        
        #parse the crap to get the address of what I want. The mp3 file.
        #had to add an if else for level 10. They changed their formatting.
        if not level == 10:
            for tag in newsoup.find_all('a'):
                listwithmp3 = re.split('\"', str(tag))
                for entry in listwithmp3:
                    if re.compile("mp3").search(entry) and re.compile("Level").search(entry):
                        print(entry)
        else:
            for tag in newsoup.find_all('a'):
                listwithmp3 = re.split('\"', str(tag))
                for entry in listwithmp3:
                    if re.compile("mp3").search(entry) and re.compile("TTMIK").search(entry):
                        print(entry)
            