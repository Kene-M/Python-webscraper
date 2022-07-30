import requests 
from bs4 import BeautifulSoup

url = input("Insert website link: ")

#Example
#url = "https://www.geeksforgeeks.org/"
#url = "https://www.facebook.com/"

html = requests.get(url)
doc = BeautifulSoup(html.text, "html.parser")

titleHeader = doc.find("title")
#titleHeader = doc.title

title = titleHeader.text
#title = titleHeader.string

print(title)
#print(doc.prettify())
