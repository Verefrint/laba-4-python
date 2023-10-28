import re
def read_html_file(filename):
    with open(filename, 'r') as f:
        html_string = f.read()
    return html_string

def parse_all_emails(html_string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, html_string)

html_string = read_html_file('example.html')
print("html file:")
print("------------------------------------")
print(html_string)
print("------------------------------------")
print(parse_all_emails(html_string))