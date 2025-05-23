import streamlit as st
import random
import time

# 기본 설정
st.set_page_config(page_title="타자 게임", layout="centered")

# 초기화
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

# 단어 리스트
words = ["apple", "banana", "python", "streamlit", "keyboard", "orange", "grape", "monitor", "escape", "click"]

# 제한 시간 (초)
TIME_LIMIT = 7

# 단어 생성
def generate_word():
    st.session_state.word = random.choice(words)
    st.session_state.start_time = time.time()
    st.session_state.word_count += 1
    st.session_state.game_active = True

# 타이머 표시
def show_timer():
    remaining = TIME_LIMIT - int(time.time() - st.session_state.start_time)
    if remaining >= 0:
        st.warning(f"⏱ 남은 시간: {remaining}초")
    return remaining

# 타자 게임 시작
st.title("⌨️ 제한시간 타자 게임")
st.write("제시된 단어를 7초 안에 입력하세요!")

# 시작/다음 단어 버튼
if not st.sessi
