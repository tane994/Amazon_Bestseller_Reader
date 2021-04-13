import requests
from bs4 import BeautifulSoup
from pygame import mixer
from gtts import gTTS
import os
from random import randint
from time import sleep
from sense_emu import SenseHat


def gimme_the_soup(url):
    headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9" }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    return soup

def title(soup):
    title = soup.find("h1", class_="a-size-large a-spacing-medium zg-margin-left-15 a-text-bold").text
    return title

def scraping_amazon(soup):
    items = []
    for item in soup.findAll("li", attrs={"class": "zg-item-immersion"})[:10]:
        name = item.find("div", attrs={"class": "p13n-sc-truncate"})
        price = item.find("span", attrs = {"class": "p13n-sc-price"})
        if name is not None:
            items.append(name.text.strip())
        else:
            items.append("unknown title")

        if price is not None:
            items.append(price.text.strip())
        else:
            items.append("unknown price")
    return items

def products_and_prices(product_details):
        top_ten = "number 1: " + product_details[0] + " Price: " + product_details[1] \
                  + "number 2: " + product_details[2] + " Price " + product_details[3] \
                  + "number 3: " + product_details[4] + " Price: " + product_details[5] + \
                  "number 4: " + product_details[6] + " Price: " + product_details[7] + \
                  "number 5: " + product_details[8] + " Price: " + product_details[9] + \
                  "number 6: " + product_details[10] + " Price: " + product_details[11] \
                  + "number 7: " + product_details[12] + " Price " + product_details[13] \
                  + "number 8: " + product_details[14] + " Price: " + product_details[15] + \
                  "number 9: " + product_details[16] + " Price: " + product_details[17] + \
                  "number 10: " + product_details[18] + " Price: " + product_details[19]
        return top_ten



def playAudioFile(filename):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy()==True:
     pass

def text2speech(lang,text):
    filename='bestsellers.mp3'
    tts=gTTS(text=text, lang=lang)
    tts.save(filename)
    playAudioFile(filename)
    os.remove(filename)

def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)