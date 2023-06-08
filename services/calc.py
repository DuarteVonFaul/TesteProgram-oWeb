def roman_to_arabic(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_numeral = 0
    previous_value = 0
    repetitions = 0

    for numeral in roman_numeral[::-1]:
        value = roman_values[numeral]

        if value > previous_value:
            arabic_numeral += value
            repetitions = 0
        elif value == previous_value:
            if repetitions >= 2:
                raise ValueError("Numeral Romano Invalido")
            arabic_numeral += value
            repetitions += 1
        else:
            arabic_numeral -= value
            repetitions = 0

        previous_value = value

    return arabic_numeral

def arabic_to_roman(arabic_numeral):
    if not (0 < arabic_numeral < 4000):
        raise ValueError("Numeral Arabico devem ser entre 0 e 3999")

    roman_values = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    roman_numeral = ''
    for value, numeral in roman_values.items():
        while arabic_numeral >= value:
            roman_numeral += numeral
            arabic_numeral -= value

    return roman_numeral