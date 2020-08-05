from data_links import file_links

def get_MSFO_links(file_links):
    MSFO_links = []
    for key, value in file_links.items():
        msfo_link = 'https://smart-lab.ru' + value + 'MSFO/download/'
        MSFO_links.append(msfo_link)
    return MSFO_links

