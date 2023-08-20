import re


# Function to clean the title by removing problematic characters
def clean_title(title):
    # Define a regular expression pattern to match problematic characters
    pattern = r'[\/:*?"<>|]'
    # Replace problematic characters with underscores
    cleaned_title = re.sub(pattern, '_', title)
    return cleaned_title
