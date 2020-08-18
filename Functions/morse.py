from morse import morse_code

def morse_a_string(mystr):
    final_str = ''
    for letter in mystr:
        final_str += morse_code[letter]
    return final_str

print(morse_a_string("Alan Loves TSwift"))
