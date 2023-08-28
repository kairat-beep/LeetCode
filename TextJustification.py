class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [[]]
        last_sum = 0
        for word in words:
            if last_sum +  len(lines[-1])  + len(word) > maxWidth:
                last_sum = len(word)
                lines.append([word])
            else:
                lines[-1].append(word)
                last_sum += len(word)

        newStr = " ".join(lines[-1])
        lines[-1] = [newStr + " " * (maxWidth - len(newStr))]

        container = []

        for line in lines:
            gaps = max(0, len(line) - 1)
            left = maxWidth - sum([len(_) for _ in line])

            if gaps == 0:
                container.append(line[0] + " " * (maxWidth - len(line[0])))
                continue
            over = left % gaps
            temporal_line = []
            for i in line:
                spaces = int(left / gaps)
                if over > 0:
                    spaces += 1
                    over -= 1
                temporal_line.append(f'{i}{" "*spaces}')
            container.append("".join(temporal_line).strip())
        return container
