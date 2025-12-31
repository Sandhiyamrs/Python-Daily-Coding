import time
import sys

class MorseCodeTranslator:
    def __init__(self):
        # Morse code dictionary
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
            ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
            '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
            '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
            '@': '.--.-.', ' ': '/'
        }
        
        # Reverse dictionary for decoding
        self.reverse_morse_dict = {v: k for k, v in self.morse_dict.items()}
    
    def text_to_morse(self, text):
        """Convert text to Morse code."""
        morse_code = []
        
        for char in text.upper():
            if char in self.morse_dict:
                morse_code.append(self.morse_dict[char])
            else:
                morse_code.append('?')  # Unknown character
        
        return ' '.join(morse_code)
    
    def morse_to_text(self, morse):
        """Convert Morse code to text."""
        morse = morse.strip()
        words = morse.split(' / ')
        decoded_message = []
        
        for word in words:
            letters = word.split(' ')
            decoded_word = ''
            
            for letter in letters:
                if letter in self.reverse_morse_dict:
                    decoded_word += self.reverse_morse_dict[letter]
                else:
                    decoded_word += '?'
            
            decoded_message.append(decoded_word)
        
        return ' '.join(decoded_message)
    
    def play_morse_audio(self, morse_code):
        """Play Morse code as audio (simple beep version)."""
        try:
            # Try to import winsound for Windows
            import winsound
            
            frequency = 800  # Frequency in Hz
            dot_duration = 100  # Duration in milliseconds
            dash_duration = 300
            pause_duration = 100
            
            print("\nPlaying Morse code audio...")
            
            for char in morse_code:
                if char == '.':
                    winsound.Beep(frequency, dot_duration)
                elif char == '-':
                    winsound.Beep(frequency, dash_duration)
                elif char == ' ':
                    time.sleep(pause_duration / 1000)
                elif char == '/':
                    time.sleep(pause_duration * 2 / 1000)
                
                time.sleep(pause_duration / 1000)
            
            print("✓ Playback complete!")
        
        except ImportError:
            print("✗ Audio playback not supported on this system (Windows only)")
        except Exception as e:
            print(f"✗ Error playing audio: {e}")
    
    def visual_morse(self, morse_code, speed=0.2):
        """Display Morse code visually with timing."""
        print("\nVisual Morse Code Display:")
        print("─" * 50)
        
        for char in morse_code:
            if char == '.':
                print('●', end='', flush=True)
                time.sleep(speed)
            elif char == '-':
                print('━━', end='', flush=True)
                time.sleep(speed * 3)
            elif char == ' ':
                print(' ', end='', flush=True)
                time.sleep(speed)
            elif char == '/':
                print('  ', end='', flush=True)
                time.sleep(speed * 2)
        
        print("\n" + "─" * 50)
    
    def save_to_file(self, content, filename):
        """Save content to file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"\n✓ Saved to {filename}")
        except Exception as e:
            print(f"✗ Error saving file: {e}")
    
    def read_from_file(self, filename):
        """Read content from file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"✗ Error reading file: {e}")
            return None

def main():
    translator = MorseCodeTranslator()
    
    while True:
        print("\n=== Morse Code Translator ===")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Play Morse Audio")
        print("4. Visual Morse Display")
        print("5. Save to File")
        print("6. Read from File")
        print("7. Show Morse Code Chart")
        print("8. Exit")
        
        choice = input("\nEnter choice (1-8): ").strip()
        
        if choice == '1':
            text = input("\nEnter text to convert: ").strip()
            
            if text:
                morse = translator.text_to_morse(text)
                print(f"\nOriginal text: {text}")
                print(f"Morse code:    {morse}")
                
                save = input("\nSave to file? (y/n):
