def log_decision(text, decision):
    print("[Logger] Saving decision...")

    with open("log.txt", "a") as file:
        file.write(f"Input: {text} | Decision: {decision}\n")