import re
from collections import Counter
import os

class WordCounter:
    def __init__(self):
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
            'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
            'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
        }
    
    def read_file(self, filepath):
        """Read text from file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    def analyze_text(self, text):
        """Perform comprehensive text analysis."""
        # Basic counts
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
        
        # Line count
        lines = text.split('\n')
        line_count = len(lines)
        
        # Word analysis
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        word_count = len(words)
        
        # Unique words
        unique_words = set(words)
        unique_count = len(unique_words)
        
        # Sentence count
        sentences = re.split(r'[.!?]+', text)
        sentence_count = len([s for s in sentences if s.strip()])
        
        # Paragraph count
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        paragraph_count = len(paragraphs)
        
        # Average calculations
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
        avg_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0
        
        # Reading time (average reading speed: 200 words per minute)
        reading_time_minutes = word_count / 200
        
        # Word frequency
        word_freq = Counter(words)
        
        # Most common words (excluding stop words)
        content_words = [w for w in words if w not in self.stop_words]
        content_word_freq = Counter(content_words)
        
        # Lexical diversity (unique words / total words)
        lexical_diversity = (unique_count / word_count * 100) if word_count > 0 else 0
        
        return {
            'characters': char_count,
            'characters_no_spaces': char_count_no_spaces,
            'words': word_count,
            'unique_words': unique_count,
            'lines': line_count,
            'sentences': sentence_count,
            'paragraphs': paragraph_count,
            'avg_word_length': avg_word_length,
            'avg_words_per_sentence': avg_words_per_sentence,
            'reading_time': reading_time_minutes,
            'lexical_diversity': lexical_diversity,
            'most_common_all': word_freq.most_common(10),
            'most_common_content': content_word_freq.most_common(10)
        }
    
    def display_analysis(self, stats):
        """Display analysis results in formatted way."""
        print("\n" + "="*70)
        print("TEXT ANALYSIS RESULTS".center(70))
        print("="*70)
        
        print("\n📊 BASIC STATISTICS:")
        print(f"  Characters (with spaces):    {stats['characters']:,}")
        print(f"  Characters (without spaces): {stats['characters_no_spaces']:,}")
        print(f"  Words:                       {stats['words']:,}")
        print(f"  Unique words:                {stats['unique_words']:,}")
        print(f"  Lines:                       {stats['lines']:,}")
        print(f"  Sentences:                   {stats['sentences']:,}")
        print(f"  Paragraphs:                  {stats['paragraphs']:,}")
        
        print("\n📈 AVERAGES:")
        print(f"  Average word length:         {stats['avg_word_length']:.2f} characters")
        print(f"  Average words per sentence:  {stats['avg_words_per_sentence']:.2f}")
        
        print("\n⏱️  READING TIME:")
        minutes = int(stats['reading_time'])
        seconds = int((stats['reading_time'] - minutes) * 60)
        print(f"  Estimated reading time:      {minutes}m {seconds}s")
        print(f"  (Based on 200 words/minute)")
        
        print("\n🎯 VOCABULARY ANALYSIS:")
        print(f"  Lexical diversity:           {stats['lexical_diversity']:.2f}%")
        print(f"  (Unique words / Total words)")
        
        print("\n🔤 TOP 10 MOST COMMON WORDS (ALL):")
        for word, count in stats['most_common_all']:
            percentage = (count / stats['words']) * 100
            print(f"  {word:<15} {count:>5} ({percentage:.1f}%)")
        
        print("\n📝 TOP 10 CONTENT WORDS (EXCLUDING COMMON WORDS):")
        for word, count in stats['most_common_content']:
            print(f"  {word:<15} {count:>5}")
        
        print("\n" + "="*70)
    
    def save_report(self, stats, filename='word_count_report.txt'):
        """Save analysis report to file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("="*70 + "\n")
                f.write("TEXT ANALYSIS REPORT\n")
                f.write("="*70 + "\n\n")
                
                f.write("BASIC STATISTICS:\n")
                f.write(f"Characters (with spaces):    {stats['characters']:,}\n")
                f.write(f"Characters (without spaces): {stats['characters_no_spaces']:,}\n")
                f.write(f"Words:                       {stats['words']:,}\n")
                f.write(f"Unique words:                {stats['unique_words']:,}\n")
                f.write(f"Lines:                       {stats['lines']:,}\n")
                f.write(f"Sentences:                   {stats['sentences']:,}\n")
                f.write(f"Paragraphs:                  {stats['paragraphs']:,}\n\n")
                
                f.write("AVERAGES:\n")
                f.write(f"Average word length:         {stats['avg_word_length']:.2f} characters\n")
                f.write(f"Average words per sentence:  {stats['avg_words_per_sentence']:.2f}\n\n")
                
                f.write("READING TIME:\n")
                minutes = int(stats['reading_time'])
                seconds = int((stats['reading_time'] - minutes) * 60)
                f.write(f"Estimated reading time:      {minutes}m {seconds}s\n\n")
                
                f.write("VOCABULARY ANALYSIS:\n")
                f.write(f"Lexical diversity:           {stats['lexical_diversity']:.2f}%\n\n")
                
                f.write("TOP 10 MOST COMMON WORDS:\n")
                for word, count in stats['most_common_all']:
                    f.write(f"{word:<15} {count:>5}\n")
                
                f.write("\nTOP 10 CONTENT WORDS:\n")
                for word, count in stats['most_common_content']:
                    f.write(f"{word:<15} {count:>5}\n")
            
            print(f"\n✓ Report saved to: {filename}")
        
        except Exception as e:
            print(f"✗ Error saving report: {e}")

