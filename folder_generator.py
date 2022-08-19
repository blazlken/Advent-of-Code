import requests
from bs4 import BeautifulSoup

import os
import datetime

AOC_EPOCH = datetime.datetime(2015, 12, 1)
TODAY = datetime.date.today()
CWD = os.getcwd()
AOC_URL = "https://adventofcode.com/"

def get_cookie() -> str:
    file = open("cookie.txt", 'r')
    output = file.read()
    file.close()

    if output == "":
        raise ValueError("Retrieved cookie is an empty string")

    return output

def get_input(login_cookie: str, year: int, day: int) -> str:
    session = requests.Session()
    session.cookies.set("session", login_cookie, domain='.adventofcode.com')
    input_html = session.get(AOC_URL + f'{year}/day/{day}/input')
    
    soup = BeautifulSoup(input_html.content, "html.parser")
    return soup.text


def generate_AoC() -> None:
    cd = None

    for year in range(AOC_EPOCH.year, TODAY.year + 1):
        cd = CWD + '\\' + str(year)

        if TODAY.month == 12:
            if not(os.path.exists(cd)):
                os.mkdir(cd)

            for day in range(AOC_EPOCH.day, min(TODAY.day, 25)+1):
                cd = CWD + '\\' + str(year) + '\\' + f'DAY_{day}'

                if not(os.path.exists(cd)):
                    os.mkdir(cd)

                if not(os.path.exists(cd + '\\input.txt')):
                    file = open(cd + '\\input.txt', 'x')
                    file.write(get_input(get_cookie(),year,day))
                    file.close()

if __name__ == '__main__':
    generate_AoC()
    print("Done")