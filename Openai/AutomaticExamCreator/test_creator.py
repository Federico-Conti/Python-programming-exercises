import os
import openai
from dotenv import load_dotenv
import json

load_dotenv("../.env")

openai.api_type = "azure"
openai.api_version = "2023-09-15-preview"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("OPENAI_API_KEY")

class TestGenerator:
    def __init__(self, topic, num_possible_answers, num_questions):
        self.topic = topic
        self.num_possible_answers = num_possible_answers
        self.num_questions = num_questions

        if self.num_questions > 6:
            raise ValueError("Attention! Generation of many questions might be expensive!")
        if self.num_possible_answers > 5:
            raise ValueError("More than 5 possible answers is not supported!")

    def run(self):
        prompt = self.create_prompt()
        if TestGenerator._verify_prompt(prompt):
            response = self.generate_quiz(prompt)
           # Convert the response to a dictionary
            response_dict = response.model_dump() 
            # Save the response to a JSON file
            with open('response.json', 'w') as f:
             json.dump(response_dict, f)
            return response.choices[0].text
        
        raise ValueError("Prompt not accepted.")


    def generate_quiz(self, prompt):

        response = openai.completions.create(
                model ="gpt-35-turbo-instruct",
                prompt= prompt,
                temperature=0.7,
                max_tokens=256,
            )
        return response
        

    @staticmethod
    def _verify_prompt(prompt):
        print(prompt)
        response = input("Are you happy with the prompt? (y/n)")

        if response.upper() == "Y":
            return True
        return False


    def create_prompt(self):
        prompt = f"Create a multiple choice quiz on the topic of {self.topic} consisting of {self.num_questions} questions. " \
                 + f"Each question should have {self.num_possible_answers} options. "\
                 + f"Also include the correct answer for each question using the starting string 'Correct Answer: '."
        return prompt
        

if __name__ == "__main__":
    gen = TestGenerator("Python", 4, 2)
    response = gen.run()
    print(response)
    
    
    