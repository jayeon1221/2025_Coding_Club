import streamlit as st

# 페이지 구성
st.set_page_config(page_title="방탈출 게임", layout="wide")

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "main"
if "room_index" not in st.session_state:
    st.session_state.room_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 방 데이터 정의 (여기선 예시로 2개 방)
rooms = [
    {
        "title": "첫 번째 방",
        "hint": "벽에 적힌 숫자는 3, 1, 4입니다. 무슨 숫자일까요?",
        "answer": "314"
    },
    {
        "title": "두 번째 방",
        "hint": "문을 열기 위해선 영어 단어 'apple'의 철자 수가 필요합니다.",
        "answer": "5"
    }
]

# 메인 화면
def show_main_page():
    st.title("🔐 방탈출 게임")
    st.markdown("버튼을 눌러 게임을 시작하세요.")
    if st.button("게임 시작"):
        st.session_state.page = "game"

# 게임 화면
def show_game_page():
    room = rooms[st.session_state.room_index]
    st.title(f"🚪 {room['title']}")
    
    # 힌트 출력
    st.markdown(f"💡 힌트: {room['hint']}")
    
    # 정답 입력
    answer = st.text_input("정답을 입력하세요:", key=st.session_state.room_index)
    if st.button("제출"):
        if answer == room["answer"]:
            st.success("정답입니다!")
            st.session_state.answers[st.session_state.room_index] = answer
        else:
            st.error("틀렸습니다. 다시 시도해보세요.")
    
    # 이동 버튼
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        if st.session_state.room_index > 0 and st.button("⬅️ 왼쪽"):
            st.session_state.room_index -= 1
    with col3:
        if st.session_state.room_index < len(rooms) - 1 and st.button("➡️ 오른쪽"):
            st.session_state.room_index += 1

# 화면 전환
if st.session_state.page == "main":
    show_main_page()
elif st.session_state.page == "game":
    show_game_page()
