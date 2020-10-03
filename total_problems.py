import os, pprint

total = {
    "Div2-A": 0,
    "Div2-B": 0,
    "Div2-C": 0,
    "Div3-A": 0,
    "Div3-B": 0,
    "Div3-C": 0,
    "Others-A": 0,
    "Others-B": 0,
    "Others-C": 0,

}

total_count = 0
pathA = "/Users/rajeevdodda/PycharmProjects/Codeforces/CF-A"
pathB = "/Users/rajeevdodda/PycharmProjects/Codeforces/CF-B"

CF_A = os.listdir(pathA)
CF_B = os.listdir(pathB)

for folder in CF_A:
    problems = os.listdir(pathA + "/" + folder)
    for problem in problems:
        if "D2-A" in problem:
            total["Div2-A"] += 1
        elif "D3-A" in problem:
            total["Div3-A"] += 1
        elif "-A" in problem:
            total["Others-A"] += 1

        total_count += 1

for folder in CF_B:
    problems = os.listdir(pathB + "/" + folder)
    for problem in problems:
        if "D2-B" in problem:
            total["Div2-B"] += 1
        elif "D3-B" in problem:
            total["Div3-B"] += 1
        elif "-B" in problem:
            total["Others-B"] += 1
        total_count += 1

pprint.pprint(total)
print(total_count)
