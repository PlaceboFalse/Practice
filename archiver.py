from typing import List


class Archiver():

    def zip_stats(line: str) -> None:

        global stats
        global list_lett

        stats = {}
        list_lett = []

        for i in line:
            if i not in stats:
                stats[i] = 0
            stats[i] += 1

        list_lett = sorted(stats.keys())

    def found_letter(line: str, letter: str) -> List[int]:
        list_found = []

        for i in range(len(line)):
            if line[i] == letter:
                list_found.append(i)

        return list_found

    def zip_line(line: str) -> str:
        Archiver.zip_stats(line)
        line_arc = ''

        for i in list_lett:
            line_arc += i
        return line_arc

    def unzip(line: str, list_pos: List[int]) -> str:
        Archiver.zip_stats(line)

        pos = 0
        i = 0
        unzip_line = ''
        max_pos = len(list_pos)

        for i in range(len(list_pos)):
            for j in range(len(list_pos[i])):
                max_pos = max(max_pos, list_pos[i][j])

        while pos != max_pos + 1:

            i += 1
            if i >= len(list_pos):
                i = 0

            if len(list_pos[i]) == 0:
                continue

            if list_pos[i][0] == pos:
                unzip_line += list_lett[i]
                list_pos[i].pop(0)
                i = 0
                pos += 1

        return unzip_line


if __name__ == '__main__':

    files = open('start.txt')
    files_end = open('end.txt', 'w+')

    list_key = []
    # В txt файле в конце добовляется '\n'
    list_key.append([8])
    list_key.append([0, 1, 2, 3])
    list_key.append([4, 5, 6, 7])

    files_end.write(Archiver.unzip(files.read(), list_key))

    files.close()
    files_end.close()
