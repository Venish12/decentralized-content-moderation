from edge_node import preprocess
from llm_node1 import check_toxicity
from llm_node2 import check_spam
from coordinator import decide
from logger import log_decision
from llm_node3 import check_hate_speech

def main():
    text = input("Enter content: ")

    # Step 1: Edge processing
    processed_text = preprocess(text)

    # Step 2: Distributed LLM nodes
    toxicity = check_toxicity(processed_text)
    spam = check_spam(processed_text)
    hate = check_hate_speech(processed_text)

    # Step 3: Coordination layer
    decision = decide(toxicity, spam, hate)

    

    # Step 4: Logging
    log_decision(processed_text, decision)

    print("\nFinal Decision:", decision)


if __name__ == "__main__":
    main()