from urllib import request
import requests as req
import time
from fake_useragent import UserAgent
#from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import tqdm
import json

print ('Эта программа парсит HH на предмет вакансий python разработчик и собранные данные сохраняет в файл vacancies.json')

data = {
    "vacancies" : []
}
i = 1
for p in range(0,40):
    page_title = F"------- PAGE {p} ----------"
    print ( page_title )
    url = f'https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&clusters=true&area=113&ored_clusters=true&enable_snippets=true&page={p}'
    ua_headers = {"User-Agent":UserAgent().firefox}
    resp = req.get(url, headers=ua_headers)
    #time.sleep ( 2 )
    #print (resp)
    soup = BeautifulSoup( resp.text, "lxml")
    #tags = soup.find_all(class_="serp-item__title")
    vacancies = soup.find_all(attrs={"data-page-analytics-event":"vacancy_search_suitable_item"})
    #print (vacancies)

    for v in tqdm.tqdm(vacancies):
        time.sleep (2)
        v_title = v.a.text
        v_url = v.a.get('href')
        v_resp = req.get(v_url, headers={"User-Agent":UserAgent().firefox})        
        v_soup = BeautifulSoup ( v_resp.text, 'lxml' )
        v_salary = v_soup.find(attrs={"data-qa":"vacancy-salary"})
        if v_salary : 
            v_salary = v_salary.text
        v_experience = v_soup.find(attrs={"data-qa":"vacancy-experience"})
        if v_experience :
            v_experience = v_experience.text
        v_region = v_soup.find(attrs={"data-qa":"vacancy-view-raw-address"})
        if v_region and v_region.contents and v_region.contents[0]:
            v_region = v_region.contents[0]
        #print (i, v_title, v_salary, v_experience, v_region )
        i = i + 1
        data["vacancies"].append({"title":v_title, "salary":v_salary, "experience":v_experience, "region":v_region})
        
    with open ("vacancies.json", "w") as f:
        json.dump(data, f, ensure_ascii='false')
