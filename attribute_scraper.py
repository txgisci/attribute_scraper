# metadata Scraper
from requests import get
from bs4 import BeautifulSoup

img_id = 'STS099-744-38'

# core url
url1 = 'https://eol.jsc.nasa.gov/SearchPhotos/photo.pl?mission='
url2 = '&roll='
url3 = '&frame='

img_list = img_id.split('-')
# Formats the final url for given image id
url = '{}{}{}{}{}{}'.format(url1, img_list[0], url2, img_list[1], url3,
                            img_list[2])
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

td_list = soup.find_all('td')

# loop through all table data to isolate specific metadata
# for i in range(20, 30):
#     print(td_list[i])

# index that accesses focul length of image id
focal_length = str(td_list[21])
print(focal_length[4:-5])
