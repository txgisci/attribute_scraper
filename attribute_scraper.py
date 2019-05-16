# metadata Scraper
import requests
from requests import get
from bs4 import BeautifulSoup
import re

# Example image id for testing purposes
img_id = 'STS110-740-54'.split('-')

# core url
url1 = 'https://eol.jsc.nasa.gov/SearchPhotos/photo.pl?mission='
url2 = '&roll='
url3 = '&frame='


# Formats the final url for given image id
url = '{}{}{}{}{}{}'.format(url1, img_id[0], url2, img_id[1], url3,
                            img_id[2])
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# Pulls all data from top right table
table_pad = soup.findAll('td',attrs={'class':'table_pad'})

# Photo ID
photo_id = table_pad[1].text

# Date Taken
date_taken = table_pad[5].text[1:]

# Time Taken
time_taken = table_pad[7].text[1:]

# Focal Length
focal_length = table_pad[3].text[1:]

# Pulls all data from Map Location bottom tab
map_location = (soup.find_all('div', class_='span5')[0].get_text()).split('\n')

# ISS lat long before conversion
iss_coords = re.findall(r'\d+\.\d+', map_location[1])
iss_direction = re.findall(r'\° (.[NSEW]?)', map_location[1])

# Nadir lat long before conversion
nadir_coords = re.findall(r'\d+\.\d+', map_location[2])
nadir_direction = re.findall(r'\° (.[NSEW]?)', map_location[2])

# altitude integer in km
temp = re.findall(r'\((\d+)', map_location[6])








