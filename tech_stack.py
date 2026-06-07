import streamlit as st


st.set_page_config(
    page_title="Rodney Alex Finkel - Portfolio",
    page_icon="🛠️",
    layout="wide", # Always opens in wide screen layout
    initial_sidebar_state="expanded"
)

def display_tech_stack():
    st.title("Rodney Alex Finkel - Tech Stack & Projects")
    st.markdown("## 🛠️ Tech Stack")
    st.markdown("---")

    # Tech Stack Columns
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown("**Languages & Core**")
        st.markdown("""
        ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
        ![SQL](https://img.shields.io/badge/SQL-4479A1?logo=sql&logoColor=white)
        ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
        """)

        st.markdown("**AI & LLM Ecosystem**")
        st.markdown("""
        ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)
        ![LangGraph](https://img.shields.io/badge/LangGraph-000000?logo=langchain&logoColor=white)
        ![Groq](https://img.shields.io/badge/Groq-00A3FF?logo=groq&logoColor=white)
        ![Hybrid-Fusion-RAG](https://img.shields.io/badge/RAG-FF6B6B?logo=ai&logoColor=white)
        ![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=black)
        ![Deepgram](https://img.shields.io/badge/Deepgram-000000?logo=deepgram&logoColor=white)
        ![Graphrag](https://img.shields.io/badge/Graphrag-000000?logo=graphrag&logoColor=white)
        """)

    with col2:
        st.markdown("**Databases & Data**")
        st.markdown("""
        ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&postgresqlColor=white)
        ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)
        ![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoftsqlserver&logoColor=white)
        ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
        ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF4B4B?logo=sqlalchemy&logoColor=white)
        ![ChromaDB](https://img.shields.io/badge/ChromaDB-000000?logo=vector&logoColor=white)
        ![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)
        ![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?logo=neo4j&logoColor=white)
        """)

        st.markdown("**Machine Learning & Analytics**")
        st.markdown("""
        ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
        ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
        ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
        ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
        ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
        ![Scipy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
        ![Transformers](https://img.shields.io/badge/Transformers-000000?logo=transformers&logoColor=white)
        ![Statsmodels](https://img.shields.io/badge/Statsmodels-000000?logo=statsmodels&logoColor=white)
        ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white)
        """)

    with col3:
        st.markdown("**Backend & APIs**")
        st.markdown("""
        ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
        ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
        ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
        """)

        st.markdown("**DevOps & Infrastructure**")
        st.markdown("""
        ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
        ![Github Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
        ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white)
        ![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)
        ![Websockets](https://img.shields.io/badge/WebSockets-000000?logo=websockets&logoColor=white)
        """)

        st.markdown("**Data Extraction & Automation**")
        st.markdown("""
        ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-8CB0A4?logo=python&logoColor=white)
        ![Doclingo](https://img.shields.io/badge/Docling-000000?logo=docling&logoColor=white)
        ![Scrapy](https://img.shields.io/badge/Scrapy-000000?logo=scrapy&logoColor=white)
        """)
        
        
    # ====================== THEORETICAL FOUNDATIONS ======================
    st.markdown("## 📐 Theoretical Foundations")
    st.markdown("---")
    
    st.markdown("**Universal Approximation Theorem**")
    st.image("static/universal_approximation_theorem.png", 
             use_container_width=True,
             caption="The Universal Approximation Theorem (Cybenko, 1989) — foundational result proving that neural networks can approximate any continuous function on a compact subset of R^n to arbitrary accuracy. This underpins the power of modern deep learning and large language models.")
    
    st.markdown("""
    This mathematical foundation justifies why modern neural networks (and by extension, transformer-based LLMs) are such powerful function approximators — a core principle behind the AI systems I've built.
    """)

    st.markdown("---")

    # ----------------------------------------------------
    # 🚀 NEW SECTION: FEATURED PROJECTS
    # ----------------------------------------------------
    st.markdown("## 🚀 Featured Projects")
    st.markdown("---")

    # Data dictionary for your apps. Update paths and URLs here.
    projects = [
        {
            "title": "FileSystem & SQL-React Agent/Dense Search Web Retriever",
            "description": "React Agent with tool bindings via Langchain and Pydantic schema validation for structured SQL queries, integrated with a custom file system retriever and vector search for enhanced RAG capabilities in web research.    ",
            "image": "static/sql_react_agent.png",  # Replace with your actual image file path or URL
            "live_url": "https://rodneyfinkel-text-analysis-pydantic-streamlit-app4-h4ppca.streamlit.app/", # Set to None if not deployed
            "github_url": "https://github.com/RodneyFinkel/text_analysis_pydantic"
        },
        {
            "title": "Kmeans PCA Quantitative Finance System",
            "description": "A speculativek-means clustering, with PCA-whitening, analysis on SP500 companies using two financial ratios Rnd as a percentage of Revenue and RnD as a percentage of Operating Expenses. Injecting these two ratios into a clustering algorithm alongside price volatility to look for a signal in the possible emergence of new market segments. Cluster stability is evaluated across rolling temporal windows.",
            "image": "static/quant_PCA_KMEANS.png",
            "live_url": "https://unsupervised-engine2.streamlit.app/",  
            "github_url": "https://github.com/RodneyFinkel/K-Means-Clustering"
        },
        
        {
            "title": "FastAPI endpoints for ReACT/Research Agents and LangGraph Orchestrator",
            "description": "Production-ready REST API built with FastAPI exposing three major endpoints: Full LangGraph Multi-Agent Orchestrator, Async Semantic Web Researcher with ChromaDB persistence, and dedicated ReAct NL2SQL + Filesystem Agent. Includes Swagger UI for easy testing.",
            "image": "static/fastapi_multiagent2.png",   # ← Update this filename if different
            "live_url": None,  # Set to your deployed URL if available
            "github_url": "https://github.com/RodneyFinkel/text_analysis_pydantic"
        },
        
        {
            "title": "Voice Agent with Hybrid RAG and Web Search",
            "description": "Multi Modal Agent using Deepgram, Groq LPU's and Sentence Transformers for Vector Embeddings, ChromaDB for persistent vector db storage and BM25 with ColBERT reranking for sparse and dense vector search and retrieval",
            "image": "static/hybrid_rag.png",
            "live_url": None,
            "github_url": "https://github.com/RodneyFinkel/Hybrid_Rag"
        }
        
        
    ]
    
    

    # Render cards in a 2-column grid layout
    project_cols = st.columns(2)

    for i, project in enumerate(projects):
        # Alternate rendering between column 0 and column 1
        with project_cols[i % 2]:
            with st.container(border=True):
                st.subheader(project["title"])
                
                # Renders the app screenshot cleanly
                st.image(project["image"], use_container_width=True)
                
                st.write(project["description"])
                
                # Dynamic action button layout based on deployment status
                if project["live_url"]:
                    btn_col1, btn_col2 = st.columns(2)
                    with btn_col1:
                        st.link_button("🚀 Live App", project["live_url"], use_container_width=True)
                    with btn_col2:
                        st.link_button("💻 GitHub Repo", project["github_url"], use_container_width=True)
                else:
                    # If no live deployment exists, fall back completely to a full-width GitHub button
                    st.link_button("💻 GitHub Repository", project["github_url"], use_container_width=True)

    st.markdown("---")
    st.caption("**Demonstrated through production-grade projects in AI, RAG, multi-agent systems, and quantitative finance.**")

if __name__ == "__main__":
    display_tech_stack()