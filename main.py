import pandas as pd
import RelXTractor
import read_dossier
import read_testimony
import sys


# two features: news sites or dossier
def use_sources():
    all_urls = RelXTractor.url_from_sources()
    articles = RelXTractor.read_news(all_urls)
    return articles


def use_dossier():
    articles = read_dossier.read_dossier()
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
    relations = RelXTractor.get_relations(articles)
    actors = RelXTractor.get_actors(relations)
    print('Saving relation data to "connections.csv"')
    df = pd.DataFrame(data=relations, columns=relations.keys())
    df.to_csv('connections.csv', sep=',')
    print('Saving actors data to "actors.csv"')
    df1 = pd.DataFrame(data=actors, columns=actors.keys())
    df1.to_csv('actors.csv', sep=',')
    print("Finished Saving. Done!")


if __name__ == '__main__':
    main()
