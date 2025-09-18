# streamlit_app.py

import streamlit as st
import random

st.title("🧮 수학 퀴즈 게임")

# 세션 상태 초기화
if "num1" not in st.session_state:
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.op = random.choice(["+", "-", "*"])

# 문제 생성
num1 = st.session_state.num1
num2 = st.session_state.num2
op = st.session_state.op

# 정답 계산
if op == "+":
    answer = num1 + num2
elif op == "-":
    answer = num1 - num2
else:
    answer = num1 * num2

# 문제 출력
st.subheader(f"문제: {num1} {op} {num2} = ?")
user_answer = st.number_input("당신의 답을 입력하세요", step=1)

# 버튼 클릭 시 결과 확인
if st.button("정답 확인"):
    if user_answer == answer:
        st.success("정답입니다! 🎉")
        st.balloons()
    else:
        st.error(f"틀렸어요 😢 정답은 {answer}입니다.")

    # 다음 문제로 초기화
    st.session_state.num1 = random.randint(1, 20)
    st.session_state.num2 = random.randint(1, 20)
    st.session_state.op = random.choice(["+", "-", "*"])
    