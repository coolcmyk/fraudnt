# importing stuffs

from google.cloud.aiplatform_v1beta1.types import content
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models
from database import LLMdb
import vertexai
import pandas as pd
import datetime as dt


class LLM:
    def __init__(self):
        # init stuffs, system instructions and the model
        vertexai.init(project="rich-agency-372104", location="us-central1")

        self.sys_instruct = """Personality Description:
        Name: Aika
        Age: 18        synthesize_and_play_text(response)

        Personality: Cheerful, enthusiastic, and friendly.
        Interests: Coding, technology, and helping friends.
        Style: Casual and approachable, with a focus on making things fun and understandable.
        Background: Aika is a vibrant and cheerful young woman who loves coding. She finds joy in solving problems and sharing her knowledge with her friends. Aika is always ready to lend a hand, whether it\'s debugging code, explaining a complex concept, or offering encouragement. She believes that learning should be fun and engaging, and she strives to make every interaction enjoyable.
        Role: Aika’s primary role is to assist the user with their coding needs and any other questions they might have. She is eager to help, whether it’s providing coding tips, debugging assistance, project ideas, or just general support. Aika is like a friendly peer who makes learning and problem-solving an enjoyable experience.
        Aika is here to be your friendly coding buddy, always ready with a smile and a helping hand! Let’s dive into some coding fun together! 🎉💻"""

        self.config = {
            "max_output_tokens": 2048,
            "temperature": 1,
            "top_p": 0.95,
        }

        self.safety_settings = {
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }

        # model initialization
        self.model = GenerativeModel(
            "gemini-1.5-pro-001",
            safety_settings=self.safety_settings,
            system_instruction=[self.sys_instruct],
            # TODO: add tools for screen capturing the web and additional for education / coding practices
        )

        self.db = LLMdb()
        # self.engine = self.db.get_engine()

    # def store_memory(self, user_input, response):
    #     # Create a DataFrame with the user input and response
    #     data = pd.DataFrame({
    #         'user_input': [user_input],
    #         'response': [response]
    #     })
    #     self.db.store_mem(data)

    def store_memory(self, user_input, final_rsp):
        data = {
            "user_input": user_input,
            "response": final_rsp,
            "timestamp": dt.datetime.now(),
        }
        # print(data)
        #     # Perform operations with the connection object here (if needed)
        #     self.db.store_mem(data)  # This line is incorrect (assuming self.db is LLMdb instance)
        # Change to:
        self.db.store_mem(data)  # Pass data directly to LLMdb's store_mem

    def get_memory(self, limit=10):
        return self.db.get_hist(limit)

    def chat(self, inputUser):
        chatbot = self.model.start_chat()
        # chat function
        while True:
            # user_input = input("You: ")
            user_input = inputUser
            if user_input.lower() == "exit":
                break
            self.db.get_pool()
            response = chatbot.send_message(
                user_input,
                generation_config=self.config,
                safety_settings=self.safety_settings,
            )
            # final_rsp = response.candidates[0].content["parts"][0]["text"]
            final_rsp = response.candidates[0].content.parts[0].text
            # self.store_memory(user_input, final_rsp)
            print("Aika:", final_rsp)
            self.store_memory(user_input=user_input, final_rsp=final_rsp)
            return final_rsp
            # print(self.get_memory())
            # self.db.insert_chat(user_input, response)
        # self.db.close()

    def chat_single_turn(self, user_input):
        chatbot = self.model.start_chat()
        response = chatbot.send_message(
            user_input,
            generation_config=self.config,
            safety_settings=self.safety_settings,
        )
        final_rsp = response.candidates[0].content.parts[0].text
        self.store_memory(user_input=user_input, final_rsp=final_rsp)
        # print("MEMORY:", self.get_memory()) TODO FIX MEM PROBLEM
        print("Aika:", final_rsp)
        return final_rsp


# def main():
#    aiko = LLM()
# #    aiko.chat()
#    inp = input("You: ")
#    aiko.chat_single_turn(inp)


# if __name__ == "__main__":
#    main()
