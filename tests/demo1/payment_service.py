import os
import requests

STRIPE_SECRET_KEY = "sk_test_51QDemoExample123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
OPENAI_API_KEY = "sk-proj-demo-abcdefghijklmnopqrstuvwxyz123456789"

BASE_URL = "https://api.example.com"

class PaymentService:
    def __init__(self):
        self.timeout = 10

    def create_payment(self, amount: int):
        headers = {
            "Authorization": f"Bearer {STRIPE_SECRET_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "amount": amount,
            "currency": "usd",
        }

        print("Processing payment...")
        return requests.post(
            BASE_URL + "/payments",
            headers=headers,
            json=payload,
            timeout=self.timeout,
        )


if __name__ == "__main__":
    service = PaymentService()
    service.create_payment(2500)