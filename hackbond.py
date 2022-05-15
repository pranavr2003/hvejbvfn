import requests
from bs4 import BeautifulSoup
import geocoder

def yoga_centres_city(city_name = 'delhi'):

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
    }

    page = requests.get(f'https://duckduckgo.com/html/?q=yoga+centres+in+{city_name}+justdial', headers=headers).text
    soup = BeautifulSoup(page, 'html.parser').find_all("a", class_="result__url", href=True)

    for link in soup:
        website_city = link['href']
        break;

    # print(website_city)

    web_page_from_search = requests.get(website_city, headers=headers).text
    soup_from_search = BeautifulSoup(web_page_from_search, 'html.parser')

    yoga_centres_names = []
    latitude_longitude_respectively = []

    for yoga_centre in soup_from_search.find_all('div', attrs={'class':'col-sm-5 col-xs-8 store-details sp-detail paddingR0'}):
        # print(yoga_centre.find('span', {'class':'lng_cont_name'}))
        # print(yoga_centre.find('span', {'class':'lng_cont_name'}).text)
        yoga_centres_names.append(yoga_centre.find('span', {'class':'lng_cont_name'}).text)
    
    # return yoga_centres_names    # returns 10 yoga centres names in a list

    for centre in yoga_centres_names:
        g = geocoder.bing(f'{centre}, {city_name}', key='AkM1C1tjs3zYcRsDCvrigXhmIKcy81N5o7J3VY8-paTqSKuQQSnMiIWAe3UN0u22')
        results = g.json
        latitude_longitude_respectively.append([results['lat'], results['lng']])

    return [yoga_centres_names, latitude_longitude_respectively]

print(yoga_centres_city('delhi'))     # better if the name of the city was in small letters - does make a difference