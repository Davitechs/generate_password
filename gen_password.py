if"__name__" == "__main__":
    import random

    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_alphabet = uppercase_alphabet.lower()
    digits = "0123456789" 
    symbols = "(){}[],;:.-/\\?+*#@"
    upper, lower,nums,syms = True, True, True, True,
    all = ""
    if upper:
        all += uppercase_alphabet
    if lower:
        all += lowercase_alphabet
    if nums:
        all += digits
    if syms:
        all += symbols

    length = 20
    amount = 15

    for i in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
