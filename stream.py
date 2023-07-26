import streamlit as st
from Process import get_text, get_chunks,\
    get_vectorstore, get_conversation_chain, answer_question
from htmlTemplate import css, bot_template, user_template

st.set_page_config(page_title="ALSA Meets", page_icon=":movie_camera:")
st.write(css, unsafe_allow_html=True)

if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

vectorstore = None

st.header("ALSA Meets :left_speech_bubble:")


def answer_user_question(question):
    response = st.session_state.conversation({'question': question})
    # st.write(response)
    st.session_state.chat_history = response['chat_history']

    length = len(st.session_state.chat_history)
    print(st.session_state.chat_history)
    for i in range(length-1, -1, -1):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", st.session_state.chat_history[i].content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", st.session_state.chat_history[i].content), unsafe_allow_html=True)


user_question = st.text_input("Your questions")
if user_question:
    answer_user_question(user_question)

st.write(bot_template.replace("{{MSG}}", "Hello Human!"), unsafe_allow_html=True)
st.write(user_template.replace("{{MSG}}", "Hello ALSA"), unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Enter audio texts")
    audio_files = st.file_uploader("Upload your files", accept_multiple_files=True)
    if st.button("Proceed"):
        with st.spinner("Processing"):
            """If button is clicked then these processes take place"""
            # raw_text = get_text.get_text("robbery.webm")
            raw_text = get_text.get_pdf(audio_files)

            text_chunks = get_chunks.get_chunks(raw_text)

            vector_store = get_vectorstore.embed_n_vectorstore(text_chunks)

            st.session_state.conversation = get_conversation_chain.get_conversation_chain(vector_store)
            print("done")

