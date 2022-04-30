from translate import Translator

trans = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
list(map(str.capitalize, trans))

def num_translate(number: str):
     new_number = input("Ввод: ")
     translator = Translator(from_lang='en', to_lang='ru')
     trans = translator.translate(new_number)

     for key, value in trans:
          if key == new_number:
               print(value)
     if number not in trans:
          print(None)

     return new_number


if __name__ == "__main__":
     print(num_translate("one"))
     print(num_translate("six"))


