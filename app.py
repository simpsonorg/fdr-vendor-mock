from fastapi import FastAPI

app = FastAPI(title="fdr-vendor-mock")

@app.get("/fdr/account/{accountId}")
def get_account(accountId: str):
    return {"accountId": accountId, "status": "ACTIVE", "externalBalance": 123.45}

@app.get("/health")
def health():
    return {"status": "fdr-vendor-up"}
