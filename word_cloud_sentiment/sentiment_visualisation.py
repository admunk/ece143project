import pandas as pd
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
from matplotlib import pyplot as plt
import pickle
nlp = spacy.load('en')


vader_model = SentimentIntensityAnalyzer()

def run_vader(textual_unit,
              lemmatize=False,
              parts_of_speech_to_consider=set(),
              verbose=0):
    """
    Generates a dictionary of sentiment scores
    :param textual_unit: sentence, in this case
    :param lemmatize: whether to lemmatize tokens or not
    :return: dict of sentiment scores
    """

    doc = nlp(textual_unit)

    input_to_vader = []

    for sent in doc.sents:
        for token in sent:

            to_add = token.text

            if lemmatize:
                to_add = token.lemma_

                if to_add == '-PRON-':
                    to_add = token.text

            if parts_of_speech_to_consider:
                if token.pos_ in parts_of_speech_to_consider:
                    input_to_vader.append(to_add)
            else:
                input_to_vader.append(to_add)

    scores = vader_model.polarity_scores(' '.join(input_to_vader))

    if verbose >= 1:
        print()
        print('INPUT SENTENCE', sent)
        print('INPUT TO VADER', input_to_vader)
        print('VADER OUTPUT', scores)

    return scores


def get_sentiment_of_sentence(sent):
    """
    Returns sentiment for a particular sentence
    :param sent: a single sentence
    :return: Sentiment of sentence
    """

    sentiment_dict = run_vader(sent)
    if sentiment_dict['compound'] >= 0.05:
        return "Positive"
    elif sentiment_dict['compound'] <= - 0.05:
        return "Negative"
    else:
        return "Neutral"



def get_sentiments(df):
    """
    Creates result_dict that contains number of positive, negative and neutral sentiments for each personality type
    :param df: original dataframe
    :return: result_dict
    """

    result_dict = {categ: {"Positive": 0, "Negative": 0, "Neutral": 0} for categ in df['type'].unique()}
    for i, row in df.iterrows():
        categ = row['type']
        post = row['posts']
        post_nolinks = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '<LINK>', post)
        postsplit = post_nolinks.split("|||")
        for comment in postsplit:
            sentiment = get_sentiment_of_sentence(comment.strip())
            result_dict[categ][sentiment] += 1
        if i % 50 == 0:
            print("%s rows done" % i)
        return result_dict



def dump_result_dict(result_dict):
    """
    Dumps the dictionary into a pickle file
    :param result_dict: Dict that contains number of positive,
    negative and neutral sentiments for each personality type
    :return: None
    """
    with open("result_dict.pkl", "wb") as p:
        pickle.dump(result_dict, p)


def load_result_dict():
    """
    Load the dictionary from a pickle file
    :param result_dict: Dict that contains number of positive,
    negative and neutral sentiments for each personality type
    :return: result_dict
    """
    with open("result_dict.pkl", "rb") as p:
        result_dict = pickle.load(p)
    return result_dict

def plot_sentiment_pie_charts(result_dict):
    '''
    Plots pie charts, showing percentage of each sentiment type for each personality type
    :param result_dict: Dict that contains number of positive,
    negative and neutral sentiments for each personality type
    :return: None
    '''
    fig, ax = plt.subplots(4, 4, figsize=(17, 17))
    i, j = 0, 0
    for key, value in result_dict.items():
        sentiment_labels = list(value.keys())
        counts = list(value.values())
        ax[i][j].pie(counts, labels=sentiment_labels, autopct='%1.2f%%')
        ax[i][j].set_title(key, fontsize=20)
        fig.show()
        j += 1
        if j == 4:
            i += 1
            j = 0


if __name__ == '__main__':
    data = pd.read_csv("../mbti_1.csv")

    #Uncomment the below 2 lines if "result_dict.pkl" does not exist
    #result_dict = get_sentiments(data)
    #dump_result_dict(result_dict)

    #If "result_dict.pkl" exists, load the result_dict from the pkl file
    result_dict = load_result_dict()
    plot_sentiment_pie_charts(result_dict)





