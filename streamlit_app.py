import streamlit as st


if 'messages' not in st.session_state:
    st.session_state.messages = [] 

if 'username' not in st.session_state:
    st.session_state.username =""
    st.session_state.ready = False


if not st.session_state.ready:
    st.title("채팅방 로그인")
    st.write("채팅방에 로그인하기 위해서는 이름을 입력해주세요")
    username_input = st.text_input("이름을 입력하세요:", st.session_state.username)
    
    if st.button("입력"):
        username_input = username_input.strip()
        if username_input:
            st.session_state.username = username_input
            st.session_state.ready =True
            st.write(f"안녕하세요, {st.session_state.username}!")
            st.rerun()
        else :
            st.error("이름은 공백일 수 없습니다")
    
else :
    st.title(f"채팅방에 오신걸 환영합니다. {st.session_state.username}님!")
    message = st.chat_input("채팅을 입력하세여")
    if message :
       st.session_state.messages.append(f"{st.session_state.username}:{message}") 
       if st.session_state.messages:
            for messages in st.session_state.messages:
                st.write(messages)
