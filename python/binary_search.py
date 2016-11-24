

def binary_search(slist, item):
    first = 0
    last = len(slist)
    found = False

    while first < last and not found:
        middle = (first+last) // 2
        if slist[middle] == item:
            found = True
        else:
            if slist[middle] < item:
                first = middle
            else:
                last = middle
    return found
    


if __name__ == '__main__':
    print binary_search(list(range(21)), 13)
    print binary_search([1], 1)
    print binary_search([3,4], 2)
