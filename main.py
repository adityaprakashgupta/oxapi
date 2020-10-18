from bs4 import BeautifulSoup
import requests

word = 'run'
def getdata(word):
    url = f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}?q={word}'

    data = requests.get(url).text

    soup = BeautifulSoup(data, 'html.parser')

    try:
        is_syno = False
        name = soup.h1.get_text()
        pos = soup.find('span', class_= 'pos').get_text()
        definition = [i.get_text() for i in soup.find_all('span', class_= 'def')]
        examples = [i.get_text() for i in soup.find_all('span', class_= 'x')]

        try:
            if soup.find('span', class_= 'prefix').get_text().lower() == 'synonym':
                syno = soup.find('span', class_= 'xh').get_text()
                is_syno =True
        except:
            is_syno = False

        filter_data = {
            'word': name,
            'pos': pos,
            'definition': definition,
            'examples': examples,
            'code': 200
        }
        if is_syno:
            filter_data["synonyms"] = syno

    except:
        filter_data = {'status': 'word dose not found', 'code': 404}

    return filter_data

if __name__ == '__main__':
    print(getdata('demoo'))
