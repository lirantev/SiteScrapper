from lxml import html
import requests

page = requests.get('http://google.com', verify=False)
tree = html.fromstring(page.content)
#images = tree.xpath('//img/@src')
links = tree.xpath('//a/@href')
if len(links) == 0:
	print("no links found")
else:
	for x in links:
		print (x)