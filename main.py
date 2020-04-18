# Caesar
def restriction(values):
    if values > 0:
        if values > 26:
            values = values % 26
    else:
        if abs(values) > 26:
            values = -(values % 26)
    return values


def cipher_caesar(string, values):
    out_list = []
    for chars in string:
        time_var = ord(chars)
        if chars.isdigit():
            time_value = values
            if values > 10:
                time_value = values % 10
            elif values < -10:
                time_value = -(values % 10)
            time_var = time_var + time_value
            if time_var > ord("9"):
                time_var = time_var - 10
            elif time_var < ord("0"):
                time_var = time_var + 10
        if chars.islower():
            time_value = restriction(values)
            time_var = time_var + time_value
            if time_var > ord("z"):
                time_var = time_var - 26
            elif time_var < ord("a"):
                time_var = time_var + 26
        if chars.isupper():
            time_value = restriction(values)
            time_var = time_var + time_value
            if time_var > ord("Z"):
                time_var = time_var - 26
            elif time_var < ord("A"):
                time_var = time_var + 26
        out_list.append(chr(time_var))
    out_string = "".join(out_list)
    return out_string


in_string = str(input("Enter the string to encrypt: "))
while True:
    try:
        value = int(input("Enter the offset: "))
    except ValueError:
        print("Enter digital integer!")
    else:
        if abs(value) > 25:
            print("Enter in the range from -25 to 25")
        else:
            break
cipher_string = cipher_caesar(in_string, value)
print("Encrypted string: " + cipher_string)
print("Check: " + cipher_caesar(cipher_string, -value))
