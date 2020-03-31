
def analyze_article(client, text) -> dict:
    """
    Analyze an Article using AWS Comprehend Service.

    Args:
        - client: boto3 comprehend client
        - text: article body or description

    Return:
        - results: dictionary of extracted results
    """
    # Key phrases
    phrases = client.detect_key_phrases(Text=text, LanguageCode='en')

    # Entities
    entities = client.detect_entities(Text=text, LanguageCode='en')

    # Sentiments
    sentiments = client.detect_sentiment(Text=text, LanguageCode='en')

    results = {
        "key_phrases": [p['Text'] for p in phrases['KeyPhrases']],
        "entities": entities['Entities'],
        "sentiment": sentiments['Sentiment'],
        "sentiment_scores": sentiments['SentimentScore']
    }
    return results
