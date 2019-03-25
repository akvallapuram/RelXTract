import pandas as pd
import read_sources
import sys
import network


def get_actors(sources):
    actors = {'NODE1': [], 'SOURCEINTEXT': [], 'DATE': [],
              'SOURCE': []}
    for source in sources:
        authors = ", ".join(source.authors)
        for actor in source.extract_actors():
            actors['NODE1'].append(actor)
            actors['SOURCEINTEXT'].append(authors)
            actors['DATE'].append(source.date)
            actors['SOURCE'].append(source.title)
    return actors


def get_relations(sources):
    relations = {'NODE1': [], 'NODE2': [], 'DATE': [],
                 'SOURCEINTEXT': [], 'SOURCE': []}
    for source in sources:
        authors = ", ".join(source.authors)
        for relation in source.extract_relations():
            relations['NODE1'].append(relation[0])
            relations['NODE2'].append(relation[1])
            relations['DATE'].append(source.date)
            relations['SOURCEINTEXT'].append(authors)
            relations['SOURCE'].append(source.title)
    return relations


def main():
    sources = ''
    if 'dossier' in sys.argv:
        sources = read_sources.read_dossier()
    elif 'sources' in sys.argv:
        sources = read_sources.read_news()
    elif 'testimony' in sys.argv:
        sources = read_sources.read_testimony()
    else:
        print("ERROR: no source given. Choose from: 'dossier' and 'sources'")
        return
    actors = get_actors(sources)
    relations = get_relations(sources)
    print('Saving relation data to "connections.csv"')
    df = pd.DataFrame(data=relations, columns=relations.keys())
    df.to_csv('Results/connections.csv', sep=',')
    print('Saving actors data to "actors.csv"')
    df1 = pd.DataFrame(data=actors, columns=actors.keys())
    df1.to_csv('Results/actors.csv', sep=',')
    network.draw_network(relations)
    print("Finished Saving. Done!")


if __name__ == '__main__':
    main()
