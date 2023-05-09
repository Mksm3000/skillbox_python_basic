class Stack:

    def __init__(self):
        self.__stack_list = list()

    def __str__(self):
        return '; '.join(self.__stack_list)

    def add(self, element):
        self.__stack_list.append(element)

    def delete(self):
        if len(self.__stack_list) == 0:
            return None
        return self.__stack_list.pop()


# my_stack = Stack()
#
# for index in range(10):
#     my_stack.add(index)
# print(my_stack)
#
# for _ in range(3):
#     my_stack.delete()
# print(my_stack)

class TaskManager:

    def __init__(self):
        self.task_dict = dict()

    def new_task(self, name, num):
        if num not in self.task_dict:
            self.task_dict[num] = Stack()
        self.task_dict[num].add(name)

    def __str__(self):
        print_list = []
        if self.task_dict:
            for i_key in sorted(self.task_dict.keys()):
                print_list.append(f'{str(i_key)}. {self.task_dict[i_key]}.\n')
        return ''.join(print_list)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
