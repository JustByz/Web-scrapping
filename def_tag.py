def find_city(tag) -> str:
    city_main_tag =  tag.find(attrs={'data-qa' : 'vacancy-serp__vacancy-address'})
    city = (city_main_tag.text + ' ')[ : city_main_tag.text.find(",")]
    return city


def find_company(tag) -> str:
    company_name = tag.find("div", class_="bloko-text").text
    return company_name


def find_link_vacancy(tag) -> str:
    link_v = tag.find("span", class_="serp-item__title-link-wrapper")
    a_tag = link_v.find("a")
    link_vacancy = a_tag["href"]
    return link_vacancy


def find_salary(soup) -> str:
    salary_main_tag = soup.find("div", class_="vacancy-title")
    salary_tag = salary_main_tag.find("span", class_="bloko-header-section-2 bloko-header-section-2_lite")
    if salary_tag == None:
        return 'Заработная плата не указана'
    else:
        salary = salary_tag.text
        return salary