import streamlit as st 
import spacy 
nlp = spacy.load('en_core_web_sm')
from spacy import displacy 
import base64
from io import StringIO

st.title('Extract Linguistic Feature Extraction')
text_uploader = st.text_input("write your document that you want to find name entity recognition")

NER_button = st.button("Get NER from document")

if NER_button:
    doc = nlp(text_uploader)
    html_string = displacy.render(doc,style='ent')
    st.markdown(html_string, unsafe_allow_html=True)
st.write("---------------------------------------")

text_uploader2 = st.text_input("Write your document that you want to find sentatic segmentation")
dep_button = st.button("return dependancy graph")

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

if dep_button:
    doc = nlp(text_uploader)
    svg=displacy.render(doc,style='dep',options={'compact':True,'distance':100})
    render_svg(svg)


