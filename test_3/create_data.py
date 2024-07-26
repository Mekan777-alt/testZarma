import json
import csv
import logging

from faker import Faker

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_product_ids(num_records):
    fake = Faker()
    product_ids = [fake.uuid4() for _ in range(num_records)]
    return product_ids


def generate_json_data(product_ids, json_file):
    fake = Faker()
    data = []

    for product_id in product_ids:
        record = {
            "sale_id": fake.uuid4(),
            "product_id": product_id,
            "amount": fake.random_number(digits=5)
        }
        data.append(record)

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def generate_csv_data(product_ids, csv_file):
    fake = Faker()
    data = []

    for product_id in product_ids:
        record = {
            "product_id": product_id,
            "product_name": fake.word()
        }
        data.append(record)

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["product_id", "product_name"])
        writer.writeheader()
        writer.writerows(data)
