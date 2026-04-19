#!/usr/bin/env python3
"""
News Sentiment Analytics - Core Batch Pipeline
Minimal version: Pre-trained model + local data
"""

import pandas as pd
import numpy as np
from datetime import datetime
import logging
from transformers import pipeline

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================
# STAGE 1: LOAD DATA
# ============================================================
def stage_1_load_data():
    """Load articles from CSV"""
    logger.info("[1/4] Loading articles...")
    
    try:
        df = pd.read_csv('data/test_articles.csv')
        logger.info(f"✅ Loaded {len(df)} articles")
        return df
    except FileNotFoundError:
        logger.error("❌ data/test_articles.csv not found")
        raise

# ============================================================
# STAGE 2: LOAD PRE-TRAINED MODEL
# ============================================================
def stage_2_load_model():
    """Load pre-trained sentiment model from HuggingFace"""
    logger.info("[2/4] Loading pre-trained model...")
    
    # Use distilbert-base-uncased-finetuned-sst-2-english
    # Small, fast, accurate for sentiment
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1  # Use CPU (-1), or 0 for GPU
    )
    
    logger.info("✅ Model loaded successfully")
    return sentiment_pipeline

# ============================================================
# STAGE 3: BATCH INFERENCE
# ============================================================
def stage_3_inference(df, model):
    """Run sentiment analysis on all articles"""
    logger.info("[3/4] Running sentiment inference on batch...")
    
    predictions = []
    
    for idx, row in df.iterrows():
        try:
            # Run inference
            result = model(row['text'][:512])  # Limit to 512 chars
            
            label = result[0]['label']  # 'POSITIVE' or 'NEGATIVE'
            score = result[0]['score']
            
            # Convert to -1 to +1 scale
            sentiment_score = score if label == 'POSITIVE' else -score
            
            predictions.append({
                'article_id': idx,
                'text': row['text'][:100],  # First 100 chars
                'sentiment_score': sentiment_score,
                'predicted_label': 'Positive' if label == 'POSITIVE' else 'Negative',
                'confidence': score,
                'prediction_timestamp': datetime.now()
            })
            
            if (idx + 1) % 5 == 0:
                logger.info(f"  Processed {idx + 1}/{len(df)} articles")
                
        except Exception as e:
            logger.warning(f"Error processing article {idx}: {e}")
            continue
    
    results_df = pd.DataFrame(predictions)
    logger.info(f"✅ Inference complete on {len(results_df)} articles")
    return results_df

# ============================================================
# STAGE 4: SAVE RESULTS & GENERATE REPORT
# ============================================================
def stage_4_save_results(results_df):
    """Save results to CSV and generate HTML report"""
    logger.info("[4/4] Saving results...")
    
    # Save CSV
    date_str = datetime.now().strftime("%Y-%m-%d")
    csv_file = f'results/sentiments_{date_str}.csv'
    results_df.to_csv(csv_file, index=False)
    logger.info(f"✅ Results saved to {csv_file}")
    
    # Generate simple HTML report
    positive_count = (results_df['predicted_label'] == 'Positive').sum()
    negative_count = (results_df['predicted_label'] == 'Negative').sum()
    avg_sentiment = results_df['sentiment_score'].mean()
    
    html_report = f"""
    <html>
    <head>
        <title>Daily Sentiment Report - {date_str}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #1f4788; }}
            .summary {{ background: #f0f0f0; padding: 15px; border-radius: 5px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #1f4788; color: white; }}
        </style>
    </head>
    <body>
        <h1>📰 Daily Sentiment Analysis Report</h1>
        <p><b>Date:</b> {date_str}</p>
        
        <div class="summary">
            <h2>Summary Statistics</h2>
            <p><b>Total Articles:</b> {len(results_df)}</p>
            <p><b>Average Sentiment:</b> {avg_sentiment:.3f}</p>
            <p><b>Positive:</b> {positive_count} ({positive_count/len(results_df)*100:.1f}%)</p>
            <p><b>Negative:</b> {negative_count} ({negative_count/len(results_df)*100:.1f}%)</p>
        </div>
        
        <h2>Top Positive Articles</h2>
        <table>
            <tr><th>Text</th><th>Sentiment Score</th><th>Confidence</th></tr>
    """
    
    for _, row in results_df.nlargest(3, 'sentiment_score').iterrows():
        html_report += f"""
            <tr>
                <td>{row['text']}</td>
                <td>{row['sentiment_score']:.3f}</td>
                <td>{row['confidence']:.3f}</td>
            </tr>
        """
    
    html_report += """
        </table>
        
        <h2>Top Negative Articles</h2>
        <table>
            <tr><th>Text</th><th>Sentiment Score</th><th>Confidence</th></tr>
    """
    
    for _, row in results_df.nsmallest(3, 'sentiment_score').iterrows():
        html_report += f"""
            <tr>
                <td>{row['text']}</td>
                <td>{row['sentiment_score']:.3f}</td>
                <td>{row['confidence']:.3f}</td>
            </tr>
        """
    
    html_report += """
        </table>
    </body>
    </html>
    """
    
    html_file = f'results/report_{date_str}.html'
    with open(html_file, 'w') as f:
        f.write(html_report)
    logger.info(f"✅ Report saved to {html_file}")

# ============================================================
# MAIN PIPELINE
# ============================================================
def main():
    logger.info("=" * 60)
    logger.info("🚀 NEWS SENTIMENT BATCH PIPELINE STARTED")
    logger.info("=" * 60)
    
    try:
        # Stage 1: Load data
        articles_df = stage_1_load_data()
        
        # Stage 2: Load model
        sentiment_model = stage_2_load_model()
        
        # Stage 3: Inference
        results_df = stage_3_inference(articles_df, sentiment_model)
        
        # Stage 4: Save results
        stage_4_save_results(results_df)
        
        logger.info("=" * 60)
        logger.info("✅ PIPELINE COMPLETE!")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"❌ Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()
