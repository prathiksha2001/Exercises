def wordUpper(name):
    return name.upper()

def wordLower(name):
    return name.lower()

def greeting(function):
    print('\n')
    print('Hi ' + function('pRAthiksha'))
    print('\n')
greeting(wordUpper)
greeting(wordLower)