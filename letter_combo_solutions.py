def letter_combinations(digits):
    if digits == "":
        return []
    string_maps = {
        "1": "abcdefghijklmnopqrstuvwxy",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

digit_string = ("19")
print(letter_combinations(digit_string))
digit_string = "12"
print(letter_combinations(digit_string))
