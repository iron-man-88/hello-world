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

#df_read_file_cell = None                                                    ## ## create var "df_read_file = None" with value "None"
#df_read_file      = None                                                    ## ## create var "df_read_file = None" with value "None"
#@st.cache_data                                                         ## ## copy FuBa "read_file_text()" to "@st.cache_data"
#def read_file_text():                                                  ## ## create FuBa "read_file_text()"
#    global df_read_file_cell                                                ## ## "global" is for global access of var "df_read_file" 
#    global df_read_file                                                ## ## "global" is for global access of var "df_read_file" 
#    df_read_file = pd.read_csv("database/text_3_lang.csv")             ## ## read csv data file, FuBa is necessary, otherwise "@st.cache_data" is not possible!!!
#    #st.write("57 df_read_file ", df_read_file)
#    row_index = df_read_file.index[df_read_file['key'] == 'greeting_2'].values[0]  # test
#    st.write("60 row_index ", row_index) # test
#    df_read_file_cell = df_read_file.iloc[row_index][2]   #    df.iloc[index][col]
#    df_read_file_cell = df_read_file.at[1][2]   #    df.iloc[index][col]
#    return df_read_file_cell, df_read_file                                                ## ## return is for selected output, otherwise value is empty    st.write("64 df_read_file " , df_read_file)

#read_file_text()
#st.write("66 df_read_file_cell ", df_read_file_cell, df_read_file)
#####################################https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###############################

@st.cache_data
#def FB_column(matrix, i):                 # Diese Funktion dient der Extraktion einzelner Spalten aus einer Liste
#    return [row[i] for row in matrix]

#df_all_column = 1

#df_all = pd.read_csv("database/text_bundle.csv")
#st.write("76 df_all ", df_all)
#rrow_index = df_all.index[df_all['key_new'] == 'greetings_2'].values[0]  # test
#st.write("78 rrow_index ", rrow_index) # test
#df_all_cell = df_all.iloc[rrow_index][4]   #    df.iloc[index][col]
#st.write("80 df_all_cell ", df_all_cell)
#FullList = df_all.values.tolist()
#st.write("82 FullList ", FullList)
#FullListColumn2 = FB_column(FullList, 4)
#st.write("84 FullListColumn2 ", FullListColumn2)
#IndexSeite = FullListColumn2.index("Hallo, Welt1!")
#st.write("86 IndexSeite ", IndexSeite)
#vvaluee = FullList[IndexSeite][4]
#st.write("88 vvaluee ", vvaluee)

#language_options = {
#    "Deutsch":"de",
#    "中文":"cn",
#    "English":"en"
#}
#locale = st.radio(label='Languages', options=list(language_options.keys()),horizontal=True)
#st.write("91 locale ", locale)

#if locale == "Deutsch":
#    df_all_column = 4
#elif locale == "中文": 
#    df_all_column = 5
#else:
#    df_all_column = 6

#sel_value = df_all.iloc[0,df_all_column]
#st.write("101 sel_value ", sel_value)



#@st.cache_data                                                         ## ## copy FuBa "read_file_text()" to "@st.cache_data"
#def namee(x):
#    x = 1+1
#    return x

#x = None                                                    ## ## create var "df_read_file = None" with value "None"

#namee(3)

#@st.cache_data                                                         ## ## copy FuBa "read_file_text()" to "@st.cache_data"
#def smaller_numm(x,y):
#    if x>y:
#        number= y
#    else:
#        number= x
#    return number

#x = 31
#y = 7

#smaller = smaller_numm(x, y)
#st.write("The smaller number between 119 ", smaller)







# https://medium.com/@groxli/konnichiwa-streamlit-689e6e48bdcb
@st.cache_data
def load_bundle(locale):
    # Load in the text bundle and filter by language locale.
    df = pd.read_csv("database/text_bundle.csv")
    #st.write("108 df ", df)
    df = df.query(f"locale == '{locale}'")# Create and return a dictionary of key/values.
    st.write("110 df.query ", df)
    lang_dict    = {df.key.to_list()[i]:df.value.to_list()[i] for i in range(len(df.key.to_list()))}
    st.write("112 lang_dict ", lang_dict)
    return lang_dict
def main():
    lang_options = {
        "English (US)":"en_US",
        "日本語":"ja_JP"
    }
    locale = st.radio(label='Language', options=list(lang_options.keys()),horizontal=True) # Note we use the selected human-readable locale to get the relevant
    st.write("120 locale ", locale)
    # ISO locale code from the lang_options dictionary.
    lang_dict = load_bundle(lang_options[locale])
    st.subheader(lang_dict['greeting'])
main()

############################################https://stackoverflow.com/questions/73727634/how-to-replace-displayed-value-on-a-button-click-on-streamlit#####################
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


#################################################################################################################

if 'bbut_click' not in st.session_state:
    st.session_state.bbut_click = ''
if 'rradio_click' not in st.session_state:
    st.session_state.rradio_click = 'Deutsch'

