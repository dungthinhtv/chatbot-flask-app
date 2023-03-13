from chatterbot import ChatBot

bot = ChatBot("units",logic_adapters=["chatterbot.logic.UnitConversion"])

print("------------Math Chatbot-------------")
while True:
    user_text = input ("Ask a question (unit conversion): ")
    print("Chatbot: " + str(bot.get_response(user_text)))