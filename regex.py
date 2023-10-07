import re

text = "https://www.youtube.com/watch?v=fghdgfh fhjfhhfdgsgsfg https://youtu.be/erretrt?t=1"
result = re.finditer(r"https://(www\.youtube.com/watch\?v=|youtu\.be/)[a-zA-Z\d-]*(\?t=\d|&t=\d|)", text, re.MULTILINE)
print()
for item in result:
    print(item.group(0))