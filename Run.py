import datetime
import requests
import json

def main():
    date = datetime.date.today()
    url = f"https://www.nytimes.com/svc/wordle/v2/{date:%Y-%m-%d}.json"
    request = requests.get(url)
    if request.status_code == 200:
        JSON = request.json()
        stats = f"""[#3af63a]
- Todays Wordle -
Answer • {JSON['solution']}
Date • {JSON['print_date']}
Editor • {JSON['editor']}
Id • {JSON['id']}
Days since Wordle #0 • {JSON['days_since_launch']}
        """
        print(stats)
        input()
        exit()
    else:
      print('[bold red]Error, check your connection.')
      exit()

if __name__ == '__main__':
    main()