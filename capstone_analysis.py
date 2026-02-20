import os
import pandas as pd
# ... (Combine the logic from above or run the notebooks)

def setup_project():
    folders = ['data', 'reports', 'presentation', 'notebooks']
    for f in folders:
        if not os.path.exists(f): os.makedirs(f)

if __name__ == "__main__":
    setup_project()
    print("Project Folders Ready. Please run notebooks in sequence.")