""" Top N items.
Given a list of words, find the top <N> words that occur the maximum time and their values. 

i.e input = ["sam", "cam", "dam", "sam", "dam", "dam", "cam", "blah"]  

N = 3

output = {"dam": 3, "sam": 2, "cam":2}

1. Write a function that takes a list of strings and an integer value N that returns the correct output

2. Describe the algorithmic runtime of the function.

3. Write a test case to validate this function

4. Discuss corner cases.
"""
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

"""

def top_n_items(data, N):
  # return a dictionary with N items where they key is the word and the value is the count.
	result = dict()
  n = 0
  for word in data:



result = {}
for k in data:
  result[k] = result.get(k, 0) + 1

top_keys = sorted(result, key=lambda x: result[x])
clean_result = {}
for k in top_keys[:N]:
  clean_result[k] = result[k]



 Random Sampling
Given CSV file <F> with <N> rows, generate an output file with a raondom selection of <K> rows.
"""