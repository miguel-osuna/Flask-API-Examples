import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask configuration
FLASK_ENV = "development"
FLASK_DEBUG = True

# Database configuration
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
    DB_USER="miguel",
    DB_PASS="password",
    DB_ADDR="127.0.0.1",
    DB_NAME="flask_notifications",
)

# Pagination configuration
PAGINATION_PAGE_SIZE = 4
PAGINATION_PAGE_ARGUMENT_NAME = "page"

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")
