from bs4 import BeautifulSoup
import re

#import requests

with open('tpl.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


#print (soup.prettify())

    pricebox = soup.find('div', class_='pricing-column')

    variant = pricebox.h3.text

    price = pricebox.h4.text
    price = price.split(' ')
    price = price[3]

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


    image = pricebox.img['src']


    #print (tax_splitted)
    #print(filer)
    #print (non_filer)


    print ()