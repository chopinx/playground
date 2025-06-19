class ConversationState:
    """Keeps the conversation log and running summary in memory."""

    def __init__(self):
        self.messages = []  # list of {"role": str, "content": str}
        self.summary = ""

    def append(self, role, content):
        self.messages.append({"role": role, "content": content})
        self._update_summary()

    def _update_summary(self):
        """Create a very small summary from the last few messages."""
        last_msgs = [m["content"] for m in self.messages[-3:]]
        text = " ".join(last_msgs)
        # keep at most 30 words in the summary
        words = text.split()
        if len(words) > 30:
            words = words[-30:]
        self.summary = " ".join(words)

    def get_summary(self):
        return self.summary


def bot_response(bot_name, topic, summary):
    """Return a simple bot response referencing the latest summary."""
    return f"{bot_name} notes: {summary}. Let's continue talking about {topic}."


def run_conversation(topic, turns=3):
    state = ConversationState()
    state.append("user", f"Let's talk about {topic}.")

    for _ in range(turns):
        summary = state.get_summary()
        reply_a = bot_response("Bot A", topic, summary)
        print(f"Bot A: {reply_a}")
        state.append("assistant", reply_a)

        summary = state.get_summary()
        reply_b = bot_response("Bot B", topic, summary)
        print(f"Bot B: {reply_b}")
        state.append("assistant", reply_b)

    print("\n--- Conversation Summary ---")
    print(state.get_summary())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple conversation with in-memory log and summary")
    parser.add_argument("topic", help="Topic to discuss")
    parser.add_argument("--turns", type=int, default=3, help="Number of exchanges per bot")
    args = parser.parse_args()

    run_conversation(args.topic, args.turns)
