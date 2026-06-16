import requests
from logger import logger


def extract_data(url):
    logger.info("Extraction Started..")

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    logger.info("Extraction Completed")

    return data["users"]
