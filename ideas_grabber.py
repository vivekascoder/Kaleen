#!/usr/bin/env python
"""
This script will scrap all the ideas of Ideasgrab site and make a json file out of it.
:: Filename: ideas.json
:: Data:
	{
		"ideas": ["IDEA-1", "IDEA-2", ...]
	}
"""


import json
import random
from requests_html import HTMLSession


# Configurations
OUTPUT_FILENAME = "ideas.json"
WEBSITE_URL = "https://www.ideasgrab.com/"
LI_XPATH = "/html/body/main/article/div[1]/div/div/div[2]/div/div/div/ol/li"
DATA = {
	"ideas": []
}



# Scraping Goes Here...
session = HTMLSession()

response = session.get(WEBSITE_URL)
li_s = response.html.xpath("li")

for li in li_s:
	DATA["ideas"].append(li.text)



# Exporting to json file
with open(OUTPUT_FILENAME, "w") as file:
	json.dump(DATA, file)


print("[KALEEN]::", "Scrapped all the ideas.")
