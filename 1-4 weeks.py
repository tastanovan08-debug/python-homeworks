def isalpha1(s):
    if len(s) != 1:
        return False
    all_letters = ("ABCDEFGHIJKLMNOPQRST" + "abcdefghijklmnopqrst" + "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + "абвгдежзийклмнопрстуфцчшщъыьэюя")
    for letter in all_letters:
        if letter == s:
            return True


#1
def analyze_text(text):
    text1 = text.lower()
    text2 = ""
    for alpha in text1:
        if isalpha1(alpha) or alpha == "":
            text2 += alpha
    dauysty = "aeiouy"
    new = ""
    for alpha in text2:
        if alpha in dauysty:
            new += alpha
    text3 = text2.split()



