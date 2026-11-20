AcuMed 🌿

**An AI tool for acupuncturists**

> AI does the work you don’t want to do.  
> Bringing peace to acupuncturists’ lives.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

AcuMed is a modern practice management platform designed specifically for solo acupuncturists. Whether you accept insurance or work cash-only, AcuMed handles the administrative burden so you can focus on what you do best — treating patients.

---

## Features

### Built for Peace of Mind

| Area | What AcuMed Handles |
|------|---------------------|
| **Claims & Billing** | Dedicated billers who submit, track, and follow up on claims |
| **Insurance Visibility** | Real-time payments, denials, status, and required documents |
| **Bookkeeping & Tax** | Certified tax support and bookkeeping tailored for acupuncturists |
| **EHR + Scheduling** | Your own system with scheduling, clinical notes, and billing |
| **Document Hub** | Secure storage and client communications |
| **HIPAA & Security** | Certified compliance and strong encryption |
| **Legal Support** | Liability protection and malpractice risk reduction |
| **Work Comp** | Administrative support and workers’ compensation handling |

**Core outcome:** Providing a service for the things you don’t want to do — so you can bring more peace into your practice and your life.

---

## Demo

This repository contains a fully interactive **Streamlit prototype** with mock data.

### Landing Page
- Beautiful hero section
- Clear value proposition
- Service cards
- Direct booking CTA

### Dashboard
Interactive tabs for:
- Claims & Medical Billing
- Payments & Status (with live metrics)
- EHR, Scheduling & Notes
- Document Hub & Communications
- Bookkeeping & Tax Snapshot
- HIPAA & Legal Checklist
- Workers’ Compensation Cases

All data is simulated for demonstration purposes.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/acumed.git
cd acumed

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install streamlit pandas

# Run the app
streamlit run app.py
