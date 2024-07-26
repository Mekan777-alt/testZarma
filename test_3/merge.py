import csv
import json
import logging

import pandas as pd

from test_3.create_data import generate_json_data, generate_product_ids, generate_csv_data


def load_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        csv_data = list(reader)

    logging.info("Прочитал CSV файл")
    return csv_data


def load_json(filename):
    with open(filename, mode='r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)

    logging.info("Прочитал JSON файл")
    return json_data


def save_merged_data(merged_data, output_file):
    merged_data.to_csv(output_file, index=False, encoding='utf-8')
    logging.info(f"Сохранил обьединенный файл в {output_file}")


def merge_data(csv_data, json_data):
    csv_data = pd.DataFrame(csv_data)
    json_data = pd.DataFrame(json_data)

    merged = pd.merge(csv_data, json_data, on='product_id')

    logging.info("Обьединил файлы")
    return merged


def create_data(json_file, csv_file):
    num_records = 100

    product_ids = generate_product_ids(num_records)

    generate_json_data(product_ids, json_file)
    generate_csv_data(product_ids, csv_file)

    logging.info("Создал тестовые данные")

    return True


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    csv_file = 'products_data.csv'
    json_file = 'sales_data.json'

    if create_data(json_file, csv_file):
        output_file = 'merged_data.csv'

        merged_data = merge_data(load_csv(csv_file), load_json(json_file))

        save_merged_data(merged_data, output_file)

        logging.info(f"Объединенные данные успешно сохранены в {output_file}")


if __name__ == '__main__':
    main()
