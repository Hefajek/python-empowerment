def extract(text):
    content = ''
    index = 1

    for elem in text:
        try:
            if text[index-1] == ">":
                while text[index+1] != "<":
                    content += text[index]
                    index += 1
            if text[index+1] == "<":
                content += text[index]
                content = content.strip()
                content += '\n'
        except:
            continue
        index += 1
    print(content.strip())

with open('html.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    for line in text:
        line.strip()
    extract(text)
