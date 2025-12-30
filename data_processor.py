#!/usr/bin/env python3
"""
Data processing script.
"""
import json
from datetime import datetime

def process_data(data):
    """Process incoming data."""
    print(f"Processing data at {datetime.now()}")
    
    # Sample processing logic
    results = []
    for item in data:
        processed_item = {
            'original': item,
            'processed': item.upper() if isinstance(item, str) else item,
            'timestamp': datetime.now().isoformat()
        }
        results.append(processed_item)
    
    return results

def main():
    sample_data = ['hello', 'world', 'python', 'django']
    results = process_data(sample_data)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
