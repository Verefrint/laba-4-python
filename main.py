import re
def read_html_file(filename):
    with open(filename, 'r') as f:
        html_string = f.read()
    return html_string



html_string = read_html_file('example.html')
print("html file:")
print("------------------------------------")
print(html_string)
print("------------------------------------")
print(parse_all_emails(html_string))