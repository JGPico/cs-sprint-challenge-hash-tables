def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    output = []

    for item_with_index in enumerate(weights):
        dictionary[item_with_index[1]] = item_with_index[0]

    for item in weights:
        if (limit-item) in dictionary:
            if limit-item > item:
                output.append(dictionary[limit-item])
                output.append(dictionary[item])
                return output
            elif (limit - item) < item:
                output.append(dictionary[item])
                output.append(dictionary[limit-item])
                return output
            else:
                output.append(1)
                output.append(0)
                return output


# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

# print("my test", answer_4)
