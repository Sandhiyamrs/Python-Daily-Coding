import pyperclip
import time
import json
import os
from datetime import datetime

class ClipboardManager:
    def __init__(self, history_file='clipboard_history.json'):
        self.history_file = history_file
        self.history = self.load_history()
        self.last_value = ""
    
    def load_history(self):
        """Load clipboard history from file."""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def save_history(self):
        """Save clipboard history to file."""
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=4, ensure_ascii=False)
    
    def add_to_history(self, content):
        """Add content to history."""
        entry = {
            'content': content,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'length': len(content)
        }
        
        # Avoid duplicates
        if not self.history or self.history[0]['content'] != content:
            self.history.insert(0, entry)
            
            # Keep only last 100 entries
            if len(self.history) > 100:
                self.history = self.history[:100]
            
            self.save_history()
            return True
        return False
    
    def monitor(self, interval=1):
        """Monitor clipboard for changes."""
        print("Monitoring clipboard... (Press Ctrl+C to stop)\n")
        
        try:
            while True:
                current_value = pyperclip.paste()
                
                if current_value != self.last_value and current_value.strip():
                    if self.add_to_history(current_value):
                        preview = current_value[:50].replace('\n', ' ')
                        if len(current_value) > 50:
                            preview += '...'
                        
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] Captured: {preview}")
                    
                    self.last_value = current_value
                
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped.")
    
    def view_history(self, limit=10):
        """View clipboard history."""
        if not self.history:
            print("No clipboard history found!")
            return
        
        print(f"\n{'='*80}")
        print(f"{'#':<5} {'Timestamp':<20} {'Content Preview':<50} {'Length':<10}")
        print(f"{'='*80}")
        
        for idx, entry in enumerate(self.history[:limit], 1):
            content = entry['content'][:47].replace('\n', ' ')
            if len(entry['content']) > 50:
                content += '...'
            
            print(f"{idx:<5} {entry['timestamp']:<20} {content:<50} {entry['length']:<10}")
        
        print(f"{'='*80}\n")
    
    def search_history(self, keyword):
        """Search clipboard history."""
        results = [entry for entry in self.history if keyword.lower() in entry['content'].lower()]
        
        if not results:
            print(f"No results found for: {keyword}")
            return
        
        print(f"\nFound {len(results)} result(s):\n")
        print(f"{'='*80}")
        
        for idx, entry in enumerate(results, 1):
            content = entry['content'][:47].replace('\n', ' ')
            if len(entry['content']) > 50:
                content += '...'
            
            print(f"{idx}. [{entry['timestamp']}] {content}")
        
        print(f"{'='*80}\n")
    
    def restore_to_clipboard(self, index):
        """Restore history item to clipboard."""
        if 0 < index <= len(self.history):
            content = self.history[index - 1]['content']
            pyperclip.copy(content)
            print(f"✓ Restored to clipboard!")
            return True
        else:
            print("✗ Invalid index!")
            return False
    
    def clear_history(self):
        """Clear all history."""
        self.history = []
        self.save_history()
        print("✓ History cleared!")

def main():
    manager = ClipboardManager()
    
    while True:
        print("\n=== Clipboard Manager ===")
        print("1. Start Monitoring")
        print("2. View History")
        print("3. Search History")
        print("4. Restore to Clipboard")
        print("5. Clear History")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            manager.monitor()
        
        elif choice == '2':
            limit = int(input("Enter number of entries to show (default 10): ").strip() or "10")
            manager.view_history(limit)
        
        elif choice == '3':
            keyword = input("Enter search keyword: ").strip()
            manager.search_history(keyword)
        
        elif choice == '4':
            manager.view_history(20)
            index = int(input("Enter item number to restore: ").strip())
            manager.restore_to_clipboard(index)
        
        elif choice == '5':
            confirm = input("Are you sure? This cannot be undone! (y/n): ").lower()
            if confirm == 'y':
                manager.clear_history()
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("✗ Invalid choice!")

if __name__ == "__main__":
    main()
