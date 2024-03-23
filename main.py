import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import csv
from tqdm import tqdm 
from def_tag import find_city, find_company, find_link_vacancy, find_salary


def gen_headers():
    headers = Headers(browser='chrome', os='win')
    return headers.generate()

    
def find_main(key1:str, key2:str) -> list:
    result_list = [['link', 'salary', 'company name', 'city']]
    main_link = f'https://spb.hh.ru/search/vacancy?area=1&area=2&ored_clusters=true&text={key1}%2C+{key2}&order_by=publication_time'
    
    response = requests.get(main_link, headers=gen_headers())
    main_html = response.text
    main_soup = BeautifulSoup(main_html, "lxml")

    article_tags = main_soup.find_all("div", class_="serp-item serp-item_link")

    for article_tag in article_tags:
        
        response = requests.get(find_link_vacancy(article_tag), headers=gen_headers())
        page_html = response.text
        page_soup = BeautifulSoup(page_html, "lxml")

        result_list.append([find_link_vacancy(article_tag), find_salary(page_soup), find_company(article_tag), find_city(article_tag)])
        
    return result_list



if __name__ == "__main__":
    
    with open("hhparsed.csv", "w", newline='', encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(find_main('django', 'flask'))