document.addEventListener('DOMContentLoaded', () => {
    const projects = [
        {
            title: "Hybrid RAG Voice Assistant",
            desc: "Real-time voice-enabled RAG system with hybrid retrieval, Deepgram STT/TTS, and live streaming dashboard.",
            tech: "Flask • Groq • ChromaDB",
            image: "static/hybrid_rag.png"
        },
        {
            title: "Multi-Database Conversational Agent",
            desc: "LangChain ReAct agent with tool-calling for natural language querying across multiple databases.",
            tech: "Streamlit • LangGraph",
            image: "static/sql_react_agent.png"
        },
        {
            title: "Email Intelligence & Triage System",
            desc: "LoRA fine-tuned MiniLM model for email classification with Outlook parsing and interactive UI.",
            tech: "Streamlit • PEFT",
            image: "static/email_classifier.png"
        },
        {
            title: "Financial Market Intelligence",
            desc: "Unsupervised learning platform using PCA whitening, K-Means++, and SHAP explainability.",
            tech: "Python • Plotly",
            image: "static/quant_PCA_KMEANS.png"
        }
    ];

    const container = document.getElementById('project-container');

    projects.forEach((p, i) => {
        const html = `
            <div class="project-card bg-white dark:bg-gray-800 rounded-3xl overflow-hidden shadow-sm group fade-in" style="animation-delay: ${i * 100}ms">
                <div class="relative h-64 bg-gray-200 overflow-hidden">
                    <img src="${p.image}" alt="${p.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
                </div>
                <div class="p-8">
                    <h3 class="text-2xl font-semibold mb-3">${p.title}</h3>
                    <p class="text-gray-600 dark:text-gray-400 mb-5">${p.desc}</p>
                    <p class="text-xs uppercase tracking-widest text-gray-500 mb-6">${p.tech}</p>
                    <div class="flex gap-4">
                        <a href="#" class="flex-1 text-center bg-blue-600 hover:bg-blue-700 text-white py-3.5 rounded-2xl font-medium transition">Live Demo</a>
                        <a href="#" class="flex-1 text-center border border-gray-300 dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 py-3.5 rounded-2xl font-medium transition">GitHub</a>
                    </div>
                </div>
            </div>
        `;
        container.innerHTML += html;
    });

    // Fade-in observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.15 });

    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
});