#!/usr/bin/env python3
"""
Emotional Analyzer: Uses transformers stub with keyword fallback.
"""

def analyze_sentiment(text):
    # Transformers stub, keyword fallback
    if "happy" in text or "good" in text:
        return "positive"
    elif "sad" in text or "bad" in text:
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    text = input("Enter text: ")
    print(analyze_sentiment(text))
