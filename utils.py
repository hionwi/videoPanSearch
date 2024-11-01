import re


def extract_code(text):
    match = re.search(r'提取码：(\w{4})', text)
    if match:
        return match.group(1)
    match = re.search(r'提取码:(\w{4})', text)
    if match:
        return match.group(1)
    return None


def extract_https_links(text):
    https_links = re.findall(r'https://\S+', text)
    return https_links