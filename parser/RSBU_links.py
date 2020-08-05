from data_links import file_links
from urllib.request import urlopen


def get_RSBU_links(file_links):
    RSBU_links = []
    for key, value in file_links.items():
        rsbu_link = 'https://smart-lab.ru' + value + 'MSFO/download/'
        RSBU_links.append(rsbu_link)
    return RSBU_links

