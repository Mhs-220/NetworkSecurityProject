import re

def escape_sql_injection(text):
    return re.sub(r"(\\*)'", r"''", text)