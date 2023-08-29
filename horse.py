def preprocess_bad_character_table(pattern):
    table = {}
    pattern_length = len(pattern)

    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - 1 - i

    return table

def horsepool_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    bad_char_table = preprocess_bad_character_table(pattern)
    i = pattern_length - 1

    while i < text_length:
        k = 0

        while k < pattern_length and pattern[pattern_length - 1 - k] == text[i - k]:
            k += 1

        if k == pattern_length:
            return i - pattern_length + 1

        if text[i] in bad_char_table:
            shift = bad_char_table[text[i]]
        else:
            shift = pattern_length

        i += shift

    return -1

if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")

    position = horsepool_search(text, pattern)

    if position != -1:
        print(f"Pattern found at position {position}")
    else:
        print("Pattern not found in the text")


# output:


#Enter the text: The quick brown fox jumps over the lazy dog.
#Enter the pattern to search: jumps
#Pattern found at position 21