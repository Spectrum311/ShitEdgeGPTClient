import EdgeGPT
import asyncio

bot = Chatbot(cookiePath='ShitEdgeGPTClient/cookies.json')

with open('./cookie.json', 'r') as f:
    cookies = json.load(f)
bot = Chatbot(cookies=cookies)


async def main():
    bot = Chatbot()
    print(await bot.ask(prompt="Hello world", conversation_style=ConversationStyle.creative, wss_link="wss://sydney.bing.com/sydney/ChatHub"))
    await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
