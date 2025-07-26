# Streaming Chat

The Blackbird SDK allows you to stream chat responses from your agents in real-time. This is useful for creating interactive and responsive applications.

## Enabling Streaming

To enable streaming, you need to start the backend in async mode. You can do this by creating a Python script with the following content:

```python
from blackbird_sdk import BlackbirdSDK

if __name__ == "__main__":
    sdk = BlackbirdSDK(runasync=True)
    print("Async backend started. You can now run chat scripts in other terminals.")
    input("Press Enter to exit this script (the backend will keep running)...")
```

Run this script in a separate terminal and leave it running while you use the chat demo in another terminal or app.

## Streaming Responses

To stream responses from an agent, you can use the `stream_chat_response` method of the `ChatService` class. This method returns a generator that yields each chunk of the response as it arrives.

```python
from blackbird_sdk import BlackbirdSDK
import json

sdk = BlackbirdSDK()
chat_service = sdk.chat_service

print("Streaming response:")
for chunk in chat_service.stream_chat_response(
    "Tell me a story about AI.",
    agent="general"
):
    # Each chunk is a line of data, usually starting with 'data: '
    if chunk.startswith('data: '):
        try:
            data = json.loads(chunk[6:])
            # Only print the actual bot message
            if 'response' in data and data['response']:
                print(data['response'], end='', flush=True)
        except Exception:
            pass
```

## Handling Streaming Responses

The streaming response from the backend is in Server-Sent Events (SSE) format. Each chunk of the response is a line of data that starts with `data: `. You should parse each chunk as JSON after removing the `data: ` prefix.

### Handling the "replace" Field

Sometimes, the backend will send a chunk with a `"replace": true` field. This means that the previous bot response should be replaced with the new one. If you simply append every chunk, you may see duplicate or repeated answers in your UI.

To handle this, you can track where the bot's response starts in your UI. If a chunk with `"replace": true` arrives, you should clear the previous bot response and insert the new one. Otherwise, you can append the new chunk as usual.

## Embedding Streaming Chat in a UI

You can embed streaming chat in your own Python applications to create a real-time chat experience. The `examples/streaming_ui.py` file provides an example of how to do this using Tkinter.

The example shows how to create a simple chat UI with a text area for displaying the chat history and an entry field for sending messages. When a message is sent, a new thread is started to stream the response from the agent. The response is then displayed in the text area in real-time.
