import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values('.env')
openai.api_key = config['OPENAI_API_KEY']

def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end

def main():
    parser = argparse.ArgumentParser(description="Simple Command line ChatBot backed up by GPT model by OPENAI")
    parser.add_argument("--personality", type=str, help="A brief summary of the chatbot's personality", default= "very friendly")
    args = parser.parse_args();
  
    messages = [
        {"role": "system", "content":f"You are a helpful assistant chatbot. And your personality is {args.personality}"}
    ]

    while True:
        try:
            user_input = input(bold(blue("You: ")))
            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages= messages,
            max_tokens=200
            )
            
            assistant_message = response["choices"][0]["message"].to_dict()
            messages.append( assistant_message)
            print("Assistant: ", bold(red(assistant_message["content"])))
        
        except KeyboardInterrupt:
            print("Exiciting....")
            break

if __name__ == "__main__":
    main()

