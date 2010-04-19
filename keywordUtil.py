from PorterStemmer import PorterStemmer

stopWords = open('english.stop', 'r').read().split()
PUNCTUATION = ",. \n\t\\\"'][#*:?!;"

def getQuestionKeywords(question):
    """Return the keywords from a question.

    The logic is: remove the stop words and punctuations from question, stem the keywords and remove duplicates
    Currently there are still issues with
    1. stop words list is not complete: eg "recommend" etc is not a stop word.
    2. stemmer issue: The current stemmer utility has an issue eg "restaurant" is stemmed to "restau"

    >>> getQuestionKeywords('what is the best preschool in Potomac?')
    ['potomac', 'preschool']

    >>> getQuestionKeywords('Can someone help with a preschool around potomac?')
    ['potomac', 'preschool']

    """

    # split the question into a list
    keywordList = question.split()

    # strip the punctuations etc
    keywordList = [keyword.strip(PUNCTUATION) for keyword in keywordList]

    # convert into lower case
    keywordList = [keyword.lower() for keyword in keywordList]

    #remove stop words from keywords
    keywordList = [keyword for keyword in keywordList if keyword not in stopWords]

    #stem the keywords
    stemmer = PorterStemmer()
    keywordList = [stemmer.stem(keyword,0,len(keyword)-1) for keyword in keywordList]

    #remove duplicates
    keywordList = list(set(keywordList))

    #sort the keywords
    keywordList.sort()
    
    return keywordList

if __name__ == '__main__':
    import doctest
    doctest.testmod()