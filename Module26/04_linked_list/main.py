from collections.abc import Iterable, Iterator


class LinkedList:
    """ Связный список """
    head = None

    class Node:
        """ Узел """
        element: int = None
        next_node: int = None

        def __init__(self, element: int, next_node=None) -> None:
            self.element = element
            self.next_node = next_node

    def append(self, element) -> int:
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    def get(self, index: int) -> int:
        i = 0
        node = self.head
        prev_node = None

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        return node.element

    def remove(self, index: int) -> int:
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        i = 0
        prev_node = node

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element

        del node
        return element

    def __str__(self) -> str:
        node = self.head
        temp = []
        while node.next_node:
            temp.append(node.element)
            node = node.next_node
        temp.append(node.element)
        return str(temp)



my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)


