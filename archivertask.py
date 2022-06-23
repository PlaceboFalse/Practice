from typing import List


class ZipLine():

    def found_letter(line: str, letter: str) -> List[int]:
        list_let = []
        # print(line)
        for i in range(len(line)):
            if line[i] == letter:
                list_let.append(i)

        return list_let

    def archiver(line: str, list_lett: List[str]) -> str:

        line_arc = ''

        for i in list_lett:
            line_arc += i
        return line_arc

    def unzip(line: str, list_lett: List[str], list_pos: List[int]) -> str:

        pos = 0
        i = 0
        unzip_line = ''
        max_pos = len(list_pos)

        while pos != max_pos:

            i += 1
            if i >= 26:
                i = 0
            if len(list_pos[i]) == 0:
                continue

            max_pos = max(max_pos, list_pos[i][0])

            if list_pos[i][0] == pos:
                unzip_line += list_lett[i]
                list_pos[i].pop(0)
                i = 0
                pos += 1

        return unzip_line

    def main(line: str) -> str:
        letter_pos = []
        stats = {}
        for i in line:
            if i not in stats:
                stats[i] = 0
            stats[i] += 1

        sorted_stats = []
        sorted_stats = sorted(stats.keys())

        for i in sorted_stats:
            letter_pos.append(ZipLine.found_letter(line, i))

        zip_str = ZipLine.archiver(line, sorted_stats)
        # zip_str = ZipLine.unzip(zip_str, sorted_stats, letter_pos)
        return zip_str


if __name__ == '__main__':

    files = open('arctest.txt')
    files_end = open('end.txt', 'w+')

    files_end.write(ZipLine.main(files.read()))

    files.close()
    files_end.close()
