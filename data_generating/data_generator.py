import os
import uuid
from datetime import date, time, datetime, timedelta
import random

import pandas as pd
from faker import Faker


# Functions definition
def generate_fake_one_order(faker_obj: Faker, datetime_obj: datetime, order_canceling_rate: float = 0.1) -> dict:
    return {
        "order_id": str(uuid.uuid4()),
        "client_id": random.randint(1, 1000),
        "product_id": random.randint(1, 100),
        "country": faker_obj.country(),
        "order_date": datetime_obj,
        "quantity": random.randint(1, 100),
        "unit_price": round(random.uniform(8, 150), 2),
        "status": random.choices(["PAID", "CANCELLED"], weights=[1 - order_canceling_rate, order_canceling_rate])[0]
    }


def generate_multi_fake_orders(faker_obj: Faker, date_obj: date, num_orders: int, order_canceling_rate: float = 0.1) -> list[dict]:
    data = []

    for i in range(num_orders):
        # Generate random time and combine it with the date object
        random_time = time(
            hour=random.randint(0, 23),
            minute=random.randint(0, 59),
            second=random.randint(0, 59)
        )
        datetime_obj = datetime.combine(date_obj, random_time)

        # Append a new fake order to the data list
        data.append(generate_fake_one_order(faker_obj, datetime_obj, order_canceling_rate))

        # Logging each 100 order created
        if i % 10000 == 0:
            print(f"Generated {i}/{num_orders} for ", datetime_obj)

    return data


def save_data_to_csv(data: list[dict], file_path: str) -> None:
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)


def run(faker_seed: int, orders_count: int, orders_channel: str, order_canceling_rate: float, days_count: int, output_folder: str) -> None:
    # Objects initialisation
    faker = Faker()
    random.seed(faker_seed)

    for date_delta in range(days_count):
        # Set the target date
        target_date = datetime.today() - timedelta(days=date_delta)

        # Ensure the output folder exists
        custom_output_folder = os.path.join(output_folder, orders_channel)
        os.makedirs(custom_output_folder, exist_ok=True)

        # Generate and save the fake orders
        orders = generate_multi_fake_orders(faker, target_date, orders_count, order_canceling_rate)
        save_data_to_csv(orders, os.path.join(custom_output_folder, f"{target_date.strftime('%Y-%m-%d')}.csv"))
