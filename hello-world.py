import streamlit as st
import pandas as pd
#import streamlit_extras as se
#from streamlit_extras.dataframe_explorer import dataframe_explorer
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

#####################################################################################################################

if 'but_click' not in st.session_state:
    st.session_state.but_click = ''
if 'radio_click' not in st.session_state:
    st.session_state.radio_click = 'DDeutsch'

button_read = st.radio('select choice',options=['DDeutsch','中文','English'],key='rrdkey',index=0,horizontal=True)
st.session_state.radio_click = button_read
if button_read == "DDeutsch":
    df_lang_column = 1
elif button_read == "中文": 
    df_lang_column = 2
else:
    df_lang_column = 3


#####################################https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###############################
#from PIL import Image
## ## create var "df_read_file = None" with value "None", copy FuBa "read_file_text()" to "@st.cache_data"

df_read_file_cell = None                                                    ## ## create var "df_read_file = None" with value "None"
df_read_file      = None                                                    ## ## create var "df_read_file = None" with value "None"
@st.cache_data                                                         ## ## copy FuBa "read_file_text()" to "@st.cache_data"
def read_file_text():                                                  ## ## create FuBa "read_file_text()"
    global df_read_file_cell                                                ## ## "global" is for global access of var "df_read_file" 
    global df_read_file                                                ## ## "global" is for global access of var "df_read_file" 
    df_read_file = pd.read_csv("database/text_3_lang.csv")             ## ## read csv data file, FuBa is necessary, otherwise "@st.cache_data" is not possible!!!
    #st.write("57 df_read_file ", df_read_file)
    row_index = df_read_file.index[df_read_file['key'] == 'greeting_2'].values[0]  # test
    st.write("60 row_index ", row_index) # test
    df_read_file_cell = df_read_file.iloc[row_index][2]   #    df.iloc[index][col]
    return df_read_file_cell, df_read_file                                                ## ## return is for selected output, otherwise value is empty    st.write("64 df_read_file " , df_read_file)

read_file_text()
st.write("66 df_read_file_cell ", df_read_file_cell, df_read_file)
#####################################https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###############################

#@st.cache_data
#def FB_column(matrix, i):                 # Diese Funktion dient der Extraktion einzelner Spalten aus einer Liste
#    return [row[i] for row in matrix]

df_all_column = 5

df_all = pd.read_csv("database/text_bundle.csv")
st.write("71 df_all ", df_all)
rrow_index = df_all.index[df_all['key_new'] == 'greetings_2'].values[0]  # test
st.write("73 rrow_index ", rrow_index) # test
df_all_cell = df_all.iloc[rrow_index][4]   #    df.iloc[index][col]
st.write("75 df_all_cell ", df_all_cell)
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
locale = st.radio(label='Languages', options=list(language_options.keys()),horizontal=True)
st.write("91 locale ", locale)

if locale == "Deutsch":
    df_all_column = 4
elif locale == "中文": 
    df_all_column = 5
else:
    df_all_column = 6

sel_value = df_all.iloc[0,df_all_column]
st.write("101 sel_value ", sel_value)


