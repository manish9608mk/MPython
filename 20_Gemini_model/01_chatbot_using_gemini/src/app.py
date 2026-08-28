import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

from chatbot import GeminiChat, GeminiError

st.set_page_config(
    page_title="MGemini",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Only CSS is injected here. Chat messages themselves use native
# Streamlit components, so raw <div> tags cannot appear in the chat.
st.markdown("""
<style>
.stApp { background:#0b0f14; color:#f4f7fb; }
[data-testid="stSidebar"] { background:#11151d; border-right:1px solid rgba(255,255,255,.08); }
.brand { font-size:1.6rem; font-weight:800; letter-spacing:-.03em; }
.brand-sub { color:#96a0ad; font-size:.85rem; margin-bottom:1.2rem; }
.hero-title { font-size:2.3rem; font-weight:850; letter-spacing:-.04em; }
.hero-sub { color:#96a0ad; margin-bottom:1.2rem; }
.stat-card {
    background:linear-gradient(145deg,#121a24,#0f141c);
    border:1px solid rgba(255,255,255,.09);
    border-radius:16px;
    padding:16px;
    min-height:88px;
}
.stat-label { color:#96a0ad; font-size:.78rem; margin-bottom:7px; }
.stat-value { font-size:1.05rem; font-weight:750; }
.empty-state { text-align:center; padding:4rem 1rem 2.5rem; color:#96a0ad; }
.quick-title {
    color:#96a0ad; font-size:.78rem; font-weight:700;
    text-transform:uppercase; letter-spacing:.08em;
    margin:1.2rem 0 .65rem;
}
[data-testid="stChatMessage"] {
    border:1px solid rgba(255,255,255,.08);
    border-radius:18px;
    padding:.9rem 1rem;
    margin-bottom:.75rem;
    background:#111720;
}
[data-testid="stChatMessage"] p { line-height:1.65; }
div.stButton > button { border-radius:11px; }
.footer { color:#66717e; font-size:.75rem; text-align:center; margin-top:1rem; }
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat" not in st.session_state:
    st.session_state.chat = None
if "profile_name" not in st.session_state:
    st.session_state.profile_name = "Guest"

gemini = GeminiChat()

with st.sidebar:
    st.markdown('<div class="brand">💬 MGemini</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-sub">Your personal Gemini AI workspace</div>', unsafe_allow_html=True)

    if st.button("＋ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat = None
        st.rerun()

    st.divider()
    st.markdown("### 💬 Chat History")

    user_messages = [m["content"] for m in st.session_state.messages if m["role"] == "user"]
    if user_messages:
        for text in user_messages[-6:]:
            st.caption(text[:50] + ("…" if len(text) > 50 else ""))
    else:
        st.caption("No conversations yet.")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat = None
        st.rerun()

    st.divider()
    st.markdown("### 👤 Profile")
    st.session_state.profile_name = st.text_input(
        "Your name",
        value=st.session_state.profile_name,
        label_visibility="collapsed",
        placeholder="Your name",
    )
    st.success(f"👋 Hello, {st.session_state.profile_name or 'Guest'}")

    st.divider()
    st.caption("MGemini • Streamlit + Google Gemini")
    st.caption("API key is read from your local .env file.")

main_col, dash_col = st.columns([3.35, 1.25], gap="large")

with main_col:
    st.markdown('<div class="hero-title">🤖 MGemini Chatbot</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-sub">Fast, clean and conversational AI powered by Google Gemini.</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.messages:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size:3rem;">✨</div>
            <h3>Start a conversation</h3>
            <p>Ask anything — Python, Cloud, DevOps, DSA, projects, or general questions.</p>
        </div>
        """, unsafe_allow_html=True)

    for message in st.session_state.messages:
        role = message["role"]
        with st.chat_message(role, avatar="🧑" if role == "user" else "🤖"):
            st.markdown(message["content"])

    st.markdown('<div class="quick-title">Quick prompts</div>', unsafe_allow_html=True)
    q1, q2, q3 = st.columns(3)
    quick_prompt = None

    with q1:
        if st.button("🐍 Python", use_container_width=True):
            quick_prompt = "Teach me one important Python concept with a simple example."
    with q2:
        if st.button("☁️ Cloud", use_container_width=True):
            quick_prompt = "Give me one practical Cloud/DevOps concept I should learn for a job."
    with q3:
        if st.button("🧠 DSA", use_container_width=True):
            quick_prompt = "Give me one interview-level DSA problem and guide me step by step."

    prompt = st.chat_input("Ask MGemini anything…")
    if quick_prompt:
        prompt = quick_prompt

    if prompt and prompt.strip():
        prompt = prompt.strip()
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user", avatar="🧑"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("MGemini is thinking…"):
                try:
                    answer = gemini.send(
                        prompt,
                        history=st.session_state.messages[:-1],
                        existing_chat=st.session_state.chat,
                    )
                    st.session_state.chat = gemini.chat
                    st.markdown(answer)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
                except GeminiError as exc:
                    st.error(str(exc))
                except Exception:
                    st.error(
                        "Unexpected error. Check your API key, internet connection, "
                        "and run: pip install -U google-genai"
                    )

with dash_col:
    st.markdown("## 📊 Dashboard")
    now = datetime.now(ZoneInfo("Asia/Kolkata"))
    stats = [
        ("📅 Date", now.strftime("%d %b %Y")),
        ("🕒 Local time", now.strftime("%I:%M:%S %p")),
        ("💬 Messages", str(len(st.session_state.messages))),
        ("🟢 Status", "Ready"),
    ]

    for label, value in stats:
        st.markdown(
            f'<div class="stat-card"><div class="stat-label">{label}</div>'
            f'<div class="stat-value">{value}</div></div>',
            unsafe_allow_html=True,
        )
        st.write("")

    st.markdown("### ⚙️ Model")
    st.info(gemini.model_name)

    st.markdown("### 💡 Tips")
    st.caption("• New Chat starts a clean conversation.")
    st.caption("• Chat history stays in the current Streamlit session.")
    st.caption("• API failures are handled without crashing the UI.")

st.markdown(
    '<div class="footer">Built with Python • Streamlit • Google Gemini</div>',
    unsafe_allow_html=True,
)
