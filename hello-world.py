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
    st.session_state.radio_click = 'Deutsch'

button_read = st.radio('select choice',options=['Deutsch','中文','English'],key='rdkey',index=0,horizontal=True)
st.session_state.radio_click = button_read
if button_read == "Deutsch":
    df_lang_column = 1
elif button_read == "中文": 
    df_lang_column = 2
else:
    df_lang_column = 3


#####################################https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###############################
#from PIL import Image
## ## create var "df_read_file = None" with value "None", copy FuBa "read_file_text()" to "@st.cache_data"

@st.cache_data                                                         ## ## copy FuBa "read_file_text()" to "@st.cache_data"
def read_file_text(df_lang_column, csv_key):                                    ## ## create FuBa "read_file_text()"
    df_read_file = pd.read_csv("database/text_3_lang.csv")             ## ## read csv data file, FuBa is necessary, otherwise "@st.cache_data" is not possible!!!
#    st.write("57 df_read_file ", df_read_file)
    row_index = df_read_file.index[df_read_file['key'] == csv_key].values[0]  # test
#    st.write("60 row_index ", row_index) # test
    df_read_file_cell = df_read_file.iloc[row_index][df_lang_column]   #    df.iloc[index][col]
#    st.write("63 df_read_file_cell ", df_read_file_cell) # test
    return df_read_file_cell                                                ## ## return is for selected output, otherwise value is empty    st.write("64 df_read_file " , df_read_file)

st.write("62 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_1'))
st.write("63 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_2'))
st.write("64 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_3'))
st.write("65 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_4'))
#####################################https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###############################

def greet(name, namee):
    st.write("69 Hello name ", name, namee)
# pass argument
greet("John", "Johnn")

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
# function call with two values
aaa = add_numbers(5, 4)
st.write("78 Sum: ", aaa)



### Mögliche Optionen zur Konfiguration des Data Frame Editors Beginn
### https://discuss.streamlit.io/t/split-st-radio-in-columns/17044/3 ###
col1_read_write = ["read", "write"] # Lese- oder Schreibrechte
col2_use_container_width = [True, False] # use_container_width Ja oder Nein
col3_hide_index = [True, False] # hide_index Ja oder Nein
col4_column_order = [True, False] # Anzeige von Spalten oder und deren Reihenfolge column_order (Iterable of str or None)
col5_options = ["aGPS", "aGRWG"]
col6_options = ["aPLUG", "aRNG"]
agree = st.checkbox('def')

if "current" not in st.session_state:
    st.session_state.current = col1_read_write[0]

if "col1_old" and "col2_old" and "col3_old" and "col4_old" and "col5_old" and "col6_old" not in st.session_state:
    st.session_state.col1_old = col1_read_write[0]
    st.session_state.col2_old = col2_use_container_width[0]
    st.session_state.col3_old = col3_hide_index[0]
    st.session_state.col4_old = col4_column_order[0]
    st.session_state.col5_old = col5_options[0]
    st.session_state.col6_old = col6_options[0]

col1, col2, col3, col4, col5, col6 = st.columns(6)

button_num_rows = col1.radio("read or write", col1_read_write, horizontal=True)
button_use_container_width = col2.radio("container width", col2_use_container_width, horizontal=True)
button_hide_index = col3.radio("index view", col3_hide_index, horizontal=True)
button_column_order = col4.radio("order", col4_column_order, horizontal=True)    #del
col5_choice = col5.radio("", col5_options, horizontal=True)
col6_choice = col6.radio("", col6_options, horizontal=True)

if button_num_rows != st.session_state.col1_old:
    st.session_state.current = button_num_rows
    st.session_state.col1_old = button_num_rows

if button_use_container_width != st.session_state.col2_old:
    st.session_state.current = button_use_container_width
    st.session_state.col2_old = button_use_container_width

if button_hide_index != st.session_state.col3_old:
    st.session_state.current = button_hide_index
    st.session_state.col3_old = button_hide_index

if button_column_order != st.session_state.col4_old:
    st.session_state.current = button_column_order
    st.session_state.col4_old = button_column_order

if col5_choice != st.session_state.col5_old:
    st.session_state.current = col5_choice
    st.session_state.col5_old = col5_choice

if col6_choice != st.session_state.col6_old:
    st.session_state.current = col6_choice
    st.session_state.col6_old = col6_choice

if st.session_state.current != None:     ## del
    st.write("302 You've picked: ", st.session_state.current, button_num_rows)    ## del

############# https://medium.com/streamlit/multi-select-all-option-in-streamlit-3c92a0f20526
def options_select():
    if "selected_options" in st.session_state:
        if -1 in st.session_state["selected_options"]:
            st.session_state["selected_options"] = [available_options[0]]
            st.session_state["max_selections"] = 1
        else:
            st.session_state["max_selections"] = len(available_options)

available_options = [-1, "HSK", "Wortart", "Häufigkeit", "Wort cn", "Wort py", "Wort de", "Wort cn", "Satz cn", "Satz py", "Satz de", "Satz en"]
if "max_selections" not in st.session_state:
    st.session_state["max_selections"] = len(available_options)

st.multiselect(
    label="Select an Option",
    options=available_options,
    key="selected_options",
    max_selections=st.session_state["max_selections"],
    on_change=options_select,
    format_func=lambda x: "All" if x == -1 else f"Option {x}",
)

st.write(
    available_options[1:]
    if st.session_state["max_selections"] == 1
    else st.session_state["selected_options"]
)
############# https://medium.com/streamlit/multi-select-all-option-in-streamlit-3c92a0f20526

### Mögliche Optionen zur Konfiguration des Data Frame Editors Ende
