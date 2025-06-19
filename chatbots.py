import argparse
import os
import openai


def chat_with_bot(system_prompt, conversation):
    messages = [{"role": "system", "content": system_prompt}] + conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content'].strip()


def run_conversation(topic, turns=5):
    bot_a_prompt = "You are ChatGPT Bot A."
    bot_b_prompt = "You are ChatGPT Bot B."
    conversation = [{"role": "user", "content": f"Let's talk about {topic}."}]

    for _ in range(turns):
        reply_a = chat_with_bot(bot_a_prompt, conversation)
        print(f"Bot A: {reply_a}")
        conversation.append({"role": "assistant", "content": reply_a})

        reply_b = chat_with_bot(bot_b_prompt, conversation)
        print(f"Bot B: {reply_b}")
        conversation.append({"role": "assistant", "content": reply_b})


if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise SystemExit("Please set OPENAI_API_KEY environment variable.")

    parser = argparse.ArgumentParser(description="Two ChatGPT bots conversation")
    parser.add_argument("topic", help="Topic for the conversation")
    parser.add_argument("--turns", type=int, default=5, help="Number of exchanges")
    args = parser.parse_args()

    run_conversation(args.topic, args.turns)
