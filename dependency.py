import spacy
from nltk import Tree

# build tree
# coreference: replace all names with their full names
# find the entities
# is_relation (tree search)


# annotates the text with nlp data and resolves coreferences
def annotate(text):
    print('Resolving coreferences')
    coref = spacy.load('en_coref_lg')
    doc = coref(text)._.coref_resolved
    print('Annotating for NLP features')
    en_nlp = spacy.load('en_core_web_sm')
    doc = en_nlp(doc)
    return doc


# get dependency tree
def dependency_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [dependency_tree(child)
                                 for child in node.children])
    else:
        return node.orth_


# searches for a node in a tree
def search_tree(node):
    if node.n_lefts + node.n_rights > 0:
        print(node.text, node.ent_id_)
        [search_tree(child) for child in node.children]
    else:
        return


# print tree
def print_tree(tree):
    tree.pretty_print()
