def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # key is the number, value is the number of times it appears
    dictionary = {}
    result = []

    # for number in a:

    #     if number not in dictionary:
    #         dictionary[number] = 1

    #     if number in dictionary and (number * -1) in dictionary and dictionary[number] == 1:
    #         dictionary[(number * -1)] += 1
    #         dictionary[number] += 1
    #         result.append(abs(number))

    for number in a:
        if abs(number) in dictionary and dictionary[abs(number)] == 1:
            dictionary[abs(number)] += 1
            result.append(abs(number))
        else:
            if abs(number) in dictionary:
                dictionary[abs(number)] += 1
            else:
                dictionary[abs(number)] = 1

    print("my result", result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
