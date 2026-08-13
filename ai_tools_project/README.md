# AI Study Assistant

A simple command-line application that uses the OpenAI API to explain study topics, give examples, and provide a practice question.

## What I learned

- **Coding:** AI can help explain errors, suggest improvements, and generate starter code.
- **Research:** AI can turn difficult topics into simple summaries and help create questions.
- **Productivity:** AI can help plan learning tasks, organize notes, and create revision material.
- **Responsible use:** Always review AI-generated content and do not share private or sensitive information in prompts.

## Setup

1. Create an OpenAI API key in the OpenAI Platform dashboard.
2. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

3. In PowerShell, set the key for the current terminal session:

   ```powershell
   $env:OPENAI_API_KEY="your_api_key_here"
   ```

4. Run the application:

   ```bash
   python study_assistant.py
   ```

Type a question such as `Explain Python lists with an example`, then type `quit` when finished.

The app uses the OpenAI Responses API. It reads `OPENAI_API_KEY` from the environment, so no secret key is stored in the source code. You may optionally set `OPENAI_MODEL` to a model your account can access.

## Important

Never commit your API key. The included `.env.example` is only a template and contains no real credential.
