def non_unique(data):
    """
        A non-empty list of integers(X) is given,
        this function will remove all unique elements and
        return a list consisting of only the non-unique elements
    """
    list = []
    #data = data.replace(" ","")
    for i in range(len(data)):
        num = data.count(data[i])
        if num > 1:
            list.append(data[i])
    return list

data = input("Enter a non-empty list of integers: ")
print(non_unique(data))