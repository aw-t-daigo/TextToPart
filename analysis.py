import MeCab
import subprocess


class Analyzer:
    __dicdir = subprocess.getoutput("mecab-config --dicdir")
    __tagger = MeCab.Tagger(f"-d {__dicdir}/mecab-ipadic-neologd")

    def __init__(self):
        self.node = None

    def parse_to_node(self, target):
        self.node = Analyzer.__tagger.parseToNode(target)

    def convert_to_part_line(self):
        if self.node is None:
            return None

        line = []
        while self.node:
            word = self.node.surface
            features = self.node.feature.split(',')
            part = features[0]
            part_detail1 = features[1] if features[1] != '*' else ''
            part_detail2 = features[2] if features[2] != '*' else ''

            if part in ['BOS/EOS', 'その他', 'フィラー', '記号']:
                line.append(word)
            else:
                s = f'[{part}:{part_detail1}:{part_detail2}]'
                line.append(s)

            self.node = self.node.next

        return ''.join(line)
