import requests
import streamlit as st

st.set_page_config(
    page_title="NxtWave AI Project Judge",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 NxtWave AI Project Judge")
st.caption("Automated AI Project Evaluation")

WEBHOOK_URL = st.secrets["N8N_WEBHOOK_URL"]

with st.form("submit_form"):

    name = st.text_input("Student Name *")
    email = st.text_input("Email *")
    college = st.text_input("College / University *")
    github_repo = st.text_input("GitHub Repository URL *")

    description = st.text_area(
        "Project Description *"
    )

    customization = st.text_area(
        "What did you customize or add? *"
    )

    submitted = st.form_submit_button(
        "🚀 Evaluate My Project"
    )

if submitted:

    if not all([
        name,
        email,
        college,
        github_repo,
        description,
        customization
    ]):
        st.error("Please fill all required fields.")
        st.stop()

    # IMPORTANT: field names must match n8n Webhook
    payload = {
        "student_name": name,
        "email": email,
        "college": college,
        "github_url": github_repo,
        "project_description": description,
        "customization_description": customization
    }

    with st.spinner(
        "Analyzing your project, repository evidence and AI implementation..."
    ):

        try:
            response = requests.post(
                WEBHOOK_URL,
                json=payload,
                timeout=180
            )

        except requests.exceptions.RequestException as e:
            st.error(f"Could not reach n8n: {e}")
            st.stop()

    if response.status_code != 200:
        st.error(
            f"n8n returned HTTP {response.status_code}"
        )
        st.code(response.text)
        st.stop()

    try:
        data = response.json()
    except ValueError:
        st.error("n8n did not return valid JSON.")
        st.code(response.text)
        st.stop()

    st.success("✅ Evaluation Complete")

    # =========================
    # TOTAL SCORE
    # =========================

    total_score = data.get("total_score", 0)

    st.metric(
        "TOTAL SCORE",
        f"{total_score} / 100"
    )

    # =========================
    # SCORE BREAKDOWN
    # =========================

    st.subheader("📊 Score Breakdown")

    scores = [
        ("Functionality", "working_score", 25),
        ("AI Usage", "ai_usage_score", 15),
        ("Technical Quality", "technical_quality_score", 15),
        ("Customization", "customization_score", 15),
        ("README / Documentation", "readme_score", 10),
        ("Reliability", "reliability_score", 10),
        ("Resume Readiness", "resume_score", 10)
    ]

    for label, key, maximum in scores:

        score = data.get(key, 0)

        st.write(
            f"**{label}: {score}/{maximum}**"
        )

        st.progress(
            min(float(score) / maximum, 1.0)
        )

    # =========================
    # STRENGTHS
    # =========================

    strengths = data.get("strengths") or []

    if strengths:
        st.subheader("💪 Strengths")

        for item in strengths:
            st.write(f"✅ {item}")

    # =========================
    # IMPROVEMENTS
    # =========================

    improvements = data.get("improvements") or []

    if improvements:
        st.subheader("🔧 Areas for Improvement")

        for item in improvements:
            st.write(f"• {item}")

    # =========================
    # EVIDENCE
    # =========================

    evidence = data.get("evidence_summary")

    if evidence:
        st.subheader("🔍 Evaluation Evidence")
        st.info(evidence)

    # =========================
    # RESUME BULLET
    # =========================

    resume_bullet = data.get("resume_bullet")

    if resume_bullet:
        st.subheader("📄 Resume-Ready Bullet")

        st.code(
            resume_bullet,
            language=None
        )

    # =========================
    # REVIEW
    # =========================

    if data.get("review_required", False):

        st.warning(
            f"⚠️ Review Recommended "
            f"({data.get('review_risk', 'unknown').upper()} risk)"
        )

        reason = data.get("review_reason")

        if reason:
            st.write(reason)

    else:

        st.success("✅ Automatically Evaluated")
