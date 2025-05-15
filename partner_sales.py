import pandas as pd
import random
import uuid
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(44)

def generate_orders(date_str, num_orders):
    data = []
    for _ in range(num_orders):
        data.append({
            "order_id": str(uuid.uuid4()),
            "client_id": random.randint(1000, 9999),
            "product_id": random.randint(1, 500),
            "country": fake.country(),
            "order_date": date_str,
            "quantity": random.randint(1, 6),
            "unit_price": round(random.uniform(8, 150), 2),
            "status": random.choices(["PAID", "CANCELLED"], weights=[0.85, 0.15])[0]
        })
    return data

def save_to_csv(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    output_dir = "./data/partner"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(5):
        date = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
        data = generate_orders(date, 180_000)
        save_to_csv(data, f"{output_dir}/partner_sales_{date}.csv")
