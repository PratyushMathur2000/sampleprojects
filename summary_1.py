from newspaper import Article
from newspaper import fulltext
import requests
import sys as sys
import pandas as pd

url_file= pd.read_csv('csv_file_name.csv')

for x in url_file['n_url']: #replace 'n_url' with the actual name in your df 
    for url in url_file.readlines():
        a = Article(x, language='en')
        html = requests.get(url).text
        text = fulltext(html)
        download = a.download()
        parse = a.parse()
        nlp = a.nlp()
        title = a.title
        publish_date = a.publish_date
        authors = a.authors
        keywords = a.keywords
        summary = a.summary
url_file.close()


with open("output_text_file_name", "w") as text_file:
    print(title, file=text_file)
    print(keywords, file=text_file)
    print(summary, file=text_file)
    

print(title)
