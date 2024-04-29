def ceaser_shift(input):
    e = ""
    for i in input:
        ascii = ord(i)
        if (ascii >= 65) and (ascii <= 90):
            new_ascii = ascii + 3
            if new_ascii > 90:
                new_ascii = 65 + (new_ascii % 90 - 1)
            e += chr(new_ascii)
            continue

        if (ascii >= 97) and (ascii <= 122):
            new_ascii = ascii + 3
            if new_ascii > 122:
                new_ascii = 97 + (new_ascii % 122 - 1)
            e += chr(new_ascii)
            continue

        e += i
    return e

def main():
    ip = input("Enter a string : ")
    e = ceaser_shift(ip)
    print(e)

main()
