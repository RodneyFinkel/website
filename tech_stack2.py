import streamlit as st

st.set_page_config(
    page_title="Rodney Alex Finkel - AI Engineer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def display_tech_stack():
    # HERO
    st.markdown("""
        <h1 style='text-align: center; font-size: 3.4rem; margin-bottom: 0.3rem;'>
            Rodney Alex Finkel
        </h1>
        <h2 style='text-align: center; color: #6366f1; margin-top: 0; font-weight: 500;'>
            AI / GenAI Engineer
        </h2>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2rem; max-width: 820px; margin: 1.2rem auto 2.5rem; color: #e2e8f0;'>
        3+ years hands-on building production-grade <strong>multi-agent systems</strong>, 
        <strong>voice-enabled Hybrid RAG</strong> pipelines, and <strong>quantitative ML models</strong>. 
        Deep expertise in LangGraph orchestration, real-time agents, advanced retrieval, and financial AI.
    </p>
    """, unsafe_allow_html=True)

    # Featured Projects
    st.markdown("## 🚀 Featured Projects")
    st.markdown("---")

    projects = [
        {
            "title": "QuickRagAgent — Voice-First Hybrid RAG",
            "desc": "Real-time voice AI system with Deepgram STT/TTS, Groq inference, hybrid retrieval (Chroma + BM25 + ColBERT reranking), Redis caching & pub/sub. Fully Dockerized.",
            "image": "static/hybrid_rag.png",
            "live": None,
            "github": "https://github.com/RodneyFinkel/Hybrid_Rag"
        },
        {
            "title": "Multi-Agent Orchestration Platform",
            "desc": "Stateful LangGraph supervisor coordinating ReAct DB agent, async semantic researcher, writer, and email dispatcher with SQL guardrails and artifact generation.",
            "image": "static/Multi-Agent-Platform.png",
            "live": "https://multi-agent-platform-alpha.onrender.com",
            "github": "https://github.com/RodneyFinkel/text_analysis_pydantic"
        },
        {
            "title": "S&P 500 R&D Clustering Engine",
            "desc": "Quantitative unsupervised ML pipeline using PCA whitening, temporal stability analysis (ARI), and SHAP explainability to discover structural market archetypes.",
            "image": "static/clusters.png",
            "live": "https://unsupervised-engine2.streamlit.app/",
            "github": "https://github.com/RodneyFinkel/K-Means-Clustering"
        }
    ]

    cols = st.columns(3)
    for idx, proj in enumerate(projects):
        with cols[idx]:
            with st.container(border=True, height=520):
                st.subheader(proj["title"])
                st.image(proj["image"], use_container_width=True)
                st.write(proj["desc"])
                
                c1, c2 = st.columns(2)
                with c1:
                    if proj.get("live"):
                        st.link_button("🚀 Live Demo", proj["live"], use_container_width=True)
                with c2:
                    st.link_button("💻 GitHub", proj["github"], use_container_width=True)

    st.markdown("---")

    # Scrolling Tech Marquee
    badges = [
        "https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white",
        "https://img.shields.io/badge/LangGraph-000000?logo=langchain&logoColor=white",
        "https://img.shields.io/badge/Groq-00A3FF?logo=groq&logoColor=white",
        "https://img.shields.io/badge/Deepgram-000000?logo=deepgram&logoColor=white",
        "https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white",
        "https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white",
        "https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white",
        "https://img.shields.io/badge/ChromaDB-000000",
        "https://img.shields.io/badge/ColBERT-000000",
        "https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white",
        "https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white",
        "https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white",
        "https://img.shields.io/badge/SHAP-000000",
        "https://img.shields.io/badge/PCA-3776AB",
    ]

    badge_html = "".join([f'<img src="{b}" style="height:28px; margin: 0 12px;">' for b in badges])

    st.markdown(f"""
        <style>
        .marquee {{
            overflow: hidden;
            white-space: nowrap;
            padding: 12px 0;
            background: linear-gradient(90deg, #1e2937, #334155);
        }}
        .marquee-content {{
            display: inline-flex;
            animation: marquee 45s linear infinite;
        }}
        @keyframes marquee {{
            from {{ transform: translateX(0); }}
            to {{ transform: translateX(-50%); }}
        }}
        </style>
        <div class="marquee">
            <div class="marquee-content">
                {badge_html}
                {badge_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Full Tech Stack & Experience Details** → See individual project READMEs on GitHub")

if __name__ == "__main__":
    display_tech_stack()