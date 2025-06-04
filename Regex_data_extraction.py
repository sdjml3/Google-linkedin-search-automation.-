import re
from email.contentmanager import raw_data_manager


def extract_industry_code(raw_data):
    pattern_for_industry_code=r'[$**](\b\d{3}\b)|[$:]( \b\d{3}\b)|[$**]( \b\d{3}\b)|[$**]( `\b\d{3}\b)|(\b\d{3}\b)[-$]|[$:]( `\b\d{3}\b)'
    match=re.search(pattern_for_industry_code,raw_data)
    if match:
        extract_code=match.group(1) or match.group(2) or match.group(3) or match.group(4) or match.group(5) or match.group(6)
        return int(extract_code)
    
def extract_company_profile(raw_data):
    pattern_for_company_profile=r'(^[\w+]+.+?\n)|[$:].+?[$*]([^w/+]+.+?\n)'
    match=re.search(pattern_for_company_profile,raw_data)
    if match:
        extract_profile=match.group(1) or match.group(2)
        return extract_profile


