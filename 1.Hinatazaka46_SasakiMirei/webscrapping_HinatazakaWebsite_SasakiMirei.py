
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# python 3.7 requirements
# conda install -c anaconda requests
# python -m pip install --upgrade pip
# pip install beautifulsoup4-4.8.2-py3-none-any.whl
# pip install lxml
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


import requests
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)\


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# 佐々木 美玲

def download_blog_images(url = 'https://www.hinatazaka46.com/s/official/diary/detail/32977?ima=0000&cd=member'):
	response = requests.get(url, proxies = None, verify = False)
	if not response.status_code == requests.codes.ALL_OKAY:
		print('Bas response : %s' % response.status_code)

	soup = BeautifulSoup(response.text, 'lxml')

	# Utilize the css selector, see [https://www.w3schools.com/cssref/css_selectors.asp]

	 # img element which has parent of <div class=p-blog-article>
	img_urls_ResultSet = soup.select('div.p-blog-article img') # bs4.element.ResultSet
	img_urls = [ img_src.attrs['src'] for img_src in img_urls_ResultSet] # get the 'src' attribute value
	# print('Now we have')
	# print(img_urls)
	
	# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
	import os
	def download_image(url, targetfolder='./'):
		filename = url.rsplit('/')[-1]
		response = requests.get(url, proxies = None, verify = False)
		print('downloading : %s' % url)
		open(os.path.join(targetfolder, filename), 'wb').write(response.content)

	# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

	import datetime
	download_folder = 'hinatazaka46_%s' % str(datetime.date.today())
	if not os.path.exists(download_folder):
		os.mkdir(download_folder)

	import time
	for img_url in img_urls:
		download_image(img_url, download_folder)
		time.sleep(0.05)


N = 35
urls = ['https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&ct=8&page=%s' % page for page in range(0, N+1)]

for idx, url in enumerate(urls):
	print('Now on page %d' % idx)
	download_blog_images(url)

