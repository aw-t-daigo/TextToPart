import sys
from part_text import PartText

args = sys.argv

if len(args) <= 1:
    print('Error! ファイル名が必要です', file=sys.stderr)
    sys.exit(1)

file_name = args[1]
part_text = PartText(file_name)

if part_text.is_empty():
    print('Error! ファイルが読み込めなかったか、空でした', file=sys.stderr)
    sys.exit(1)

part_lyric_lines = [line for line in part_text.part_line_generator()]

for lyric_line in part_lyric_lines:
    print(lyric_line)
