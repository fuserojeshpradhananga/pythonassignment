def convert_to_uppercase(string_list):
    return list(map(lambda x: x.upper(), string_list))


input_list = ["apple", "banana", "cherry", "date"]
result = convert_to_uppercase(input_list)
print(result)
