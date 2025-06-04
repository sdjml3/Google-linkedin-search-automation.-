#AIM-->(1) the numbers of words should not be less than 40
# (2) the  company profile must contain the name of the company name
# (3) validation must be carried out to check the result.
# (4) the output must cannot be Null so must contain some value or response code.
import re
import time


def count_words(param):
    time.sleep(0.5)
    words=re.findall(r'\w+',param)
    if len(words)<33:
        time.sleep(0.5)
        return 'insufficient words'
    else:
        time.sleep(0.5)
        words=str(len(words))
        return words

def null_values_in_industry_code(industry_code):
    if len(str(industry_code))==0:
        return 'Absent'
    else:
        return 'Present'