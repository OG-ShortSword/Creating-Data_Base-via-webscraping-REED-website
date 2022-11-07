import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

joblist = []


def getjobs(page):
    url = f'https://www.reed.co.uk/jobs?pageno={page}&sortby=DisplayDate&hideTrainingJobs=True'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    job_info = soup.select('div.col-sm-12.col-md-9.details')
    for item in job_info:
        question = {
            'title': item.select_one("h3.job-result-heading__title").text.strip(),
            'company': item.select_one("a.gtmJobListingPostedBy").text.strip(),
            'post': item.select_one("div.job-result-heading__posted-by").text.strip(),
            'location': item.select_one("li.job-metadata__item.job-metadata__item--location").text.strip(),
            'wage': item.select_one("li.job-metadata__item.job-metadata__item--salary").text.strip(),
            'type': item.select_one("li.job-metadata__item.job-metadata__item--type").text.strip(),
        }
        joblist.append(question)
    return


while True:

    for x in range(1000):
        getjobs(x)
    
    df = pd.DataFrame(joblist)
    df.to_csv('Job_Info')
    print('File Created, Terminating program.')
    sys.exit()
