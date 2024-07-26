"""
File: data_analysis.py
----------------------
This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""


def load_data(filename):

    with open(filename) as f:
      lines = f.readlines()
    text = ' '.join(lines)

    text = text.strip()
    text = text.split('\n')

    for i in range(0, len(text)):
        text[i] = text[i].split(',', 1)
        text[i][0] = text[i][0].strip()
        while ' ' in text[i][1]:
            text[i][1] = text[i][1].replace(' ', '')
        text[i][1] = text[i][1].split(',')
        for j in range(len(text[i][1])):
            text[i][1][j] = int(text[i][1][j])
    
    dictionary = {}

    for i in range(0, len(text)):
        dictionary[text[i][0]] = text[i][1]

    return dictionary



def daily_cases(cumulative):

    cumulative = list(cumulative.items())
    
    for i in range(len(cumulative)):
        for j in range(len(cumulative[i][1]) - 1, 0, -1):
            cumulative[i][1][j] -= cumulative[i][1][j - 1]
    
    cumulative = dict(cumulative)

    return cumulative


def main():
    filename = 'data/disease1.txt'

    data = load_data(filename)
    print(f"Loaded datafile {filename}:")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()
