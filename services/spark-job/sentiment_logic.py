from pyspark.sql.functions import lit, when, length, lower, udf
from pyspark.sql.types import StringType
import logging
from transformers import pipeline
import os

logger = logging.getLogger(__name__)

# Initialize DistilBERT model once (cached for performance)
_sentiment_model = None

def get_sentiment_model():
    """
    Lazy load DistilBERT model on first use.
    Model is cached globally to avoid reloading.
    """
    global _sentiment_model
    if _sentiment_model is None:
        logger.info("Loading DistilBERT sentiment model...")
        # Disable GPU for Spark environment
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        _sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=-1  # Use CPU
        )
        logger.info("✅ DistilBERT model loaded successfully")
    return _sentiment_model


def ml_sentiment_score(text):
    """
    ML-based sentiment analyzer using DistilBERT transformer model.
    Returns: positive or negative
    
    Model: distilbert-base-uncased-finetuned-sst-2-english
    - Trained on Stanford Sentiment Treebank (SST-2)
    - Accurate binary sentiment classification
    - Returns confidence score 0-1
    """
    if not text:
        return "neutral"
    
    try:
        model = get_sentiment_model()
        # Limit input to 512 tokens (DistilBERT max)
        text_truncated = str(text)[:512]
        result = model(text_truncated)
        
        label = result[0]['label']  # 'POSITIVE' or 'NEGATIVE'
        score = result[0]['score']
        
        # Return lowercase label
        return label.lower()
    except Exception as e:
        logger.warning(f"Error in sentiment analysis: {e}. Defaulting to neutral.")
        return "neutral"


def analyze_sentiment(df):
    """
    Sentiment analysis on news articles using DistilBERT ML model.
    Returns dataframe with original fields + sentiment label
    
    Model: distilbert-base-uncased-finetuned-sst-2-english
    - Pre-trained on Stanford Sentiment Treebank (SST-2)
    - Accurate binary sentiment classification
    - Works across all domains and article types
    """
    
    # Register UDF for DistilBERT sentiment analysis
    from pyspark.sql.functions import udf
    from pyspark.sql.types import StringType
    
    sentiment_udf = udf(ml_sentiment_score, StringType())
    
    # Apply ML sentiment analysis on text_to_analyze column
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

