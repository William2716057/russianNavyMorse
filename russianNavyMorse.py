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

#unnecessary function, remove later
def transform(locations):
    transformed = []
    for loc in locations:
        if loc.startswith("99"):
            loc = "Lon: " + loc[2:]  # degrees north or south of equater 
            loc = loc[:6] + "." + loc[6:]  # Add decimal after index 1
        elif loc.startswith("10"): #1 = E can also be 
            loc = "Lat:Q" + loc[2:]  
            loc = loc[:7] + "." + loc[7:] if len(loc) > 7 else loc  # Add decimal in correct position
        transformed.append(loc)
    return ", ".join(transformed)

result = transform(locations)
print(result) 
value = locations[1][2]  # Extract index 2 of the second value

if value == '1':
    print("North of the equator and east of the Greenwich Meridian")
elif value == '7':
    print("North of the equator and west of the Greenwich Meridian")
elif value == '3':
    print("South of the equator and east of the Greenwich Meridian")
elif value == '5':
    print("South of the equator and west of the Greenwich Meridian")
else:
    print("Unrecognized or invalid value")

def direction_speed(input_string):
    match = re.search(r'\b222\d{2}\b', input_string)
    if match:
        direction = match.group()
        print(f"Direction chunk: {direction}")
        
        # Extract the 4th character (index 3)
        if direction[3] == '1':
            print("Travelling northeast")
        elif direction[3] == '2':
            print("Travelling east")
        elif direction[3] == '3':
            print("Travelling southeast")
        elif direction[3] == '4':
            print("Travelling south")
        elif direction[3] == '5':
            print("Travelling southwest")
        elif direction[3] == '6':
            print("Travelling west")
        elif direction[3] == '7':
            print("Travelling northwest")
        elif direction[3] == '8':
            print("Travelling north")
        elif direction[3] == '9':
            print("unknown")
    else:
        print("Section 222 not found")
        
    if match:
        direction = match.group() 
        # Extract the 5th character (index 4)
        if direction[4] == '1':
            print("0 knot")
        elif direction[4] == '2':
            print("1 to 5 knots")
        elif direction[4] == '3':
            print("6 to 10 knots")
        elif direction[4] == '4':
            print("16 to 20 knots")
        elif direction[4] == '5':
            print("21 to 25 knots")
        elif direction[4] == '6':
            print("26 to 30 knots")
        elif direction[4] == '7':
            print("31 to 35 knots")
        elif direction[4] == '8':
            print("36 to 40 knots")
        elif direction[4] == '9':
            print("Over 40 knots")
    else:
        print("Unfound or invalid")

direction_speed(translation)

#precipitation data indicator irixhVV
#always encoded as 4
#find 4 
#if 4 followed by 1
#if 4 followed by 3
#print(precipitation data ommitted or unavailable)

def precipitation(input_string):
    match = re.search(r'\b41\d{3}\b', input_string)
    if match:
        height = match.group()
        print(f"Precipitation and cloud height chunk: {height}")
        
        # Extract the 4th character (index 3)
        if height[2] == '2':
            print("0 to 50")
        elif height[2] == '1':
            print("50 to 100")
        elif height[2] == '2':
            print("100 to 200")
        elif height[2] == '3':
            print("200 to 300")
        elif height[2] == '4':
            print("300 to 600")
        elif height[2] == '5':
            print("600 to 1000")
        elif height[2] == '6':
            print("1000 to 1500 ")
        elif height[2] == '7':
            print("1500 to 2000")
        elif height[2] == '8':
            print("2000 to 2500")
        elif height[2] == '9':
            print("2500 or more, or no clouds")
    else:
        print("Section 41 not found")
        
precipitation(translation)