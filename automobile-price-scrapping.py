#This script scrapes, price list of automobiles from the given website.

from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import os
import re


############
# Parsing current date and time to form the output filename.

now = datetime.now()
base_filename = now.strftime("%d%m%Y-%H%M%S")
basefilename = 'TCM-Price_list-'+base_filename
extension ="csv"
dir_name = 'Price-List-Output-Direcotry'
filename = os.path.join(dir_name, base_filename + "." + extension)

############

link = 'https://toyota-central.com/Vehicle/PriceList'
source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')


# Scrapping Data and writing CSV
with open(filename, 'w', newline="") as f:
    data_handler = csv.writer(f, delimiter=",")
    data_handler.writerow(['Variant','Price', 'Tax (Filer)', 'Tax  (Non-Filer)','Image_link'])

    for pricebox in soup.find_all('div', class_='pricing-column'):

        # Variant
        variant = pricebox.h3.text

        # Price
        price = pricebox.h4.text
        price = price.split(' ')
        price = price[3]
        price = price.strip()

        # Tax
        taxbox = pricebox.div.ul.text
        taxbox = taxbox.split('\nNon')
        filer_data = taxbox[0]
        filer_data = filer_data.split(' ')
        non_filer_data = taxbox[1]
        non_filer_data = non_filer_data.split(' ')

        tax_filer = "N/A"
        non_tax_filer = "N/A"

        for entry in filer_data:
            if re.search("^(\d+|\d{1,3}(,\d{3})*)(\.\d+)?$", entry):
                tax_filer = entry

        for entry in non_filer_data:
            if re.search("^(\d+|\d{1,3}(,\d{3})*)(\.\d+)?$", entry):
                non_tax_filer = entry

        # Vehicle Image
        image = pricebox.img['src']
        image = image.replace('..','https://toyota-central.com')
        data_handler.writerow([variant, price, tax_filer, non_tax_filer, image])


print ('Scrapping Completed Successfully')
