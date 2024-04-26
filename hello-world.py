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

# Create a two-column layout
col1, col2 = st.columns([0.001, 1]) # this will just call methods directly in the returned objects
# Inside the first column, add the answer text
with col1:
    st.write("")
# Inside the second column, add the image
with col2:
#    st.image("img/001.jpg", caption="Lightning Image", use_column_width=True)
    st.write("")

#####################################################################################################################

if 'but_click' not in st.session_state:
    st.session_state.but_click = ''
if 'radio_click' not in st.session_state:
    st.session_state.radio_click = 'Deutsch'

button_read = st.radio('select choice',options=['Deutsch','中文','English'],key='rrdkey',index=0,horizontal=True)
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

df_read_file = None                                                    ## ## create var "df_read_file = None" with value "None"
@st.cache_data                                                         ## ## copy FuBa "read_file_text()" to "@st.cache_data"
def read_file_text():                                                  ## ## create FuBa "read_file_text()"
    global df_read_file                                                ## ## "global" is for global access of var "df_read_file" 
    df_read_file = pd.read_csv("database/text_3_lang.csv")             ## ## read csv data file, FuBa is necessary, otherwise "@st.cache_data" is not possible!!!
    #st.write("65 df_read_file ",df_read_file)
    return df_read_file                                                ## ## return is for selected output, otherwise value is empty    st.write("64 df_read_file " , df_read_file)

read_file_text()
st.write("68 df_read_file ",df_read_file)
#####################################https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###############################

#####################################
#dddf = df_read_file.query(f"page == 1")# Create and return a dictionary of key/values.
#st.write("73 df.query ", dddf)

#selWert2 = 1
#pdfSelectedFilename = (df_read_file[df_read_file["page"] == selWert2])["key"].values[0]
#st.write("74 pdfSelectedFilename ", pdfSelectedFilename)

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Bob'],
        'Age': [21, 22, 23, 24],
        'Grade': ['A', 'B', 'A', 'C']}
df = pd.DataFrame(data)
filtered_df = df[df['Grade'] == 'A']
st.write("80 filtered_df" , filtered_df)

no_of_media = df[df['Name'].str.contains('Bob')].shape[0]
st.write("88 no_of_media " , no_of_media)


#####################################

############https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop#######################
var_temp_list = []
for k in range(5):
    var_temp_list.append(exec(f'cat_{k} = k'))

var_temp_list[4] = "Wert"

for j in range(5):
    var_temp_list[j] = None

for i in range(5):
    var_temp_list[i] = i+8

st.write(cat_0)
st.write(cat_1)
st.write(cat_2)
st.write(cat_3)
st.write(cat_4)
st.write("94 var_temp_list ", var_temp_list)
############https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop#######################

read_file_text()
st.write("89 df_read_file ", df_read_file)
df_single_value = read_file_text()

row_index = df_single_value.index[df_single_value['key'] == 'greeting_1'].values[0]  # test
#st.write("93 row_index ", row_index) # test
#st.write("94 df_single_value.iloc[row_index,df_lang_column]", df_single_value.iloc[row_index,df_lang_column])

greeting_1 = df_single_value.iloc[row_index,df_lang_column]
#st.write("97 greeting_1 ", greeting_1)
#st.write("98 greeting_2 ", greeting_2)
#st.write("99 greeting_3 ", greeting_3)
#st.write("100 greeting_4 ", greeting_4)

###################################################################################################################
###################################################################################################################
###################################################################################################################


#@st.cache_data
#def FB_column(matrix, i):                 # Diese Funktion dient der Extraktion einzelner Spalten aus einer Liste
#    return [row[i] for row in matrix]

df_all_column = 5

df_all = pd.read_csv("database/text_bundle.csv")
st.write("143 df_all ", df_all)
rrow_index = df_all.index[df_all['key_new'] == 'greetings_1'].values[0]  # test
#st.write("80 row_index ", rrow_index) # test
df_all_cell = df_all.iloc[0][4]   #    df.iloc[index][col]
st.write("82 df_all_cell ", df_all_cell)
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
st.write("64 locale ", locale)

if locale == "Deutsch":
    df_all_column = 4
elif locale == "中文": 
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
    #st.write("179 df ", df)
    df = df.query(f"locale == '{locale}'")# Create and return a dictionary of key/values.
    st.write("181 df.query ", df)
    lang_dict    = {df.key.to_list()[i]:df.value.to_list()[i] for i in range(len(df.key.to_list()))}
    st.write("183 lang_dict ", lang_dict)
    return lang_dict
def main():
    lang_options = {
        "English (US)":"en_US",
        "日本語":"ja_JP"
    }
    locale = st.radio(label='Language', options=list(lang_options.keys()),horizontal=True) # Note we use the selected human-readable locale to get the relevant
    st.write("191 locale ", locale)
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
                st.write("156 bbutton_read ", bbutton_read)

#st.write("239 bbutton_read ", bbutton_read)





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










@st.cache(allow_output_mutation=True)
def get_data():
    return []

user_id = st.text_input("User ID")
foo = st.slider("foo", 0, 100)
bar = st.slider("bar", 0, 100)
b=st.text_area('TType in the text_area and click copy')

if st.button("Add row"):
    get_data().append({"UserID": user_id, "foo": foo, "bar": bar, "st.text_area": b})

st.write(pd.DataFrame(get_data()))




