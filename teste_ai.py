import asyncio
from openai import AsyncOpenAI

ai = AsyncOpenAI(
)

async def main():
    print("Enviando pergunta para a OpenAI...")

    resposta = await ai.responses.create(
        model="gpt-4.1-mini",
        input="Diga olá em português brasileiro."
    )

    print(resposta.output_text)

asyncio.run(main())