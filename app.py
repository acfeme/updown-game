import streamlit as st
import random

st.title("🎮 업다운 게임 (1~20)")

if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 20)
    st.session_state.tries = 0
    st.session_state.message = "숫자를 입력하고 [확인]을 누르세요!"

guess = st.number_input("숫자 입력", min_value=1, max_value=20, step=1)

col1, col2 = st.columns(2)
with col1:
    if st.button("확인"):
        st.session_state.tries += 1
        if guess < st.session_state.answer:
            st.session_state.message = "⬆️ 업!"
        elif guess > st.session_state.answer:
            st.session_state.message = "⬇️ 다운!"
        else:
            st.session_state.message = f"🎉 정답! {st.session_state.tries}번 만에 성공!"

with col2:
    if st.button("새 게임"):
        st.session_state.answer = random.randint(1, 20)
        st.session_state.tries = 0
        st.session_state.message = "🔄 새 게임 시작! 숫자를 입력하세요!"

st.info(st.session_state.message)
