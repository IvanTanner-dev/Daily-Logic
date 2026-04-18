def get_next_bingo_number(n):
    letter = n[0]
    number_str = n[1:]
    number = int(number_str)
    next_number = number + 1
    output = letter+str(next_number)
    new_output = []
    if output == "B16":
        new_output = "I16"
    elif output == "I31":
        new_output = "N31"
    elif output == "N46":
        new_output = "G46"
    elif output == "G61":
        new_output = "O61"
    elif output == "O76":
        new_output = "B1"
    else:
        new_output = output

    return new_output