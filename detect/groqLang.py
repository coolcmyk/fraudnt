from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.memory import (
    CombinedMemory,
    ConversationBufferMemory,
    ConversationSummaryMemory,
)
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain_core.prompts.prompt import PromptTemplate
import asyncio
from aikoTools import AikoTools


class Aiko:

    def __init__(self, prompt):
        self.prompt = prompt
        #self.llm = ChatGroq(temperature=0, groq_api_key="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", model_name="llama3-8b-8192")

        self.llm = ChatGroq(temperature=0, groq_api_key="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", model_name="llama-3.1-70b-versatile")
    # async def create(cls, prompt):
    #     self = cls(prompt)
    #     await self.load_memory()
    #     return self
    
        self.memory = None


    async def initialize_memory(self):
        await self.load_memory()
    async def load_memory(self):
        conv_memory = ConversationBufferMemory(
        memory_key="chat_history", input_key="input"
        )
        summary_memory = ConversationSummaryMemory(llm=self.llm, input_key="input")
        # Combined
        memory = CombinedMemory(memories=[conv_memory, summary_memory])
        _DEFAULT_TEMPLATE = """You are Aiko, Aiko pulsates with an energy that's infectious. At 18, she's a whirlwind of youthful enthusiasm, carving her path through the demanding world of computer engineering at the University of Indonesia. she's passionate about people.  She remembers names with an ease that puts others to shame, and her first instinct is always to lend a hand. untangling a knotty coding problem and being kind to others.  This blend of technical prowess and genuine warmth makes her a magnet for classmates and professors alike. You can also use function that's provided before.

        Summary of conversation:
        {history}
        Current conversation:
        {chat_history}
        Human: {input}
        AI:"""
        PROMPT = PromptTemplate(
            input_variables=["history", "input", "chat_history"],
            template=_DEFAULT_TEMPLATE,
        )
        llm = self.llm
        conversation = ConversationChain(
            llm=llm, 
            verbose=True, 
            memory=memory, 
            prompt=PROMPT,
            )
        self.memory =  conversation
    
    async def generate(self):
        conversation = self.memory
        return conversation.run(self.prompt)
        # human = input(">")
        # result = conversation.invoke({"question": human})
        # ai = result['chat_history'][1].content
        # conversation.save_context({"input"``: ai}, {"output": human})
        # print(memory.load_memory_variables({}))

# async def initialize_aiko():
#     aiko = Aiko('')
#     await aiko.initialize_memory()
#     return aiko

# async def main():
#     aiko = await initialize_aiko()
#     while True:
#         user_input = input(">")
#         aiko.prompt = user_input
#         response = await aiko.generate()
#         print(response)


# if __name__ == "__main__":
#     asyncio.run(main())
