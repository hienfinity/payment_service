from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime, timezone

#FastAPI-App initialisieren
app = FastAPI(title="Payment Service", version="1.0")

#Datenmodelle
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

#Zahlung ausführen
@app.post("/payments", response_model=PaymentResponse, status_code=201)
def create_payment(request: PaymentRequest):

    #Fehlerfall 1: Nicht genug Guthaben
    if request.amount > 1000: #weil wir keine echten Kontostand haben
        raise HTTPException(
            status_code=402,
            detail="Payment declined: not enough balance on account."
)

    #Fehlerfall 2: Timeout beim Zahlungsanbieter
    if request.order_id == "TIMEOUT":
        raise HTTPException(
            status_code=504,
            detail="Payment failed: payment provider did not respond in time."
        )

    #Erfolgreiche Zahlung
    payment_id = str(uuid4())
    created_at = datetime.now(timezone.utc).isoformat()

    payment = PaymentResponse(
        payment_id=payment_id,
        order_id=request.order_id,
        status="CAPTURED",   
        amount=request.amount,
        currency=request.currency,
        created_at=created_at
    )

    print(f"[LOG] Payment created: {payment}")
    return payment