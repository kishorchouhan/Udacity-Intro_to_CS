def split_string(source,splitlist):
    word_list = ['']
    at_split = False
    for char in source:
        if char in splitlist:
            at_split = True
        else:
            if at_split:
                # We've now reached the start of the word, time to make a new element in the list
                word_list.append(char) # This creates a new element in the array with the value of 'char'
                # Reset at_split so no more elements are created until we reach a new word
                at_split = False
            else:
                # Char is not in splitlist, and we're not at the start of a word, so simply concatenate
                # char with the last entry in word_list
                word_list[-1] = word_list[-1] + char

    # Once we've filled word list, we'll want to return the list containing all the words
    return word_list

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print (out)
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print (out)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
