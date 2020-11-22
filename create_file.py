import requests
import sys
import os

url = sys.argv[1]

data = requests.get(url=url)
div = None
if "Div. 2" in data.text:
    div = "D2"
elif "Div. 3" in data.text:
    div = "D3"
*_, contest, problem = url.split("/")
print(contest, problem)

codeforces_path = f'/Users/rajeevdodda/PycharmProjects/Codeforces/CF-{problem}'

folders = os.listdir(codeforces_path)

for folder in folders:
    a, b = folder.split('-')
    if int(a) <= int(contest) <= int(b):
        try:
            if div:
                f = open(f"{codeforces_path}/{folder}/CF{contest}-{div}-{problem}.py", mode="a")
            else:
                f = open(f"{codeforces_path}/{folder}/CF{contest}-{problem}.py", mode="a")
            f.write(f"# {url}")
            break

        except Exception as e:
            print(f"Unable to create file due to : {e}")



