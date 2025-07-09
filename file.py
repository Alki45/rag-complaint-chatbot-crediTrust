import os

# List of folders to create
folders = [
    "data/raw",
    "notebooks",
    "src",
    "vector_store",
    "app",
    "reports/screenshots",
    "tests"
]

# List of files to create with placeholder content
files = [
    "data/filtered_complaints.csv",
    "notebooks/eda_preprocessing.ipynb",
    "src/data_processing.py",
    "src/chunking.py",
    "src/embedding.py",
    "src/vector_store.py",
    "src/rag_pipeline.py",
    "src/prompts.py",
    "src/evaluation.py",
    "app/app.py",
    "reports/interim_report.md",
    "reports/final_report.md",
    ".gitignore",
    "requirements.txt",
    "README.md",
    "LICENSE"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with headers
for file in files:
    with open(file, "w") as f:
        f.write(f"# {os.path.basename(file)}\n")

print("✅ Project structure created successfully.")
