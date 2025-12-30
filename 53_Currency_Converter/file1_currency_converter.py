import requests
import json
import os
from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self, cache_file='exchange_rates.json'):
        self.cache_file = cache_file
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
        self.rates = self.load_rates()
        self.last_updated = None
    
    def load_rates(self):
        """Load cached rates from file."""
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                data = json.load(f)
                self.last_updated = datetime.fromisoformat(data.get('timestamp', '2000-01-01'))
                return data.get('rates', {})
        return {}
    
    def save_rates(self, rates):
        """Save rates to cache file."""
        data = {
            'rates': rates,
            'timestamp': datetime.now().isoformat()
        }
        with open(self.cache_file, 'w') as f:
            json.dump(data, f, indent=4)
        self.rates = rates
        self.last_updated = datetime.now()
    
    def fetch_rates(self, base='USD'):
        """Fetch latest exchange rates from API."""
        try:
            response = requests.get(f"{self.api_url}{base}", timeout=5)
            response.raise_for_status()
            data = response.json()
            
            if 'rates' in data:
                self.save_rates(data['rates'])
                return data['rates']
            else:
                print("Error: Invalid API response")
                return None
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching rates: {e}")
            return None
    
    def should_update(self):
        """Check if rates should be updated (older than 1 hour)."""
        if not self.last_updated:
            return True
        
        time_diff = datetime.now() - self.last_updated
        return time_diff > timedelta(hours=1)
    
    def convert(self, amount, from_currency, to_currency):
        """Convert amount from one currency to another."""
        # Update rates if needed
        if self.should_update():
            print("Fetching latest exchange rates...")
            self.fetch_rates(from_currency)
        
        # Use cached rates if available
        if not self.rates:
            print("No exchange rates available. Fetching...")
            if not self.fetch_rates(from_currency):
                return None
        
        # Convert
        if from_currency != 'USD':
            # Fetch rates with from_currency as base
            rates = self.fetch_rates(from_currency)
            if not rates:
                return None
        else:
            rates = self.rates
        
        if to_currency in rates:
            rate = rates[to_currency]
            converted_amount = amount * rate
            return converted_amount, rate
        else:
            print(f"Error: Currency '{to_currency}' not found")
            return None
    
    def get_available_currencies(self):
        """Get list of available currencies."""
        if not self.rates:
            self.fetch_rates()
        
        return sorted(self.rates.keys()) if self.rates else []

def main():
    converter = CurrencyConverter()
    
    # Popular currencies
    popular = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'INR']
    
    print("=== Currency Converter ===\n")
    
    while True:
        print("\nOptions:")
        print("1. Convert Currency")
        print("2. View Available Currencies")
        print("3. Batch Conversion")
        print("4. Update Exchange Rates")
        print("5. Exit")
        
        choice = input
