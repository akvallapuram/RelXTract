import spacy
import string


coref = spacy.load('en_coref_lg')
nlp = spacy.load("en_core_web_sm")
sent = "This was confirmed by Source D, a close associate of Trump who had organized and managed his recent trips to Moscow."
doc = nlp(sent)
# for token in list(doc.doc.sents)[0]:
#     print(token.text, token.pos_, token.head, token.dep_)


# Problem 1: coreferencing relative clauses
def corelcl(text):
    clauses = []
    for sent in doc.sents:
        clauses.append(" ".join([token.text for token in sent]))
        for token in sent:
            if token.dep_ == "relcl":
                subj = " ".join([c.text for c in list(token.head.subtree)
                                 if c not in list(token.subtree)
                                 and c.is_punct is False])
                subj = subj.translate(string.punctuation)
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
