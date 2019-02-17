from fuzzywuzzy import fuzz


def check_alias(alias, name):
    return (fuzz.ratio(alias, name)) > 50
