from pyspark.sql.functions import lit, when, length, lower
import re


def analyze_sentiment(df):
    """
    Sentiment analysis on news articles.
    Returns dataframe with original fields + sentiment score
    """
    
    def simple_sentiment_score(text):
        """
        Simple keyword-based sentiment analyzer
        Returns: positive, negative, or neutral
        """
        if not text:
            return "neutral"
        
        text = str(text).lower()
        
        # Positive keywords
        positive_words = [
            "good", "great", "excellent", "positive", "gain", "rise", "surge",
            "growth", "success", "breakthrough", "triumph", "profit", "boom",
            "rally", "strong", "opportunity", "improved", "amazing", "wonderful"
        ]
        
        # Negative keywords
        negative_words = [
            "bad", "terrible", "worst", "negative", "loss", "fall", "crash",
            "decline", "failure", "disaster", "loss", "slump", "weak",
            "threat", "risk", "danger", "dropped", "plunged", "collapse"
        ]
        
        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
    # Register UDF for sentiment analysis
    from pyspark.sql.functions import udf
    from pyspark.sql.types import StringType
    
    sentiment_udf = udf(simple_sentiment_score, StringType())
    
    # Apply sentiment analysis on text_to_analyze column
    result_df = df.withColumn(
        "sentiment",
        sentiment_udf(df.text_to_analyze)
    )
    
    # Select and order columns for output
    return result_df.select(
        "source",
        "author",
        "title",
        "description",
        "url",
        "published_at",
        "sentiment",
        "fetched_at"
    )

