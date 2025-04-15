


import streamlit as st
from huggingface_hub import InferenceClient

# Hardcoded API key (for testing only - use secrets in production)
HF_API_KEY = "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"

st.title('🦜🔗 Hugging Face Chat App')

def generate_response(input_text):
    try:
        client = InferenceClient(token=HF_API_KEY)
        response = client.text_generation(
            model="google/flan-t5-large",
            prompt=input_text,
            temperature=0.7,
            max_new_tokens=250,  # Must be ≤250 for this model
            do_sample=True  # Helps with more varied responses
        )
        st.success(response)
    except Exception as e:
        st.error(f"Error: {str(e)}")

with st.form('my_form'):
    text = st.text_area('Enter your question:', 'What is the capital of France?')
    submitted = st.form_submit_button('Submit')
    
    if submitted:
        generate_response(text)