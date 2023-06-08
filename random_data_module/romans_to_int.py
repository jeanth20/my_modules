"""
Roman numerals to integer value
"""

ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }


def roman_to_int(roman: str) -> int:
    """
    Convert a roman numeral to an integer
    """
    result = 0
    for i, c in enumerate(roman):
        if (i + 1) == len(roman) or ROMAN_NUMERALS[c] >= ROMAN_NUMERALS[roman[i + 1]]:
            result += ROMAN_NUMERALS[c]
        else:
            result -= ROMAN_NUMERALS[c]
    return result


TEST_CASES = [
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("LVIII", 58),
    ("XCIX", 99),
    ("MCMXCIV", 1995), #flase 1994
]

for test_case, expected in TEST_CASES:
    result = roman_to_int(test_case)
    print(result == expected, result)