#11#############################
#https://docs.streamlit.io/develop/concepts/design/dataframes
#Copy and paste support
dataf = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(dataf, use_container_width=True)
st.write("309 dataf ", dataf)
#11#############################









ddf = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(ddf, column_config = config, num_rows='dynamic')

#if st.button('Get results'):
 #   st.write(result)
st.write("352 ", result)






st.write("339 ", result)
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
st.markdown(f"386 Your favorite command is **{favorite_command}** 🎈")
st.write("368 ")



###############################################
df = pd.DataFrame({'A':[1,2,3],'B':[1,2,3]})

cols = st.columns(3)
df = df.reset_index()
cols[0].write('Dataframe display')
cols[0].dataframe(df)
cols[1].write('Data Editor display')
cols[1].experimental_data_editor(df, num_rows='dynamic')
cols[2].write('Column Types')
cols[2].write(df.dtypes)
st.write("441 ")

cols = st.columns(3)
df.index = ['a','b','c']
cols[0].write('Dataframe display')
cols[0].dataframe(df)
cols[1].write('Data Editor display')
cols[1].experimental_data_editor(df, num_rows='dynamic')
cols[2].write('Column Types')
cols[2].write(df.dtypes)

cols = st.columns(3)
df = df.reset_index()
cols[0].write('Dataframe display')
cols[0].dataframe(df)
cols[1].write('Data Editor display')
cols[1].experimental_data_editor(df, num_rows='dynamic')
cols[2].write('Column Types')
cols[2].write(df.dtypes)
###############################################

st.write("404 ", result) #######################################################

### https://discuss.streamlit.io/t/split-st-radio-in-columns/17044/3 ###
### Mögliche Optionen zur Konfiguration des Data Frame Editors
col1_options = ["read", "write"]
col2_options = ["GPS", "GRWG"]
col3_options = ["PLUG", "RNG"]
col4_options = ["aAPPS", "aBBBY"]
col5_options = ["aGPS", "aGRWG"]
col6_options = ["aPLUG", "aRNG"]

if "current" not in st.session_state:
    st.session_state.current = col1_options[0]

if "col1_old" and "col2_old" and "col3_old" and "col4_old" and "col5_old" and "col6_old" not in st.session_state:
    st.session_state.col1_old = col1_options[0]
    st.session_state.col2_old = col2_options[0]
    st.session_state.col3_old = col3_options[0]
    st.session_state.col4_old = col4_options[0]
    st.session_state.col5_old = col5_options[0]
    st.session_state.col6_old = col6_options[0]

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1_choice = col1.radio("choose read or write", col1_options,horizontal=True)
col2_choice = col2.radio("", col2_options,horizontal=True)
col3_choice = col3.radio("", col3_options,horizontal=True)
col4_choice = col4.radio("", col4_options,horizontal=True)
col5_choice = col5.radio("", col5_options,horizontal=True)
col6_choice = col6.radio("", col6_options,horizontal=True)

if col1_choice != st.session_state.col1_old:
    st.session_state.current = col1_choice
    st.session_state.col1_old = col1_choice

if col2_choice != st.session_state.col2_old:
    st.session_state.current = col2_choice
    st.session_state.col2_old = col2_choice

if col3_choice != st.session_state.col3_old:
    st.session_state.current = col3_choice
    st.session_state.col3_old = col3_choice


if col4_choice != st.session_state.col4_old:
    st.session_state.current = col4_choice
    st.session_state.col4_old = col4_choice

if col5_choice != st.session_state.col5_old:
    st.session_state.current = col5_choice
    st.session_state.col5_old = col5_choice

if col6_choice != st.session_state.col6_old:
    st.session_state.current = col6_choice
    st.session_state.col6_old = col6_choice

if st.session_state.current != None:
    st.write("You've picked: ", st.session_state.current)
### Mögliche Optionen zur Konfiguration des Data Frame Editors

#button_num_rows=None
button_use_container_width=True
button_num_rows = st.radio('select choice',options=['read','write'],key='read_write',index=0,horizontal=True)
if button_num_rows == 'read':
    readwrite = 'static'
else:
    readwrite = 'dynamic'
    
st.write("406 button_num_rows ", button_num_rows)

ddata = [['HSK 1', 'Adjektiv',10, 'dom'],['HSK 1','Adjektiv',12, 'dom'],
['HSK 1', 'Adjektiv',7, 'dom']]
dframe = pd.DataFrame(ddata,columns=['HSK', 'Wortart','age','name'])
hsks = ['HSK 1', 'HSK 2', 'HSK 3', 'HSK 4', 'HSK 5']
wortarten = ['Adjektiv', 'Abverb', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'HSK' : st.column_config.SelectboxColumn('HSK', options=hsks),
    'Wortart' : st.column_config.SelectboxColumn('Wortart', options=wortarten),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'name' : st.column_config.TextColumn('Name (required)', width='large', default="st.", required=True)
}
result = st.data_editor(dframe, column_config = config, num_rows=readwrite, hide_index=False) #org dynamic
if st.button('Get results'):
    st.write("422 ", result)
#######################################################

############################################
st.write("426 ")
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
            "446 Widgets",
            help="Streamlit **widget** commands 🎈 her you can explain a little bit",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=False,
)
st.write("448 ")
##################################################











#file:///F:/uni/Faecher/Unterricht/2023/22-Konversation/Konversation/Konversation.html
#PDF 3 Definite articles + indefinite articles.
#3-nominakkusnegation_Ocean.pdf
#https://de.savefrom.net


