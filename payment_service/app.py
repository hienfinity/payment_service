from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

app = FastAPI()

class PaymentRequest(BaseModel):
    order_id: str
    amount: float
    currency: str
    method: str

class PaymentResponse(BaseModel):
    payment_id: str
    order_id: str
    status: str
    amount: float
    currency: str
    created_at: str

@app.post("/payments", response_model=PaymentResponse)
def create_payment(request: PaymentRequest):
    payment_id = str(uuid4())
    status = "CAPTURED"  
    created_at = datetime.utcnow().isoformat()

    payment = PaymentResponse(
        payment_id=payment_id,
        order_id=request.order_id,
        status=status,
        amount=request.amount,
        currency=request.currency,
        created_at=created_at
    )

    print(f"[LOG] Payment created: {payment}")
    return payment


@app.get("/")
def root():
    return {"message": "Payment Service läuft 🚀"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)