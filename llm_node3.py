import time
import random

def check_hate_speech(text):
    print("[LLM Node 3] Checking hate speech...")
    
    time.sleep(random.uniform(0.5, 1.5))  # simulate delay
    
    hate_words = ["racist", "kill", "terrorist", "nigga"]
    result = any(word in text for word in hate_words)
    
    print("[LLM Node 3] Hate Speech:", result)
    return result