class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val_stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.val_stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        top = self.val_stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    # stack = MinStack()
    # stack.push(10)
    # stack.push(11)
    # stack.push(9)
    # stack.push(7)
    # stack.push(13)
    # assert stack.top() == 13
    # assert stack.min() == 7
    # stack.pop()
    # assert stack.top() == 7
    # assert stack.min() == 7
    # stack.pop()
    # assert stack.top() == 9
    # assert stack.min() == 9

    stack = MinStack()
    stack.push(0)
    stack.push(1)
    stack.push(0)
    assert stack.min() == 0
    stack.pop()
    assert stack.min() == 0