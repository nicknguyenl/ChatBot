# Simple Demo of ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('MyChatBot')
trainer = ListTrainer(bot)

conversation = open('demodata.txt', 'r').readlines()
trainer.train(conversation)

while True:
    message = input('You: ')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
    print('ChatBot:', reply)
    if message.strip() == 'Bye':
        print('ChatBot:Bye')
        break