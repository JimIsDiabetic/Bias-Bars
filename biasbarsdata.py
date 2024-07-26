"""
File: biasbarsdata.py
------------------
Add your comments here
"""

KEY_WOMEN = "W"
KEY_MEN = "M"

def convert_rating_to_index(rating):
    if rating < 2.5:
        return 0
    elif rating > 3.5:
        return 2
    else:
        return 1

def add_data_for_word(word_data, word, gender, rating):
    if word not in word_data:
        word_data[word] = {
            KEY_WOMEN: [0, 0, 0],
            KEY_MEN: [0, 0, 0]
        }

    word_data[word][gender][convert_rating_to_index(rating)] += 1

    return word_data

def read_file(filename):
    with open(filename) as f:
      lines = f.readlines()
    text = ''.join(lines)

    text = text.strip()
    text = text.split('\n')

    for i in range(len(text)):
        text[i] = text[i].split(',')
        text[i][2] = text[i][2].split()

    text.pop(0)

    word_data = {}

    for i in range(len(text)):
        for j in range(len(text[i][2])):
            add_data_for_word(word_data, text[i][2][j], text[i][1], float(text[i][0]))
    
    return word_data

def search_words(word_data, target):
    word_data_list = list(word_data.items())

    list_of_search_words = []
    for i in range(len(word_data_list)):
        if target.lower() in word_data_list[i][0].lower():
            list_of_search_words.append(word_data_list[i][0])

    return list_of_search_words

def print_words(word_data):
    """
    (This function is provided for you)
    Given a word_data dictionary, print out all its data, one word per line.
    The words are printed in alphabetical order,
    with the corresponding frequency data displayed in order
    of associated review quality for each gender.

    This code makes use of the sorted function, which is given as input a 
    list of elements and returns a list containing the same elements sorted in
    increasing order. For strings, "increasing" order maps to alphabetical 
    ordering.

    Input:
        word_data (dictionary): a dictionary containing word frequency data organized by gender and rating quality
    """
    for key, value in sorted(word_data.items()):
        print(key, end=" ")
        for gender, counts in sorted(value.items()):
            print(gender, counts, end=" ")
        print("")
        
    pass


def main():
    # (This function is provided for you)
    import sys
    args = sys.argv[1:]

    if len(args) == 0: return
    # Two command line forms
    # 1. data_file
    # 2. -search target data_file

    # Assume no search, so filename to read
    # is the first argument
    filename = args[0]

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filename = args[2]  # Update filename to skip first 2 args

    # Read in the data from the file name
    word_data = read_file(filename)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_words(word_data, target)
        for word in search_results:
            print(word)
    else:
        print_words(word_data)


if __name__ == '__main__':
    main()