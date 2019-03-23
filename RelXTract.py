"""
    RelXTract
    written by Anish Krishna Vallapuram
    15 February, 2019
"""
import dependency
import read_sources


class Source:

    def __init__(self, authors, date, text, title):
        self.authors = authors
        self.date = date
        self.text = text
        self.title = title
        self.actors = []
        self.relations = []
        self.doc = dependency.annotate(self.text)
        self.trees = [dependency.dependency_tree(sent.root)
                      for sent in self.doc.sents]

    # add actor
    def add_actor(self, actor):
        self.actors.append(actor)

    # realises actors
    def extract_actors(self):
        ignore_ents = ['CARDINAL', 'DATE', 'PRODUCT', 'EVENT',
                       'FAC', 'WORK_OF_ART']
        for ent in self.doc.ents:
            if ent.label_ not in ignore_ents and ent.text not in self.actors:
                self.add_actor(ent.text)
        print("extracted actors from " + self.title)
        return self.actors

    # get relations
    def extract_relations(self):
        for actor in self.actors:
            print(actor.name, actor.ent.pos_, actor.ent.dep_)
        print("extracted relations from " + self.title)


def main():
    text = read_sources.read_dossier()[0]
    actors = text.extract_actors()
    print(text.text)
    print(actors)


if __name__ == '__main__':
    main()
