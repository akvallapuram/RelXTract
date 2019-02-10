ReadMe
----------

This is a simple relation extraction model that extracts relations from news texts. The model uses Stanford NER library and the idea of co-occurence which states that if two social entities are present in a sentence in a news source, then they must be related. 

1. paste the url links of the news sources to the sources.txt as described
2. run the program using the following command in terminal: 'python main.py dossier' or 'python main.py sources' 
3. the connections.csv file will be updated with the connections
4. the actors.csv file will be updated with the actors

Note: This extraction model is still very naive. It cannot differentiate between same people called with aliases. The sentiment between relations is limited to the sentiment of the overall sentence that the relation is present in. Further updates will be made to optimise this naivety. 


Post-Scriptum:

This project was originally intended for my Undergraduate Reasearch Project. The aim of the project was to analyse the Steele Dossier for Trump-Russia relations and develop social networks from the assigned texts. It was originally intended that this analysis of the Dossier be done through manual reading. However, I wanted to automate the process, leading to the inception of RelXTract. 
