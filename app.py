import requests
import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="NxtWave AI Project Judge",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Global */
    .stApp {
        background: #f7f9fc;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hide Streamlit chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Brand */
    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 2rem;
    }

    .brand-logo {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(135deg, #4f46e5, #2563eb);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 18px;
    }

    .brand-title {
        font-size: 19px;
        font-weight: 700;
        color: #111827;
    }

    .brand-subtitle {
        font-size: 12px;
        color: #6b7280;
    }

    /* Hero */
    .hero {
        padding: 3rem 2rem;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #eef2ff 0%,
            #f8fbff 60%,
            #ffffff 100%
        );
        border: 1px solid #e5e7eb;
        margin-bottom: 2rem;
    }

    .hero-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background: #e0e7ff;
        color: #4338ca;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 14px;
    }

    .hero-title {
        font-size: 42px;
        line-height: 1.1;
        font-weight: 800;
        color: #111827;
        margin-bottom: 12px;
    }

    .hero-text {
        font-size: 16px;
        color: #6b7280;
        max-width: 720px;
        line-height: 1.6;
    }

    /* Cards */
    .card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.04);
    }

    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 5px;
    }

    .section-subtitle {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 20px;
    }

    /* Score */
    .score-card {
        background: linear-gradient(135deg, #111827, #1f2937);
        color: white;
        border-radius: 22px;
        padding: 30px;
        text-align: center;
        margin-bottom: 24px;
    }

    .score-label {
        font-size: 13px;
        color: #cbd5e1;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .score-value {
        font-size: 58px;
        font-weight: 800;
        margin-top: 4px;
    }

    .score-total {
        color: #94a3b8;
        font-size: 18px;
    }

    /* Result cards */
    .result-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 20px;
        min-height: 120px;
        box-shadow: 0 6px 20px rgba(15, 23, 42, 0.03);
    }

    .result-title {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 8px;
    }

    .result-score {
        font-size: 28px;
        font-weight: 750;
        color: #111827;
    }

    .result-max {
        font-size: 13px;
        color: #9ca3af;
    }

    /* Progress */
    .progress-bg {
        width: 100%;
        height: 7px;
        background: #eef2f7;
        border-radius: 999px;
        margin-top: 12px;
        overflow: hidden;
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #4f46e5, #2563eb);
        border-radius: 999px;
    }

    /* Lists */
    .list-item {
        background: #f8fafc;
        border: 1px solid #eef2f7;
        border-radius: 12px;
        padding: 13px 15px;
        margin-bottom: 10px;
        color: #374151;
        line-height: 1.5;
    }

    /* Resume */
    .resume-box {
        background: #f8faff;
        border: 1px solid #dbe4ff;
        border-radius: 14px;
        padding: 18px;
        color: #1f2937;
        line-height: 1.6;
    }

    /* Warning */
    .warning-box {
        background: #fff7ed;
        border: 1px solid #fed7aa;
        border-radius: 14px;
        padding: 18px;
        color: #9a3412;
        margin-bottom: 20px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 12px;
        padding-top: 30px;
    }

    /* Buttons */
    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 10px;
        border: none;
        font-weight: 600;
        padding: 0.65rem 1.2rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# WEBHOOK
# --------------------------------------------------

WEBHOOK_URL = st.secrets["N8N_WEBHOOK_URL"]

# --------------------------------------------------
# BRAND
# --------------------------------------------------

