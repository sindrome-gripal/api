import os


class DefaultConfig:
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

    # MongoDB Cluter
    CLUSTER_USERNAME = os.environ.get("CLUSTER_USERNAME")
    CLUSTER_PASSWORD = os.environ.get("CLUSTER_PASSWORD")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")

    # Email
    FROM_EMAIL = os.environ.get("FROM_EMAIL")
    FROM_PWD = os.environ.get("FROM_PWD")
    IMAP_SERVER = os.environ.get("IMAP_SERVER")
