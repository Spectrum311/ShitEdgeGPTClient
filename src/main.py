bot = Chatbot(cookiePath='ShitEdgeGPTClient/cookies.json')

with open('./cookie.json', 'r') as f:
    cookies = json.load(f)
bot = Chatbot(cookies=cookies)
