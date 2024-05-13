def count_vowels(text):
    vowels = "AEIOUaeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "AEIOU222222!"
num_vowels = count_vowels(text)
print("Number of vowels:", num_vowels)
