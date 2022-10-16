# https://discuss.huggingface.co/t/question-answering-bot-fine-tuning-with-custom-dataset/4412/2
# In Progress
import json
from datasets import load_dataset

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
                answers["text"] = [a["text"] for a in qa["answers"]]
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


ds = load_dataset("json", data_files=output_filename)

