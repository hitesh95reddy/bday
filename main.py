import streamlit as st
import base64

st.title("Happy Birthday Thushu :partying_face::birthday::gift::champagne::smile: !!!")
#st.write("Here's a little something for you:")
col1,col2,col3=st.columns([1, 1, 1])
col1.write("I love you more every day.")
col2.write("I'm grateful for every moment we share.") 
col3.write("May this day be filled with as much love and joy as you bring into our lives.:smile:")

col1,col2,col3=st.columns([.5, 2, .5])
#col1.write("=================:smile:")
col2.title("Happy Birthday, My Beautiful Wife.!!! :partying_face:")
#col3.write(":smile:=================")
col1, col2 ,col3, col4, col5 = st.columns([3, 4, 5,4,3])
col1.image('gif1.gif') # This is the same as the above line, but I have the GIF saved in the same directory as the script.
col2.image('1.jpeg')
col3.image('2.jpeg')
col4.image('3.jpeg')
col5.image('gif2.gif')
# file_ = open("./gif1.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

# st.markdown(
#     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
#     unsafe_allow_html=True,
# )
