import time
import random

def check_spam(text):
    print("[LLM Node 2] Checking spam...")
    
    time.sleep(random.uniform(0.5, 1.5))  # simulate distributed delay
    
    spam_words = ["buy now", "click here", "subscribe"]
    result = any(word in text for word in spam_words)
    
    print("[LLM Node 2] Spam:", result)
    return result