import textwrap

def wrap(string, max_width):
    mensage = ""
    for i in range(len(string)):
        if i % max_width == 0:
            if i == 0:
                mensage += f"{string[i]}"
            else:
                mensage += f"\n{string[i]}"
        else:
            mensage += f"{string[i]}"
    return mensage

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)