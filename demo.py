# Simple Demo of ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
import en_core_web_sm

bot = ChatBot('MyChatBot')
trainer = ListTrainer(bot)
database = ["What is your favorite college?", "What is your favorite subject?", "Good morning, how are you?", "Who are you?"]
trainer.train(database)
nlp = en_core_web_sm.load()
default = 0
savedquestion = 0
comparison = " "

while True:
    message = input('You: ')
    if message.strip() != 'Bye':
        # reply = bot.get_response(message)
        for i in database:
            doc1 = nlp(message)
            doc2 = nlp(i)
            comparison = doc1.similarity(doc2)
            if comparison > default:
                default = comparison
                savedquestion = i
        if default == 0:
            print("Please ask another question")

    print('ChatBot:', bot.get_response(savedquestion))
    if message.strip() == 'Bye':
        print('ChatBot:Bye')
        break
