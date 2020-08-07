def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    dictionary = {}
    result = []

    for number in a:
        if abs(number) in dictionary and dictionary[abs(number)] == 1:
            dictionary[abs(number)] += 1
            result.append(abs(number))
        else:
            if abs(number) in dictionary:
                dictionary[abs(number)] += 1
            else:
                dictionary[abs(number)] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
