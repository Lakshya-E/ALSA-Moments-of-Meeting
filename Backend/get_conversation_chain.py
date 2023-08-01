from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.chains import RetrievalQA

load_dotenv()
llm = OpenAI()


def get_conversation_chain_home(retriever, question):
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    query = question
    result = qa({"query": query})

    return result


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

