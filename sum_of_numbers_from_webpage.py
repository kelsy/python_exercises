# This requires the BeautifulSoup library from:
# https://www.crummy.com/software/BeautifulSoup/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (from Py4E example)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Sample URL:
# http://py4e-data.dr-chuck.net/comments_42.html
url = input("Enter a URL: ")

try:
    html = urlopen(url, context = ssl_context).read()
except:
    print("URL could not be opened:", url)
    quit()

parsed_html = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
spans = parsed_html('span')

sum = 0
count = 0

for span in spans:
    count += 1
    sum += int(span.contents[0])

print("Count", count)
print("Sum", sum)
