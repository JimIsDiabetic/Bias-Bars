"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""

def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    with open(filename) as f:
      lines = f.readlines()
    text = ' '.join(lines)

    text = text.strip()
    text = text.split('\n')
    
    for i in range(0, len(text)):
        text[i] = text[i].split(',')
        for j in range(0, len(text[i])):
           text[i][j] = text[i][j].strip()
    
    text.pop(0)

    total_men = 0
    total_women = 0
    high_men = 0
    high_women = 0

    for i in range(0, len(text)):
        if text[i][1] == 'M':
            total_men += 1
            if float(text[i][0]) > 3.5:
                high_men += 1
        elif text[i][1] == 'W':
            total_women += 1
            if float(text[i][0]) > 3.5:
                high_women += 1

    high_men_percentage = round((high_men / total_men) * 100)
    high_women_percentage = round((high_women / total_women) * 100)

    print(f'{high_men_percentage}% of reviews for men in the dataset are high.')
    print(f'{high_women_percentage}% of reviews for women in the dataset are high.')

    pass


def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)

if __name__ == '__main__':
    main()