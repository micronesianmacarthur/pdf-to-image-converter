# progress_bar.py

import sys
import time

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end='\r'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character (e.g. '\r', '\n') (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}{print_end}')
    sys.stdout.flush() # Ensure immediate display
    # Print New Line on Complete
    if iteration == total:
        sys.stdout.write('\n')

# # Example Usage:
# total_items = 50
# print_progress_bar(0, total_items, prefix='Progress:', suffix='Complete', length=30)
# for i in range(total_items):
#     time.sleep(0.1) # Simulate a task
#     print_progress_bar(i + 1, total_items, prefix='Progress:', suffix='Complete', length=30)