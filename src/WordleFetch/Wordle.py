import datetime
import json
import urllib.request
import logging
from .Theme import *
logger = logging.getLogger("WordleFetch")


def get_wordle_display(data):
    """Generates the display strings using the fetched JSON data."""
    return {
        "header": f"{COLOR_HEADER}- Todays Wordle -{ANSI_RESET}",
        "answer": f"{COLOR_INFO}Answer {ANSI_RESET}• {COLOR_CONTENT}{data['solution']}{ANSI_RESET}",
        "date": f"{COLOR_INFO}Date {ANSI_RESET}• {COLOR_CONTENT}{data['print_date']}{ANSI_RESET}",
        "editor": f"{COLOR_INFO}Editor {ANSI_RESET}• {COLOR_CONTENT}{data['editor']}{ANSI_RESET}",
        "id": f"{COLOR_INFO}Id{ANSI_RESET} • {COLOR_CONTENT}{data['id']}{ANSI_RESET}",
        "days_since_launch": f"{COLOR_INFO}Days since Wordle #0{ANSI_RESET} • {COLOR_CONTENT}{data['days_since_launch']}{ANSI_RESET}"
    }

def fetch_wordle_data(date=None, url=None):
    if date is None:
        date = datetime.date.today()
    if url is None:
        url = f"https://www.nytimes.com/svc/wordle/v2/{date:%Y-%m-%d}.json"
    with urllib.request.urlopen(url) as request:
        if request.status == 200:
            JSON = json.loads(request.read().decode('utf-8'))
            return get_wordle_display(JSON)
        else:
            logger.error(f"{COLOR_ERROR}Error, check your connection.{ANSI_RESET}")
            raise Exception("RequestError")