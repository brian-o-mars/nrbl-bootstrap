from bs4 import BeautifulSoup as bs
import requests

url = "https://scholar.google.com/citations?hl=en&user=87rhAcgAAAAJ&view_op=list_works&sortby=pubdate"

result = requests.get(url)

doc = bs(result.text, "html.parser")


print("**************************")
print(doc.prettify())
print("**************************")


