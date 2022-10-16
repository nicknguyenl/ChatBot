from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datasets import load_dataset
import json

# In Progress
data = 'dev-v2.0.json2'
for row in data:
    data.replace('"','')

train = []

for k, row in enumerate(data):
    train.append(row['question'])
    train.append(row['answers'])

chatbot = ChatBot('QA')

trainer = ListTrainer(chatbot)
trainer.train(train)

while True:
    request = input(('User: '))
    response = chatbot.get_response(request)
    print('ChatBot: ', response)

