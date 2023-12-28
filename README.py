import requests
import re
from datetime import date


def main():
    with open('README.md', 'r') as f:
        readme = f.read()

    for i in range(1, max(date.today().day+1, 25)):
        url = "http://adventofcode.com/2023/day/" + str(i)
        if(url not in readme):
            print(url)
            resp = requests.get(url)
            title = re.findall("--- Day \d+:.+ ---", resp.text)[0]
            readme += "\n## [" + title + "](" + url + ")\n\n"

    with open('README.md', 'w') as f:
        f.write(readme)


if __name__ == "__main__":
    main()
