"""
    This file has various functions for reading the following types of texts:
    1. online news texts
    2. Steele Dossier Report
    3. Donald Trump Testimony
    4. New York Times API
"""
from RelXTract import Source


# reads from Steele_dossier.txt
def read_dossier():
    print("Reading the Dossiers")
    # store information
    articles = []
    # open file
    dossier = open('Sources/Steele_dossier.txt', 'r',
                   encoding='ascii', errors='ignore').read()
    # split the individual texts
    texts = dossier.split("-----------------------------------------------------------------------------------")
    for t in range(len(texts)):
        # get info
        texts[t] = texts[t].strip()
        info = texts[t].split('Summary')[0]
        info_clean = info.split('\n')
        info = [i for i in info_clean if i != '']
        # get text
        try:
            text = texts[t].split('Detail')[1]
        except IndexError:
            continue
        # update
        author = ['Christopher Steele']
        try:
            source_name = info[0].replace('COMPANY INTELLIGENCE REPORT ',
                                            'Steele dossier ')
        except IndexError:
            source_name = 'source not found'
        try:
            date = info[1].replace('[ ', '').replace(' ]', '')
            # weird exception
            if "DEMISE" in date:
                date = info[2].replace('[ ', '').replace(' ]', '')
        except IndexError:
            date = None
        # case of assumed gender (important for co-referencing)
        text = text.replace('S/he', 'She').replace('s/he', 'she')
        source = Source(author, date, text, source_name)
        # append to result
        articles.append(source)
    # return information
    return articles


# reads the web urls for newspaper articles
def read_news():
    from newspaper import Article
    print('reading news sources from "sources.txt"')
    all_urls = []
    sources = open('Sources/sources.txt', 'r').read()
    sources = sources.split('\n')
    for line in sources:
        if len(line) == 0:
            continue
        elif line[0] == '#':
            continue
        all_urls.append(line)
    articles = []
    for url in all_urls:
        print('reading news from:\n', url)
        article = Article(url)
        article.download()
        article.parse()
        authors = article.authors
        date = article.publish_date
        if date is not None:
            date = article.publish_date.strftime('%d/%m/%Y')
        source_url = url
        # weird work-around
        article_ascii = article.text.encode('ascii', 'ignore')
        text = article_ascii.decode('utf-8').replace('\n\n', ' ')
        source = Source(authors, date, text, source_url)
        # add to result
        articles.append(source)
    return articles


# TODO
# reads the Trump testimony file
def read_testimony():
    print("Reading the Testimony")
    # store information
    articles = {'Authors': [], 'Date': [], 'SOURCE': [], 'TEXT': []}
    testimony = open('Sources/Carter_Page_testimony.txt', 'r',
                     encoding='ascii', errors='ignore').read()
    testimony = testimony.replace('\n', '').split('UNCLASSIFIED')
    texts = [i for i in testimony if i != ''][0:50]
    [articles['TEXT'].append(text) for text in texts]
    [articles['Authors'].append(None) for text in texts]
    [articles['Date'].append(None) for text in texts]
    [articles['SOURCE'].append(None) for text in texts]
    return articles


# TODO
# reads new york times archives
