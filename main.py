import streamlit as st
import random
import time

st.set_page_config(page_title="Hack Typing Game", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #00FF00;
    }
    .stApp {
        background-color: #000000;
        color: #00FF00;
        font-family: 'Courier New', monospace;
    }
    .stTextInput > div > div > input {
        background-color: #000000;
        color: #00FF00;
        font-family: 'Courier New', monospace;
    }
    .stButton > button {
        background-color: #003300;
        color: #00FF00;
        font-family: 'Courier New', monospace;
    }
    </style>
""", unsafe_allow_html=True)

if "score" not in st.session_state:
    st.session_state.score = 0
if "word" not in st.session_state:
    st.session_state.word = ""
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "word_count" not in st.session_state:
    st.session_state.word_count = 0
if "game_active" not in st.session_state:
    st.session_state.game_active = False

words = ["binary", "compile", "debug", "variable", "streamlit", "python", "pointer", "stack", "recursion", "algorithm"]
TIME_LIMIT = 7

def generate_word():
    st.session_state.word = random.choice(words)
    st.session_state.start_time = time.time()
    st.session_state.word_count += 1
    st.session_state.game_active = True

def show_timer():
    remaining = TIME_LIMIT - int(time.time() - st.session_state.start_time)
    if remaining >= 0:
        st.markdown(f"### ⏱ 남은 시간: `{remaining}` 초")
    return remaining

st.markdown("<h1 style='color:#00FF00'>⌨️ HACK-TYPING GAME</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#00FF00'>7초 안에 정확하게 입력하세요!</h3>", unsafe_allow_html=True)

if not st.session_state.game_active or st.session_state.word == "":
    if st.button("게임 시작 / 다음 단어"):
        generate_word()
        st.experimental_rerun()
        return  # rerun 후 바로 종료

if st.session_state.word:
    st.markdown(f"## TARGET: `{st.session_state.word}`")
    remaining_time = show_timer()

    input_area = st.empty()
    answer = input_area.text_input(">>", key=st.session_state.word_count)

    if remaining_time < 0:
        st.error("⏰ TIMEOUT! 실패!")
        st.session_state.word = ""
        st.session_state.game_active = False
        st.experimental_rerun()
        return  # rerun 후 바로 종료

    if answer:
        if answer.strip().lower() == st.session_state.word.lower():
            st.success("✅ 정답! +1점")
            st.session_state.score += 1
        else:
            st.error("❌ 오답!")
        st.session_state.word = ""
        st.session_state.game_active = False
        st.experimental_rerun()
        return  # rerun 후 바로 종료

st.markdown("---")
st.markdown(f"### 🎯 SCORE: `{st.session_state.score}`", unsafe_allow_html=True)

if st.button("🔁 RESET"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()
    return
