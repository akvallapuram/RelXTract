import pandas as pd
import RelXTract
import read_dossier
import read_testimony
from dependency import coreference
import sys


# two features: news sites or dossier
def use_sources():
    all_urls = RelXTract.url_from_sources()
    articles = RelXTract.read_news(all_urls)
    return articles


def use_dossier():
    articles = read_dossier.read_dossier()
    for text in articles['TEXT']:
        text = coreference(text)
    return articles


def main():
    articles = ''
    if 'dossier' in sys.argv:
        articles = use_dossier()
    elif 'sources' in sys.argv:
        articles = use_sources()
    elif 'testimony' in sys.argv:
        articles = read_testimony.read_testimony()
    else:
        print("ERROR: no source given. Choose from: 'dossier' and 'sources'")
        return
    relations = RelXTract.get_relations(articles)
    actors = RelXTract.get_actors(relations)
    print('Saving relation data to "connections.csv"')
    df = pd.DataFrame(data=relations, columns=relations.keys())
    df.to_csv('Results/connections.csv', sep=',')
    print('Saving actors data to "actors.csv"')
    df1 = pd.DataFrame(data=actors, columns=actors.keys())
    df1.to_csv('Results/actors.csv', sep=',')
    print("Finished Saving. Done!")


if __name__ == '__main__':
    main()
