import logging
import os

# ================================
# CREATE LOG DIRECTORY
# ================================
LOG_FILE = "app.log"

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

# ================================
# LOGGER CONFIG
# ================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("cricket-ai")


# ================================
# HELPER FUNCTIONS
# ================================
def log_info(msg: str):
    logger.info(msg)


def log_error(msg: str):
    logger.error(msg)


def log_warning(msg: str):
    logger.warning(msg)