st.markdown(
    """
    <div class="brand">
        <div class="brand-logo">AI</div>
        <div>
            <div class="brand-title">NxtWave AI Project Judge</div>
            <div class="brand-subtitle">Automated AI Project Evaluation</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">AI-POWERED EVALUATION</div>

        <div class="hero-title">
            Evaluate your AI project.
        </div>

        <div class="hero-text">
            Submit your GitHub project and receive an automated evaluation
            based on implementation evidence, AI integration, technical
            quality, customization, documentation, reliability and
            resume readiness.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SUBMISSION FORM
# --------------------------------------------------

st.markdown(
    """
    <div class="card">
        <div class="section-title">Project Submission</div>
        <div class="section-subtitle">
            Provide your project details for automated evaluation.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

with st.form("submit_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Student Name *")
        email = st.text_input("Email *")
        college = st.text_input("College / University *")

    with col2:
        github_repo = st.text_input("GitHub Repository URL *")

        st.write("")
        st.write("")

        st.caption(
            "Your repository should be publicly accessible."
        )

    description = st.text_area(
        "Project Description *",
        height=120,
        placeholder="Describe what your project does and the problem it solves..."
    )

    customization = st.text_area(
        "What did you customize or add? *",
        height=120,
        placeholder="Describe the features, changes or improvements you personally added..."
    )

    submitted = st.form_submit_button(
        "Evaluate My Project",
        use_container_width=True
    )

# --------------------------------------------------
# SUBMIT
# --------------------------------------------------

if submitted:

    if not all([
        name,
        email,
        college,
        github_repo,
        description,
        customization
    ]):
        st.error("Please complete all required fields.")
        st.stop()

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
            st.error(f"Evaluation service is unavailable: {e}")
            st.stop()

    if response.status_code != 200:
        st.error(
            f"Evaluation service returned HTTP {response.status_code}"
        )
        st.stop()

    try:
        data = response.json()

    except ValueError:
        st.error("The evaluation service returned an invalid response.")
        st.stop()

    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------

    st.markdown("---")

    st.markdown(
        """
        <div class="section-title">
            Evaluation Complete
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        f"Evaluation generated for {data.get('student_name', name)}"
    )

    # --------------------------------------------------
    # TOTAL SCORE
    # --------------------------------------------------

    total_score = data.get("total_score", 0)

    st.markdown(
        f"""
        <div class="score-card">
            <div class="score-label">TOTAL SCORE</div>
            <div class="score-value">
                {total_score}
                <span class="score-total">/ 100</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # SCORE BREAKDOWN
    # --------------------------------------------------

    st.markdown(
        """
        <div class="section-title">Score Breakdown</div>
        <div class="section-subtitle">
            Detailed evaluation across seven dimensions.
        </div>
        """,
        unsafe_allow_html=True
    )

    scores = [
        ("Functionality", "working_score", 25),
        ("AI Usage", "ai_usage_score", 15),
        ("Technical Quality", "technical_quality_score", 15),
        ("Customization", "customization_score", 15),
        ("README / Documentation", "readme_score", 10),
        ("Reliability", "reliability_score", 10),
        ("Resume Readiness", "resume_score", 10),
    ]

    for i in range(0, len(scores), 2):

        cols = st.columns(2)

        for j, col in enumerate(cols):

            if i + j >= len(scores):
                break

            label, key, maximum = scores[i + j]

            score_value = data.get(key, 0) or 0

            try:
                percentage = min(
                    max(float(score_value) / maximum * 100, 0),
                    100
                )
            except:
                percentage = 0

            with col:

                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="result-title">{label}</div>
                        <div class="result-score">
                            {score_value}
                            <span class="result-max">/ {maximum}</span>
                        </div>

                        <div class="progress-bg">
                            <div
                                class="progress-fill"
                                style="width:{percentage}%">
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

    # --------------------------------------------------
    # STRENGTHS
    # --------------------------------------------------

    strengths = data.get("strengths") or []

    if strengths:

        st.markdown(
            '<div class="section-title">Strengths</div>',
            unsafe_allow_html=True
        )

        for item in strengths:
            st.markdown(
                f'<div class="list-item">{item}</div>',
                unsafe_allow_html=True
            )

    # --------------------------------------------------
    # IMPROVEMENTS
    # --------------------------------------------------

    improvements = data.get("improvements") or []

    if improvements:

        st.markdown(
            '<div class="section-title">Areas for Improvement</div>',
            unsafe_allow_html=True
        )

        for item in improvements:
            st.markdown(
                f'<div class="list-item">{item}</div>',
                unsafe_allow_html=True
            )

    # --------------------------------------------------
    # EVIDENCE
    # --------------------------------------------------

    evidence = data.get("evidence_summary")

    if evidence:

        st.markdown(
            '<div class="section-title">Evaluation Evidence</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="card">
                {evidence}
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------
    # RESUME BULLET
    # --------------------------------------------------

    resume_bullet = data.get("resume_bullet")

    if resume_bullet:

        st.markdown(
            '<div class="section-title">Resume-Ready Project Bullet</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="resume-box">
                {resume_bullet}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.code(resume_bullet, language=None)

    # --------------------------------------------------
    # REVIEW
    # --------------------------------------------------

    review_required = data.get("review_required", False)

    if review_required:

        risk = data.get("review_risk", "unknown")
        reason = data.get("review_reason", "")

        st.markdown(
            f"""
            <div class="warning-box">
                <strong>Review Recommended</strong><br>
                Risk Level: {risk.upper()}<br><br>
                {reason}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.success(
            "Automatically Evaluated"
        )

    # --------------------------------------------------
    # NEW EVALUATION
    # --------------------------------------------------

    st.write("")

    if st.button(
        "Evaluate Another Project",
        use_container_width=True
    ):
        st.rerun()

    st.markdown(
        """
        <div class="footer">
            NxtWave AI Project Judge · Automated Project Evaluation
        </div>
        """,
        unsafe_allow_html=True
    )