import streamlit as st
import pandas as pd

# Data provided
data = {
    'Capability': ['MMLU', 'CoT@32*', 'Big-Bench Hard', 'DROP', 'HellaSwag', 'GSM8K', 'maj1@32', 'MATH', 'HumanEval', 'Natural2Code'],
    'Benchmark': ['Representation of questions in 57 subjects', 'Reasoning', 'Reading comprehension (F1 Score)', 'Commonsense reasoning for everyday tasks', 'Basic arithmetic manipulations', 'Basic arithmetic manipulations', 'Python code generation', 'Challenging math problems', 'Python code generation', 'Python code generation'],
    'Higher is better': [90.0, 86.4, 83.6, 82.4, 87.8, 94.4, 92.0, 53.2, 74.4, 74.9],
    'Description': ['CoT@32*', '5-shot** (reported)', '3-shot', 'Variable shots', '10-shot*', 'maj1@32', '5-shot CoT (reported)', '4-shot', '0-shot (IT)*', '0-shot']
}
# Create a DataFrame from the data
df = pd.DataFrame(data)

# Page Title
st.title("AnyAI Use Guide 🚀🤖")

# Introduction to AnyAI
st.header("Introduction to AnyAI")
st.write("""
AnyAI is a versatile AI tool consisting of two main components:

1. **AI Content Generator**: This component uses the Google Gemini API to create content for various platforms, including:
    - LinkedIn Post
    - Blog Post
    - Instagram Post
    - Tweet
    - Product Description
    - Email
    - Ad Copy
    - Tagline
    - Video Script
    - Podcast Script
    - SEO Content
    - README
    - Documentation
    - Presentation
    - Social Media Post
    - Article

         

2. **Image Classifier**: Utilizing Google Vision, this component classifies images either via upload or URL based on the entered query.
""")

# Web Application for Google Gemini and Vision API
st.header("Web Application for Google Gemini and Vision API")
st.write("""
To leverage AnyAI's capabilities in your web application, follow these steps:

1. **Visit Google AI Studio:**
   Go to [Google AI Studio](https://ai.google.dev/).

2. **Get API Key:**
   Click on "Get API Key" and create your API key.

3. **Copy API Key:**
   Copy the generated API key.

4. **Paste in Web Application:**
   In your web application, there should be an input field to paste your API key. Paste the copied API key into this field.

5. **Generate Content and Classify Images:**
   Once the API key is validated, you can use the Gemini API to generate text content and the Vision API to classify images within your web application.
""")

# Gemini Model Capabilities Table
st.header("Gemini Model Capabilities")
st.table(df)

st.header("Made By John Paul")
st.markdown("[Visit Me](https://github.com/RJohnPaul)")
# Add a clickable link
st.markdown("""
For a deeper understanding and additional insights, check out the accompanying [blog post](https://deepmind.google/technologies/gemini/#introduction) dedicated to Google's Gemini Model. Let's embark on this exciting journey together! 🌟🔍.
""", unsafe_allow_html=True)
