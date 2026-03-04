import re

def companies(cemail):
    pattern = r'(?<=@)(?:\w+)(?=\.)'
    domains = [
        re.search(pattern, email).group() for email in cemail
    ]

    return set(domains)



def empIDs(fullID):
    pattern = r'^(?P<department>[A-Z]+)-(?P<emp_id>\d+)$'
    emp_ids = [
        re.match(pattern, items).group("emp_id") 
        for items in fullID
        if re.match(pattern, items)
    ]

    return emp_ids

def positive_lookahead(task):
    pattern = r'(?=Project Flow:)(.*$)'
    results = [
        re.search(pattern, items).group(1) 
        for items in task
        if re.search(pattern, items)
    ]

    return results



def negative_lookahead(task):
    pattern = r'^(?!Project Brave:)(.*$)'
    results = [
        re.search(pattern, items).group(1)
        for items in task
        if re.search(pattern, items)
    ]

    return results

def positive_lookbehind(report):
    pattern = r'(?<=syntax errors).*'
    results = [
        items
        for items in report
        if re.search(pattern, items, flags = re.IGNORECASE)
    ]

    return results

def negative_lookbehind(report):
    pattern = r"(?<!errors\s)build-time"
    results = [
        items
        for items in report
        if not re.search(pattern, items, flags = re.IGNORECASE)
    ]

    return results