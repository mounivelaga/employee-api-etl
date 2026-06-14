from config import APT_URL, DB_CONFIG
from extract import extract_data
from transform import transform_data
from load import load_data


def main():
    data = extract_data(APT_URL)
    df = transform_data(data)
    load_data(df, DB_CONFIG)

    print("ETL pipeline completed sucessfully")


if __name__ == "__main__":
    main()
