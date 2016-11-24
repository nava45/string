

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
    

def recursive_binary_search(slist, item):
    first = 0
    last = len(slist)
  
    middle = (first+last) // 2

    if not slist:
        return False

    if slist[middle] == item:
        return True
    else:
        if slist[middle] < item:
            return recursive_binary_search(slist[middle:], item)
        else:
            return recursive_binary_search(slist[:middle], item)
    return False
  


if __name__ == '__main__':
    print binary_search(list(range(21)), 13)
    print binary_search([1], 1)
    print binary_search([3,4], 2)

    print recursive_binary_search(list(range(21)), 13)
    print recursive_binary_search([1], 1)
    print recursive_binary_search([3,4], 2)
