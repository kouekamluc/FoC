def most_frequent(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    most_freq_num = max(freq_dict, key=freq_dict.get)
    return most_freq_num

numbers = [64, 34, 25, 11,12, 22, 11, 90, 34, 25, 11]
print(most_frequent(numbers))