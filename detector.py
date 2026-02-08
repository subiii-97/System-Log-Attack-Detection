
import os

def start_detection():
    filename = "mylogs.txt" 
    
    if os.path.exists(filename):
        print("--- Log Scanner Started ---")
        
        with open(filename, "r") as file:
            for line in file:
                if "Failed" in line or "Unauthorized" in line:
                    print(f"ALERT: Security Threat Found -> {line.strip()}")
        
        print("--- Scan Finished ---")
    else:
        print("Error: mylogs.txt not found! Make sure it's in the same folder.")


start_detection()
