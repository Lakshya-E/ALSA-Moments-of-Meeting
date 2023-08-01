import streamlit as st
from Backend import get_text, get_chunks, \
    get_vectorstore, get_conversation_chain, get_answers
# from Database import save_embedings


def main_process_home(text, question):
    """This function takes audio and question and returns final response"""
    # text = get_text.get_text(audio)
    # save_embedings.save_embeds(text)

    chunks = get_chunks.get_chunks(text)
    chroma_db_retriever = get_vectorstore.chroma_vector_store(chunks)
    results = get_conversation_chain.get_conversation_chain_home(chroma_db_retriever, question)
    print(results['result'])
    # return results


def main_process_meetings(question):
    """This function takes audio and question and returns final response"""
    with open("data.txt", "r") as f:
        raw_text = f.read().replace('\n', '')

    text_chunks = get_chunks.get_chunks(raw_text)
    vector_store = get_vectorstore.embed_n_vectorstore(text_chunks)
    st.session_state.conversation = get_conversation_chain.get_conversation_chain_meetings(vector_store)
    get_answers.answer_user_question_meetings(question)
