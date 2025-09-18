# streamlit_app.py

import streamlit as st
import random

st.title("🎯 숫자 맞히기 게임")

# 세션 상태로 정답 저장
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)

# 사용자 입력
guess = st.number_input("1부터 100 사이의 숫자를 입력하세요", min_value=1, max_value=100, step=1)

# 버튼 클릭 시 결과 출력
if st.button("확인"):
    if guess < st.session_state.answer:
        st.info("너무 낮아요! 더 큰 숫자를 입력해보세요.")
    elif guess > st.session_state.answer:
        st.warning("너무 높아요! 더 작은 숫자를 입력해보세요.")
    else:
        st.success("정답입니다! 🎉")
        # 게임 리셋
        st.session_state.answer = random.randint(1, 100)
        st.balloons()