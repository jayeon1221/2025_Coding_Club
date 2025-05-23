import streamlit as st

# 페이지 설정
st.set_page_config(page_title="퀴즈 게임", layout="centered")

# 세션 상태 초기화
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# 퀴즈 데이터
quizzes = [
    {
        "question": "다음 중 대한민국의 수도는?",
        "options": ["서울", "부산", "인천", "대구"],
        "answer": "서울"
    },
    {
        "question": "파이썬에서 리스트를 만드는 키워드는?",
        "options": ["set", "list", "dict", "tuple"],
        "answer": "list"
    },
    {
        "question": "3 + 5 * 2 는?",
        "options": ["13", "16", "10", "8"],
        "answer": "13"
    }
]

# 퀴즈 로직
def show_quiz():
    quiz = quizzes[st.session_state.quiz_index]
    st.header(f"문제 {st.session_state.quiz_index + 1} / {len(quizzes)}")
    st.write(quiz["question"])
    
    selected = st.radio("보기 중에서 하나를 선택하세요.", quiz["options"], key=st.session_state.quiz_index)
    
    if st.button("제출", key=f"submit_{st.session_state.quiz_index}") and not st.session_state.submitted:
        st.session_state.submitted = True
        if selected == quiz["answer"]:
            st.success("정답입니다! +1점")
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다. 정답은 '{quiz['answer']}'입니다.")

    if st.session_state.submitted:
        if st.session_state.quiz_index < len(quizzes) - 1:
            if st.button("다음 문제로"):
                st.session_state.quiz_index += 1
                st.session_state.submitted = False
        else:
            st.markdown("---")
            st.subheader("🎉 퀴즈 완료!")
            st.success(f"당신의 점수는 {st.session_state.score} / {len(quizzes)}점 입니다.")
            if st.button("처음부터 다시하기"):
                st.session_state.quiz_index = 0
                st.session_state.score = 0
                st.session_state.submitted = False

# 실행
st.title("📝 간단한 퀴즈 게임")
show_quiz()
