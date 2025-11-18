import time

for i in range(10):
    print(f"Processing item {i+1} of 10...", end='\r')
    time.sleep(0.3)
print("\nProcessing complete!") # Print a newline at the end to move to a new line