from dotenv import load_dotenv
import os

def configurar_app():
    load_dotenv()
    host = os.getenv("BROKER_HOST", "broker")
    if host is None:
        host = "localhost"
    return host