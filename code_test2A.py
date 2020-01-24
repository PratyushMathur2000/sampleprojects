

url_file = open('test1.txt')
for url in url_file.readlines():
  a = Article(url, language='en')
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