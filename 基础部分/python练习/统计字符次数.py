def count_characters(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


string = "hello world"
character_count = count_characters(string)
print(character_count)
