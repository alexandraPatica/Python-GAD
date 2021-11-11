import requests
from bs4 import BeautifulSoup

standings = []
lpf_domain = 'http://frsah.ro/'
columns = ['image', 'title', 'date', 'text']

if __name__ == '__main__':
    page = requests.get(f'{lpf_domain}')
    soup = BeautifulSoup(page.content, features='html.parser')

    # content = soup.find('div', {"class": 'td-ss-main-content td_block_template_1'})
    content = soup.find(class_='td-ss-main-content td_block_template_1').find_all('div')
    print(content)

    news = content.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')
    # print(news)
    for new in news:
        divs = new.find_all('div')
        text_from_divs = [
            div for div in new.find_all('div')
        ]
        # print(text_from_divs)
        data_from_news = []
        img_src = divs[1].find('img')['src']
        title = divs[2].find('h3')

        data_from_news.append(divs[1].find())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
