import string
def count_words(text,words):
    """
     Count how many words are included in the given text
    """
    count = 0
    temp = text.lower()
    list = words.split(',')
    print(list)
    for i in range(len(list)):
        if list[i] in temp:
            count = count + 1
    return count

text = raw_input("Enter a text: ")
words = raw_input("Enter a set of words seperated by comma: ")
result = count_words(text,words)
print(result)