
def oxford_comma(element):
    if len(element) == 1:
        return element[0]
    elif len(element) == 2:
        return f'{element[0]} and {element[1]}'
    else:
        comma_str = ', '.join(element[:-1])
        return f'{comma_str}, and {element[-1]}'

print(oxford_comma)