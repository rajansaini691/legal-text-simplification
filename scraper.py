
import requests
from bs4 import BeautifulSoup

for i in range(10030, 20000):
    response = requests.get(f"https://edit.tosdr.org/points/{i}")
    if response.status_code != 200:
        continue
    soup = BeautifulSoup(response.text, 'html.parser')

    # Parse original legal text
    legal_text = ''
    for blockquote in soup.find_all('blockquote'):
        for x in blockquote.find_all('footer'):
            x.decompose()
        for x in blockquote.find_all('span'):
            x.decompose()
        for x in blockquote.find_all('strong'):
            x.decompose()
        parsed_line = ''.join(map(lambda x : x.strip().replace('\n', ' '), blockquote.strings))
        legal_text += parsed_line

    # Parse simplified text
    all_h4 = soup.find_all('h4')
    assert(len(all_h4) == 1)
    simplified_text = ''.join(all_h4[0].strings)

    tsv_row = f"{legal_text}\t{simplified_text}"
    print(tsv_row)
