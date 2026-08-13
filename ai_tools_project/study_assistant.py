"""A command-line AI Study Assistant powered by the OpenAI API."""

import os

from openai import OpenAI


SYSTEM_INSTRUCTIONS = """You are a helpful study assistant for beginner learners.
Explain concepts clearly, use short examples when useful, and end with one
quick practice question. Keep answers concise and encouraging."""


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set.")
        print("Set your API key as an environment variable, then run this program again.")
        return

    client = OpenAI()
    print("=== AI Study Assistant ===")
    print("Ask a study question. Type 'quit' to exit.\n")

    while True:
        question = input("You: ").strip()
        if question.lower() in {"quit", "exit"}:
            print("Keep learning!")
            break
        if not question:
            print("Please enter a question.")
            continue

        try:
            response = client.responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
                instructions=SYSTEM_INSTRUCTIONS,
                input=question,
            )
            print(f"\nAssistant: {response.output_text}\n")
        except Exception as error:
            print(f"\nCould not get a response: {error}\n")


if __name__ == "__main__":
    main()
