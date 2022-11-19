# Import Required Packages for ChatBot
import en_core_web_sm
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Read and Convert Data File into an Array
# Database must be Question & Answer Based

# Open 'customdata.txt' to add questions and answers you may want your ChatBot to learn
# data_file = open("customdata.txt", "r")

# Sample file of dev-v2.0.json(SQuAD2.0 File)
# This is due to the SQuAD database being to large
# New sample file is named as "SQuAD.json"
data_file = open("SQuAD.json", "r")
data = data_file.read()

# May replace data for a more successful comparison
# Must always include .split to separate Questions from Answers
data_array = data.replace('{"question":','').split("\n")
# data_array = data.split("\n")

data_file.close()

# Create new ChatBot
bot = ChatBot('MyChatBot')
trainer = ListTrainer(bot)
# Train ChatBot with Database
trainer.train(data_array)
# Initialize Variables
nlp = en_core_web_sm.load()
default = 0
savedQuestion = " "
doc1 = " "
doc2 = " "

# Begin Program
print("\nPlease say 'Bye' to leave the program\n")
while True:
    # Prompt User for Question
    message = input('You: ')
    if message.strip() != 'Bye':
        for item in data_array:
            doc1 = nlp(message)
            doc2 = nlp(item)
            comparison = doc1.similarity(doc2)
            # Looks for the most similar question
            # Saying that the user's input includes human errors
            if comparison > default:
                default = comparison
                savedQuestion = item

        # If no similarities in database then ask the user for another question
        if default == 0:
            print("Please ask another question")

        # Print Response From Chosen Database
        print('ChatBot:', bot.get_response(savedQuestion))

        # Reinitialize Default and SavedQuestion After Search
        default = 0
        savedQuestion = " "

    # End Program When User Says 'Bye'
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break

