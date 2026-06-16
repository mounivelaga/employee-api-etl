import pandas as pd
from logger import logger


def transform_data(data):
    logger.info("Transformation Started..")

    df = pd.json_normalize(data)

    selected_columns = [
        "id",
        "firstName",
        "lastName",
        "email",
        "phone",
        "age",
        "company.department",
    ]

    df = df[selected_columns]

    df.rename(
        columns={
            "id": "employee_id",
            "firstName": "first_name",
            "lastName": "last_name",
            "company.department": "department",
        },
        inplace=True,
    )

    logger.info("Transformation Completed..")

    return df
