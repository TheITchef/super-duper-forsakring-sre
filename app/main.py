from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Super Duper Forsakring – Policy API",
    version="0.1.0"
)

# Sample data simulating a database
policies = {
    "P001": {"id": "P001", "holder": "Anna Svensson", "coverage": "comprehensive", "status": "active"},
    "P002": {"id": "P002", "holder": "Erik Karlsson", "coverage": "basic", "status": "active"},
    "P003": {"id": "P003", "holder": "Maria Lindgren", "coverage": "comprehensive", "status": "expired"},
}


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "policy-api"}


@app.get("/policy/{policy_id}")
def get_policy(policy_id: str):
    if policy_id not in policies:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policies[policy_id]
