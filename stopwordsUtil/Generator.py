stopWords = open('english.stop', 'r').read().split()
f = open('stopwords.py', 'w')
print >> f, "stopWords = ", stopWords
