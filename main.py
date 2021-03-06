import requests
from bs4 import BeautifulSoup
import pprint

# Make request
res = requests.get('https://news.ycombinator.com/news?p=1')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# Parse the data
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# Get the data
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({
                    'title': title,
                    'link': href,
                    'votes': points
                })
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
