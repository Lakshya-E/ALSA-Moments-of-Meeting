import streamlit as st
from Backend import get_text, get_chunks, \
    get_vectorstore, get_conversation_chain, get_answers
# from Database import save_embeddings


def main_process_home(text, question, input_name):
    """This function takes audio and question and returns final response"""
    if "value_question" or "value_summary" not in st.session_state:
        # save_embeddings.save_embeds(text)
        chunks = get_chunks.get_chunks(text)
        chroma_db_retriever = get_vectorstore.chroma_vector_store(chunks)
        results = get_conversation_chain.get_conversation_chain_home(chroma_db_retriever, question)
        print(results['result'])

        if input_name == "summary":
            st.session_state['value_summary'] = results['result']
        else:
            st.session_state['value_question'] = results['result']
        # st.experimental_rerun()

    else:
        chunks = get_chunks.get_chunks(text)
        chroma_db_retriever = get_vectorstore.chroma_vector_store(chunks)
        results = get_conversation_chain.get_conversation_chain_home(chroma_db_retriever, question)
        print(results['result'])

        if input_name == "summary":
            st.session_state['value_summary'] = results['result']
        else:
            st.session_state['value_question'] = results['result']
        # st.experimental_rerun()


# def main_process_home(audio, question, input_name):
#     """This function takes audio and question and returns final response"""
#     if "value_question" or "value_summary" not in st.session_state:
#         text = get_text.get_text(audio)
#         # save_embeddings.save_embeds(text)
#
#         chunks = get_chunks.get_chunks(text)
#         chroma_db_retriever = get_vectorstore.chroma_vector_store(chunks)
#         results = get_conversation_chain.get_conversation_chain_home(chroma_db_retriever, question)
#
#         if input_name == "summary":
#             st.session_state['value_summary'] = results['result']
#         else:
#             st.session_state['value_question'] = results['result']
#
#         print(results['result'])
#
#     else:
#         text = get_text.get_text(audio)
#         # save_embeddings.save_embeds(text)
#
#         chunks = get_chunks.get_chunks(text)
#         chroma_db_retriever = get_vectorstore.chroma_vector_store(chunks)
#         results = get_conversation_chain.get_conversation_chain_home(chroma_db_retriever, question)
#
#         if input_name == "summary":
#             st.session_state['value_summary'] = results['result']
#         else:
#             st.session_state['value_question'] = results['result']
#
#         print(results['result'])
#         # st.experimental_rerun()


def main_process_save(audio):
    """This function takes audio and question and saves to database"""
    print("***Saving to database***")
    # text = get_text.get_text(audio)
    # save_embeddings.save_embeds(text)


def main_process_meetings(raw_text, question):
    """This function takes audio and question and returns final response"""
    text_chunks = get_chunks.get_chunks(raw_text)
    vector_store = get_vectorstore.embed_n_vectorstore(text_chunks)
    st.session_state.conversation = get_conversation_chain.get_conversation_chain_meetings(vector_store)
    get_answers.answer_user_question_meetings(question)
