"""day 10"""

from typing import List, Optional


class CorruptedError(BaseException):
    pass


class Chunks:
    def __init__(self, filepath: str = "./data/day10_sample.txt"):
        self.lines = self.read_data(filepath)
        # bracket, paranthesis, curly, sharp
        self.values = {"p": 3, "b": 57, "c": 1197, "s": 25137}
        self.closure_values = {")": 1, "]": 2, "}": 3, ">": 4}
        self.illegal_characters = {"]": 57, ")": 3, "}": 1197, ">": 25137}
        self.score = 0
        self.scores: List[int] = []
        self.incomplete_chunks: List[Chunk] = []
        self.fixes: List[str] = []

    def read_data(self, filepath: str) -> List[str]:
        with open(filepath, "r") as f:
            data = [x.strip() for x in f.readlines()]

        return data

    def check(self) -> None:
        for i, line in enumerate(self.lines):
            chunk: Chunk = Chunk(line, i)
            try:
                status = chunk.run()
            except CorruptedError:
                status = None
            if status == "Incomplete":
                self.incomplete_chunks.append(chunk)
            else:
                value = self.illegal_characters[chunk.illegal_character]
                self.score += value
        print("Done")

        return None

    def get_middle_score(self):
        scores: List[int] = []
        for chunk in self.incomplete_chunks:
            score = 0
            for char in reversed(chunk.key):
                score = score * 5 + self.closure_values[char]
            scores.append(score)
        self.scores = sorted(scores)
        return self.scores[len(self.scores) // 2]


class Chunk:
    def __init__(self, line: str, idx: int):
        self.line = line
        self.is_valid = True
        self.direction_map = {
            "[": "open",
            "]": "closed",
            "(": "open",
            ")": "closed",
            "{": "open",
            "}": "closed",
            "<": "open",
            ">": "closed",
        }

        self.closures = {"[": "]", "(": ")", "{": "}", "<": ">"}
        self.key: List[str] = []
        self.illegal_character: Optional[str] = None
        self.idx = idx
        self.score = 0

    def run(self):
        for x in self.line:
            self.check_character(x)

        return "Incomplete"

    def check_character(self, x: str) -> None:
        if self.direction_map[x] == "open":
            self.open(x)
        else:
            self.closed(x)

    def open(self, x: str) -> None:
        self.key.append(self.closures[x])

    def closed(self, x: str) -> None:
        if self.key[-1] == x:
            self.key = self.key[:-1]
            return None
        else:
            print(f"Expected {self.key[-1]}, but found {x} instead.")
            self.illegal_character = x
            raise CorruptedError

    def calculate_score(self):
        pass
