# http://www.azalea.com/upc/check-digit/
# https://en.wikipedia.org/wiki/Check_digit#UPC
#
# 1. Add the digits in the odd-numbered positions (first, third, fifth, etc.) together.
# 2. Multiply that number by three.
# 3. Add the digits in the even-numbered positions (second, fourth, sixth, etc.) to the result.
# 4. Find the result modulo 10 (i.e. the remainder when the result is divided by 10).
# 5. If the result is not zero, subtract the result from ten.
#
# There are two scenarios:
# A. Given a UPC code not including the last digit, calculate the last digit.
# B. Given a UPC code that includes the check digit, verify that it's correct.

def calculate_check_digit(upc_code):
  pass


def verify_upc_code(upc_code):
  pass
