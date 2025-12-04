import os
from datetime import datetime

def generate_random_email(domain="gmail.com"):
    counter_file = "email_counter.txt"
    
    # Counter Logic to maintain sequence
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            try:
                last_count = int(f.read().strip())
                new_count = last_count + 1
            except:
                new_count = 1
    else:
        new_count = 1
        
    with open(counter_file, "w") as f:
        f.write(str(new_count))
    
    # Format: test_user{Count}_{Date}@domain.com
    # Example: test_user5_041225@gmail.com
    date_str = datetime.now().strftime("%d%m%y")
    email = f"test_user{new_count}_{date_str}@{domain}"
    return email