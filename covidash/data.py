"""
This module provides functionality for the Dash app to load data.
"""
import os
import pickle

import numpy as np
import pandas as pd


def load_topics():
    """
    Load list of available topics.
    """
    path = 'covidash/data'
    return [n for n in os.listdir(path) if os.path.isdir(os.path.join(path, n))]


def load_processed_dataset(topic):
    """
    Load processed articles.
    """
    path = f'covidash/data/{topic}/articles.txt'
    return pd.read_csv(path)


def load_topic_comprehend(topic) -> list:
    """
    Load AWS Comprehend analysis results for a given topic
    """
    data_path = f'covidash/data/{topic}/comprehend/comprehend.pickle'
    with open(data_path, 'rb') as f:
        return pickle.load(f)


def general_sentiment(data):
    """
    Compute genera sentiment stats from Comprehend data.
    """
    res = {}
    res['mean_pos_sent'] = np.mean(
        [r['sentiment_scores']['Positive'] for r in data])
    res['mean_neg_sent'] = np.mean(
        [r['sentiment_scores']['Negative'] for r in data])
    res['mean_neutral_sent'] = np.mean(
        [r['sentiment_scores']['Neutral'] for r in data])
    res['mean_mixed_sent'] = np.mean(
        [r['sentiment_scores']['Mixed'] for r in data])
    return res


def load_embeddings(topic):
    """
    Load TSNE 2D Embeddings generated from fitting BlazingText on the news articles.
    """
    print(topic)
    embeddings = pickle.load(
        open(f'covidash/data/{topic}/blazing_text/embeddings.pickle', 'rb'))
    labels = pickle.load(
        open(f'covidash/data/{topic}/blazing_text/labels.pickle', 'rb'))
    return embeddings, labels
