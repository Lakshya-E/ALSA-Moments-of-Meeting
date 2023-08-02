"""This is the home page for streamlit home button"""
import streamlit as st
# from streamlit
from Backend import get_audio
from threading import Thread
from streamlit.runtime.scriptrunner import add_script_run_ctx
from Frontend.htmlTemplate import css, summary_template, question_template

# st.set_page_config(page_title="ALSA Meets", page_icon="🏠")
st.write(css, unsafe_allow_html=True)

st.header("i-Meets :left_speech_bubble:")

if 'start' in st.session_state:
    if 'value_summary' in st.session_state:
        st.write(summary_template.replace("{{MSG}}", st.session_state.value_summary), unsafe_allow_html=True)
        st.write('\n\n')
    if 'value_question' in st.session_state:
        st.write(question_template.replace("{{MSG}}", st.session_state.value_question.replace('?', '?<br/>')), unsafe_allow_html=True)
        st.write('\n\n')

    summary_btn = st.button("Summary")
    st.write("Click *Summary* button to get the meeting summary")

    questions_btn = st.button("Questions")
    st.write("Click *Questions* button to get the brainstorm questions")

    stop_btn = st.button("Stop")
    st.write("Click *Stop* button to stop the meeting")

    reload_btn = st.button("Reload")

    if summary_btn:
        print("summary button clicked")
        get_audio.is_summary = True

    if questions_btn:
        print("questions button clicked")
        get_audio.is_question = True

    if stop_btn:
        print("stop button clicked")
        print("********************************")
        get_audio.is_stop = True
        del st.session_state['start']
        st.experimental_rerun()
    if reload_btn:
        st.experimental_rerun()

else:
    start_btn = st.button("Start")
    st.write("Click *Start* button to start the meeting")
    if start_btn:
        if "start" not in st.session_state:
            st.session_state['start'] = "Meeting Started"
        else:
            st.session_state.meet1 = "Meeting Started"

        record_thread = Thread(target=get_audio.record)
        add_script_run_ctx(record_thread)
        record_thread.start()
        st.experimental_rerun()




