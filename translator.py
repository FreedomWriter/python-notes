from translate import Translator
translator= Translator(to_lang="sw")
try:
    with open('./translator_text.txt', mode='r') as my_file:
        print(my_file.read())
        my_file.seek(0)
        translation = translator.translate(my_file.read())
        print(translation)
        with open('./translated_text.txt', mode='w') as my_translation:
            my_translation.write(translation)
except FileNotFoundError as e:
    print('Check your file path')

# pipenv install translate
## https://pypi.org/project/translate/
## offline translator

# to run in a virutal environment:
## pipenv shell
## gives you the virtual environment which you can now run:
### python3 file_name.py
