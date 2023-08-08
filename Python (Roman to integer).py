#Roman to Integer:

def roman_to_integer(s):
    roman_numerals = {
        'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    total = 0
    prev_value = 0
    for char in s:
        value = roman_numerals[char]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total
# Examples:
print(roman_to_integer("III"))  # Output: 3
print(roman_to_integer("LVIII")) # Output: 58
print(roman_to_integer("MCMXCIV")) # Output: 1994
