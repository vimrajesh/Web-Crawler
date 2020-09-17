import  urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# javascript:void(0)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter:-")
html = urllib.request.urlopen(url, context = ctx).read()

soup = BeautifulSoup(html,"html.parser")

# print(soup.get_text())
print("..............................")
# retrieving
tags = soup("a")
for tag in tags:
    if (tag.get("href",None)) == "javascript\:void(0)":
        tag.contents[0]

    print("..............................")

    javascript:void(0)