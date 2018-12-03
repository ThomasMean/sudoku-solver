def render(input):
    output=""
    for row in input:
        for number in row:
            output += (str(number) + "|")
        output = output[:-1]
        output += ("\n")
    output = output[:-1]
    return output
