from ollama import Client
from httpx import ConnectError

from config import LLM_MODEL
from utils.prompts import SYSTEM_PROMPT

# Persistent Ollama client
client = Client(
    host="http://127.0.0.1:11434"
)


def build_history(messages, max_messages: int = 6) -> str:
    """
    Build conversation history from the latest chat messages.
    """

    if not messages:
        return "No previous conversation."

    history = []

    for message in messages[-max_messages:]:

        role = message["role"].capitalize()

        history.append(
            f"{role}: {message['content']}"
        )

    return "\n".join(history)


def generate_answer(
    context: str,
    question: str,
    history: str = ""
) -> str:
    """
    Generate a complete response.
    """

    prompt = SYSTEM_PROMPT.format(
        history=history,
        context=context,
        question=question
    )

    try:

        response = client.chat(
    model=LLM_MODEL,
    keep_alive="30m",
    options={
        "temperature": 0.2,
        "num_ctx": 2048,
        "num_predict": 256
    },
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

        return response["message"]["content"]

    except ConnectError:

        return (
            "❌ Unable to connect to Ollama.\n\n"
            "Please make sure:\n"
            "- Ollama is running\n"
            "- The model is installed\n"
            "- Port 11434 is available"
        )

    except Exception as e:

        return f"❌ {str(e)}"


def stream_answer(
    context: str,
    question: str,
    history: str = ""
):
    """
    Stream the response token-by-token.
    """

    prompt = SYSTEM_PROMPT.format(
        history=history,
        context=context,
        question=question
    )

    try:

        stream = client.chat(
    model=LLM_MODEL,
    keep_alive="30m",
    options={
        "temperature": 0.2,
        "num_ctx": 2048,
        "num_predict": 256
    },
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    stream=True
)

        for chunk in stream:

            if "message" not in chunk:
                continue

            content = chunk["message"].get(
                "content",
                ""
            )

            if content:
                yield content

    except ConnectError:

        yield (
            "❌ Unable to connect to Ollama.\n\n"
            "Please start Ollama and try again."
        )

    except Exception as e:

        yield f"❌ {str(e)}"