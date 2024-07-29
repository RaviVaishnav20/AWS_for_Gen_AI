# # The below frontend code is provided by AWS and Streamlit. I have only modified it to make it look attractive.
# import streamlit as st 
# import rag_backend as demo ### replace rag_backend with your backend filename

# st.set_page_config(page_title="HR Q and A with RAG") ### Modify Heading

# new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">HR Q & A with RAG 🎯</p>'
# st.markdown(new_title, unsafe_allow_html=True) ### Modify Title

# if 'vector_index' not in st.session_state: 
#     with st.spinner("📀 Wait for magic...All beautiful things in life take time :-)"): ###spinner message
#         st.session_state.vector_index = demo.hr_index() ### Your Index Function name from Backend File

# input_text = st.text_area("Input text", label_visibility="collapsed") 
# go_button = st.button("📌Learn GenAI with Rahul Trisal", type="primary") ### Button Name

# if go_button: 
    
#     with st.spinner("📢Anytime someone tells me that I can't do something, I want to do it more - Taylor Swift"): ### Spinner message
#         response_content = demo.hr_rag_response(index=st.session_state.vector_index, question=input_text) ### replace with RAG Function from backend file


import streamlit as st
import rag_backend as demo  # Replace rag_backend with your backend filename

# Page configuration
st.set_page_config(
    page_title="AI-Powered HR Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS to enhance the UI
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .header-style {
        font-size: 48px;
        font-weight: bold;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 30px;
    }
    .subheader-style {
        font-size: 24px;
        color: #4A4A4A;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Main title and subtitle with custom styling
st.markdown('<div class="header-style">AI-Powered HR Assistant 🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader-style">Your intelligent companion for HR queries</div>', unsafe_allow_html=True)

# Initialize vector index if not already in session state
if 'vector_index' not in st.session_state:
    with st.spinner("🔧 Initializing AI system... Building knowledge base."):
        st.session_state.vector_index = demo.hr_index()  # Your Index Function from Backend File

# Input area for user questions
input_text = st.text_area("What's your HR-related question?", 
                          placeholder="E.g., What are the company's policies on remote work?",
                          height=100)

# Submit button
go_button = st.button("🚀 Get Expert Answer", type="primary")

# Process the query when button is clicked
if go_button and input_text:
    with st.spinner("🧠 Analyzing... Preparing a comprehensive response for you!"):
        response_content = demo.hr_rag_response(
            index=st.session_state.vector_index, 
            question=input_text
        )  # RAG Function from backend file
        
        # Display the response in a nice box
        st.markdown("### 📌 AI Assistant's Response:")
        st.info(response_content)

# Footer
st.markdown("---")
st.markdown(
    "Powered by Advanced RAG Technology | Developed with ❤️ by Ravi Vaishnav",
    help="RAG: Retrieval-Augmented Generation"
)