morseDict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' ',
    '-.-.--': '!', '.-.-.-': '.', '--..--': ',', '---...': ':', '..--..': '?', '-....-': '-', '-..-.': '/', '.----.': "'",
    '...-..-': '$', '.--.-.': '@', '-.--.-': '(', '-.--.': ')', '.-...': '&', '-.-.-.': ';'
}

def english_morse(morse_code):
    words = morse_code.split(' / ')
    translated_chars = []
    
    for word in words:
        chars = word.split()
        translated_char = ''.join(morseDict.get(char, '?') for char in chars)
        translated_chars.append(translated_char)
        
    return ' '.join(translated_chars)
    
if __name__ == "__main__":
    morse_code = input("Enter Navy Code: ")
    #check for valid before translating
    #
    translation = english_morse(morse_code)
    #else
    #print("invalid or unrecognised identifier")
    print("Original:", translation)
