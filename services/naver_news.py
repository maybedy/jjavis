import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# add some restriction method preventing over request
headline_news_url_path = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1="
headline_news_section_id = {
    'politics': '100',
    'economics': '101',
    'society': '102',
    'life/culture': '103',
    'world': '104',
    'it/science': '105',
}

main_news_url_path = "http://news.naver.com/main/history/mainnews/index.nhn"
ranking_news_url_path = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId="
naver_news = "http://news.naver.com"

def get_soup(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        soup = BeautifulSoup(response_body, 'lxml', from_encoding='utf-8')
        return soup
    else:
        raise Exception("Error code {}".format(str(rescode)))

class NaverNewsService:
    def __init__(self):
        pass

    def get_headline_keys(self):
        return headline_news_section_id.keys()

    def get_headline_news(self, section):
        assert section in headline_news_section_id
        url_path = "{}{}".format(headline_news_url_path, headline_news_section_id[section])
        soup = get_soup(url_path)

        news_cluster_list = soup.find_all('ul', {'class', 'cluster_list'})
        count = 0
        return_news_cluster_list = []
        for news_cluster in news_cluster_list:
            return_news_cluster_list.append([])
            news_list = news_cluster.find_all('li', {'class', 'cluster_item'})
            for news in news_list:
                link = news.findChild('a', {'class': 'cluster_text_headline'})
                press = news.findChild('div', {'class', 'cluster_text_press'}).contents[0]
                link_href = link.attrs['href']
                link_content = link.contents[0]
                return_news_cluster_list[count].append((link_href, link_content, press))
            count+=1
        return return_news_cluster_list

    def get_ranking_news(self, section):
        assert section in headline_news_section_id
        url_path = "{}{}".format(ranking_news_url_path, headline_news_section_id[section])
        soup = get_soup(url_path)

        ranking_list = soup.find_all('li', {'class', 'ranking_item'})
        return_rank_news_list = []

        for rank_news in ranking_list:
            news = rank_news.findChild('div', 'ranking_headline')
            link = news.findChild('a')
            link_href = "{}{}".format(naver_news, link.attrs['href'])
            link_content = link.contents[0]
            press = rank_news.findChild('div', 'ranking_office').contents[0]
            link_detail = rank_news.findChild('div', 'ranking_lede').contents[0]
            link_detail = link_detail.strip()

            content = (link_href, link_content, press, link_detail)
            return_rank_news_list.append(content)
        return return_rank_news_list

    def get_main_news(self, date=None, time=None):
        if date and time:
            pass
        soup = get_soup(main_news_url_path)
        news_list = soup.find_all('div', {'class', 'newsnow_tx_inner'})
        return_news_list = []
        for news in news_list:
            link = news.findChild('a')
            link_href = link.attrs['href']
            link_content = link.contents[0]
            return_news_list.append((link_href, link_content))
        return return_news_list
#
#
# class NaverNewsSearchService:
#     def __init__(self):
#         self.url_path = 'https://openapi.naver.com/v1/search/news.json'
#         pass
#
#     def get_news(self, query):
#         query = urllib.parse.quote(query)
#         request = urllib.request.Request("{}?query={}".format(self.url_path, query))
#         request.add_header('X-Naver-Client-Id', client_id)
#         request.add_header('X-Naver-Client-Secret', client_secret)
#
#         response = urllib.request.urlopen(request)
#         rescode = response.getcode()
#
#         if rescode == 200:
#             response_body = response.read()
#             response_body_json = response_body.decode('utf-8')
#             print(response_body_json)
#         else:
#             print("Error\n{}".format(rescode))
#


