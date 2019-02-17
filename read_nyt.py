from urllib.request import urlopen


# python wrapper for archive search
def read_nyt_archive(year, month, dict):
    if 'api-key' not in dict.keys():
        print('Error: No API key.')
        return
    request = 'https://api.nytimes.com/svc/archive/v1/{}/{}.json?'.format(year, month)

    for key, value in dict.items():
        if key != 'api-key':
            request += '&{}={}'.format(key, value)
    request += '&{}={}'.format('api-key', dict['api-key'])
    json = urlopen(request).read()
    return json


def read_nyt_article(url, api_key):
    request = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'
    web_url = url
    if 'https://' in url:
        web_url.replace('https://', '')
    request += 'fq=web_url:' + web_url
    request += '&api-key=' + api_key
    json = urlopen(request).read()
    return json


if __name__ == '__main__':
    json = read_nyt_article('https://www.nytimes.com/2018/09/15/us/politics/jim-mattis-trump-defense-relationship.html', 'jevVlFssmqtMh2RwcUHSGkkGpb4uzeG5')
    print(json)
