from typing import List


class CQueue:

    def __init__(self):
        self.stack: List[int] = []

    def appendTail(self, value: int) -> None:
        tmp_stack: List[int] = []
        for _ in range(len(self.stack)):
            tmp_stack.append(self.stack.pop())
        self.stack.append(value)
        for _ in range(len(tmp_stack)):
            self.stack.append(tmp_stack.pop())
        return None


    def deleteHead(self) -> int:
        return -1 if len(self.stack) == 0 else self.stack.pop()


if __name__ == '__main__':
    queue = CQueue()
    queue.appendTail(3)
    assert queue.deleteHead() == 3
    assert queue.deleteHead() == -1
    queue.appendTail(5)
    queue.appendTail(2)
    assert queue.deleteHead() == 5
    assert queue.deleteHead() == 2
