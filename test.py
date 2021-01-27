#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from urllib import urlopen
import urllib
#import urllib.parse
#import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


def getinfo( url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('meta', attrs={'property': 'og:description'})

    img_data = soup.find_all('meta', attrs={'property': 'og:image'})
    img_text = img_data[0].get('content').split()
    
    profile_url = img_text[0]
    text = data[0].get('content').split()
    followers = text[0]
    following = text[2]
    posts = text[4]
    print ('Profile:', profile_url)
    print ('Followers:', followers)
    print ('Following:', following)
    print ('Posts:', posts)
    print ('---------------------------')


if __name__ == '__main__':
    getinfo('https://www.instagram.com/belle_lucia/?hl=en')
