"""
    RelXTract
    written by Anish Krishna Vallapuram
    15 February, 2019
"""
import dependency
from itertools import combinations


class Source:

    def __init__(self, authors, date, text, title):
        self.authors = authors
        self.date = date
        self.text = text
        self.title = title
        self.actors = []
        self.relations = []
        self.doc = dependency.annotate(self)
        self.trees = [dependency.dependency_tree(sent.root)
                      for sent in self.doc.sents]

    # add actor
    def add_actor(self, actor):
        self.actors.append(actor)

    # realises actors
    def extract_actors(self):
        allowed_types = ['PERSON', 'ORG', 'NORP', 'GPE', 'LOC']
        for ent in self.doc.ents:
            if ent.label_ in allowed_types:
                self.add_actor(ent)
        print("extracted actors from " + self.title)
        # unique array of actors
        str = []
        [str.append(actor.text) for actor in self.actors if actor.text not in str]
        return str

    # get relations
    def extract_relations(self):
        if len(self.actors) == 0:
            self.extract_actors()
        potential_relations = combinations(self.actors, 2)
        for rel in potential_relations:
            if rel[0].text != rel[1].text and \
               dependency.verb_dep(rel[0]) == dependency.verb_dep(rel[1]):
                self.relations.append(rel)
        print("extracted relations from " + self.title)
        return [(rel[0].text, rel[1].text) for rel in self.relations]

    def show_actors(self):
        ", ".join([actor.text for actor in self.actors])
