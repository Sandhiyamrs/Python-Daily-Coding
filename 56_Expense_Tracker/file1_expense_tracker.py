import json
import os
from datetime import datetime
from collections import defaultdict
import csv

class ExpenseTracker:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.transactions = self.load_data()
        self.categories = [
            'Food & Dining', 'Transportation', 'Shopping', 'Entertainment',
            'Bills & Utilities', 'Healthcare', 'Education', 'Travel',
            'Groceries', 'Salary', 'Freelance', 'Investment', 'Other'
        ]
    
    def load_data(self):
        """Load transactions from file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_data(self):
        """Save transactions to file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.transactions, f, indent=4)
    
    def add_transaction(self, amount, category, description, trans_type='expense'):
        """Add a new transaction."""
        transaction = {
            'id': len(self.transactions) + 1,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'amount': amount,
            'category': category,
            'description': description,
            'type': trans_type  # 'expense' or 'income'
        }
        
        self.transactions.append(transaction)
        self.save_data()
        return transaction['id']
    
    def delete_transaction(self, trans_id):
        """Delete a transaction."""
        self.transactions = [t for t in self.transactions if t['id'] != trans_id]
        self.save_data()
    
    def get_transactions(self, start_date=None, end_date=None, trans_type=None):
        """Get filtered transactions."""
        filtered = self.transactions
        
        if start_date:
            filtered = [t for t in filtered if t['date'] >= start_date]
        
        if end_date:
            filtered = [t for t in filtered if t['date'] <= end_date]
        
        if trans_type:
            filtered = [t for t in filtered if t['type'] == trans_type]
        
        return filtered
    
    def get_summary(self, start_date=None, end_date=None):
        """Get financial summary."""
        transactions = self.get_transactions(start_date, end_date)
        
        total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
        total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
        balance = total_income - total_expense
        
        # Category breakdown
        category_totals = defaultdict(float)
        for t in transactions:
            if t['type'] == 'expense':
                category_totals[t['category']] += t['amount']
        
        return {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
            'category_breakdown': dict(category_totals),
            'transaction_count': len(transactions)
        }
    
    def display_transactions(self, transactions):
        """Display transactions in table format."""
        if not transactions:
            print("\nNo transactions found!")
            return
        
        print("\n" + "="*90)
        print(f"{'ID':<5} {'Date':<12} {'Type':<10} {'Category':<20} {'Amount':<12} {'Description':<20}")
        print("="*90)
        
        for t in transactions:
            amount_str = f"${t['amount']:,.2f}"
            if t['type'] == 'income':
                amount_str = f"+{amount_str}"
            else:
                amount_str = f"-{amount_str}"
            
            desc = t['description'][:17] + '...' if len(t['description']) > 20 else t['description']
            
            print(f"{t['id']:<5} {t['date']:<12} {t['type']:<10} {t['category']:<20} {amount_str:<12} {desc:<20}")
        
        print("="*90)
    
    def display_summary(self, summary):
        """Display financial summary."""
        print("\n" + "="*60)
        print("FINANCIAL SUMMARY".center(60))
        print("="*60)
        
        print(f"\n💰 Total Income:    ${summary['total_income']:,.2f}")
        print(f"💸 Total Expenses:  ${summary['total_expense']:,.2f}")
        print(f"{'─'*60}")
        
        balance_symbol = "📈" if summary['balance'] >= 0 else "📉"
        print(f"{balance_symbol} Net Balance:    ${summary['balance']:,.2f}")
        
        if summary['category_breakdown']:
            print(f"\n📊 EXPENSES BY CATEGORY:")
            print(f"{'─'*60}")
            
            sorted_categories = sorted(
                summary['category_breakdown'].items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            for category, amount in sorted_categories:
                percentage = (amount / summary['total_expense'] * 100) if summary['total_expense'] > 0 else 0
                bar_length = int(percentage / 2)
                bar = '█' * bar_length
                
                print(f"{category:<20} ${amount:>10,.2f} {bar} {percentage:.1f}%")
        
        print("="*60)
    
    def export_to_csv(self, filename='expenses_export.csv'):
        """Export transactions to CSV."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'date', 'type', 'category', 'amount', 'description'])
                writer.writeheader()
                writer.writerows(self.transactions)
            
            print(f"\n✓ Exported to {filename}")
        except Exception as e:
            print(f"✗ Error exporting: {e}")
    
    def get_monthly_report(self, year, month):
        """Get monthly report."""
        start_date = f"{year}-{month:02d}-01"
        
        # Calculate last day of month
        if month == 12:
            end_date = f"{year}-12-31"
        else:
            end_date = f"{year}-{month+1:02d}-01"
        
        return self.get_summary(start_date, end_date)

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Summary")
        print("5. Monthly Report")
        print("6. Delete Transaction")
        print("7. Export to CSV")
        print("8. Exit")
        
        choice = input("\nEnter choice (1-8): ").strip()
        
        if choice == '1':
            amount = float(input("\nIncome amount: $").strip())
            
            print("\nCategories: Salary, Freelance, Investment, Other")
            category = input("Category: ").strip()
            
            description = input("Description: ").strip()
            
            trans_id = tracker.add_transaction(amount, category, description, 'income')
            print(f"\n✓ Income added with ID: {trans_id}")
        
        elif choice == '2':
            amount = float(input("\nExpense amount: $").strip())
            
            print("\nCategories:")
            for i, cat in enumerate(tracker.categories[:9], 1):
                print(f"{i}. {cat}")
            
            cat_choice = int(input("Choose category (1-9): ").strip())
            category = tracker.categories[cat_choice - 1] if 1 <= cat_choice <= 9 else 'Other'
            
            description = input("Description: ").strip()
            
            trans_id = tracker.add_transaction(amount, category, description, 'expense')
            print(f"\n✓ Expense added with ID: {trans_id}")
        
        elif choice == '3':
            print("\nFilter options:")
            print("1. All transactions")
            print("2. Only income")
            print("3. Only expenses")
            print("4. Date range")
            
            filter_choice = input("Enter choice (1-4): ").strip()
            
            if filter_choice == '1':
                transactions = tracker.get_transactions()
            elif filter_choice == '2':
                transactions = tracker.get_transactions(trans_type='income')
            elif filter_choice == '3':
                transactions = tracker.get_transactions(trans_type='expense')
            elif filter_choice == '4':
                start = input("Start date (YYYY-MM-DD): ").strip()
                end = input("End date (YYYY-MM-DD): ").strip()
                transactions = tracker.get_transactions(start, end)
            else:
                transactions = tracker.get_transactions()
            
            tracker.display_transactions(transactions)
        
        elif choice == '4':
            print("\n1. All time")
            print("2. This month")
            print("3. Custom date range")
            
            period = input("Enter choice (1-3): ").strip()
            
            if period == '1':
                summary = tracker.get_summary()
            elif period == '2':
                now = datetime.now()
                start = f"{now.year}-{now.month:02d}-01"
                summary = tracker.get_summary(start)
            elif period == '3':
                start = input("Start date (YYYY-MM-DD): ").strip()
                end = input("End date (YYYY-MM-DD): ").strip()
                summary = tracker.get_summary(start, end)
            else:
                summary = tracker.get_summary()
            
            tracker.display_summary(summary)
        
        elif choice == '5':
            year = int(input("\nEnter year (e.g., 2024): ").strip())
            month = int(input("Enter month (1-12): ").strip())
            
            summary = tracker.get_monthly_report(year, month)
            
            month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June',
                          'July', 'August', 'September', 'October', 'November', 'December']
            
            print(f"\n📅 Report for {month_names[month]} {year}")
            tracker.display_summary(summary)
        
        elif choice == '6':
            trans_id = int(input("\nEnter transaction ID to delete: ").strip())
            tracker.delete_transaction(trans_id)
            print("✓ Transaction deleted!")
        
        elif choice == '7':
            filename = input("\nExport filename (default: expenses_export.csv): ").strip()
            filename = filename if filename else 'expenses_export.csv'
            tracker.export_to_csv(filename)
        
        elif choice == '8':
            print("\nGoodbye!")
            break
        
        else:
            print("✗ Invalid choice!")

if __name__ == "__main__":
    main()
