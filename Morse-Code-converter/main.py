def create_morse_dict():
    return {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', '0': '-----', ' ': ' '
    }

def convert_to_morse(text, morse_dict):
    try:
        morse_code = ""
        for char in text.upper():
            if char in morse_dict:
                morse_code += morse_dict[char] + " "
            else:
                return f"Error: Invalid character '{char}' found. Only letters, numbers, and spaces are supported."
        return morse_code.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    morse_dict = create_morse_dict()
    
    while True:
        print("\n=== Morse Code Converter ===")
        print("1. Convert text to Morse code")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            text = input("Enter the text to convert to Morse code: ")
            result = convert_to_morse(text, morse_dict)
            print(f"\nOriginal text: {text}")
            print(f"Morse code: {result}")
        
        elif choice == "2":
            print("Thank you for using Morse Code Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
