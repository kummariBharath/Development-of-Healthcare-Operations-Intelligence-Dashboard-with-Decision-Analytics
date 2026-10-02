# Medical Operations Intelligence & Automation Command System

A production-grade Medical Operations Intelligence platform connecting a React + TypeScript frontend to a secure FastAPI Python backend powered by AWS S3, AWS Glue Data Catalog, Amazon Athena, and Amazon Bedrock.

---

## 🏗️ Architecture Overview

```
                                 [ Healthcare Dataset ]
                                           │
                                           ▼
                                      [ AWS S3 ]
                   (medical-operations-bharath-2026 / Local Dataset)
                                           │
                                           ▼
                                [ AWS Glue Data Catalog ]
                                (medical_operations_db)
                                           │
                                           ▼
                                  [ Amazon Athena ]
                               (Workgroup: primary)
                                           │
                                           ▼
                               [ Secure FastAPI Backend ]
                                (Python 3.14 + Boto3)
                                ├── /api/health
                                ├── /api/dashboard/*
                                ├── /api/glue/*
                                ├── /api/athena/*
                                └── /api/copilot/*
                                           │
                                           ▼
                                [ React + Vite Frontend ]
                            (Tailwind CSS v4 + Recharts)
```

---

## 🔒 Security Architecture

- **Zero Client-Side Credentials**: AWS Access Keys, Secret Keys, and Session Tokens exist **ONLY** within server-side environment variables (`backend/.env`), IAM roles, or local AWS credential configurations.
- **Frontend Isolation**: React frontend communicates exclusively with the backend via REST endpoints (`http://127.0.0.1:8000/api`).
- **Protected Environment**: Secret values are excluded from version control via `.gitignore`.

---

## 🚀 Quick Start Guide

### Prerequisites
- Node.js (v18+)
- Python (v3.10+)
- AWS Account with S3, Glue, Athena, and Bedrock permissions

---

### 1. Launch FastAPI Backend

```powershell
cd d:\Infosys\backend

# Install Python Dependencies
python -m pip install fastapi uvicorn boto3 pydantic python-dotenv pandas

# Start Backend Server (Runs on http://127.0.0.1:8000)
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Backend API documentation (Swagger UI) is available at:
`http://127.0.0.1:8000/docs`

---

### 2. Launch React Frontend

```powershell
cd d:\Infosys

# Install Node Dependencies (if needed)
npm install

# Start Vite Development Server
npm run dev
```

Application will open at:
`http://localhost:5173`

---

## ⚙️ Backend Environment Variables (`backend/.env`)

```ini
AWS_REGION=ap-south-1
AWS_GLUE_DATABASE=medical_operations_db
AWS_S3_BUCKET=medical-operations-bharath-2026
AWS_ATHENA_WORKGROUP=primary
AWS_ATHENA_OUTPUT=s3://medical-operations-bharath-2026/athena-query-results/
AWS_BEDROCK_MODEL=anthropic.claude-3-5-sonnet-20240620-v1:0

# (Optional: If not using default AWS CLI credentials or IAM Role)
# AWS_ACCESS_KEY_ID=
# AWS_SECRET_ACCESS_KEY=
# AWS_SESSION_TOKEN=
```

---

## 📡 API Endpoint Summary

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/health` | `GET` | Health check & live connection statuses for S3, Glue, Athena, Bedrock |
| `/api/dashboard/facilities` | `GET` | Discovered facility list (`FAC001` - `FAC005`) |
| `/api/dashboard/summary` | `GET` | Aggregated executive KPIs filtered by facility |
| `/api/dashboard/facilities-comparison` | `GET` | Cross-facility performance leaderboard |
| `/api/dashboard/billing` | `GET` | Revenue, gross billing, & departmental breakdown |
| `/api/dashboard/claims` | `GET` | Claims volume, denial rate, & top denial reasons |
| `/api/dashboard/patient-ops` | `GET` | Admissions, length of stay, & patient demographics |
| `/api/dashboard/doctor-staff` | `GET` | Doctor workload, utilization %, & shift metrics |
| `/api/dashboard/laboratory` | `GET` | Lab test orders, turnaround times (TAT), & categories |
| `/api/dashboard/pharmacy-inventory` | `GET` | Stock levels, low stock alerts, & reorder thresholds |
| `/api/glue/tables` | `GET` | List of all 41 tables in `medical_operations_db` catalog |
| `/api/glue/tables/{table}/schema` | `GET` | Detailed column definitions and data types |
| `/api/athena/execute` | `POST` | Executes real SQL queries on Amazon Athena |
| `/api/copilot/query` | `POST` | Natural language queries via Amazon Bedrock |

---

## 🌐 Facilities Discovered in Dataset

1. `FAC001` — Hyderabad Central Hospital (Hyderabad, Telangana)
2. `FAC002` — Hyderabad West Clinic (Hyderabad, Telangana)
3. `FAC003` — Secunderabad Medical Center (Secunderabad, Telangana)
4. `FAC004` — Bengaluru Care Hospital (Bengaluru, Karnataka)
5. `FAC005` — Chennai Health Center (Chennai, Tamil Nadu)
