


def binary(s):
    result = ""
    while s!=0:
        temp = s // 2
        result += str(s % 2)
        s = temp
    res = result[::-1]
    return res

def octal(s):
    result = ""
    while s!=0:
        temp = s // 8
        result += str(s % 8)
        s = temp
    res = result[::-1]
    return res

def hexa(s):
    result = ""
    while s!=0:
        temp = s // 16
        result += str(s % 16)
        s = temp
    res = result[::-1]
    return res



s = int(input("Enter a decimal number: "))
ans = dict({"binary": binary(s)})
ans.update({"octal": octal(s)})
ans.update({"hexa": hexa(s)})
print(ans)

