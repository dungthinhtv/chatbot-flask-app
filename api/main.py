from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

bot = ChatBot("chatbot",read_only=False,
                logic_adapters=[{
                    "import_path":"chatterbot.logic.BestMatch",
                    "default_response":"Sorry, I dont' have an answer",
                    "maximum_similarity_threshold":0.9
                }
            ])

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)

# list_to_train = [
#                 "hi",
#                 "hi there",
#                 "what's your name?",
#                 "I'm a chatbot",
#                 "How old are you?",
#                 "I'm ageless"
# ]

# list_to_train_2 = [
#                 "hi",
#                 "hi mate!",
#                 "what's your name?",
#                 "I'm your assistant",
#                 "How old are you?",
#                 "I'm 30 years old"
# ]




# list_trainer = ListTrainer(bot)

# list_trainer.train(list_to_train)
# list_trainer.train(list_to_train_2)




# while True:

#     user_response = input("User: ")

#     print("Chatbot: " + str(bot.get_response(user_response)))