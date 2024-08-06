import time
import streamlit as st
from hachikosjournal import Hachiko

hachiko = Hachiko()

def response_generator(response: str):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.set_page_config(
    page_title='Hachiko\' Journal',
    page_icon='img/HachikoAvatar.png',
    layout='centered',
)

with st.sidebar:
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.image('img/Hachiko.gif')

    st.write('Hi! I\'m Hachiko!')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
        with st.chat_message(message['role'], avatar=message['avatar']):
            st.markdown(message['content'])

if prompt := st.chat_input('Tell me what you\'re thinking.'):
    st.chat_message('user', avatar='https://api.dicebear.com/8.x/icons/svg?seed=Willow').markdown(prompt)
    st.session_state.messages.append(
        {
            'role': 'user',
            'content': prompt,
            'avatar': 'https://api.dicebear.com/8.x/icons/svg?seed=Willow',
        },
    )

    try:
        response = hachiko.talk(prompt)
    except:
        response = 'Sorry, something went wrong. Can we try that again?'

    with st.chat_message('hachiko', avatar='img/HachikoAvatarBG.png'):
        st.write_stream(response_generator(response))

    st.session_state.messages.append(
        {
            'role': 'hachiko',
            'content': response,
            'avatar': 'img/HachikoAvatarBG.png',
        },
    )

# with col2:
#     st.image('img/Hachiko.gif')

# _, col1, _, col2, _ = st.columns([1, 3, 1, 1, 1])

# st.markdown(
#     """
#     <style>
#     [data-testid="stAppViewContainer"] {
#         background-image: linear-gradient(to right, #2c2751, #233155, #1e3957, #224156, #2c4754);
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# with col1:
#     st.header('Hachiko\'s Journal')
#     text = st.text_area(
#         'Tell Hachiko your thoughts',
#         height=300,
#     )

# default_response = '#### Tell me how you\'re feeling, friendo!'
# with col2:
#     st.image('img/Hachiko.gif')
#     with st.empty():
#         if len(text.strip()) == 0:
#             st.write(default_response)
#         else:
#             try:
#                 response = hachiko.talk(text)
#                 st.write('#### ' + hachiko.talk(text))
#             except:
#                 st.write(default_response)
