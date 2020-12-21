import requests
from bs4 import BeautifulSoup
import pprint

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('span',text='citation needed')
    print('The number of citation needed is:',len(results))
    print('*'*33)
    return len(results)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('span',text='citation needed')
    
    final_result = []
    citation = 1
    for x in results:
        if x not in final_result: 
            final_result.append(x)
            
    for element in final_result:
        parent = element.find_parent('p')
        # pprint.pprint(parent.text)
        print(parent.text.strip())
        citation = citation + 1
        print('*'*77)

if __name__ == "__main__":
    get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')