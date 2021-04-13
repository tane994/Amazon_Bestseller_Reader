"""
TITLE: Amazon Bestseller Reader
Inspiration Project: I was inspired by the Mashup project "COVID-19 Audio Alert"
Physical inputs/outputs: I used SenseHat for greeting messages and for displaying a simple figure.
Non-physical inputs/outputs: I used bs4 for web scraping, gTTS for text to speech and pygame for playing audio.
Interaction: The goal of this project is to extract the titles and prices of the top ten articles of the amazon category "electronics and photo",
converting this data to a mp3 file and playing the audio generated.
@Author: Andres Tanesini
"""


from project_functions import gimme_the_soup, title, scraping_amazon, products_and_prices, playAudioFile, text2speech, pick_random_colour
from time import sleep
from sense_emu import SenseHat

sense = SenseHat()
grey = (169, 169, 169)
green = (0, 255, 0)
while True:
    sense.show_message("Welcome to my Maker Lab Project!", text_colour = green, back_colour = grey, scroll_speed = 0.1)
    break

url_amazon = "https://www.amazon.co.uk/Best-Sellers-Electronics/zgbs/electronics"
soup = gimme_the_soup(url_amazon)
title = title(soup)
electronics_bestsellers = scraping_amazon(soup)
lang = "en"
text2speech(lang, title)
top_ten = products_and_prices(electronics_bestsellers)
text2speech(lang, top_ten)

while True:
        sense.show_message("Thank you for your attention!", text_colour=green, back_colour=grey, scroll_speed=0.1)
        break

while True:
    sense.show_letter("A", pick_random_colour())
    sleep(1)
    sense.show_letter("n", pick_random_colour())
    sleep(1)
    sense.show_letter("d", pick_random_colour())
    sleep(1)
    sense.show_letter("r", pick_random_colour())
    sleep(1)
    sense.show_letter("e", pick_random_colour())
    sleep(1)
    sense.show_letter("s", pick_random_colour())
    sleep(1)
    sense.clear(255, 255, 255)
    sleep(4)
    break

sense.set_pixel(1, 1, (0, 0, 255))
sense.set_pixel(1, 2, (0, 0, 255))
sense.set_pixel(2, 1, (0, 0, 255))
sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(5, 1, (0, 0, 255))
sense.set_pixel(5, 2, ( 0, 0, 255))
sense.set_pixel(6, 1, (0, 0, 255))
sense.set_pixel(6, 2,  (0, 0, 255))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(6, 5, (255, 0, 0))
sense.set_pixel(1, 6, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 6, (255, 0, 0))
sense.set_pixel(6, 6, (255, 0, 0))
sense.clear