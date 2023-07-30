import streamlit as st
from Backend import get_text, get_chunks, \
    get_vectorstore, get_conversation_chain, get_answers


def main_process_home(audio, question):
    """This function takes audio and question and returns final response"""
    raw_text = get_text.get_text(audio)
    print(raw_text)
    text_chunks = get_chunks.get_chunks(raw_text)
    print(text_chunks)
    vector_store = get_vectorstore.embed_n_vectorstore(text_chunks)
    get_answers.answer_user_question_home(question)
    return "response"


def main_process_meetings(audio, question):
    """This function takes audio and question and returns final response"""
    raw_text = get_text.get_text(audio)
    text_chunks = get_chunks.get_chunks(raw_text)
    vector_store = get_vectorstore.embed_n_vectorstore(text_chunks)
    st.session_state.conversation = get_conversation_chain.get_conversation_chain_home(vector_store)
