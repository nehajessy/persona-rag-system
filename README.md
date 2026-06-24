# Adaptive Persona RAG System

## Overview

This project processes conversation history chronologically and builds:

1. Topic checkpoints
2. 100-message checkpoints
3. Persona extraction
4. Persona drift detection
5. Offline intent classification
6. Contradiction-aware retrieval
7. Interactive chatbot

---

## Part 1: Topic Checkpoints

Conversations are processed message-by-message.

Topic changes are detected using sentence embeddings and cosine similarity.

When similarity falls below a threshold, a new topic checkpoint is created.

Output:

- topic_checkpoints.json

Example:

Topic 1 → messages 1-25

Topic 2 → messages 26-60

Topic 3 → messages 61-90

---

## Part 2: 100 Message Checkpoints

Independent summaries are created every 100 messages.

Output:

- hundred_checkpoints.json

---

## Part 3: Persona Extraction

The system extracts:

- Habits
- Personal facts
- Personality traits
- Communication style

Output:

- persona.json

---

## Part 4: Persona Drift Detection

Mood and tone are tracked across conversation days.

Examples:

Day 1 → Curious

Day 4 → Frustrated

Day 7 → Playful

Triggers are detected using dominant topics and keywords.

Output:

- mood_timeline.json

---

## Part 5: Offline Intent Classifier

Classes:

- reminder
- emotional-support
- action-item
- small-talk
- unknown

Model:

- TF-IDF
- Logistic Regression

Runs fully offline.

No LLM APIs used.

---

## Part 6: Contradiction Resolver

For memory questions such as:

"Did I mention my sister?"

The system:

1. Retrieves all relevant chunks
2. Ranks by recency
3. Applies emotional weighting
4. Detects contradictions
5. Generates merged answer

---

## Running

pip install -r requirements.txt

Run notebook cells sequentially.

Launch chatbot:

python app.py

---

## Demo

Hosted Gradio Link:

[https://2c1a69e9b996a78ffb.gradio.live/]

Loom Video:
[https://www.loom.com/share/31e60e7fbe854da09256a94369aab936]