import re
from urllib.request import urlopen as open


url = "http://olympus.realpython.org/profiles/dionysus"
page = open(url)
html = page.read().decode("utf-8")
pattern = "<title.*?>.*?</title.*?>"


match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

print(title)