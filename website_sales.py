import pandas as pd
import random
import uuid
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)

def generate_orders(date_str, num_orders):
    data = []
    for _ in range(num_orders):
        data.append({
            "order_id": str(uuid.uuid4()),
            "client_id": random.randint(1000, 9999),
            "product_id": random.randint(1, 500),
            "country": fake.country(),
            "order_date": date_str,
            "quantity": random.randint(1, 5),
            "unit_price": round(random.uniform(10, 100), 2),
            "status": random.choices(["PAID", "CANCELLED"], weights=[0.9, 0.1])[0]
        })
    return data

def save_to_csv(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    output_dir = "./data/website"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(5):
        date = (datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
        data = generate_orders(date, 170_000)  # ~1/3 of 500k
        save_to_csv(data, f"{output_dir}/website_sales_{date}.csv")
