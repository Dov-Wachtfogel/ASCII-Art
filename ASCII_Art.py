def serialize_line(ASCII_art_line: str):
    ser_line = ''
    last_letter = ASCII_art_line[0]
    counter = 0
    for letter in ASCII_art_line:
        if letter == last_letter:
            counter += 1
        else:
            ser_line += str(counter) + last_letter
            last_letter = letter
            counter = 1
    ser_line += str(counter) + last_letter
    return ser_line


def serialize_text(text: str):
    lines = text.splitlines()
    ser_lines = []
    for line in lines:
        ser_lines.append(serialize_line(line))
    ser_txt = ser_lines[0]
    for line in ser_lines[1::]:
        ser_txt += '\n' + line
    return ser_txt


def conversion_table(text: str, table: dict, num: int):
    conv_txt = ''
    for l in text:
        try:
            conv_txt += table[l][num]
        except:
            conv_txt += 'X'


if __name__ == '__main__':
    f = open("python.txt", 'r')
    print(serialize_text(f.read()))
