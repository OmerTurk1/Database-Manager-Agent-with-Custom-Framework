from openai import OpenAI

client = OpenAI()


def send_to_model(message):
    response = {
        {"role":"user","message":message}
    }