import requests
from abc import abstractmethod
from user_agent import generate_user_agent, generate_navigator

class Get:
    def __init__(self):
        # self.headers = {"User-Agent": "Mozilla/5.0", "Referer": "http://data.krx.co.kr/"}
        self.headers = {
            'User-Agent': generate_user_agent(device_type='desktop'),
            "Referer": "http://data.krx.co.kr/"
        }
        # print(self.headers)

    def read(self, **params):
        resp = requests.get(self.url, headers=self.headers, params=params)
        return resp

    @property
    @abstractmethod
    def url(self):
        return NotImplementedError


class Post:
    def __init__(self, headers=None):
        # self.headers = {"User-Agent": "Mozilla/5.0", "Referer": "http://data.krx.co.kr/"}
        self.headers = {
            'User-Agent': generate_user_agent(device_type='desktop'),
            "Referer": "http://data.krx.co.kr/"
        }
        # print(self.headers)
        if headers is not None:
            self.headers.update(headers)

    def read(self, **params):
        resp = requests.post(self.url, headers=self.headers, data=params)
        return resp

    @property
    @abstractmethod
    def url(self):
        return NotImplementedError
