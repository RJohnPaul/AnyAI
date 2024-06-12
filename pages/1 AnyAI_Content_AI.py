import os
import streamlit as st
import google.generativeai as genai
from textwrap import indent
from datetime import datetime
import base64

# Set up Gemini API key
os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key="key")

# Set up Streamlit app config
st.set_page_config(page_title="AnyAI", page_icon=":pencil2:", layout="wide")

# Function to display text as Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return indent(text, '> ', predicate=lambda _: True)

# Function to initialize session state
def initialize_session_state():
    return st.session_state.setdefault('api_key', None)

st.title("AnyAI : AI Content Generator 🚀🤖")

content_type = st.sidebar.selectbox("Select Content Type", [
    "LinkedIn Post",
    "Blog Post",
    "Instagram Post",
    "Tweet",
    "Product Description",
    "Email",
    "Ad Copy",
    "Tagline",
    "Video Script",
    "Podcast Script",
    "SEO Content",
    "README",
    "Documentation",
    "Presentation",
    "Social Media Post",
    "Article",
])

if content_type == "LinkedIn Post":
    prompt = st.text_area("Enter the topic and target audience for your LinkedIn post")
    if st.button("Generate LinkedIn Post"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="linkedin_post.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Blog Post":
    prompt = st.text_area("Enter the topic, target audience, and desired tone for your blog post")
    if st.button("Generate Blog Post"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="blog_post.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Instagram Post":
    prompt = st.text_area("Enter the topic, target audience, and desired tone for your Instagram post")
    if st.button("Generate Instagram Post"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="instagram_post.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Tweet":
    prompt = st.text_area("Enter the topic, target audience, and desired tone for your tweet")
    if st.button("Generate Tweet"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="tweet.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Product Description":
    prompt = st.text_area("Enter the product details, target audience, and desired tone for the product description")
    if st.button("Generate Product Description"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="product_description.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Email":
    st.subheader("Email Generator")
    email_type = st.selectbox("Email Type", ["Professional", "Personal", "Marketing"])
    prompt = st.text_area(f"Enter the topic, recipient details, and desired tone for your {email_type.lower()} email")
    if st.button(f"Generate {email_type} Email"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{email_type.lower()}_email.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Ad Copy":
    st.subheader("Ad Copy Generator")
    ad_type = st.selectbox("Ad Type", ["Social Media", "Print", "Video"])
    prompt = st.text_area(f"Enter the product/service details, target audience, and desired tone for your {ad_type.lower()} ad")
    if st.button(f"Generate {ad_type} Ad Copy"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{ad_type.lower()}_ad_copy.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Tagline":
    prompt = st.text_area("Enter the product/service details, target audience, and desired tone for your tagline")
    if st.button("Generate Tagline"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="tagline.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Podcast Script":
    st.subheader("Podcast Script Generator")
    podcast_type = st.selectbox("Podcast Type", ["Interview", "Storytelling", "Educational"])
    prompt = st.text_area(f"Enter the topic, target audience, desired tone, and any specific details for your {podcast_type.lower()} podcast script")
    if st.button(f"Generate {podcast_type} Podcast Script"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{podcast_type.lower()}_podcast_script.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "SEO Content":
    st.subheader("SEO Content Generator")
    content_type = st.selectbox("Content Type", ["Blog Post", "Product Description", "Landing Page"])
    keywords = st.text_input("Enter target keywords (separated by commas)")
    prompt = st.text_area(f"Enter the topic, target audience, desired tone, and any specific details for your SEO-optimized {content_type.lower()}")
    if st.button(f"Generate SEO-Optimized {content_type}"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"{prompt}\n\nTarget Keywords: {keywords}")
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="seo_content.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "README":
    st.subheader("README Generator")
    project_type = st.selectbox("Project Type", ["Software", "Library", "Framework"])
    prompt = st.text_area(f"Enter the project details, target audience, and any specific requirements for your {project_type.lower()} project README")
    if st.button(f"Generate {project_type} README"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{project_type.lower()}_readme.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Documentation":
    st.subheader("Documentation Generator")
    doc_type = st.selectbox("Documentation Type", ["API Reference", "User Guide", "Tutorial"])
    prompt = st.text_area(f"Enter the project details, target audience, and any specific requirements for your {doc_type.lower()} documentation")
    if st.button(f"Generate {doc_type} Documentation"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{doc_type.lower()}_documentation.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Presentation":
    st.subheader("Presentation Generator")
    presentation_type = st.selectbox("Presentation Type", ["Pitch Deck", "Training", "Conference Talk"])
    prompt = st.text_area(f"Enter the topic, target audience, desired tone, and any specific details for your {presentation_type.lower()} presentation")
    if st.button(f"Generate {presentation_type} Presentation"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{presentation_type.lower()}_presentation.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Social Media Post":
    st.subheader("Social Media Post Generator")
    platform = st.selectbox("Select Platform", ["Facebook", "Twitter", "Instagram", "LinkedIn"])
    prompt = st.text_area(f"Enter the topic, target audience, and desired tone for your {platform.lower()} post")
    if st.button(f"Generate {platform} Post"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{platform.lower()}_post.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

elif content_type == "Article":
    article_type = st.selectbox("Select Article Type", ["News", "Opinion", "Editorial", "Feature"])
    prompt = st.text_area(f"Enter the topic, target audience, and desired tone for your {article_type.lower()} article")
    if st.button(f"Generate {article_type} Article"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        st.markdown(to_markdown(response.text))
        st.markdown("**Copy Output:**")
        output = response.text
        b64 = base64.b64encode(output.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{article_type.lower()}_article.txt">Download File</a>'
        st.markdown(href, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ by [John Paul](https://github.com/RJohnPaul)")