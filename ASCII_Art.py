import csv


def serialize_line(ASCII_art_line: str):
    if len(ASCII_art_line) == 0:
        return ''
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
            rot_txt += line[::-1] + '\n'
        return rot_txt[:-1:]
    if rot == 90:
        max_line = len(max(lines, key=lambda l: len(l)))
        rot_lines = [''] * max_line
        for line in lines:
            for i in range(max_line):
                try:
                    rot_lines[i] += line[i]
                except:
                    rot_lines[i] += ' '
        for line in rot_lines:
            rot_txt += line[::-1] + '\n'
        return rot_txt[:-1:]


def deserialize_line(line: str):
    for i in range(1, len(line)):
        if not line[i].isdigit():
            return line[i] * int(line[:i]) + deserialize_line(line[i + 1::])
    return ''


def deserialize(txt: str):
    lines = txt.splitlines()
    des_txt = ''
    for line in lines:
        des_txt += deserialize_line(line) + '\n'
    return des_txt[:-1:]


def csv_to_convert_table(csv_path: str):
    csv_file = open(csv_path, 'r')
    csv_reader = csv.reader(csv_file, delimiter=',')
    dict_table = {}
    for row in csv_reader:
        dict_table[row[0]] = list(row[1:])
    return dict_table


def main():
    to_serialize = False
    to_rotate = False
    to_convert = False
    table = csv_to_convert_table('convertion_table.csv')
    a = input('serialize / deserialize (s / d): ')
    if not a in ['serialize', 'deserialize', 's', 'd']:
        print('unknown action, try again')
        main()
        return None
    file_path = input("please enter file's path: ")
    try:
        f = open(file_path, 'r')
        txt = f.read()
        f.close()
    except:
        print('file not found, try again')
        main()
        return None
    r = input('rotate image? (True / False): ')
    while not r in ['T', 'F', 'True', 'False']:
        r = input('illegal answer, try again: \n rotate image? (True / False): ')
    if 'T' in r:
        to_rotate = True
        rotation_angle = input('enter rotate angle: ')
        while not rotation_angle in ['90', '180', '270', '360']:
            rotation_angle = input('illegal angle, try again \nenter rotate angle: ')
        rotation_angle = int(rotation_angle)
    c = input('convert image? (True / False): ')
    while c not in ['T', 'F', 'True', 'False']:
        c = input('illegal answer, try again: \n convert image? (True / False): ')
    if 'T' in c:
        to_convert = True
        conversion = input('enter conversion: ')
        while not conversion.isdigit():
            conversion = input('illegal conversion, try again \nenter conversion ')
        conversion = int(conversion)
    if to_serialize:
        if to_convert:
            txt = conversion_table(txt, table, conversion)
        if to_rotate:
            txt = rotation(txt, rotation_angle)
        ser_txt = serialize_text(txt)
        f = open(file_path + '.saa', 'w')  # saa = serialized ASCII art
        f.write(ser_txt)
        f.close()
        print('the file saved as ' + file_path + '.saa')
    if not to_serialize:
        txt = deserialize(txt)
        if to_convert:
            txt = conversion_table(txt, table, conversion)
        if to_rotate:
            txt = rotation(txt, rotation_angle)
        new_path = file_path + '.ASCIIart'
        if file_path[-4:] == '.saa':
            new_path = file_path[:-4]

        f = open(new_path, 'w')  # saa = serialized ASCII art
        f.write(txt)
        f.close()
        print('the file saved as ' + new_path)


if __name__ == '__main__':
    main()
