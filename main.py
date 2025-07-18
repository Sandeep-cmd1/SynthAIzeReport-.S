import google.generativeai as genai
from tavily import TavilyClient
from dotenv import load_dotenv
import os

#loading .env locally
load_dotenv()

#tavily client setup 
tavily_api_key=os.getenv("TAVILY_API_KEY")
tavily_client=TavilyClient(tavily_api_key)

#tavily web search function
research_question=input("Enter your research question: ")
def web_search (query):
    response=tavily_client.search(query=query,max_results=5)
    return response
web_results=web_search(research_question)

#gemini client setup
gemini_api_key=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)
client=genai.GenerativeModel("gemini-2.5-flash")

#gemini query function
def askAI(prompt):
    response=client.generate_content(prompt)
    return response.text

#sources (titles and urls) listing function
def sources_lister(web_results):
    titles_urls=""
    for i,r in enumerate(web_results.get('results')):
        titles_urls+=f"{i+1}. {r['title']}\n{r['url']}\n\n"
    return titles_urls
gathered_sources=sources_lister(web_results)
print(gathered_sources)

#source wise summarizing function
def summarizer(web_results):
    summarizer_prompt=f"""You are an expert in data extraction and summarizing content. Provide
    a bullet point summary of information given in each 'content' in web_results data and add the 
    'title' and serial number associated to each 'content' for each generated summary.
    Without any heading, directly display titles with serial numbers and their associated bullet point summaries.

    web_results:{web_results}"""

    return askAI(summarizer_prompt)
source_wise_summary=summarizer(web_results)
print(source_wise_summary)

#final research report generating function
def research_report(source_wise_summary):
    research_report_prompt=f"""You are an expert in creating research reports from given information.
    Generate a concise, clean, human-readable, cohesive research report with suitable sub-headings 
    based on all findings in given_data below. 
    Output should be in plain language and include a suitable short title for this research report.

    given_data:{source_wise_summary}"""
    
    return askAI(research_report_prompt)
final_report=research_report(source_wise_summary)
print(final_report)

