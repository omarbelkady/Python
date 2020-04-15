import random
import urllib.request #allows us to download data from websites
def download_web_image(url):
	name=random.randrange(1,1000)
	full_name=str(name)+“.jpg”	#converting name from number to a string
	#urllib.request.urlretrieve(url, whatdoyouwanttonamefile)
	urllib.request.urlretrieve(url,full_name)#downloadtheimage
download_web_image(“https://i.pinimg.com/474x/85/70/5f/85705f58dfae3341afe10b61a82f92ad--custom-pc-pc-gamer.jpg”)
