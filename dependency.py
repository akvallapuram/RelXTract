import spacy
import read_sources
from nltk import Tree


# get dependency tree
def dependency_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [dependency_tree(child)
                                 for child in node.children])
    else:
        return node.orth_


# print tree
def print_tree(sent):
    dependency_tree(sent.root).pretty_print()


# annotates the text with nlp data and resolves coreferences
def annotate(text):
    print('Resolving coreferences')
    coref = spacy.load('en_coref_lg')
    doc = coref(text)._.coref_resolved
    print('Annotating for NLP features')
    en_nlp = spacy.load('en_core_web_sm')
    doc = en_nlp(doc)
    return doc


# find the root of a sentence
def find_root(docu):
    for token in docu:
        if token.head is token:
            return token


# returns source if any in the sentence.
# def get_source(sent):

#get actors
def get_actors(doc, text):
    ignore_list = ['CARDINAL']
    actors = {'NODE1': [], 'TYPE': [], 'ALIAS': [], 'DATE': [], 'SOURCE': []}
    for ent in doc.ents:
        actors['NODE1'].append(ent.text)
        actors['LABEL'].append(ent.label_)
        actors['SOURCE'].append(text[''])



# checks if two entities are related
# def is_relation(sent):

def main():
    text = read_sources.read_dossier()['TEXT'][0]
    doc = annotate(text)
    sent = list(doc.sents)[1]
    [print(ent.text) for ent in sent.ents]
    [print(chunk) for chunk in sent.noun_chunks]
    print_tree(sent)


if __name__ == '__main__':
    main()
