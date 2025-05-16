
def count_words(text):
    return len(text.split())

def count_chars(text):
    result = {}
    for char in text:
       char = char.lower()
       if char in result:
        result[char] += 1
       else:
        result[char] = 1
    return result

def sorted_char_count(count_chars):
    result = []
    for c, v in count_chars.items():
        char_dict = {"char": c, "num": v}
        result.append(char_dict)
    result.sort(reverse=True, key=lambda x: x["num"])
    return result



