import time
import random

def check_toxicity(text):
    print("[LLM Node 1] Checking toxicity...")
    
    time.sleep(random.uniform(0.5, 1.5))  # simulate distributed delay
    
    toxic_words = ["hate", "idiot", "stupid","dumb"]
    result = any(word in text for word in toxic_words)
    
    print("[LLM Node 1] Toxicity:", result)
    return result