import spacy
from nltk import Tree

# build tree
# coreference: replace all names with their full names
# find the entities
# is_relation (tree search)


# Problem 1: coreferencing relative clauses
def corelcl(text):
    clauses = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "relcl":
                subj = " ".join([c.text for c in list(token.head.subtree)
                                 if c not in list(token.subtree)
                                 and c.is_punct is False])
                clause = " ".join([subj if i.dep_ == "nsubj" else i.text
                                   for i in token.subtree]) + "."
                clauses.append(clause)
    result = " ".join(clauses)
    return(result)

# Problem 2: coreferencing possesive pronouns
# doc = coref(u'Trump is the president of US. His ally is Putin.')
# print(doc._.coref_clusters[0].main)
# # [print(token) for token in doc]
# x = doc._.coref_clusters[0].mentions[-1]
# print(x)
# print(x.doc[x.start].dep_)
# print(x.doc[x.start]._.in_coref)


# Problem 3: coreferencing appositional modifiers.


# Problem 4: Traverse till first verb
def verb_dep(ent):
    verb = ent[-1]
    while verb.pos_ != "VERB" and verb.dep_ != "xcomp":
        verb = verb.head
    return verb.text


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


if __name__ == "__main__":
    coref = spacy.load('en_coref_lg')
    nlp = spacy.load("en_core_web_sm")
    sent = "This was confirmed by Source D, a close associate of Trump who had organized and managed his recent trips to Moscow."
    doc = nlp(sent)
