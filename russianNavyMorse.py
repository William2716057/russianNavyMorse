import re

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
    translation = english_morse(morse_code)
    print("Original:", translation)
    #check for validation before processing
    #if not
    #VVV
    #RBEG
    #RGR70
    #RAL2
    #RMDV
    #RDNK 
    #RCV
    #RMI93
    #print sections
    locations = []
def location_identifiers(s):
    chunks = s.split()
    first = next((num for num in chunks if num.startswith('99')), None)
    second = next((num for num in chunks if num.startswith('10')), None)
                  
    if first and second:
        locations.append(first)
        locations.append(second)
        print(f"Location identifiers: {first}, {second}")
    else:
        print("Identifiers not found")
location_identifiers(translation)
#print(locations)

#unnecessary function, remove later
def transform(locations):
    transformed = []
    for loc in locations:
        if loc.startswith("99"):
            loc = "Lon: " + loc[2:]  # Remove "99" and add lon
            loc = loc[:6] + "." + loc[6:]  # Add decimal after index 1
        elif loc.startswith("10"): #1 = E can also be 
            loc = "Lat: Q" + loc[2:]  # return Q103,46, do not replace 
            loc = loc[:7] + "." + loc[7:] if len(loc) > 7 else loc  # Add decimal in correct position
        transformed.append(loc)
    return ", ".join(transformed)

result = transform(locations)
print(result) 

