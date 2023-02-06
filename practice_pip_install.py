from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 콘솔 >> pip install beautifulsoup4
# 콘솔 >> pip list
# 콘솔 >> pip show beautifulSoup4
# 콘솔 >> pip --upgrade beautifulsoup4
# 콘솔 >> pip uninstall beautifulsoup4
#     >> y
