from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI()


def get_conversation_chain_home(vectorstore):
    """This function takes the vectorstore and makes a conversation chain for it"""
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return conversation_chain


def get_conversation_chain_meetings(vectorstore):
    """This function takes the vectorstore and makes a conversation chain for it"""
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain

