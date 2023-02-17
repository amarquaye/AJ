# To read and print form the terminal

import basic

while True:
    text = input('aj >> ')
    result, error = basic.run(text)

    if error: print(error.as_string())
    else: print(result)