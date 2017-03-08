from pycorenlp import StanfordCoreNLP

f = open("../Data/Plain Text/A Short History of Nearly Everything.txt")
nlp = StanfordCoreNLP('http://localhost:9000')

for line in f.readlines():
    text = line
    print(text)
    output = nlp.annotate(text, properties={
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })
    print(output)