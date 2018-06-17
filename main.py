from rest_api import run_api_server
from configurations import * # TODO
from services import naver_news

if __name__ == '__main__':
    service = naver_news.NaverNewsService()
    service.get_news("주식")