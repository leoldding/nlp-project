import pandas as pd
from sklearn.model_selection import train_test_split

# things to avoid
punctuation_and_numbers = ["!", "@", "#", "$", "%", "'", "^", "&", "*", "(", ")", "{", "}", "[", "]", "\\", "|", "=",
                           "+", "/", "?", "-", "_", ".", "<", ">", "`", "~", ";", ":", ",",
                           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# many more things to avoid
stop_words = ['a', 'the', 'an', 'and', 'or', 'but', 'about', 'above', 'after', 'along', 'amid', 'among',
              'as', 'at', 'by', 'for', 'from', 'in', 'into', 'like', 'near', 'of', 'off', 'on',
              'onto', 'out', 'over', 'past', 'per', 'plus', 'since', 'till', 'to', 'under', 'until', 'up',
              'via', 'vs', 'with', 'that', 'could', 'may', 'might', 'must',
              'need', 'ought', 'shall', 'should', 'will', 'would', 'have', 'had', 'has', 'having', 'be',
              'is', 'am', 'are', 'was', 'were', 'being', 'been', 'get', 'gets', 'got', 'gotten',
              'getting', 'seem', 'seeming', 'seems', 'seemed',
              'enough',  'both',  'all',  'your' 'those',  'this',  'these',
              'their',  'the',  'that',  'some',  'our',  'neither',  'my',
              'its',  'his' 'her',  'every',  'either',  'each',  'any',  'another',
              'an',  'a',  'just',  'mere',  'such',  'merely' 'right',
              'only',  'sheer',  'even',  'especially',  'namely',  'as',  'more',
              'most',  'less', 'least',  'so',  'enough',  'too',  'pretty',  'quite',
              'rather',  'somewhat',  'sufficiently' 'same',  'different',  'such',
              'when',  'why',  'where',  'how',  'what',  'who',  'whom',  'which',
              'whether',  'why',  'whose',  'if',  'anybody',  'anyone',  'anyplace',
              'anything',  'anytime' 'anywhere',  'everybody',  'everyday',
              'everyone',  'everyplace',  'everything' 'everywhere',  'whatever',
              'whenever',  'whereever',  'whichever',  'whoever',  'whomever' 'he',
              'him',  'his',  'her',  'she',  'it',  'they',  'them',  'its',  'their', 'theirs',
              'you', 'your', 'yours', 'me', 'my', 'mine', 'i', 'we', 'us', 'much', 'and/or'
              ]

flip_words = ['no', 'not', 'rather', 'couldn\'t', 'wasn\'t', 'didn\'t', 'wouldn\'t', 'shouldn\'t', 'weren\'t',
              'don\'t', 'doesn\'t', 'haven\'t', 'hasn\'t', 'won\'t', 'hadn\'t', 'never', 'none', 'nobody',
              'nothing', 'neither', 'nor', 'nowhere', 'isn\'t', 'can\'t', 'cannot', 'musn\'t', 'mightn\'t', 'shan\'t',
              'without', 'needn\'t']

diminish_words = ['hardly', 'less', 'little', 'rarely', 'scarcely', 'seldom']


# check if a 'word' is something we need to avoid
def checkWord(check):
    for word in stop_words:
        if word == check:
            return False
    for char in punctuation_and_numbers:
        if char in check:
            return False
    return True


# read in data to dataframe
data = pd.read_csv("all-data.csv", delimiter=',', encoding="ISO-8859-1", header=None, names=["sentiment", "headlines"])

# create train and test data splits
train, test = train_test_split(data, test_size=0.15)

test.to_csv('test.csv', index=False)

# dictionary to hold words and their sentiment values
word_sentiments = {}
word_counts = {}
stemmer_sentiments = {}
stemmer_counts = {}

# iterate through each headline and increment valid words based on attached sentiment
for i in range(len(train)):
    sentiment = train.sentiment.iloc[i]
    headline = train.headlines.iloc[i].lower().split(' ')
    for word in headline:
        if checkWord(word):
            if word not in word_sentiments:
                word_sentiments[word] = 1 if sentiment == 'positive' else -1 if sentiment == 'negative' else 0
            else:
                word_sentiments[word] += 1 if sentiment == 'positive' else -1 if sentiment == 'negative' else 0
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

# normalize word sentiment values
with open('sentiments.txt', 'w') as f:
    for word in word_sentiments.keys():
        word_sentiments[word] /= word_counts[word]
        f.write(word + ' ' + str(word_sentiments[word]) + '\n')