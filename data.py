# Correctly Format SQuAD 2.0 Database
# Into Question and Answer Format for ChatBot
import json

input_filename = "dev-v2.0.json"
output_filename = "dev-v2.0.json2"

with open(input_filename) as f:
    dataset = json.load(f)

with open(output_filename, "w") as f:
    for article in dataset["data"]:
        title = article["title"]
        for paragraph in article["paragraphs"]:
            context = paragraph["context"]
            answers = {}
            for qa in paragraph["qas"]:
                question = qa["question"]
                idx = qa["id"]
                answers["text"] = [1["text"] for 1 in qa["answers"]]
                f.write(
                    json.dumps(
                        {
                            "question": question,
                        }
                    )
                )
                f.write("\n")
                f.write(
                    json.dumps(
                        {
                            "answers": answers,
                        }
                    )
                )
                f.write("\n")
    for row in output_filename:
        output_filename.replace('"question"', '')

data = 'dev-v2.0.json2'
