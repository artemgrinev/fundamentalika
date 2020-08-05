import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_html(url):
    r = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    return r.text


def get_data_links(html):
    all_data_links = {}

    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', class_ = 'simple-little-table little trades-table').find_all('tr')
    for i in table:
        try:
            name = i.find_all('a')[0].text
        except:
            name = ''
            
    links = i.find_all('a', class_ ='charticon2')
    for i in links:
        try:
            link = i.get('href')
        except:
            link = ''
        data = {name:link}
        all_data_links.update(data)
    return all_data_links


def file_links():
    url = 'https://smart-lab.ru/q/shares_fundamental/'
    return get_data_links(get_html(url))


if __name__ == '__main__':
    file_links()