with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns([1,0.001,0.001],gap='small')

    with left_column:
        st.subheader(16)
        # n = st.session_state.bt
        c = st.button("Click me ⤵️")

        if (c) or (st.session_state.bbut_click == 'y'):
            bbutton_read = st.radio('select choice',options=['Deutsch','中文','English'],key='rdkey',index=0,horizontal=True)
            #brd_sel = bbutton_read
            st.session_state.bbut_click = 'y'
            if (st.session_state.bbut_click=='y') and (bbutton_read == bbutton_read):
                st.session_state.rradio_click = bbutton_read
                st.write("166 bbutton_read ", bbutton_read)

#st.write("208 bbutton_read ", bbutton_read)





# https://docs.streamlit.io/develop/api-reference/data/st.dataframe
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 
                             4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

ddf = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(ddf, use_container_width=st.session_state.use_container_width)



a=st.text_area('Type in the text_area and click copy')
if st.button('Copy'):
    st.success('Text copied successfully!')



#https://docs.streamlit.io/develop/concepts/design/dataframes
ddf = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(ddf, column_config = config, num_rows='dynamic')
#st.write("212 ", result)

dff = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(
    dff, hide_index=False,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
#    hide_index=True,

)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"241 Your favorite command is **{favorite_command}** 🎈")
st.write("242 ")

# st.write("244 ", result) #######################################################


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
### Hier wird die Konfiguration "eingestellt"
### Konfiguration Data-Frame-Editor Nur Leserechte oder Schreibrechte
if button_num_rows == 'read':
    readWrite = 'static'
else:
    readWrite = 'dynamic'
### Konfiguration Data-Frame-Editor Gesamte Bilschirmbreite oder nicht
if button_use_container_width == True:
    useContainerWidth = True
else:
    useContainerWidth = False
### Konfiguration Data-Frame-Editor index Anzeige oder nicht
if button_hide_index == True:
    useHideIndex = False
else:
    useHideIndex = True
### Konfiguration Data-Frame-Editor Spalten Anzeige oder nicht oder welche Reihenfolge
if button_column_order == False:
    useColumnOrder = ('HSK', 'Wortart','Häufigkeit','Wort cn','Wort py','Wort de','Wort en',
                      'Satz cn','Satz py','Satz de','Satz en')
else:
    useColumnOrder = st.session_state["selected_options"]
#    useColumnOrder = ('HSK', 'Wortart','Häufigkeit')

ddata = [['HSK 1', 'Adjektiv',10, 'cndom', 'pydom', 'dedom', 'endom', 'cndom', 'pydom', 'dedom', 'endom'],
         ['HSK 2','Verb',12, 'cndomm', 'pydomn', 'dedomu', 'endomv', 'cndom', 'pydom', 'dedom', 'endom']]
dframe = pd.DataFrame(ddata,columns=['HSK', 'Wortart','Häufigkeit','Wort cn','Wort py','Wort de','Wort en',
                                     'Satz cn','Satz py','Satz de','Satz en',])
hsks = ['HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5']
wortarten = ['Adjektiv', 'Abverb', 'yellow', 'green', 'blue', 'indigo', 'violet']
### Hier wird die Konfiguration durchgeführt
config = {
    'HSK' : st.column_config.SelectboxColumn('HSK', options=hsks),
    'Wortart' : st.column_config.SelectboxColumn('Wortart', options=wortarten),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'name' : st.column_config.TextColumn('Name (required)', width='large', default="st.", required=True)
}
result = st.data_editor(dframe, column_config = config, num_rows=readWrite,
                        hide_index=useHideIndex, use_container_width=useContainerWidth, column_order=(useColumnOrder)) #org dynamic
if st.button('Get results'):
    st.write("374 ", result)
#######################################################

######### https://discuss.streamlit.io/t/session-state-issue-with-st-checkbox/24020/2
checks = st.columns(4)
with checks[0]:
    st.checkbox('HSK', key='cb_HSK')
    st.write(st.session_state.cb_HSK)
with checks[1]:
    st.checkbox('Wortart', key='cb_Wortart')
    st.write(st.session_state.cb_Wortart)
with checks[2]:
    st.checkbox('Flip the value3', key='test3')
    st.write(st.session_state.test3)
with checks[3]:
    st.checkbox('Flip the value4', key='test4')
    st.write(st.session_state.test4)

if st.session_state.cb_HSK == True:
    st.write('430 Greattttttttttttttttt!')
else:
    st.write('432 buuuuuuuuuuuuuuu Great!')

#########

############################################
st.write("400 ")
data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox_xxx", "st.number_input", "st.text_area", "st.button"],
        "widgetss": ["st.selectbox_x", "st.number_input", "st.text_area", "st.button"],
        "widgetsss": ["st.selectbox_xx", "st.number_input", "st.text_area", "st.button"],
    }
)
st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "412 Widgets",
            help="Streamlit **widget** commands 🎈 her you can explain a little bit",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=False,
)
st.write("421 ")
##################################################

#file:///F:/uni/Faecher/Unterricht/2023/22-Konversation/Konversation/Konversation.html
#PDF 3 Definite articles + indefinite articles.
#3-nominakkusnegation_Ocean.pdf
#https://de.savefrom.net


