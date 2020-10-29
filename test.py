# BLANK = " "
# CORNER = "+"
# HORIZONTAL = "-"
# VERTICAL = "|"
#
#
# def _create_rectangle(width, height, fill):
#     rows = [[fill for _ in range(width)] for _ in range(height)]
#     for x in range(1, width - 1):
#         rows[0][x] = HORIZONTAL
#         rows[height - 1][x] = HORIZONTAL
#     for y in range(1, height - 1):
#         rows[y][0] = VERTICAL
#         rows[y][width - 1] = VERTICAL
#     for y, x in ((0, 0), (0, width - 1), (height - 1, 0), (height - 1, width -1)):
#         rows[y][x] = CORNER
#     return rows
#
# print(_create_rectangle(10, 10, '*'))

# class Bar:
#     def __call__(self, *args, **kwargs):
#         print('i am instance method')
#
# b = Bar()  # 实例化
# b()  # 实例对象b 可以作为函数调用 等同于b.__call__ 使用


# assert True == False
# print("test")

strtemp = ''
for i in range(3):
    strtemp += strtemp + '-'

print(strtemp)
