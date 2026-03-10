num_to_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety", 
    100: "hundred",
    1000: "thousand"
}

def num_to_str(num: int) -> str:
    if num < 20:
        return num_to_word[num]
    
    if num < 100:
        if num % 10 != 0:
            return num_to_word[(num // 10) * 10] + "-" + num_to_word[num % 10]
        else:
            return num_to_word[num]
    
    if num % 1000 == 0:
        return num_to_word[num / 1000] + " " + "thousand"
    
    if num % 100 == 0:
        return num_to_word[num / 100] + " " + "hundred"

    # 3 digits
    num_in_str = str(num)
    
    return num_to_str(int(num_in_str[0]) * 100) + " and " + num_to_str(int(num_in_str[1:]))
    
def count_letters(s: str) -> int:
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
        
    return count

total = 0
for num in range(1, 1001):
    total += count_letters(num_to_str(num))

print(total)