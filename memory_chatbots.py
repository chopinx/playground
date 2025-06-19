class ConversationState:
    """Keeps the conversation log and running summary in memory."""

    def __init__(self, rot=30):
        self.messages = []  # list of {"role": str, "content": str}
        self.summary = ""
        self.rot = rot

    def append(self, role, content):
        self.messages.append({"role": role, "content": content})
        self._update_summary()

    def _update_summary(self):
        """Create a very small summary from the last few messages."""
        last_msgs = [m["content"] for m in self.messages[-3:]]
        text = " ".join(last_msgs)
        # keep at most ``rot`` words in the summary
        words = text.split()
        if len(words) > self.rot:
            words = words[-self.rot:]
        self.summary = " ".join(words)

    def get_summary(self):
        return self.summary


PERSONALITIES = {
    "neutral": {
        "rot": 30,
        "template": "{bot_name} notes: {summary}. Let's continue talking about {topic}."
    },
    "excited": {
        "rot": 15,
        "template": "{bot_name} exclaims: {summary}! Can't wait to discuss more about {topic}!"
    },
}


def bot_response(personality, bot_name, topic, summary):
    """Return a bot response using the personality template."""
    template = PERSONALITIES[personality]["template"]
    return template.format(bot_name=bot_name, topic=topic, summary=summary)


def run_conversation(topic, turns=3, personality="neutral"):
    rot = PERSONALITIES.get(personality, PERSONALITIES["neutral"])['rot']
    state = ConversationState(rot=rot)
    state.append("user", f"Let's talk about {topic}.")

    for _ in range(turns):
        summary = state.get_summary()
        reply_a = bot_response(personality, "Bot A", topic, summary)
        print(f"Bot A: {reply_a}")
        state.append("assistant", reply_a)

        summary = state.get_summary()
        reply_b = bot_response(personality, "Bot B", topic, summary)
        print(f"Bot B: {reply_b}")
        state.append("assistant", reply_b)

    print("\n--- Conversation Summary ---")
    print(state.get_summary())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple conversation with in-memory log and summary")
    parser.add_argument("topic", help="Topic to discuss")
    parser.add_argument("--turns", type=int, default=3, help="Number of exchanges per bot")
    parser.add_argument("--personality", choices=list(PERSONALITIES.keys()), default="neutral",
                        help="Personality preset which also controls rot")
    args = parser.parse_args()

    run_conversation(args.topic, args.turns, args.personality)
