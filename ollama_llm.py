# ollama_llm.py
import subprocess

def query_ollama(transcript: str, model: str = "gemma") -> dict:
    prompt = f"""
You are a helpful assistant. Read the meeting transcript below and extract:
1. A short summary
2. Client objections and how they were addressed
3. Action items or follow-up tasks

Transcript:
{transcript}
"""

    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    output = result.stdout.decode('utf-8')
    return parse_output(output)

def parse_output(text: str) -> dict:
    sections = {"summary": "", "objections": "", "action_items": ""}
    current = None
    for line in text.splitlines():
        if "summary" in line.lower():
            current = "summary"
        elif "objection" in line.lower():
            current = "objections"
        elif "action" in line.lower():
            current = "action_items"
        elif current:
            sections[current] += line + "\n"
    return sections
