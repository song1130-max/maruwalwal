# streamlit_app.py

import streamlit as st

st.title("💪 BMI 계산기")

# 사용자 입력
height = st.number_input("키를 입력하세요 (cm)", min_value=100.0, max_value=250.0, step=0.1)
weight = st.number_input("몸무게를 입력하세요 (kg)", min_value=30.0, max_value=200.0, step=0.1)

# BMI 계산
if st.button("BMI 계산하기"):
    if height and weight:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.write(f"당신의 BMI는 **{bmi:.2f}** 입니다.")

        # 결과 해석
        if bmi < 18.5:
            st.warning("저체중입니다. 건강에 유의하세요.")
        elif bmi < 23:
            st.success("정상 체중입니다. 잘 유지하세요!")
        elif bmi < 25:
            st.info("과체중입니다. 운동을 고려해보세요.")
        else:
            st.error("비만입니다. 건강 관리가 필요합니다.")
    else:
        st.warning("키와 몸무게를 모두 입력해주세요.")
        