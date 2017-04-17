from colorama import Fore

print(Fore.LIGHTYELLOW_EX)
data = ["sam", "cam", "dam", "sam", "dam", "dam", "cam", "blah"]
result = dict()
for word in data:
    result[word] = result.get(word, 0) + 1

top_keys = sorted(result, key=lambda x: result[x])
clean_result = {}
for k in top_keys[:3]:
    clean_result[k] = result[k]

print(result)
print(Fore.GREEN)
print(clean_result)

def top_n_items(data, N):
    from colorama import Fore
    print(Fore.LIGHTYELLOW_EX)
    data = ["sam", "cam", "dam", "sam", "dam", "dam", "cam", "blah"]
    result = dict()
    for word in data:
        result[word] = result.get(word, 0) + 1

    top_keys = sorted(result, key=lambda x: result[x])
    clean_result = {}
    for k in top_keys[:N]:
        clean_result[k] = result[k]

    print(result)
    return result