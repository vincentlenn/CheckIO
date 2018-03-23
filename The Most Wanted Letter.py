import string

# my original solution
def checkio(text):
    "The most frequent letter in lower case in a string."
    count = {}
    string = str.lower(text)
    for letter in string:
        if not str.isalpha(letter):
            continue
        else:
            if count.__contains__(letter):
                count[letter] = count[letter] + 1
            else:
                count[letter] = 1
    print(count)
    s = sorted(count.items(), key=lambda x:x[1], reverse=True)
    print(s)
    list = []
    list.append(s[0][0])
    for index in range(len(s)-1):
        if s[0][1] > s[1][1]:
            list.pop(0)
            break
        elif s[index][1] > s[index+1][1]:
            break
        else:
            list.append(s[index+1][0])
    if list:
        list.sort()
        return list[0]
    else:
        return s[0][0]

# the best solution
def max_count(text):
    """
        We iterate through latyn alphabet and count each letter in the text.
        Then 'max' selects the most frequent letter.
        For the case when we have several equal letter,
        'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

data = raw_input("Please input string: ")
re = max_count(data)
print(re)