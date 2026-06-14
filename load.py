from sqlalchemy import create_engine
from logger import logger


def load_data(df, db_config):
    logger.info("Load Started")

    connection_string = (
        f"postgresql://{db_config['user']}:"
        f"{db_config['password']}@"
        f"{db_config['host']}/"
        f"{db_config['database']}"
    )

    engine = create_engine(connection_string)

    df.to_sql("employees", engine, if_exists="replace", index=False)

    logger.info("Load Completed")
