def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    print line
    group = []
    sub = ''
    if len(line) <= 1:
        return len(line)
    else:
        s = 0
        for i in range(1, len(line)):
            if line[i - 1] == line[i]:
                if i == len(line) - 1:
                    sub = line[s:]
                    group.append((sub, len(sub)))
                else:
                    continue
            else:
                sub = line[s:i]
                group.append((sub, len(sub)))
                if i == len(line) - 1:
                    group.append((line[i], 1))
                else:
                    s = i
        print group
        #print sorted(group, key=lambda x:x[1], reverse=True)[0][1]
        return sorted(group, key=lambda x:x[1], reverse=True)[0][1]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"