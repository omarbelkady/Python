import request
from bs4 import BeautifulSoup #this package imports all the data from the website

def trade_spider(max_pages):
	page=1
	while page < max_pages:
		url= "https://buckyroom.org/trade/search.php?page="+str(page)
		source_code=request.get(url)
		#all the page source is now stored in the source_code variable
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)#creating a beautiful soup object
		#go to page source to find all the links for specific articles to browse in a class
		for link in soup.findAll('a',{'class': 'item-name'}): #getting all the titles
			href= "http://buckyroom.org/"+link.get(href)#we want only the data in the href
				title=link.string()
				#print(href)
        #print(title)
			page += 1

def get_single_item_data(item_url): 
	source_code=request.get(item_url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	#for item_name in soup.findAll('a', {'class': 'item-name'}):
	for item_name in soup.findAll('div', {'class': 'i-name'}):
print(item-name.string)
#how to crawl a page that is a link on the page you already crawled
for link in soup.findAll('a'):
	href= "http://www.buckysroom.org" + link.get('href')
print(href)
	
	
trade_spider(3)#crawling 3 pages
