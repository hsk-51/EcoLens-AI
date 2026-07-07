"""EcoLens AI – Home page and application entry point."""

import streamlit as st

from ecolens.config.settings import APP_NAME, APP_TAGLINE, DEFAULT_SESSION_KEYS, PROGRAM
from ecolens.ui.components import (
    init_session_state,
    render_hero,
    render_info_card,
    render_metric_card,
    render_sidebar_branding,
    render_sdg_badges,
)
from ecolens.ui.theme import apply_theme

st.set_page_config(
    page_title=f"{APP_NAME} – Home",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state(DEFAULT_SESSION_KEYS)
apply_theme()
render_sidebar_branding()

render_hero(APP_NAME, APP_TAGLINE)

st.markdown(f"*{PROGRAM}*")

col1, col2, col3, col4 = st.columns(4)
with col1:
    render_metric_card("Audit Modules", "10")
with col2:
    render_metric_card("SDG Goals", "5")
with col3:
    render_metric_card("Score Range", "0–100")
with col4:
    score_display = f"{st.session_state.overall_score:.0f}" if st.session_state.audit_complete else "—"
    render_metric_card("Your Score", score_display)

st.divider()

left, right = st.columns([3, 2])

with left:
    st.subheader("🎯 Mission")
    st.markdown(
        """
        Educational institutions consume significant resources — electricity, water, paper, and plastics —
        yet most lack affordable tools to assess their sustainability practices.

        **EcoLens AI** bridges this gap with an AI-powered self-assessment that delivers:

        - **Sustainability Score** (0–100) with category breakdowns
        - **Agent-generated recommendations** tailored to your institution
        - **Risk assessment** and priority improvements
        - **Environmental impact estimates**
        - **Downloadable PDF report** for stakeholders
        """
    )

    render_info_card(
        "Primary SDG Alignment",
        "SDG 12 – Responsible Consumption and Production. "
        "Secondary alignment with SDGs 6 (Water), 7 (Energy), 11 (Cities), and 13 (Climate).",
    )

    st.subheader("🚀 Get Started")
    if st.session_state.audit_complete:
        st.success(f"✅ Audit complete! Your score: **{st.session_state.overall_score}/100**")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("View Results →", type="primary", use_container_width=True):
                st.switch_page("pages/3_📊_Results.py")
        with c2:
            if st.button("Download Report →", use_container_width=True):
                st.switch_page("pages/6_📄_PDF_Report.py")
    else:
        st.info("Complete the 10-module sustainability audit to receive your personalized score and recommendations.")
        if st.button("Start Audit →", type="primary", use_container_width=True):
            st.switch_page("pages/2_🔍_Start_Audit.py")

with right:
    st.subheader("🌍 SDG Alignment")
    render_sdg_badges()

    st.subheader("📋 Audit Modules")
    modules_list = [
        ("⚡", "Energy"), ("💧", "Water"), ("♻️", "Waste"),
        ("📄", "Paper Usage"), ("🥤", "Plastic Usage"), ("🚌", "Transportation"),
        ("☀️", "Renewable Energy"), ("💻", "Digital Practices"),
        ("📢", "Awareness Programs"), ("🌍", "Carbon Reduction"),
    ]
    for icon, name in modules_list:
        st.markdown(f"- {icon} {name}")

st.divider()
st.caption("Built with Python · Streamlit · OpenAI · Pandas · Plotly | No personal data collected")






