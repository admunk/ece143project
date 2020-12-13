import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS
import spacy
from matplotlib import pyplot as plt

nlp = spacy.load('en')

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()
cachedStopWords = stopwords.words("english")


def pre_process_data(data, remove_stop_words=True):
    '''
    This function preprocesses and cleans the text by removing links, punctuation and lower case
    :param data: original dataframe
    :param remove_stop_words: whether to remove stop words or not
    :return: new data frame with the preprocessed text column appended
    '''

    data['pp_post'] = None
    len_data = len(data)
    i = 0

    for row in data.iterrows():
        i += 1
        if i % 500 == 0:
            print("%s | %s rows" % (i, len_data))

        # Remove and clean comments
        posts = row[1].posts
        temp = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', posts)
        temp = re.sub("[^a-zA-Z]", " ", temp)
        temp = re.sub(' +', ' ', temp).lower()
        if remove_stop_words:
            temp = " ".join([lemmatiser.lemmatize(w) for w in temp.split(' ') if w not in cachedStopWords])
        else:
            temp = " ".join([lemmatiser.lemmatize(w) for w in temp.split(' ')])

        row[1].pp_post = temp
    return data


def generate_wordcloud_tfidf(data_new, ngrams):
    '''
    Generates wordcloud based on tfidf weights, considering all the possible personality types.
    This may take a significant amount of time to run, since it iterates through all the data.
    :param data_new: dataframe with the new preprocessed column
    :param ngrams: the number of ngrams to consider
    :return: None
    '''
    corpus = data_new['pp_post'].values  # get for all possible categories
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(ngrams, ngrams))
    vecs = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    dense = vecs.todense()
    lst1 = dense.tolist()
    df = pd.DataFrame(lst1, columns=feature_names)
    wordcloud = WordCloud(width=800, height=400, background_color="white", max_words=120).generate_from_frequencies(
        df.T.sum(axis=1))

    #Plot the wordcloud
    plt.figure(figsize=(14, 7))
    plt.imshow(wordcloud)
    plt.axis('off')


if __name__ == '__main__':
    data = pd.read_csv("../mbti_1.csv")
    data_new = pre_process_data(data, remove_stop_words=True)
    generate_wordcloud_tfidf(data_new, ngrams=1) #consider unigrams