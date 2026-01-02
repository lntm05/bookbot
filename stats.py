def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    occurrences = {}
    for char in text:
        lchar = char.lower()
        if lchar in occurrences:
            occurrences[lchar] += 1
        else:
            occurrences[lchar] = 1
    return occurrences

def sort_on_num(items):
    return items["num"]

def sort_occurrences(occurrences):
    sorted_occurrences = []
    for k in occurrences:
        entry = {}
        entry["char"] = k
        entry["num"] = occurrences[k]
        sorted_occurrences.append(entry)
    sorted_occurrences.sort(reverse=True, key=sort_on_num)
    return sorted_occurrences    