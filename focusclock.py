import time

def focus_timer(minute):
    second = minute * 60
    print(f"Start focusing for {minute} minutes:")
    
    while second > 0:
        print(f"Remaining time: {second//60} minutes {second%60} seconds")
        second -= 1
        time.sleep(1)
        
    print("Time up! ")
