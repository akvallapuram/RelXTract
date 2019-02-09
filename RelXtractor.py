"""
    RelXTractor
    written by Anish Krishna Vallapuram
    09 Feb, 2019
"""
import sys
from newspaper import Article
from nltk.tag import StanfordNERTagger
from nltk.tokenize import sent_tokenize as sentence
from textblob import TextBlob
from itertools import groupby, combinations
import pandas as pd
from string import punctuation


# reads sources.txt and returns urls
def url_from_sources():
    print('reading URLs from "sources.txt"')
    all_urls = []
    sources = open('sources.txt', 'r').read()
    sources = sources.split('\n')
    for line in sources:
        if len(line) == 0:
            continue
        elif line[0] == '#':
            continue
        all_urls.append(line)
    return all_urls


# read the news sources
def read_news(all_urls):
    articles = {'Authors': [], 'Date': [], 'URL': [], 'TEXT': []}
    for url in all_urls:
        print('reading news from:\n', url)
        article = Article(url)
        article.download()
        article.parse()
        articles['Authors'].append(article.authors)
        date = article.publish_date
        if (date is None):
            articles['Date'].append(date)
        else:
            articles['Date'].append(article.publish_date.strftime('%d/%m/%Y'))
        articles['URL'].append(url)
        # weird work-around
        article_ascii = article.text.encode('ascii', 'ignore')
        text = article_ascii.decode('utf-8').replace('\n\n', ' ')
        articles['TEXT'].append(text)
    return articles


# groups the entity tags from STANFORD NER
def grouptags(tags, ignore="O", join=" "):
    for c, g in groupby(tags, lambda t: t[1]):
        if ignore is None or c != ignore:
            if join is None:
                entity = [e for e, _ in g]
            else:
                entity = join.join(e for e, _ in g)
            yield((c, entity))


# removes punctuation
def strip_punct(s):
    return ''.join(c for c in s if c not in punctuation)


# returns all the co-occurences in a give text
def get_relations(articles):
    relations = {'NODE1': [], 'NODE2': [], 'TYPE': [], 'DATE': [],
                 'SOURCE': [], 'URL': [], 'CONTEXT': []}
    gz_path = 'stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz'
    jar_path = 'stanford-ner-2018-10-16/stanford-ner.jar'
    if sys.platform == 'win32':
        gz_path = "stanford-ner-2018-10-16\\classifiers\\english.all.3class.distsim.crf.ser.gz"
        jar_path = 'stanford-ner-2018-10-16\\stanford-ner.jar'
    st = StanfordNERTagger(gz_path, jar_path, encoding='utf-8')
    for text in range(len(articles['TEXT'])):
        print('Analysing for sentiment and relations in:\n',
              articles['URL'][text])
        sentences = sentence(articles['TEXT'][text])
        for sent in sentences:
            # sentiment analysis
            sentiment = TextBlob(sent).sentiment[0]
            if sentiment > 0:
                sentiment = 'positive'
            elif sentiment < 0:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
            # relation extraction
            tags = st.tag(sent.split())
            uniques = []
            for t in tags:
                if t not in uniques:
                    uniques.append(t)
            relate = combinations(grouptags(uniques), 2)
            # add to the output
            for r in relate:
                relations['NODE1'].append(strip_punct(r[0][1]))
                relations['NODE2'].append(strip_punct(r[1][1]))
                relations['TYPE'].append(sentiment)
                relations['DATE'].append(articles['Date'][text])
                relations['SOURCE'].append(','.join(articles['Authors'][text]))
                relations['URL'].append(articles['URL'][text])
                relations['CONTEXT'].append(sent)
    print('Finished Analysing all news sources.')
    return relations


# returns a list of all actors
def get_actors(relation_data):
    print("Collecting Actors")
    actors = {'NODE1': [], 'SOURCE': [], 'DATE': [],
              'URL': []}
    for r in range(len(relation_data['NODE1'])):
        source = relation_data['SOURCE'][r]
        date = relation_data['DATE'][r]
        url = relation_data['URL'][r]
        if relation_data['NODE1'][r] not in actors['NODE1']:
            actors['NODE1'].append(relation_data['NODE1'][r])
            actors['SOURCE'].append(source)
            actors['DATE'].append(date)
            actors['URL'].append(url)
        if relation_data['NODE2'][r] not in actors['NODE1']:
            actors['NODE1'].append(relation_data['NODE2'][r])
            actors['SOURCE'].append(source)
            actors['DATE'].append(date)
            actors['URL'].append(url)
    return actors


def main():
    all_urls = url_from_sources()
    articles = read_news(all_urls)
    relations = get_relations(articles)
    actors = get_actors(relations)
    print('Saving relation data to "connections.csv"')
    df = pd.DataFrame(data=relations, columns=relations.keys())
    df.to_csv('connections.csv', sep=',')
    print('Saving actors data to "actors.csv"')
    df1 = pd.DataFrame(data=actors, columns=actors.keys())
    df1.to_csv('actors.csv', sep=',')
    print("Finished Saving. Done!")


if __name__ == '__main__':
    main()
