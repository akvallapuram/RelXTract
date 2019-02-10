# read the input.txt
def read_dossier():
    # store information
    articles = {'Authors': [], 'Date': [], 'SOURCE': [], 'TEXT': []}
    # open file
    dossier = open('Steele_dossier.txt', 'r',
                   encoding='ascii', errors='ignore').read()
    # split the individual texts
    texts = dossier.split("-----------------------------------------------------------------------------------")
    for t in range(len(texts)):
        # get info
        info = texts[t].split('Summary')[0]
        info_clean = info.split('\n')
        info = [i for i in info_clean if i != '']
        # get text
        text = texts[t].split('Detail')[1]
        # update
        articles['Authors'].append(['Christopher Steele'])
        articles['SOURCE'].append(info[0]
                                  .replace('COMPANY INTELLIGENCE REPORT ',
                                           'Steele dossier '))
        date = info[1].replace('[ ', '').replace(' ]', '')
        # weird exception
        if "DEMISE" in date:
            date = info[2].replace('[ ', '').replace(' ]', '')
        articles['Date'].append(date)
        articles['TEXT'].append(text.replace('\n\n', ''))
    # return information
    return articles
