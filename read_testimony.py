

def read_testimony():
    # store information
    articles = {'Authors': [], 'Date': [], 'SOURCE': [], 'TEXT': []}
    testimony = open('Carter_Page_testimony.txt', 'r',
                     encoding='ascii', errors='ignore').read()
    testimony = testimony.replace('\n', '').split('UNCLASSIFIED')
    texts = [i for i in testimony if i not in ['', ' ']][10:13]
    [articles['TEXT'].append(text) for text in texts]
    [articles['Authors'].append(None) for text in texts]
    [articles['Date'].append(None) for text in texts]
    [articles['SOURCE'].append('Testimony Page {}'.format(text+1))
     for text in range(len(texts))]
    return articles


print(read_testimony()['TEXT'][2])
