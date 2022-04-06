sample_dict= {'A':'Hello', 'B': 'World', 'C': 'Buddy'}

def get_output(dic, expresion):
    res = ""
    if " and " in expresion:
        element = expresion.split(" and ")
        for i in element:
            if dic.get(i):
                res += dic.get(i)
            else:
                continue
        return res

    elif " or " in expresion:
        aaa = expresion.split(" or ")
        for i in aaa:
            if dic.get(i):
                return dic.get(i)

def get_op(dic, expresion):
    if "(" and ")" in expresion:
        res = ""
        start, stop = expresion.find("("), expresion.find(")")
        if " and " or " or " in expresion[:start]:
            if " and " in expresion[:start]:
                element = expresion.split(" and ", 1)
                res += dic[element[0]]
                returned = get_output(dic, element[1][1:-1])
                res += returned
                return res

            elif " or " in expresion[:start]:
                element = expresion.split(" or ", 1)
                if dic.get(element[0]):
                        res += dic.get(element[0])
                        returned = get_output(dic, element[1][1:-1])
                        res += returned
                        return res
    else:
        res = get_output(dic, expresion)
        return res


sample_expresion = input("Please provide an expression to evaluate: ")
print(get_op(sample_dict, sample_expresion))
