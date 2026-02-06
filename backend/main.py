from fastapi import FastAPI, UploadFile
import pandas as pd

app = FastAPI(title="SME Financial Health API")

@app.get("/")
def root():
    return {"status": "SME Financial Health Platform running"}

@app.post("/upload")
def upload_financials(file: UploadFile):
    df = pd.read_csv(file.file)
    summary = {
        "revenue": float(df["revenue"].sum()) if "revenue" in df else 0,
        "expenses": float(df["expenses"].sum()) if "expenses" in df else 0
    }
    return {"summary": summary}

@app.get("/health-score")
def health_score():
    return {
        "credit_score_band": "Medium Risk",
        "recommendation": "Improve receivables cycle and reduce operating expenses"
    }
