# note: this should be much more functional rather than procedural in style... 

import os

# find all end marks
# if not ellipses, mark for newline insertion

end_marks = ['.', '!', '?']
file_name = 'file-object_parsing-and-printing_sample-text.txt' 

t = open(f'{os.getcwd()}/{file_name}', mode='r')
text = t.readlines()

# print('\nHITS & ADJACENCIES\n') # DEBUG
for i, line in enumerate(text):
    newline_index = []

    for j, char in enumerate(line):
        if char in end_marks:
            prev_char = None
            next_char = None

            if j > 0:   #not first character
                prev_char = line[j-1]

            if j < len(line) - 1:   #not last character
                next_char = line[j+1]

            if '.' not in (prev_char, next_char):
                newline_index.append(j)
    
    for k in newline_index[::-1]:
        if k < len(text[i]) - 2: # -2 because existing line ends don't need fixing
            newline_char = '\n'
            # newline_char = '🦀' # DEBUG

            pre_split   = text[i][:k+1]
            post_split  = text[i][k+1:][1:]
            text[i]     = f'{pre_split}{newline_char}{post_split}'

[print(f'{_}', end='') for _ in text]

print('\n')
t.close()