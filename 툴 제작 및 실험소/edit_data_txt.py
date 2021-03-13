import os

now = os.getcwd()
txts = [d for d in os.listdir(now) if d[-4:] == '.txt']

for txt in txts:
    contents = []
    with open(txt, mode='r') as f:
        for content in f.readlines():
            label_number = content[:1]
            if label_number == '1':
                contents.append('0' + content[1:])
            elif label_number == '2':
                contents.append('1' + content[1:])
            elif label_number == '3':
                contents.append('2' + content[1:])

    with open(txt, mode='w') as f:
        f.writelines(contents)
    print(txt)