def main():
    counter = WordCounter()
    
    print("=== Word Counter & Text Analyzer ===\n")
    
    while True:
        print("\nOptions:")
        print("1. Analyze Text File")
        print("2. Analyze Text Input")
        print("3. Compare Multiple Files")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            filepath = input("\nEnter file path: ").strip()
            
            if not os.path.exists(filepath):
                print("✗ File not found!")
                continue
            
            text = counter.read_file(filepath)
            
            if text:
                stats = counter.analyze_text(text)
                counter.display_analysis(stats)
                
                save = input("\nSave report to file? (y/n): ").lower()
                if save == 'y':
                    report_name = input("Report filename (default: word_count_report.txt): ").strip()
                    report_name = report_name if report_name else 'word_count_report.txt'
                    counter.save_report(stats, report_name)
        
        elif choice == '2':
            print("\nEnter your text (type 'END' on a new line to finish):")
            lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                lines.append(line)
            
            text = '\n'.join(lines)
            
            if text.strip():
                stats = counter.analyze_text(text)
                counter.display_analysis(stats)
            else:
                print("✗ No text entered!")
        
        elif choice == '3':
            num_files = int(input("\nHow many files to compare? ").strip())
            files_data = []
            
            for i in range(num_files):
                filepath = input(f"Enter file {i+1} path: ").strip()
                
                if os.path.exists(filepath):
                    text = counter.read_file(filepath)
                    if text:
                        stats = counter.analyze_text(text)
                        files_data.append((os.path.basename(filepath), stats))
                else:
                    print(f"✗ File not found: {filepath}")
            
            if files_data:
                print("\n" + "="*100)
                print("COMPARISON RESULTS".center(100))
                print("="*100)
                print(f"\n{'Metric':<30}", end='')
                for filename, _ in files_data:
                    print(f"{filename[:20]:<25}", end='')
                print("\n" + "-"*100)
                
                metrics = [
                    ('Words', 'words'),
                    ('Characters', 'characters'),
                    ('Sentences', 'sentences'),
                    ('Paragraphs', 'paragraphs'),
                    ('Unique words', 'unique_words'),
                    ('Avg word length', 'avg_word_length'),
                    ('Reading time (min)', 'reading_time'),
                    ('Lexical diversity %', 'lexical_diversity')
                ]
                
                for metric_name, metric_key in metrics:
                    print(f"{metric_name:<30}", end='')
                    for _, stats in files_data:
                        value = stats[metric_key]
                        if isinstance(value, float):
                            print(f"{value:<25.2f}", end='')
                        else:
                            print(f"{value:<25,}", end='')
                    print()
                
                print("="*100)
        
        elif choice == '4':
            print("\nGoodbye!")
            break
        
        else:
            print("✗ Invalid choice!")

if __name__ == "__main__":
    main()
