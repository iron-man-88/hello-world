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
    st.image("img/001.jpg", caption="Lightning Image", use_column_width=True)

@st.cache_data
def FB_column(matrix, i):                 # Diese Funktion dient der Extraktion einzelner Spalten aus einer Liste
    return [row[i] for row in matrix]

df_all_column = 5

df_all = pd.read_csv("database/text_bundle.csv")
st.write("41 df_all ", df_all)

FullList        = df_all.values.tolist()
st.write("44 FullList ", FullList)
FullListColumn2 = FB_column(FullList, 4)
st.write("50 FullListColumn2 ", FullListColumn2)
IndexSeite = FullListColumn2.index("Hallo, Welt1!")
st.write("52 IndexSeite ", IndexSeite)
FullList[IndexSeite].tolist()
#st.write("54 FullList ", FullList)
vvaluee = FullList[IndexSeite][4]
st.write("56 vvaluee ", vvaluee)


#row_index = df_all.index[df_all['key_new'] == 'greetings_1']  # test
#st.write("43 row_index ", row_index) # test

language_options = {
    "Deutsch":"de",
    "中文":"cn",
    "English":"en"
}
lllocale = st.radio(label='Languages', options=list(language_options.keys()))
st.write("49 lllocale ", lllocale)

if lllocale == "Deutsch":
    df_all_column = 4
elif lllocale == "中文": 
    df_all_column = 5
else:
    df_all_column = 6

sel_value = df_all.iloc[0,df_all_column]
st.write("59 sel_value ", sel_value)

# https://medium.com/@groxli/konnichiwa-streamlit-689e6e48bdcb
@st.cache_data
def load_bundle(locale):
    # Load in the text bundle and filter by language locale.
    df = pd.read_csv("database/text_bundle.csv")
    st.write("df ", df)
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
    locale = st.radio(label='Language', options=list(lang_options.keys())) # Note we use the selected human-readable locale to get the relevant
    st.write("60 locale ", locale)
    # ISO locale code from the lang_options dictionary.
    lang_dict = load_bundle(lang_options[locale])
    st.subheader(lang_dict['greeting'])
main()
