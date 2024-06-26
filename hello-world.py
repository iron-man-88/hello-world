import streamlit as st
import pandas as pd
import streamlit_extras as se
from streamlit_extras.grid import grid
from streamlit_extras.stylable_container import stylable_container
import base64
import textwrap
import numpy as np
#from streamlit_extras.dataframe_explorer import dataframe_explorer
st. set_page_config(layout="wide") # https://discuss.streamlit.io/t/how-to-increase-the-width-of-web-page/7697
import streamlit.components.v1 as components
### extra
import csv
file = open("./database/neu.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

## print(data)
#st.write(data)
import json
dates_json = json.dumps(data)
#st.write("22 " + dates_json)
dates_json_type = json.dumps(data)
#st.write("24 ", type(dates_json_type))

html_string27 = '''
<script language="javascript">
  alert({{dates_json_type}})
</script>
'''
components.html(html_string27)
#st.markdown(html_string27, unsafe_allow_html=True)
### extra
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

# css laden
with open('./static/main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
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

st.write("70 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_1'))
st.write("71 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_2'))
st.write("72 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_3'))
st.write("73 df_read_file_cell ",read_file_text(df_lang_column, 'greeting_4'))
#####################################https://stackoverflow.com/questions/73659180/how-to-stop-streamlit-to-reseting-after-using-radio###############################

def greet(name, namee):
    st.write("77 Hello name ", name, namee)
# pass argument
greet("John", "Johnn")

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
# function call with two values
aaa = add_numbers(5, 4)
st.write("86 Sum: ", aaa)



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
    st.write("139 You've picked: ", st.session_state.current, button_num_rows)    ## del

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
    st.write("218 ", result)
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
    st.write('231 Greattttttttttttttttt!')
else:
    st.write('233 buuuuuuuuuuuuuuu Great!')

#########

############################################
st.write("244 ")
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
            "256 Widgets",
            help="Streamlit **widget** commands 🎈 her you can explain a little bit",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=False,
)
st.write("265 ")



#################################################
svg_url = "AB_01_01.svg"
#my_png = cairosvg.svg2png(url=svg_url, output_width=426, output_height=240)
st.image(svg_url)
################################################


def change_label_style(label, font_size='12px', font_color='blue', font_family='sans-serif'):
    html = f"""
    <script>
        var elems = window.parent.document.querySelectorAll('p');
        var elem = Array.from(elems).find(x => x.innerText == '{label}');
        elem.style.fontSize = '{font_size}';
        elem.style.color = '{font_color}';
        elem.style.fontFamily = '{font_family}';
    </script>
    """
    st.components.v1.html(html)

label = " 288 My text here"
### st.text_input(label)

change_label_style(label, '90px', 'green' 'sans-serif')
#################################################

#https://discuss.streamlit.io/t/passing-variable-containing-text-to-markdown/16069/3
# st.sidebar
left_position = st.sidebar.slider("Left", 1, 1340, value=0, help='Select left position of Div!!!')
top_position = st.sidebar.slider("Top", 1, 800, value=0)
variable_output = st.sidebar.text_area("Enter some text", value="298 Streamlit is awesome<br>aaa")
div_id = "my_div_1"
#<div id = {div_id}  class="square div-id" contenteditable="true"><a href='#' id={div_id}>Second link</a>{variable_output}
html_str = f"""
<style>div.square{{left: {left_position}px; top: {top_position}px;}}</style>
<div id = {div_id}  class="square div-id" contenteditable="true">{variable_output}
<p>My mother has <span style="color:green">green</span> eyes.</p>
<p>This is a simple <bigcolor>Streamlit</bigcolor> app with a Jinja2 template.</p>
<p>We're sorry, that <bigcolor><red>todo</red></bigcolor> item was not found:</p>
</div>
"""
#<div class="square"><a data-tooltip="Kampf" class="ttip">K&auml;mpfer + {variable_output}</div>
#st.markdown(html_str, unsafe_allow_html=True, help='354 Select a number out of 3 choices')
st.markdown(html_str, unsafe_allow_html=True)
#################################################
with st.popover("OP"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)

####################################################################################################
####################################################################################################
ddd = "pppqqq373"
lleft = "100px"
#https://discuss.streamlit.io/t/applying-custom-css-to-manually-created-containers/33428/9
def create_container_with_color(id, color="#E4F2EC", left="0px"):
    #stw(id)
    # todo: instead of color you can send in any css
    plh = st.container()
    html_code = """<div id = 'my_div_outer'>"380outer"</div>"""
    st.markdown(html_code, unsafe_allow_html=True)
    with plh:
        inner_html_code = """<div id = 'my_div_inner_%s'>"inner383"</div>""" % id
        plh.markdown(inner_html_code, unsafe_allow_html=True)
    ## applying style
    chat_plh_style = """
        <style>
            div[data-testid='stVerticalBlock']:has(div#my_div_inner_%s):not(:has(div#my_div_outer)) {
                background-color: %s;
#                border-radius: 10px;
                padding: 10px 10px 20px 10px;height:10px
                width: fit-content;
#                position: relative;
                left: %s;
#                width:fit-content;
                height:fit-content;
                text-align: center;
                position:relative;
  #left: {left_position}px;
  #top: {top_position}px;
                z-index: 1;
                border-width: 3px;
                border-style: solid;
                border-color: blue;
                border-radius: 10px;
           };
        </style>
        """
    chat_plh_style = chat_plh_style % (id, color, left)
    st.markdown(chat_plh_style, unsafe_allow_html=True)
    return plh

create_container_with_color(ddd, color="red", left=lleft)
###########################################################################
ccccc = "<span style="""""color:___">xxx</span>"""""
st.write("416_ ", ccccc)
from st_copy_to_clipboard import st_copy_to_clipboard

# Render copy to clipboard button
st.write("blue")
st_copy_to_clipboard(ccccc)
##########################################################
# https://discuss.streamlit.io/t/styling-a-specific-container-with-a-specific-div-class/68912
def local_css(file_name, id_, llleft_position, tttop_position):
    with open(file_name) as f:
        css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

css_style = """<style>div.id{{left:{llleft_position}px; top:{tttop_position}px;}}</style>"""
div = """<div id = 'my_div_iinner_%s' class="square">"inner473"</div>""" % id

#st.markdown(css_style, div, unsafe_allow_html=True)
st.markdown(div, unsafe_allow_html=True)

local_css("./static/main.css", "div_1", 100, 100)
#test#local_css("./static/main.css", "div_1", left="100px", top="100px")

#################################################################################################################
#https://www.codingdeeply.com/dynamic-variable-name-python/
prefix = "dynamic_"
suffix = "_variable"
var_ = 1
# Creating dynamic variable name using globals()
globals()[prefix + str(var_) + suffix] = 42
# Accessing dynamic variable
st.write(dynamic_1_variable) # Output: 42
dynamic_1_variable = dynamic_1_variable +1
st.write(dynamic_1_variable) # Output: 43
#################################################################################################################
bgcolor=None; fontcolor=None; pos_top = ""; pos_left = ""
page_no = "div_S001"
bgcolor = st.color_picker("Pick a Background color")
fontcolor = st.color_picker("Pick a Font Color","#fff")
var_num = 1 # eigentlich später Wert aus DB
globals()[page_no + "_" + str(var_num) + pos_left] = "100px" # eigentlich später Wert aus DB
globals()[page_no + "_" + str(var_num) + pos_top] = "10px" # eigentlich später Wert aus DB
div_content="""405 K&auml;mpfer<p>My mother has <span style="color:blue">blue</span> eyes.</p><p>This is a simple
            <bigcolor>Streamlit</bigcolor> app with a Jinja2 template.</p><p>We're sorry, that <bigcolor>
            <red>todo</red></bigcolor> item was not found:</p>"""

fhtmll_code = f"""<div id={page_no} style='background-color:{bgcolor}; color:{fontcolor}; position:relative; contenteditable:true;
              left:{globals()[page_no + "_" + str(var_num) + pos_left]}; top:{globals()[page_no + "_" + str(var_num) + pos_top]}; width:fit-content; height:fit-content;'>
              <a data-tooltip={var_num} class="ttip">{div_content}</div>"""
st.markdown(fhtmll_code,unsafe_allow_html=True)
#####
html_temp = """
<div style="background-color:{};padding:10px">
<h1 style="color:{};text-align:center;">Streamlit Simple CSS Shape Generator </h1>
</div>
"""
#st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)

#htmll_code = """<div id='mmy_div_outer' style='background-color:{}; color:{}; position:relative; left:{}; top:{}; width:fit-content;
#height:fit-content;'>aaa</div>"""
#st.markdown(htmll_code.format(bgcolor, fontcolor, pos_left, pos_top),unsafe_allow_html=True)
###########################################################################
#https://pytutorial.com/python-variable-in-string/#%%20Operator
# Variables
name = "red"
age = 22

# Insert Variables into String using f-string
formatted_string = f"Hello, {name}! You are {age} years old."

# Print Result
st.write(formatted_string)
###########################################################################





###########################################################################
# https://stackoverflow.com/questions/67977391/can-i-display-custom-javascript-in-streamlit-web-app
#import streamlit.components.v1 as components

html_string = '''
<h1>HTML string in RED</h1>
<script language="javascript">
    document.querySelector("h1").style.color = "red";
  console.log("Streamlit runs JavaScript");
  alert("Streamlit runs JavaScript");
</script>
'''

components.html(html_string)  # JavaScript works

st.markdown(html_string, unsafe_allow_html=True)  # JavaScript doesn't work
###########################################################################
st.write('Hello, *World!* :sunglasses:')
###########################################################################

# https://stackoverflow.com/questions/67977391/can-i-display-custom-javascript-in-streamlit-web-app
html_string464 = '''
<script language="javascript">
var info = function(dd) {
  return function() {
      var offsets = dd.getBoundingClientRect();
	  var top = offsets.top + window.scrollY;
	  var left = offsets.left + window.scrollX;
    alert(dd.id + " 68 dd.id, " + dd.offsetWidth + " dd.offsetWidth, " + dd.offsetHeight + " dd.offsetHeight, " + top + " top, " + left + " left" );
  }
};
var dds = document.getElementsByClassName("div-id");
for (var i = 0, l = dds.length; l > i; i++)
  dds[i].onclick = info(dds[i]);
</script>
'''

components.html(html_string464)  # JavaScript works

st.markdown(html_string464, unsafe_allow_html=True)  # JavaScript doesn't work
###########################################################################


from st_clickable_images import clickable_images

clicked = clickable_images(
    [
        "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
        "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
        "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
    ],
    titles=[f"Image #{str(i)}" for i in range(5)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")



###########################################################################
from st_click_detector import click_detector

content = """<p><a href='#' id='Link 1'>First link</a></p>
    <p><a href='#' id='Link 2'>Second link</a></p>
    <a href='#' id='I-bin-Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    <a href='#' id='I-bin-Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
    """
clicked = click_detector(content)
st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")

#div_clicked = click_detector(html_str)
#st.markdown(f"**{div_clicked} div_clicked**" if div_clicked != "" else "**No div_clicked**")
#st.write(div_clicked)



