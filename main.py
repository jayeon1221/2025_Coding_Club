import streamlit as st

def run_quiz():
    st.title("파이썬 기초 퀴즈! 🐍")
    st.write("아래 질문에 답하고 파이썬 지식을 테스트해보세요!")

    # 퀴즈 데이터 정의
    # 각 딕셔너리는 질문, 보기, 정답 인덱스, 정답 설명을 포함합니다.
    questions = [
        {
            "question": "파이썬에서 변수를 선언할 때 사용하는 키워드는 무엇인가요?",
            "options": ["var", "let", "const", "파이썬은 변수 선언 시 별도의 키워드를 사용하지 않습니다."],
            "answer_index": 3,
            "explanation": "파이썬은 변수 선언 시 `var`, `let`, `const`와 같은 별도의 키워드를 사용하지 않고, 단순히 변수 이름과 할당 연산자(=)를 사용하여 값을 할당합니다."
        },
        {
            "question": "다음 중 파이썬에서 주석을 나타내는 기호는 무엇인가요?",
            "options": ["//", "/* */", "#", "--"],
            "answer_index": 2,
            "explanation": "파이썬에서는 `#` 기호를 사용하여 한 줄 주석을 나타냅니다. 여러 줄 주석은 보통 삼중 따옴표(```'''``` 또는 `\"\"\"\"\"\"`)를 사용합니다."
        },
        {
            "question": "파이썬에서 리스트(list)의 특징이 아닌 것은 무엇인가요?",
            "options": ["순서가 있다", "변경 가능하다 (mutable)", "중복된 값을 가질 수 없다", "다양한 데이터 타입의 요소를 포함할 수 있다"],
            "answer_index": 2,
            "explanation": "파이썬 리스트는 순서가 있고, 변경 가능하며, 중복된 값을 포함할 수 있고, 다양한 데이터 타입의 요소를 가질 수 있습니다. 중복된 값을 가질 수 없는 자료구조는 주로 세트(set)입니다."
        }
    ]

    # 세션 상태 초기화 (사용자가 새로고침해도 점수 유지)
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'show_feedback' not in st.session_state:
        st.session_state.show_feedback = False
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None
    if 'quiz_finished' not in st.session_state:
        st.session_state.quiz_finished = False

    # 퀴즈 진행 로직
    if not st.session_state.quiz_finished:
        current_q_data = questions[st.session_state.current_question]
        st.subheader(f"문제 {st.session_state.current_question + 1}. {current_q_data['question']}")

        # 라디오 버튼으로 보기 표시
        selected_option_index = st.radio(
            "답을 선택하세요:",
            options=current_q_data["options"],
            index=st.session_state.selected_option,
            key=f"question_{st.session_state.current_question}"
        )

        if st.session_state.selected_option != selected_option_index:
            st.session_state.selected_option = selected_option_index
            st.session_state.show_feedback = False # 새로운 선택 시 피드백 숨김

        # '정답 확인' 버튼
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("정답 확인", key=f"check_answer_{st.session_state.current_question}"):
                if st.session_state.selected_option is not None:
                    st.session_state.show_feedback = True
                else:
                    st.warning("답을 선택해주세요!")

        # 피드백 표시
        if st.session_state.show_feedback:
            if st.session_state.selected_option == current_q_data["answer_index"]:
                st.success("🎉 정답입니다!")
                if not st.session_state.get(f'answered_correctly_{st.session_state.current_question}', False):
                    st.session_state.score += 1
                    st.session_state[f'answered_correctly_{st.session_state.current_question}'] = True
            else:
                st.error(f"❌ 오답입니다. 정답은 '{current_q_data['options'][current_q_data['answer_index']]}' 입니다.")
            st.info(f"**설명:** {current_q_data['explanation']}")

            # '다음 문제' 버튼
            with col2:
                if st.button("다음 문제", key=f"next_question_{st.session_state.current_question}"):
                    if st.session_state.current_question < len(questions) - 1:
                        st.session_state.current_question += 1
                        st.session_state.show_feedback = False
                        st.session_state.selected_option = None
                    else:
                        st.session_state.quiz_finished = True
                        st.session_state.show_feedback = False
    else:
        # 퀴즈 종료 화면
        st.success("✨ 퀴즈가 종료되었습니다! ✨")
        st.balloons()
        st.write(f"총 {len(questions)}문제 중 **{st.session_state.score}** 문제를 맞히셨습니다!")

        if st.button("다시 시작하기"):
            st.session_state.score = 0
            st.session_state.current_question = 0
            st.session_state.show_feedback = False
            st.session_state.selected_option = None
            st.session_state.quiz_finished = False
            # 정답 여부 기록 초기화 (모든 문제에 대해)
            for i in range(len(questions)):
                if f'answered_correctly_{i}' in st.session_state:
                    del st.session_state[f'answered_correctly_{i}']
            st.experimental_rerun()

if __name__ == "__main__":
    run_quiz()
