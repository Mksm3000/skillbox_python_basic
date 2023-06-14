
def singleton(cls):
    def wrapper():
        pass
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)


# Результат:
# ```
# 1986890616688
# 1986890616688
# True
