from urllib import request
goog_url="http://real-chart-finance.yahoo.com/table-csv?s=GOOG&d=8&e=2&f=2014&g=d&a=2&b=27&c=2014&ignore=.csv"
#we need a function to download the data from the file

def download_stock_data(csv_url):
	response=request.urlopen(csv_url)
  csv=response.read()#this will read all the data from the url you pointed it to
	csv_str=str(noname)#this will convert the the no name variable we read to a string
	lines=csv_str.split('\\n')
	dest_url()= r'goog.csv'#this is a raw string make a file
	fx=open(dest_url, "w")
	for line in lines:
	  fx.write(line + "\n")
	fx.close()
download_stock_data(goog_url)
