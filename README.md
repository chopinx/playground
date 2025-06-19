# Playground

This repository contains sample scripts.

## chatbots.py

`chatbots.py` uses the OpenAI API to simulate two ChatGPT bots that talk to each other about a user-provided topic.

### Requirements

- Python 3.8+
- `openai` Python package
- An OpenAI API key set in the `OPENAI_API_KEY` environment variable

### Usage

```bash
python chatbots.py "<topic>" --turns 3
```

The script will alternate messages between Bot A and Bot B for the specified number of turns.

## memory_chatbots.py

`memory_chatbots.py` demonstrates how to keep a conversation log and running summary entirely in memory without external dependencies.

### Usage

```bash
python memory_chatbots.py "<topic>" --turns 3
```

The bots will read the current summary before replying so they retain a minimal context.

