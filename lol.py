from translate import Translator


def to_translate():
    lang = input(
        "Enter language to be translated(e.g. en, ja, ko, pt, zh, zh-TW, ...): "
    )
    translator = Translator(to_lang=lang)
    file1 = open("new_file.txt", "a", encoding="utf-8")
    try:
        file2 = open("translate.txt", "r")
        x = file2.read()
        trans = translator.translate(x)
        print(trans)
        file1.write(trans)
        file1.write("\n")
        file2.close()
    except FileExistsError:
        print("file not found silly!")
    file1.close()


def input_file():
    file = open("translate.txt", "w")
    ch = "y"
    while ch == "y":
        sentence = input("Enter a sentence: ")
        file.write(sentence)
        file.write("\n")
        ch = input("Do you want to add another sentence?(y/n): ")
        ch = ch.lower()
    file.close()


def process():
    input_file()
    to_translate()


def bye():
    print("Thank You!")


choice = "y"
while choice == "y":
    process()
    choice = input("Do you wish to translate again (y/n)?: ")
    choice = choice.lower()

bye()
