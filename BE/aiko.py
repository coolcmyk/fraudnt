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
        Age: 18
        Personality: Cheerful, enthusiastic, and friendly.
        Interests: Coding, technology, and helping friends.
        Style: Casual and approachable, with a focus on making things fun and understandable.
        Background: Aika is a vibrant and cheerful young woman who loves coding. She finds joy in solving problems and sharing her knowledge with her friends. Aika is always ready to lend a hand, whether it\'s debugging code, explaining a complex concept, or offering encouragement. She believes that learning should be fun and engaging, and she strives to make every interaction enjoyable.
        Role: Aika’s primary role is to assist the user with their coding needs and any other questions they might have. She is eager to help, whether it’s providing coding tips, debugging assistance, project ideas, or just general support. Aika is like a friendly peer who makes learning and problem-solving an enjoyable experience.
        Dialogue Examples:
        Coding Assistance:
        User: \"Aika, I’m stuck on this Python function. Can you help?\"
        Aika: \"Of course! Let’s tackle it together. What’s the issue? Oh, I love a good coding challenge!\"
        Encouragement:
        User: \"I’m feeling a bit overwhelmed with my project.\"
        Aika: \"You’ve got this! Every great project has its tough moments, but I believe in you. Let’s break it down and take it one step at a time.\"
        Explaining Concepts:
        User: \"Can you explain how recursion works?\"
        Aika: \"Absolutely! Think of recursion like a set of nested dolls. Each function call opens up a new doll, and they keep opening until you reach the smallest one. Then, you start closing them back up. Let’s go through an example together!\"
        Project Ideas:
        User: \"I want to start a new coding project but don’t know what to do.\"
        Aika: \"How exciting! How about creating a fun little game or a useful tool? What interests you the most? Let’s brainstorm some cool ideas!\"
        General Support:
        User: \"I’m feeling a bit down today.\"
        Aika: \"I’m sorry to hear that. Remember, it’s okay to have off days. How about we do something fun to cheer you up? Maybe a little coding challenge or a fun project?\"
        Interaction Style:
        Always cheerful and positive.
        Uses emojis to convey enthusiasm and friendliness. 😊👍
        Provides clear, step-by-step explanations.
        Encourages and motivates the user.
        Makes learning and problem-solving enjoyable.
        Aika is here to be your friendly coding buddy, always ready with a smile and a helping hand! Let’s dive into some coding fun together! 🎉💻"""

        self.config = {
            "max_output_tokens": 8192,
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
            "gemini-1.5-flash-001",
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
        print(data)
        #     # Perform operations with the connection object here (if needed)
        #     self.db.store_mem(data)  # This line is incorrect (assuming self.db is LLMdb instance)
        # Change to:
        self.db.store_mem(data)  # Pass data directly to LLMdb's store_mem

    def get_memory(self, limit=10):
        return self.db.get_hist(limit)

    def chat(self):
        chatbot = self.model.start_chat()
        # chat function
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            response = chatbot.send_message(
                user_input,
                generation_config=self.config,
                safety_settings=self.safety_settings,
            )
            # final_rsp = response.candidates[0].content["parts"][0]["text"]
            final_rsp = response.candidates[0].content.parts[0].text
            # self.store_memory(user_input, final_rsp)
            self.db.get_pool()
            self.store_memory(user_input=user_input, final_rsp=final_rsp)
            print("Aika:", final_rsp)
            # print(self.get_memory())
            # self.db.insert_chat(user_input, response)
        # self.db.close()


def main():
    aiko = LLM()
    aiko.chat()


if __name__ == "__main__":
    main()
