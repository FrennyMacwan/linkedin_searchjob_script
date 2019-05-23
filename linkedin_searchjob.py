"""
Created on Mon May 10 09:45:24 2019

@author: frenny
"""
#list of jobs in munich
from bs4 import BeautifulSoup
import requests

page_link ='https://www.linkedin.com/jobs/search?keywords=&location=%2C%20Germany&trk=homepage-jobseeker_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'

page_response = requests.get(page_link, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

textContent = []

for i in range(0, 200):
    paragraphs = page_content.find_all("h3", class_ ="result-card__title job-result-card__title")[i].text
    textContent.append(paragraphs)
    
print(textContent)
