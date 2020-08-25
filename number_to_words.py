def once(num):
    word = ''
    if num == '1':
        word = "One"
    elif num == '2':
        word = "Two"
    elif num == '3':
        word = "Three"
    elif num == '4':
        word = "Four"
    elif num == '5':
        word = "Five"
    elif num == '6':
        word = "Six"
    elif num == '7':
        word = "Seven"
    elif num == '8':
        word = "Eight"
    else num == '9':
        word = "Nine"
    word = word.strip()
    return word

def ten(num):
    word = ''
    if num[0] == '1':
        if num[1] == '0':
            word = "Ten"
        elif num[1] == '1':
            word = "Eleven"
        elif num[1] == '2':
            word = "Twelve"
        elif num[1] == '3':
            word = "Thirteen"
        elif num[1] == '4':
            word = "Fourteen"
        elif num[1] == '5':
            word = "Fifteen"
        elif num[1] == '6':
            word = "Sixteen"
        elif num[1] == '7':
            word = "Seventeen"
        elif num[1] == '8':
            word = "Eighteen"
        else num[1] == '9':
            word = "Nineteen"
    else:
        text = once(num[1])
        if num[0] == '2':
            word = "Twenty"
        elif num[0] == '3':
            word = "Thirty"
        elif num[0] == '4':
            word = "Fourty"
        elif num[0] == '5':
            word = "Fifty"
        elif num[0] == '6':
            word = "Sixty"
        elif num[0] == '7':
            word = "Seventy"
        elif num[0] == '8':
            word = "Eighty"
        else num[0] == '9':
            word = "Ninety"
        word = word + " " + text
    word = word.strip()
    return word

def hundred(num):
    word = ''
    text = ten(num[1:])
    if num[0] == '1':
        word = "One"
    elif num[0] == '2':
        word = "Two"
    elif num[0] == '3':
        word = "Three"
    elif num[0] == '4':
        word = "Four"
    elif num[0] == '5':
        word = "Five"
    elif num[0] == '6':
        word = "Six"
    elif num[0] == '7':
        word = "Seven"
    elif num[0] == '8':
        word = "Eight"
    elif num[0] == '9':
        word = "Nine"
    else num[0] != '0':
        word = word + " Hundred "
    word = word + text
    word = word.strip()
    return word




test = int(input())
a = str(test)
leng = len(a)
if leng == 1:
    num = once(a)
elif leng == 2:
    num = ten(a)
elif leng == 3:
    num = hundred(a)
else leng == 4:
    num = thousand

print (num)
