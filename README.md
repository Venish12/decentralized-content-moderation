# Decentralized Content Moderation using Large Language Models

## Overview

This project explores a decentralized approach to content moderation using ideas from distributed systems and large language models (LLMs). Traditional moderation systems are usually centralized, where all data is sent to a server for processing. While that works, it introduces problems like higher latency, privacy concerns, and dependency on a single system.

In this project, we try to simulate how moderation can be handled in a more distributed way by breaking the system into multiple components that work together.

---

## What this project does

The system takes user input and processes it through multiple independent nodes, where each node is responsible for checking a different type of content issue. The final decision is made by combining the results from all nodes.

This is not a full-scale distributed system, but a simplified prototype that demonstrates the idea.

---

## System Design (Simple Explanation)

The workflow is roughly:

```
User Input → Edge Processing → Multiple Moderation Nodes → Final Decision → Logging
```

* The **edge node** handles basic preprocessing (like cleaning input)
* Multiple **LLM nodes** analyze the text
* A **coordinator** combines the results
* A **logger** stores the decisions for traceability

---

## Components

### Edge Node

Handles basic preprocessing of input text (lowercasing, trimming, etc.). This represents the idea of processing data closer to the source instead of sending everything to a central server.

---

### LLM Nodes

There are three separate nodes in this project:

* **Node 1:** Checks for toxic content
* **Node 2:** Checks for spam
* **Node 3:** Checks for hate speech

Each node runs independently and simulates a distributed setup using small delays.

---

### Coordinator

The coordinator collects results from all nodes and decides whether the content should be approved or rejected.

Instead of picking just one issue, it can return multiple reasons, for example:

```
Rejected (Toxic Content, Spam)
```

---

### Logger

The logger writes decisions to a file (`log.txt`). This is a simple way to represent transparency and traceability, similar to how decentralized systems might store records.

---

## How to Run

Make sure you have Python installed, then run:

```
python main.py
```

Enter any text when prompted.

---

## Example Inputs

| Input                 | Output                   |
| --------------------- | ------------------------ |
| you are stupid        | Rejected (Toxic Content) |
| buy now and subscribe | Rejected (Spam)          |
| you are a terrorist   | Rejected (Hate Speech)   |
| hello world           | Approved                 |

---

## Why this approach

The goal of this project is to show how moderation tasks can be split across multiple nodes instead of relying on a single centralized system.

This approach can:

* reduce latency (processing closer to user)
* improve privacy (less data transfer)
* scale better (more nodes can be added)

---

## Limitations

This is a simplified prototype, so:

* It uses keyword-based detection instead of real LLMs
* The distributed behavior is simulated, not real network communication
* It’s meant for demonstration, not production use

---

## Future Improvements

Some things that could be added:

* Use real LLM APIs (like HuggingFace or OpenAI)
* Convert nodes into separate services (microservices)
* Add a web interface
* Implement real communication between nodes
* Add performance metrics

---

## Project Structure

```
main.py
edge_node.py
llm_node1.py
llm_node2.py
llm_node3.py
coordinator.py
logger.py
.gitignore
README.md
```

---

## Notes

* `log.txt` is generated when the program runs and is not included in the repository.
* This project was developed as part of a distributed systems course.

---

## Authors

Venish Korat
Vansh Sutariya

California State University, Long Beach
