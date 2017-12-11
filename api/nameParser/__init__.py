import requests
from bs4 import BeautifulSoup

ROOT_URL = 'http://www.babynames.net'


class NameParser:
    def callByEnglishName(self, name):
        subPath = '/names/'
        responseOfHtml = requests.get(ROOT_URL + subPath + name)
        soupedResponse = BeautifulSoup(responseOfHtml.text, "html.parser")
        soupedResponse = soupedResponse.find('div', attrs={'class': 'main-col'})
        if soupedResponse is None:
            return {}
        commonInforms = soupedResponse.find('div', attrs={'class': 'name-info-left'}).find_all('dl')
        country = commonInforms[0].dd.text
        pronunciation = commonInforms[1].dd.text
        meaning = commonInforms[2].dd.text
        gender = 'boy'
        if soupedResponse.find('span', attrs={'class': 'result-gender boy'}) is None:
            gender = 'girl'

        randomName = soupedResponse.find('a', attrs={'class': 'random'})['href'].replace('/names/', '')
        return {'name': name, 'country': country, 'pronumciation': pronunciation, 'meaning': meaning, 'gender': gender,
                'random_name': randomName}

    def callAnyName(self):
        return self.callByEnglishName(self.callByEnglishName('torborg').get('random_name'))

