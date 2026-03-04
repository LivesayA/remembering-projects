import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name) - %(message)s",
        handlers=[
            logging.FileHandler("autoclicker.log"),
            logging.StreamHandler()
        ]
    )