# Metadata Scraper
import requests
from requests import get
from bs4 import BeautifulSoup
import re

# Example image id for testing purposes
img_id = 'ISS039-E-15368'.split('-')

# Core url
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

# Pulls all data from Map Location bottom tab
map_location = (soup.find_all('div', class_='span5')[0].get_text()).split('\n')

# ISS lon lat
iss_coords = [float(i) for i in re.findall(r'\d+\.\d+', map_location[1])]
iss_direction = re.findall(r'\° (.[NSEW]?)', map_location[1])

if iss_direction[0] == 'S':
    iss_coords[0] *= -1
if iss_direction[1] == 'W':
    iss_coords[1] *= -1

# Nadir lon lat
nadir_coords = [float(i) for i in re.findall(r'\d+\.\d+', map_location[2])]
nadir_direction = re.findall(r'\° (.[NSEW]?)', map_location[2])

if nadir_direction[0] == 'S':
    nadir_coords[0] *= -1
if nadir_direction[1] == 'W':
    nadir_coords[1] *= -1

# Altitude integer in km
altitude = [float(i) for i in re.findall(r'\((\d+)', map_location[6])]

# Pulls all data from Image Details bottom tab
image_info = (soup.find_all('div', class_='span12')[0].get_text()).split('\n')

# Features
features = re.findall(r': (.*)', image_info[3])

# Cloud Coverage
cloud_coverage = re.findall(r': (.*)', image_info[4])

# Solar Elevation
solar_elevation = [float(i) for i in re.findall(r'\d+', image_info[5])]

# Solar Azimuth
solar_azimuth = [float(i) for i in re.findall(r'\d+', image_info[6])]

# Pulls all data from Camera Information bottom tab
camera_info = (soup.find_all('div', class_='span12')[1].get_text()).split('\n')

# Camera
camera = re.findall(r': (.*)', camera_info[2])

# Focal Length
focal_length = [int(i) for i in re.findall(r'\d+', camera_info[3])]

# Format
format = re.findall(r': (.*)', camera_info[5])

# Film exsposure
film_exposure = re.findall(r': (.*)', camera_info[6])
