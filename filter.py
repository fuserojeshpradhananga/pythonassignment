def filter_long_strings(string_list):
    return list(filter(lambda x: len(x) > 5, string_list))


input_list = ["apple", "banana", "cherry", "date", "grapes", "kiwi"]
result = filter_long_strings(input_list)
print(result)
