import streamlit as st


st.set_page_config(
    page_title="Rodney Alex Finkel - Portfolio",
    page_icon="🛠️",
    layout="wide", # Always opens in wide screen layout
    initial_sidebar_state="expanded"
)

 # ================= TECH STACK MARQUEE =================





def display_tech_stack():
    
    st.markdown("""
        <h1 style='text-align: center; font-size: 3.2rem; margin-bottom: 0.2rem;'>
            Rodney Alex Finkel
        </h1>
        <h2 style='text-align: center; color: #6366f1; margin-top: 0;'>
            ML /  AI / GenAI Engineer
        </h2>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <p style='text-align: center; font-size: 1.15rem; max-width: 800px; margin: 0 auto 2rem;'>
        3+ years hands-on building production-grade multi-agent systems, voice-enabled Hybrid RAG pipelines, 
        and quantitative ML models. Expertise in LangGraph orchestration, real-time agents and advanced retrieval.
    </p>
    """, unsafe_allow_html=True)
    
    

    


    st.markdown("## 🚀 Featured Projects")
    
    projects = [
        {
            "title": "QuickRagAgent — Voice-First Hybrid RAG",
            "desc": "End-to-end real-time voice AI system with Deepgram STT/TTS, Groq inference, hybrid retrieval (Chroma + BM25 + ColBERT), Redis caching & pub/sub. Fully Dockerized.",
            "image": "static/hybrid_rag.png",
            "live": None,
            "github": "https://github.com/RodneyFinkel/Hybrid_Rag"
        },
        {
            "title": "Multi-Agent Orchestration Platform",
            "desc": "Stateful LangGraph supervisor coordinating ReAct DB/File agent, async semantic researcher, writer, and email dispatcher with SQL guardrails and artifact generation.",
            "image": "static/Multi-Agent-Platform.png",
            "live": "https://multi-agent-platform-alpha.onrender.com",
            "github": "https://github.com/RodneyFinkel/text_analysis_pydantic"
        },
        {
            "title": "S&P 500 R&D Clustering Engine",
            "desc": "Quantitative unsupervised ML pipeline using PCA whitening, temporal stability analysis, and SHAP explainability to uncover structural market archetypes based on R&D investment patterns.",
            "image": "static/clusters.png",
            "live": "https://unsupervised-engine2.streamlit.app/",
            "github": "https://github.com/RodneyFinkel/K-Means-Clustering"
        }
    ]
    
    cols = st.columns(3)
    for idx, proj in enumerate(projects):
        with cols[idx]:
            with st.container(border=True):
                st.subheader(proj["title"])
                st.image(proj["image"], use_container_width=True)
                st.write(proj["desc"])
                c1, c2 = st.columns(2)
                with c1:
                    if proj["live"]:
                        st.link_button("🚀 Live Demo", proj["live"], use_container_width=True)
                with c2:
                    st.link_button("💻 GitHub", proj["github"], use_container_width=True)
    
  
    
        
    
    
    
        # FEATURED PROJECTS
    
    
    badges = [
    "https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white",
    "https://img.shields.io/badge/SQL-4479A1?logo=sql&logoColor=white",
    "https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black",
    "https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white",
    "https://img.shields.io/badge/LangGraph-000000?logo=langchain&logoColor=white",
    "https://img.shields.io/badge/Groq-00A3FF?logo=groq&logoColor=white",
    "https://img.shields.io/badge/RAG-FF6B6B",
    "https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=black",
    "https://img.shields.io/badge/Deepgram-000000?logo=deepgram&logoColor=white",
    "https://img.shields.io/badge/GraphRAG-000000",
    "https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white",
    "https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white",
    "https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoftsqlserver&logoColor=white",
    "https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white",
    "https://img.shields.io/badge/SQLAlchemy-FF4B4B?logo=sqlalchemy&logoColor=white",
    "https://img.shields.io/badge/ChromaDB-000000",
    "https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white",
    "https://img.shields.io/badge/Neo4j-008CC1?logo=neo4j&logoColor=white",
    "https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white",
    "https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white",
    "https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white",
    "https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white",
    "https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white",
    "https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white",
    "https://img.shields.io/badge/Transformers-000000",
    "https://img.shields.io/badge/Statsmodels-000000",
    "https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white",
    "https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white",
    "https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white",
    "https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white",
    "https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white",
    "https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white",
    "https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white",
    "https://img.shields.io/badge/WebSockets-000000",
    "https://img.shields.io/badge/YAML-000000",
    "https://img.shields.io/badge/BeautifulSoup-8CB0A4?logo=python&logoColor=white",
    "https://img.shields.io/badge/Docling-000000",
    "https://img.shields.io/badge/Scrapy-000000?logo=scrapy&logoColor=white",
    ]

    badge_html = "".join(
        [f'<img src="{badge}" style="height:26px;margin-right:10px;">' for badge in badges]
    )

    st.markdown(
        f"""
        <style>
        .tech-banner {{
            position: sticky;
            top: 0;
            z-index: 999;
            width: 100%;
            overflow: hidden;
            background: transparent;
            padding: 8px 0;
        }}

        .tech-track {{
            display: flex;
            width: max-content;
            animation: scroll-left 70s linear infinite;
        }}

        @keyframes scroll-left {{
            from {{
                transform: translateX(0);
            }}
            to {{
                transform: translateX(-50%);
            }}
        }}
        </style>

        <div class="tech-banner">
            <div class="tech-track">
                {badge_html}
                {badge_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    
    
    
    
    
 
  
   
    
    
# ====================== THEORETICAL FOUNDATIONS ======================
    st.markdown("**Theoretical Foundations")
     
    
    
    st.markdown("---")

if __name__ == "__main__":
    display_tech_stack()