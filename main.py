MorseCode = {"a": ".-", "b": "-...", "c": "-.-.",
             "d": "-..", "e": ".", "f": "..-.",
             "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "-.-", "l": ".-..",
             "m": "--", "n": "-.", "o": "---",
             "p": ".--.", "q": "--.-", "r": ".-.",
             "s": "...", "t": "-", "u": "..-",
             "v": "...-", "w": ".--", "x": "-..-",
             "y": "-.--", "z": "--..", " ": "",
             "0": "-----", "1": ".----", "2": "..---",
             "3": "...--", "4": "....-", "5": ".....",
             "6": "-....", "7": "--...", "8": "---..",
             "9": "----."}


def encode_to_morse(text):
    text = text.lower()
    res = ''
    for i in range(len(text)):
        res += MorseCode[text[i]]
        res += ' '
    return res.rstrip()


def decode_from_morse(code):
    res = ''
    code = [elem.split() for elem in code.split('  ')]
    for word in code:
        for letter in word:
            for elem in MorseCode:
                if letter == MorseCode[elem]:
                    res += elem
        res += ' '
    return res.rstrip()


def main():
    letters = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    text = input('Введите текст или закодированное сообщение: ')
    for elem in letters:
        if elem not in text:
            continue
        else:
            print(encode_to_morse(text))
            return main()
    print(decode_from_morse(text))
    return main()


# пользователь может ввести текст и получить зашифрованное сообщение, или
# ввести зашифрованное сообщение, получив при этом его расшифровку.
if __name__ == '__main__':
    main()
