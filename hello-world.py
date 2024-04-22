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
    #st.write("84 df ", df)
    df = df.query(f"locale == '{locale}'")# Create and return a dictionary of key/values.
    st.write("171 df.query ", df)
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

#st.write("158 bbutton_read ", bbutton_read)





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

if st.button("Add row"):
    get_data().append({"UserID": user_id, "foo": foo, "bar": bar})

st.write(pd.DataFrame(get_data()))
