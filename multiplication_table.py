def multiply_sheet(start, end):

    for x in range(start, end + 1):
        count = len(str(start)) + len(str(end)) + len(str(
            end * end)) + 3  # 确定每个乘法的宽度
        print('{:>{}}:'.format(x, len(str(end))),
              end=' ')  # 打印序号,宽度用输入2个数字中的大数位为准
        for y in range(start, x + 1):
            result = str(x) + '*' + str(y) + "=" + str(
                x * y)  # 打印乘法表的表达式用字符串保存
            fmt = '{{:{}}}'.format(count)  # 用这个标识宽度
            print(fmt.format(result), end=' ')
        print()


numbers = input("Pls input the numbers, such as 1-9, use '-'':")
temp = numbers.split('-')
start = int(temp[0])
end = int(temp[1])
multiply_sheet(start, end)
