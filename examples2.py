def mode():
    l = list(map(int, input("Enter numbers separated by space: ").split()))
    frequencies = {}
    for number in l:
        frequencies[number] = frequencies.get(number , 0 )+1

    max_frequency = max(frequencies.values())
    modes = [number for number, frequency in frequencies.items() if frequency == max_frequency]
    
    return modes

print(mode())