import logging

import chainlit as cl
from openai import AsyncClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


client = AsyncClient()
system = dict(role="system", content="You are a helpful assistant.")
settings = dict(temperature=0, max_tokens=100, model='gpt-3.5-turbo-1106')


@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [system])


@cl.on_message
async def message(message: cl.Message):
    chat_history = cl.user_session.get("chat_history")
    chat_history.append(dict(role="user", content=message.content))

    stream = await client.chat.completions.create(
        messages=chat_history, stream=True, **settings
    )

    out = cl.Message(content="")
    await out.send()

    async for chunk in stream:
        if token := chunk.choices[0].delta.content or "":
            await out.stream_token(token)

    await out.update()
    chat_history.append(dict(role="assistant", content=out.content))
    logging.info(chat_history)
