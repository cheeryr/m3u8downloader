# -*- coding:utf-8 -*-  
import requests
import os
import datetime
import re
# file name
name = 'lecture#2.mp4'
#m3u8 url
url = 'https://cfvod.kaltura.com/scf/hls/p/2011531/sp/201153100/serveFlavor/entryId/1_3qusz2fr/v/11/ev/3/flavorId/1_zjdnoc0h/name/a.mp4/index.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMjAxMTUzMS9zcC8yMDExNTMxMDAvc2VydmVGbGF2b3IvZW50cnlJZC8xXzNxdXN6MmZyL3YvMSoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1NzcwNDE1Mjl9fX1dfQ__&Signature=WV7YtKkNAYLg2Y1SJFm4xriOWRxQvLKKl-0rPAr~aFQbV4DgbDNCw7BKKLkJhjQCZt18luoSXgZ88mr~qwHgjw9~Nx7r0wta9vgHX0hG5YwQsA5C-3UOQ5xKdSBRzxHntZGNMqtPnWXYI2yn4AXXBFCOsBAU0~osjPKm6YchOfToTnB-oBue6XsWDHZF0g~ygwPxsPNOVnxPBF24-ZjK84YIwokJ54eeCFho4gXCBBAxHoYoLTa4Fy5-XWSTpLShsLlYeCTytZpEbG7qUrwrB4WjvCnxBmbx2-nrL~Xm7vNyDpS4DHURUFpnddbGvVQSv2nefSKGhVe28NSx9Bj7tw__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#get m3u8 file
r = requests.get(url,headers=headers)
t = re.compile(r"https://.*?\.ts.*")
ts_urls = t.findall(r.text)
#print(ts_urls)
count = 1
for ts_url in ts_urls:
	ts = requests.get(ts_url).content
	with open(name, "ab") as file:
		#write into file
		file.write(ts)
		print("downloading: #", count)
		count=count+1
print(name,"Download success")

