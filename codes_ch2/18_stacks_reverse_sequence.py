class Text:
    def __init__(self):
        self.stack = []

    def read_file(self, filename):
        print('input:')

        with open(filename) as fid:
            for line in fid:
                print(line.strip())
                self.stack.append(line.strip())

        print()
        fid.closed

    def reverse_lines(self):
        print('output:')

        while len(self.stack) > 0:
            print(self.stack.pop())


if __name__ == '__main__':
    t = Text()
    t.read_file('stacks_text.txt')
    t.reverse_lines()
