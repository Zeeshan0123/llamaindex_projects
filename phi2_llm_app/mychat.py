import streamlit as st
from llama_index.llms.ollama import Ollama

# Ollama model configuration
model_name = "phi:2.7b-chat-v2-q2_K"
request_timeout = 30.0

# Initialize Ollama instance
llm = Ollama(model=model_name, request_timeout=request_timeout)

# Initialize empty variables for UI elements
user_query = ""
past_queries = []
past_responses = []

def generate_response(query):
    """Generates a response from the Phi-2 model based on the user query."""
    try:
        global response
        response = llm.complete(query)
        past_queries.append(query)
        past_responses.append(response)
        
    except Exception as e:
        st.error(f"Error: {e}")

# App layout and logic
st.title("Phi-2 Explorer: Ask Anything!")

# Sidebar: Query input and buttons
with st.sidebar:
    st.subheader("Your Question:")
    user_query = st.text_input("")

    if st.button("Ask Phi-2"):
        if user_query.strip() == "":
            st.warning("Please enter a question.")
        else:
            generate_response(user_query)
            st.subheader("Response:")
            if response:
                st.markdown(f"**Phi-2:** ", unsafe_allow_html=True)
            else:
                st.error("Error generating response.")

        # Clear query history button
        if st.button("Clear History"):
            past_queries.clear()
            past_responses.clear()

# Main panel: Response and history
if past_queries:
    st.subheader("Past Queries:")
    for i, query in enumerate(past_queries):
        st.markdown(f"**Query {i+1}:** {query}")
        st.markdown(f"**Response:** {past_responses[i]}", unsafe_allow_html=True)

# Customize the app (optional)
# Modify theme, fonts, background, etc. using Streamlit features

# Run the app
# st.run()
