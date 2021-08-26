from bs4 import BeautifulSoup
import requests
import csv
#print(chr(27) + "[2J")
url= "http://www.values.com/inspirational-quotes"
res=requests.get(url)
#print(res.content)      # raw HTML content of the webpage. It is of ‘string’ type

soup=BeautifulSoup(res.content,'html5lib')   # Parsing the HTML content
#print(soup)
#print(soup.prettify())   #it gives the visual representation of the parse tree created from the raw HTML content.

quotes = [] # a list to store quotes

table = soup.find('div', attrs = {'id':'all_quotes'})  #div with id all_quotes
#print(table)

for i in table.findAll('div',attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = i.h5.text
    quote['url'] = i.a['href']
    quote['img'] = i.img['src']
    quote['lines'] = i.img['alt'].split(" #")[0]
    quote['author'] = i.img['alt'].split(" #")[1]
    quotes.append(quote)


filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)








# containers = soup.find_all("div",{"class": "_3O0U0u"})

# for i in containers:  
#     product_name = i.div.img["alt"]  
  
#     price_container = i.find_all("div", {"class": "col col-5-12 _2o7WAb"})  
#     price = price_container[0].text.strip()  
  
#     rating_container = i.find_all("div",{"class":"niH0FQ"})  
#     ratings = rating_container[0].text  

#     print("name",product_name)