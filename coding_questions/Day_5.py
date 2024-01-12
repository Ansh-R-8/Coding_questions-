'''Q Create a function eq_all that determines if all elements of any iterable are equal; the iterable may be infinite. Return value is a bool.

Examples
eq_all('aaa')   : True
eq_all('abc')   : False
eq_all('')      : True

eq_all([0,0,0]) : True
eq_all([0,1,2]) : False
eq_all([])      : True'''

# code
def eq_all(iterable):
    # iter() to create an iterator from the iterable
    iterator = iter(iterable)
    
    try:
        ref_val = next(iterator)
    except StopIteration:
        # If the iterable is empty, return True
        return True
    return all(element == ref_val for element in iterator)


'''Q Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.'''

#code
class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                      90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        result= ''
        for value, numeral in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
            while val >= value:
                result += numeral
                val -= value
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for numeral in reversed(roman_num):
            value = roman_numerals[numeral]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result
        

