import random
import re

from lxml import html
import requests

# website with lists of moods (stored as <li> items in html format)
URL = 'http://examples.yourdictionary.com/mood-examples.html'

# extracting list of moods from webpage (ignoring whitespace entries)
page = requests.get(URL)
tree = html.fromstring(page.content)
all_moods = [name for name in tree.xpath('//li/text()') if name.strip()]


def get_mood():
    '''
    Selects a random mood from the list of all moods
    input: None
    output: String
    '''
    mood = random.choice(all_moods)
    return 'Yo Dog, today I feel {}'.format(mood)


if __name__ == '__main__':
    print('Getting 3 random moods for our bot: ')
    for i in range(3):
        print(get_mood())