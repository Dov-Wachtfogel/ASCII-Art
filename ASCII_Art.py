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
    if num == 0:
        return text
    conv_txt = ''
    lines = text.splitlines()
    for line in lines:
        conv_line = ''
        for l in line:
            try:
                conv_line += table[l][num - 1]
            except:
                conv_line += 'X'
        conv_txt += conv_line + '\n'
    return conv_txt[:-1]


def rotation(text: str, rot):
    if rot == 180:
        return rotation(text[::-1], 360)
    if rot == 270:
        return rotation(text[::-1], 90)
    lines = text.splitlines()
    rot_txt = ''
    if rot == 360:
        for line in lines:
            rot_txt += line[::-1]+'\n'
        return rot_txt[:-1:]
    if rot == 90:
        max_line = len(max(lines, key=lambda l: len(l)))
        rot_lines = ['']*max_line
        for line in lines:
            for i in range(max_line):
                try:
                    rot_lines[i]+=line[i]
                except:
                    rot_lines[i] += ' '
        for line in rot_lines:
            rot_txt += line[::-1] + '\n'
        return rot_txt[:-1:]



if __name__ == '__main__':
    f = open("python.txt", 'r')
    t = f.read()
    print(t)
    print(rotation(t, 360))
    #print(rotation(rotation(t, 360), 360))
