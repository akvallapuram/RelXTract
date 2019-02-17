"""
    RelXTract
    written by Anish Krishna Vallapuram
    15 February, 2019
"""
import dependency
import read_sources


class Actor:

    def __init__(self, name, ent):
        self.name = name
        self.ent = ent
        self.aliases = []
        self.sources = []
        self.relations = []

    def add_alias(self, al):
        self.aliases.append(al)

    def add_source(self, source):
        self.sources.append(source)


class Source:

    def __init__(self, authors, date, text, source):
        self.authors = authors
        self.date = date
        self.text = text
        self.source = source
        self.actors = []
        self.doc = dependency.annotate(self.text)

    # add actor
    def add_actor(self, actor):
        self.actors.append(actor)

    # realises actors
    def extract_actors(self):
        for ent in self.doc.ents:
            if ent.label_ not in ['CARDINAL', 'DATE']:
                new_actor = Actor(ent.text, ent)
                new_actor.add_source(self)
                self.add_actor(new_actor)

    # get relation
    def extract_relations(self):
        for ent in self.doc.ents:
            print('ent: ', ent.text, ' head: ', list(ent)[-1].head.text, ' type:', list(ent)[-1].head.type)


if __name__ == '__main__':
    text = read_sources.read_dossier()[0]
    text.extract_relations()
