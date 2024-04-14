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

df_all = pd.read_csv("database/text_bundle.csv")
st.write("df_all ", df_all)
FullListColumn2 = FB_column(df_all, 1) # Spalte "1" wird extrahiert
#st.write("FullListColumn2 ", FullListColumn2)

# https://medium.com/@groxli/konnichiwa-streamlit-689e6e48bdcb
@st.cache_data
def load_bundle(locale):
    # Load in the text bundle and filter by language locale.
    df = pd.read_csv("database/text_bundle.csv")
    st.write("df ", df)
    df_de = df[['de']] # selber
    st.write("df_de ", df_de) # selber
    #df_de_Column2    = FB_column(FullList, 2)
    df_de_index0 = df_de.index[1] # selber
    st.write("df_de_index0 ", df_de_index0) # selber
    df = df.query(f"locale == '{locale}'")# Create and return a dictionary of key/values.
#    df_en = df.query(f"key_new == '{locale}'")# Create and return a dictionary of key/values.
    st.write("df.query ", df)
#    st.write("df.query_en ", df_en)
    lang_dict    = {df.key.to_list()[i]:df.value.to_list()[i] for i in range(len(df.key.to_list()))}
#    lang_dict_en = {df_en.key_new.to_list()[i]:df_en.en_US.to_list()[i] for i in range(len(df_en.key_new.to_list()))}
    st.write("lang_dict ", lang_dict)
#    st.write("lang_dict_en ", lang_dict_en)
    return lang_dict
def main():
    lang_options = {
        "English (US)":"en_US",
        "日本語":"ja_JP"
    }
    locale = st.radio(label='Language', options=list(lang_options.keys())) # Note we use the selected human-readable locale to get the relevant
    st.write("lllocale ", locale)
    # ISO locale code from the lang_options dictionary.
    lang_dict = load_bundle(lang_options[locale])
    st.subheader(lang_dict['greeting'])
main()
