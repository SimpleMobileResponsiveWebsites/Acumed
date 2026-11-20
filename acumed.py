import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import random

st.set_page_config(
    page_title="AcuMed",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------
# CSS
# ------------------------------------------------------------------
st.markdown("""
<style>
    .hero {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d6a4f 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero h1 { font-size: 3.2rem; margin-bottom: 0.5rem; font-weight: 700; color: white; }
    .hero p { font-size: 1.4rem; opacity: 0.95; color: white; }
    .peace { font-size: 1.6rem; font-weight: 500; color: #d8f3dc; margin-top: 1rem; }

    .service-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2d6a4f;
        height: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        color: #000000 !important;
    }
    .service-card h4 { margin-top: 0; color: #1e3a5f !important; }
    .service-card p { color: #000000 !important; }

    .highlight { 
        background-color: #d8f3dc; 
        padding: 1.5rem; 
        border-radius: 10px; 
        color: #000000 !important;
    }
    .highlight h3, .highlight p, .highlight li, .highlight ul, .highlight strong {
        color: #000000 !important;
    }
    .highlight strong { color: #1e3a5f !important; }

    .cta-box {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d6a4f 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-top: 2rem;
    }
    .cta-box h2 { color: white; margin-bottom: 0.5rem; }
    .cta-box p { color: #e8f5e9; font-size: 1.15rem; margin-bottom: 1.5rem; }
    .book-btn {
        display: inline-block;
        background-color: #ffffff;
        color: #1e3a5f !important;
        font-weight: 700;
        font-size: 1.15rem;
        padding: 0.9rem 2.2rem;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    .book-btn:hover {
        background-color: #d8f3dc;
        transform: translateY(-2px);
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Session state (mock data)
# ------------------------------------------------------------------
if "view" not in st.session_state:
    st.session_state.view = "Landing"

if "claims" not in st.session_state:
    st.session_state.claims = pd.DataFrame({
        "Claim ID": [f"CLM-{1000+i}" for i in range(8)],
        "Patient": ["Jane Doe", "John Smith", "Maria Garcia", "Robert Lee", "Emily Chen", "David Kim", "Sarah Johnson", "Michael Brown"],
        "DOS": [(datetime.now() - timedelta(days=random.randint(5, 40))).strftime("%Y-%m-%d") for _ in range(8)],
        "Amount": [random.randint(85, 220) for _ in range(8)],
        "Status": random.choices(["Submitted", "Paid", "Pending", "Denied"], weights=[3, 3, 2, 2], k=8),
        "Payer": random.choices(["Aetna", "Blue Cross", "United", "Medicare", "Cash"], k=8)
    })

if "appointments" not in st.session_state:
    st.session_state.appointments = pd.DataFrame({
        "Time": ["09:00", "10:30", "13:00", "14:30", "16:00"],
        "Patient": ["Jane Doe", "John Smith", "Maria Garcia", "New Patient", "Emily Chen"],
        "Type": ["Follow-up", "Initial", "Follow-up", "Initial", "Follow-up"],
        "Status": ["Confirmed", "Confirmed", "Pending", "Confirmed", "Completed"]
    })

if "notes" not in st.session_state:
    st.session_state.notes = []

# ------------------------------------------------------------------
# Sidebar navigation
# ------------------------------------------------------------------
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/1e3a5f/ffffff?text=AcuMed", use_container_width=True)
    st.markdown("### Navigation")
    if st.button("🏠 Landing Page", use_container_width=True):
        st.session_state.view = "Landing"
    if st.button("📊 App Dashboard", use_container_width=True):
        st.session_state.view = "Dashboard"
    st.markdown("---")
    st.caption("Prototype • Mock data only")

# ------------------------------------------------------------------
# LANDING PAGE
# ------------------------------------------------------------------
if st.session_state.view == "Landing":
    st.markdown("""
    <div class="hero">
        <h1>AcuMed</h1>
        <p>An AI tool for acupuncturists</p>
        <p class="peace">AI does the work you don’t want to do.<br>Bringing peace to acupuncturists’ lives.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Built for solo practitioners — whether you accept insurance or not.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight">
        <h3>What we do</h3>
        <p>We handle the administrative burden so you can focus on patients.</p>
        <ul>
            <li>Claims & medical billing</li>
            <li>Insurance payments, status & documents</li>
            <li>Bookkeeping & certified tax support</li>
            <li>EHR, scheduling, notes & billing</li>
            <li>Document hub & communications</li>
            <li>HIPAA compliance & data encryption</li>
            <li>Legal support for liability protection</li>
            <li>Work comp & reference systems</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="highlight">
        <h3>The outcome</h3>
        <p><strong>Peace of mind.</strong></p>
        <p>Track insurance payments and claim status without chasing anyone.</p>
        <p>Your own EHR system that pulls what you need — easy for you, powerful for your admin team.</p>
        <p>Quality service, strong presence, and tools designed so the AI (and the team) do the work.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Everything bundled in one place")

    services = [
        ("Claims & Medical Billing", "Dedicated billers who submit, track, and follow up on claims."),
        ("Insurance Payments & Status", "Real-time visibility into payments, denials, and required docs."),
        ("Accountant & Tax Specialists", "Certified tax support and bookkeeping tailored for acupuncturists."),
        ("Attorney & Liability Support", "Legal help focused on reducing malpractice exposure."),
        ("EHR + Scheduling + Notes", "Your own system — scheduling, clinical notes, and billing integrated."),
        ("Doc Hub & Comms", "Secure document storage and client communication platform."),
        ("HIPAA & Encryption", "Certified compliance and strong data encryption."),
        ("Admin & Work Comp", "Administrative support and workers’ compensation handling."),
    ]

    cols = st.columns(4)
    for i, (title, desc) in enumerate(services):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="service-card">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

    st.markdown("---")
    st.markdown("""
    ### Designed for ease of use
    - **Practitioners** get a simple interface and peace of mind.  
    - **Administrative staff** can track insurance payments, claim status, and documents efficiently.  
    - Everything is pulled together so you don’t have to manage multiple vendors or systems.

    **Core outcome:** Providing a service for the things you don’t want to do — so you can bring more peace into your practice and your life.
    """)

    st.markdown("""
    <div class="cta-box">
        <h2>See AcuMed in Action</h2>
        <p>Book a short software presentation and discover how AcuMed removes the administrative load<br>so you can focus on your patients — and your peace of mind.</p>
        <a class="book-btn" href="https://book.squareup.com/appointments/6kib7afaj4d9tv/location/LBDGTAVYB2WK6?buttonTextColor=ffffff&color=212121&locale=en&referrer=so&service_id=C6SYSXTTBBVJIMRL5VI2IMDS" target="_blank">
            Book Your Presentation
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.caption(f"AcuMed • An AI tool for acupuncturists • {datetime.now().year}")

# ------------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------------
else:
    st.title("AcuMed Dashboard")
    st.caption("Prototype • All data is mock")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Claims & Billing",
        "Payments & Status",
        "EHR & Scheduling",
        "Documents & Comms",
        "Bookkeeping & Tax",
        "HIPAA & Legal",
        "Work Comp"
    ])

    # ----- Claims -----
    with tab1:
        st.subheader("Claims & Medical Billing")
        st.dataframe(st.session_state.claims, use_container_width=True, hide_index=True)

        with st.expander("Submit New Claim (demo)"):
            with st.form("new_claim"):
                c1, c2, c3 = st.columns(3)
                patient = c1.text_input("Patient Name")
                amount = c2.number_input("Amount ($)", min_value=0, value=120)
                payer = c3.selectbox("Payer", ["Aetna", "Blue Cross", "United", "Medicare", "Cash"])
                if st.form_submit_button("Submit Claim"):
                    new_row = pd.DataFrame([{
                        "Claim ID": f"CLM-{random.randint(2000, 9999)}",
                        "Patient": patient or "Unknown",
                        "DOS": datetime.now().strftime("%Y-%m-%d"),
                        "Amount": amount,
                        "Status": "Submitted",
                        "Payer": payer
                    }])
                    st.session_state.claims = pd.concat([st.session_state.claims, new_row], ignore_index=True)
                    st.success("Claim submitted (mock)")
                    st.rerun()

    # ----- Payments -----
    with tab2:
        st.subheader("Insurance Payments & Status")
        paid = st.session_state.claims[st.session_state.claims["Status"] == "Paid"]
        pending = st.session_state.claims[st.session_state.claims["Status"].isin(["Submitted", "Pending"])]
        denied = st.session_state.claims[st.session_state.claims["Status"] == "Denied"]

        m1, m2, m3 = st.columns(3)
        m1.metric("Paid", f"${paid['Amount'].sum():,.0f}", f"{len(paid)} claims")
        m2.metric("Pending", f"${pending['Amount'].sum():,.0f}", f"{len(pending)} claims")
        m3.metric("Denied", f"${denied['Amount'].sum():,.0f}", f"{len(denied)} claims")

        st.dataframe(st.session_state.claims, use_container_width=True, hide_index=True)

    # ----- EHR & Scheduling -----
    with tab3:
        st.subheader("EHR • Scheduling • Notes")
        col_a, col_b = st.columns([1, 1])

        with col_a:
            st.markdown("**Today’s Schedule**")
            st.dataframe(st.session_state.appointments, use_container_width=True, hide_index=True)

        with col_b:
            st.markdown("**Add Clinical Note**")
            with st.form("note_form"):
                patient_note = st.selectbox("Patient", st.session_state.appointments["Patient"].tolist())
                note_text = st.text_area("Note")
                if st.form_submit_button("Save Note"):
                    st.session_state.notes.append({
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "patient": patient_note,
                        "note": note_text
                    })
                    st.success("Note saved")

        if st.session_state.notes:
            st.markdown("**Recent Notes**")
            for n in reversed(st.session_state.notes[-5:]):
                st.info(f"**{n['patient']}** ({n['time']})\n\n{n['note']}")

    # ----- Documents & Comms -----
    with tab4:
        st.subheader("Document Hub & Communications")
        docs = pd.DataFrame({
            "Document": ["Superbill_2025.pdf", "Aetna_Auth.pdf", "Intake_Form.pdf", "Treatment_Plan.pdf", "EOBs_Nov.pdf"],
            "Type": ["Billing", "Insurance", "Forms", "Clinical", "Payments"],
            "Uploaded": ["2025-11-10", "2025-11-12", "2025-10-28", "2025-11-05", "2025-11-15"],
            "Status": ["Ready", "Needs Review", "Complete", "Signed", "Ready"]
        })
        st.dataframe(docs, use_container_width=True, hide_index=True)

        st.markdown("**Secure Message**")
        msg = st.text_input("Message to admin / biller")
        if st.button("Send"):
            st.success("Message sent (mock)")

    # ----- Bookkeeping -----
    with tab5:
        st.subheader("Bookkeeping & Tax Support")
        income = st.session_state.claims[st.session_state.claims["Status"] == "Paid"]["Amount"].sum()
        expenses = random.randint(1800, 3200)
        col1, col2, col3 = st.columns(3)
        col1.metric("YTD Income (Paid)", f"${income:,.0f}")
        col2.metric("YTD Expenses (est.)", f"${expenses:,.0f}")
        col3.metric("Estimated Profit", f"${income - expenses:,.0f}")

        st.info("Certified tax support and bookkeeping are handled by the AcuMed team. This is a high-level snapshot only.")

    # ----- HIPAA & Legal -----
    with tab6:
        st.subheader("HIPAA Compliance & Liability Support")
        st.checkbox("Business Associate Agreement signed", value=True)
        st.checkbox("Data encrypted at rest and in transit", value=True)
        st.checkbox("Access logs enabled", value=True)
        st.checkbox("Annual risk assessment completed", value=True)

        st.markdown("**Legal Resources**")
        st.markdown("- Malpractice insurance checklist")
        st.markdown("- Informed consent templates")
        st.markdown("- Scope of practice reference (state-specific)")

    # ----- Work Comp -----
    with tab7:
        st.subheader("Workers’ Compensation")
        wc = pd.DataFrame({
            "Case ID": ["WC-4412", "WC-4418", "WC-4421"],
            "Patient": ["Robert Lee", "Sarah Johnson", "Michael Brown"],
            "Injury": ["Low back", "Neck strain", "Shoulder"],
            "Status": ["Authorized", "Pending Auth", "In Treatment"],
            "Next Action": ["Submit notes", "Await carrier", "Schedule follow-up"]
        })
        st.dataframe(wc, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.caption("AcuMed Prototype • All data is simulated for demonstration purposes.")
