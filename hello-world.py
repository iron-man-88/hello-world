import streamlit as st
import pandas as pd
st. set_page_config(layout="wide") # https://discuss.streamlit.io/t/how-to-increase-the-width-of-web-page/7697

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
st.markdown( # https://stackoverflow.com/questions/74611608/how-to-change-the-height-of-streamlit-sidebar
    """
    <style>
    section[data-testid="stSidebar"][aria-expanded="true"]{height: 100% !important;}
    section[data-testid="stSidebar"][aria-expanded="false"]{height: 100% !important;}              
    div[class='appview-container st-emotion-cache-1wrcr25 ea3mdgi4']{margin-top: -60px;}
    div[class='st-emotion-cache-6qob1r eczjsme3']{margin-top: -80px;}
    div[class='st-emotion-cache-1nm2qww eczjsme2']{margin-top: 70px;}
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown( # Breite des main divs
    """<style>.block-container {padding-bottom: 0.01rem;: 0 !important; padding-top: 0.5rem;: 0 !important;  \
        padding-left: 0.25rem;: 0 !important; padding-right: 0.25rem;: 0 !important;}</style>""",
    unsafe_allow_html=True,)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

st.sidebar.title('Hello, World! It is wonderful')
st.title('Hello Jesus Christ!')
st.title('You are great!')
st.title('The Preeminent One')

# Create a two-column layout
col1, col2 = st.columns([0.001, 1]) # this will just call methods directly in the returned objects
# Inside the first column, add the answer text
with col1:
    st.write("")
# Inside the second column, add the image
with col2:
#    st.image("img/001.jpg", caption="Lightning Image", use_column_width=True)
    st.write("")
###################################################################################################################
#@st.cache_data
#def FB_column(matrix, i):                 # Diese Funktion dient der Extraktion einzelner Spalten aus einer Liste
#    return [row[i] for row in matrix]

df_all_column = 5

df_all = pd.read_csv("database/text_bundle.csv")
st.write("46 df_all ", df_all)
row_index = df_all.index[df_all['key_new'] == 'greetings_1'].values[0]  # test
st.write("48 row_index ", row_index) # test
df_all_cell = df_all.iloc[0][4]   #    df.iloc[index][col]
st.write("50 df_all_cell ", df_all_cell)
#FullList = df_all.values.tolist()
#st.write("51 FullList ", FullList)
#FullListColumn2 = FB_column(FullList, 4)
#st.write("54 FullListColumn2 ", FullListColumn2)
#IndexSeite = FullListColumn2.index("Hallo, Welt1!")
#st.write("56 IndexSeite ", IndexSeite)
#vvaluee = FullList[IndexSeite][4]
#st.write("58 vvaluee ", vvaluee)


language_options = {
    "Deutsch":"de",
    "中文":"cn",
    "English":"en"
}
lllocale = st.radio(label='Languages', options=list(language_options.keys()),horizontal=True)
st.write("64 lllocale ", lllocale)

if lllocale == "Deutsch":
    df_all_column = 4
elif lllocale == "中文": 
    df_all_column = 5
else:
    df_all_column = 6

sel_value = df_all.iloc[0,df_all_column]
st.write("77 sel_value ", sel_value)

# https://medium.com/@groxli/konnichiwa-streamlit-689e6e48bdcb
@st.cache_data
def load_bundle(locale):
    # Load in the text bundle and filter by language locale.
    df = pd.read_csv("database/text_bundle.csv")
    #st.write("84 df ", df)
    df = df.query(f"locale == '{locale}'")# Create and return a dictionary of key/values.
    st.write("df.query ", df)
    lang_dict    = {df.key.to_list()[i]:df.value.to_list()[i] for i in range(len(df.key.to_list()))}
    st.write("lang_dict ", lang_dict)
    return lang_dict
def main():
    lang_options = {
        "English (US)":"en_US",
        "日本語":"ja_JP"
    }
    locale = st.radio(label='Language', options=list(lang_options.keys()),horizontal=True) # Note we use the selected human-readable locale to get the relevant
    st.write("96 locale ", locale)
    # ISO locale code from the lang_options dictionary.
    lang_dict = load_bundle(lang_options[locale])
    st.subheader(lang_dict['greeting'])
main()


##https://stackoverflow.com/questions/73727634/how-to-replace-displayed-value-on-a-button-click-on-streamlit###
if 'num' not in st.session_state:
    st.session_state.num = "1"
def update1():
    st.session_state.num = "1"
def update2():
    st.session_state.num = "2"
def update3():
    st.session_state.num = "3"

key2 = "key_2"

st.write(st.session_state.num)
st.button("Perform calculation 1", on_click=update1, key="key_1")
st.button("Perform calculation 2", on_click=update2, key=key2)
st.button("Perform calculation 3", on_click=update3, key='key_3')

##https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###
from PIL import Image
df_read_file = None
@st.cache_data
def read_file_text():
    global df_read_file
    df_read_file = pd.read_csv("database/text_3_lang.csv")
    st.write("127 df_read_file ", df_read_file)
    st.write("128 df_read_file.iloc[0,1]", df_read_file.iloc[0,1])
    return df_read_file

read_file_text()
st.write("132 df_read_file.iloc[0,1]", df_read_file)

if 'but_click' not in st.session_state:
    st.session_state.but_click = ''
if 'radio_click' not in st.session_state:
    st.session_state.radio_click = 'Deutsch'

with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns([1,0.001,0.001],gap='small')

    with left_column:
        st.subheader(16)
        # n = st.session_state.bt
        c = st.button("Click me ⤵️")

        if (c) or (st.session_state.but_click == 'y'):
            brd = st.radio('select choice',options=['Deutsch','中文','English'],key='rdkey',index=0,horizontal=True)
            #brd_sel = brd
            st.session_state.but_click = 'y'
            if (st.session_state.but_click=='y') and (brd == brd):
                st.session_state.radio_click = brd
                st.write(brd)

