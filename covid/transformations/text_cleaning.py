"""
This module hosts the logic for cleaning raw text data
"""
import re

import nltk
from nltk.corpus import stopwords


def remove_punct(text: str):
    """
    Remove punctuations using regex rules.
    """
    # remove tbc dots
    text = re.sub('…', '', text)
    # remove urls
    text = re.sub('http\S+', '', text, flags=re.MULTILINE)
    # remove periods and commas, etc.
    text = (text
            .replace('.', '')
            .replace(',', '')
            .replace(':', '')
            .replace('#', '')
            .replace('"', '')
            .replace("'", '')
            .replace(")", '')
            .replace("(", '')
            .replace("</s>", '')
            )
    # remove single character words
    text = ' '.join([word for word in text.split() if len(word) > 1])
    return text


def clean_articles(data: list) -> list:
    """
    Full text cleaning pipeline.
    """

    # lowercase all words
    data = [sentence.lower() for sentence in data]

    # download english stop words from nltk
    nltk.download('stopwords')

    # load stop words
    stop_words = stopwords.words('english')

    # remove stop words
    data = [' '.join(
        [w for w in sentence.split() if w not in stop_words]) for sentence in data]

    # remove punctuation
    data = [remove_punct(sentence) for sentence in data]

    return data
