import streamlit as st
import google.generativeai as genai
from tavily import TavilyClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API keys
tavily_api_key = os.getenv("TAVILY_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=gemini_api_key)
gemini_client = genai.GenerativeModel("gemini-2.5-flash")

# Initialize Tavily
tavily_client = TavilyClient(tavily_api_key)

# Title
st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("📊 SynthAIzeReport")

# Research question input
research_question = st.text_input("🔍 Enter your research question", placeholder="e.g., What are the impacts of AI on mental health?")

# Function to call Tavily for web search
def web_search(query):
    response = tavily_client.search(query=query, max_results=5)
    return response

# Function to generate Gemini responses
def askAI(prompt):
    response = gemini_client.generate_content(prompt)
    return response.text

# Function to list sources
def sources_lister(web_results):
    titles_urls = ""
    for i, r in enumerate(web_results.get('results', [])):
        titles_urls += f"{i+1}. {r['title']}\n{r['url']}\n\n"
    return titles_urls

# Function to summarize each source
def summarizer(web_results):
    summarizer_prompt = f"""You are an expert in data extraction and summarizing content. Provide
    a bullet point summary of information given in each 'content' in web_results data and add the 
    'title' and serial number associated to each 'content' for each generated summary.
    Without any heading, directly display titles with serial numbers and their associated bullet point summaries.

    web_results: {web_results}"""
    return askAI(summarizer_prompt)

# Function to create final report
def research_report(source_summary):
    report_prompt = f"""You are an expert in creating research reports from given information.
    Generate a concise, clean, human-readable, cohesive research report with suitable sub-headings 
    based on all findings in given_data below. 
    Output should be in plain language and include a suitable short title for this research report.

    given_data: {source_summary}"""
    return askAI(report_prompt)

# Submit button
if st.button("🔎 Generate Research Report"):
    if research_question.strip() == "":
        st.warning("Please enter a research question.")
    else:
        with st.spinner("Searching the web for relevant information..."):
            web_results = web_search(research_question)

        # Display gathered sources
        with st.expander("📚 Gathered Sources"):
            gathered_sources = sources_lister(web_results)
            st.text(gathered_sources)

        # Generate and display source-wise summaries
        with st.spinner("Summarizing each source..."):
            source_wise_summary = summarizer(web_results)

        with st.expander("📝 Source-wise Summaries"):
            st.markdown(source_wise_summary)

        # Generate and display final report
        with st.spinner("Generating final research report..."):
            final_report = research_report(source_wise_summary)

        st.subheader("📄 Final Research Report")
        st.markdown(final_report)
