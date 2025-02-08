# # import the packages
# import streamlit as st
# import google.generativeai as genai
# from streamlit_chat import message

# # Provide the api key
# api_key = "<Api-Key>"
# genai.configure(api_key=api_key)

# # Read the Model

# # Streamlit UI Parameters
# st.title("Google Gemini Chatbot")


# def generate_response(prompt):
#     model = genai.GenerativeModel("gemini-1.5-flash-latest")
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     output = response.text
#     return output


# # create chat history
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# if 'bot_history' not in st.session_state:
#     st.session_state['bot_history'] = []

# input_container = st.container()
# response_container = st.container()

# # capture user input and display bot response
# user_input = st.text_input("You: ", "", key="input")

# with response_container:
#     if user_input:
#         response = generate_response(user_input)
#         st.session_state['chat_history'].append(user_input)
#         st.session_state['bot_history'].append(response)

#     num_messages = min(len(st.session_state['chat_history']), len(st.session_state['bot_history']))
#     if num_messages > 0:
#         for i in range(num_messages):
#             message(st.session_state['chat_history'][i], is_user=True, key=str(i) + '_user', avatar_style="initials",
#                     seed="Me")
#             message(st.session_state['bot_history'][i], key=str(i), avatar_style="initials", seed="AI", )

# with input_container:
#     display_input = user_input
    


#pip install google-generativeai
#pip install streamlit-chat
# streamlit run filename.py
# python -m streamlit run filename.py

import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# Provide the API key
api_key = "YOUR_API_KEY"   # enter your api key
genai.configure(api_key=api_key)

# Streamlit UI Parameters
st.title("Google Gemini Chatbot")

# Function to generate response
def generate_response(prompt, chat_history):
    # Include previous messages in the history to maintain context
    history = [{"author": "user", "content": msg} for msg in chat_history]
    response = genai.chat(messages=history + [{"author": "user", "content": prompt}])
    return response["candidates"][0]["content"]

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'bot_history' not in st.session_state:
    st.session_state['bot_history'] = []

# Input and response containers
input_container = st.container()
response_container = st.container()

# Capture user input and display bot response
user_input = st.text_input("You: ", "", key="input")

with response_container:
    if user_input:
        response = generate_response(user_input, st.session_state['chat_history'])
        st.session_state['chat_history'].append(user_input)
        st.session_state['bot_history'].append(response)

    num_messages = min(len(st.session_state['chat_history']), len(st.session_state['bot_history']))
    if num_messages > 0:
        for i in range(num_messages):
            message(st.session_state['chat_history'][i], is_user=True, key=str(i) + '_user', avatar_style="initials", seed="Me")
            message(st.session_state['bot_history'][i], key=str(i), avatar_style="initials", seed="AI")

with input_container:
    display_input = user_input








