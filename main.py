import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="타자 게임", layout="centered")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "word" not in st.session_state:
    st.session_state.word = ""
if "event" not in st.session_state:
    st.session_state.event = None
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "word_count" not in st.session_state:
    st.session_state.word_count = 0

# 단어 목록
words = ["apple", "banana", "python", "streamlit", "computer", "typing", "keyboard", "monitor", "orange", "grape"]

# 이벤트 목록
events = ["BONUS", "TIMER", "BOMB", None, None]

# 새 단어 생성 함수
def generate_word():
    st.session_state.word = random.choice(words)
    st.session_state.event = random.choice(events)
    st.session_state.start_time = time.time()
    st.session_state.word_count += 1

# 게임 시작
st.title("⌨️ 타자 게임")
st.write("화면에 표시된 단어를 빠르게 입력하세요!")

# 단어 생성 버튼
if st.button("게임 시작 / 다음 단어"):
    generate_word()

# 이벤트 설명
event_msg = {
    "BONUS": "🎁 보너스 단어! 맞추면 +2점!",
    "TIMER": "⏱ 제한 시간 5초! 빨리 입력하세요!",
    "BOMB": "💣 폭탄 단어! 틀리면 -2점!",
    None: "일반 단어입니다. 맞추면 +1점"
}

if st.session_state.word:
    st.markdown(f"## 단어: `{st.session_state.word}`")
    st.info(event_msg[st.session_state.event])

    typed = st.text_input("입력하세요:", key=st.session_state.word_count)

    if typed:
        correct = typed.strip().lower() == st.session_state.word.lower()
        time_taken = time.time() - st.session_state.start_time

        if st.session_state.event == "TIMER" and time_taken > 5:
            st.warning("⏰ 시간이 초과되었습니다! 실패!")
        elif correct:
            if st.session_state.event == "BONUS":
                st.success("🎉 보너스 정답! +2점")
                st.session_state.score += 2
            else:
                st.success("✅ 정답! +1점")
                st.session_state.score += 1
        else:
            if st.session_state.event == "BOMB":
                st.error("💥 폭탄 단어 틀림! -2점")
                st.session_state.score -= 2
            else:
                st.error("❌ 틀렸습니다.")

        # 다음 단어 위해 초기화
        st.session_state.word = ""

# 점수 출력
st.markdown("---")
st.subheader(f"🎯 현재 점수: {st.session_state.score}점")

# 다시 시작 버튼
if st.button("처음부터 다시하기"):
    st.session_state.score = 0
    st.session_state.word = ""
    st.session_state.event = None
    st.session_state.word_count = 0
