from typing import List


class LinkedList:
    class Node:
        def __init__(self, val: int):
            self.data = val
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(index):
            current = current.next

        return current.data

    def insertHead(self, val: int) -> None:
        new_node = self.Node(val)
        new_node.next = self.head
        self.head = new_node

        if self.size == 0:
            self.tail = new_node

        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = self.Node(val)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        # Removing the head
        if index == 0:
            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None

            return True

        # Find the node before the one being removed
        previous = self.head

        for _ in range(index - 1):
            previous = previous.next

        removed = previous.next
        previous.next = removed.next

        # If removing the tail, update tail
        if removed == self.tail:
            self.tail = previous

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values