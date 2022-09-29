import os
from analysis import Analyzer


class PartText:
    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            self.lines = f.read().split(os.linesep)
        self.analyzer = Analyzer()

    def is_empty(self):
        return self.lines is None

    def part_line_generator(self):
        for line in self.lines:
            self.analyzer.parse_to_node(line)
            yield self.analyzer.convert_to_part_line()
