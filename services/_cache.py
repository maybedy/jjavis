import pymongo as mongo
from datetime import datetime

class NaverNewsCache:
    def __init__(self):
        # Each cache expired after 1 hour (only 1 update acceptable for each cache in an hour)
        self._headline_cache = {}
        self._headline_cache_last_update = {}
        self._ranking_cache = {}
        self._ranking_cache_last_update = {}
        self._main_news_cache = None
        self._main_news_cache_last_update = None

    def get_headline_news(self, section):
        if section not in self._headline_cache_last_update \
                or (datetime.now() - self._headline_cache_last_update[section]).min() > 60:
            return None
        return self._headline_cache[section]

    def set_headline_news(self, section, contents):
        self._headline_cache[section] = contents
        self._headline_cache_last_update[section] = datetime.now()

    def get_ranking_news(self, section):
        if section not in self._ranking_cache_last_update \
                or (datetime.now() - self._ranking_cache_last_update[section]).min() > 60:
            return None
        return self._ranking_cache[section]

    def set_ranking_news(self, section, contents):
        self._ranking_cache[section] = contents
        self._ranking_cache_last_update[section] = datetime.now()

    def get_main_news(self):
        if self._main_news_cache_last_update is None \
            or (datetime.now() - self._main_news_cache_last_update).min() > 60:
            return None
        return self._main_news_cache

    def set_main_news(self, contents):
        self._main_news_cache = contents
        self._main_news_cache_last_update = datetime.now()

