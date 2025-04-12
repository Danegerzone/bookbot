def word_count(text): # the "text" input will be defined and called in main.py
    words = text.split() # split() function takes the text string and creates a list of all the individual words
    return len(words) # the len() takes the split() output words list and the total length of the list (which is the same as the total # of words) is returned

# word_count function returns the word count of a string ("text") and takes that string as input

def count_chars(text): # text input will be defined and called in main.py
    char_counts = {} # initializes an empty dictionary to add to later in the function
    
    for char in text.lower(): # adding the .lower() function inline here automatically filters out capital letter duplicates from the count
        if char in char_counts: # checks if the character is already in our primary dictionary
            char_counts[char] += 1 # if the key char is already found, the count is incremented by 1
        else:
            char_counts[char] = 1 # if key char is not found, it is added to the dictionary with an initial value of 1
    return char_counts 

# count_chars returns the char_counts dictionary after the for loop is completed, taking the "text" string as input

def sort_char_dict(char_dict): # function sorts the dictionary created in count_chars() function, takes the dictionary from count_chars as input
    sorted_list = [] # intializes an empty list to add new two key-value dictionary pairs to

    for char, count in char_dict.items(): # iterates through the character dictionary using the .items() function to separate keys and values
        if char.isalpha(): # if statement checks that char is an alpha character to filter out non-alpha characters
            char_pair = {"char": char, "count": count} # creates a two key-value pair dictionary where char is key1 and count is key2
            sorted_list.append(char_pair)

    def sorter(list): # sorter function takes the sorted list as input
        return list["count"] # and returns the "count" key as output
    
    sorted_list.sort(reverse=True, key=sorter) # uses the sort() function and the sorter() function to organize the list of characters -- reverse=True makes it work from highest to lowest

    return sorted_list

