import re
import os

readme_path = os.path.join("jquery", "README.md")
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Simple regex approach to inject image before the separator
# We look for the pattern: (## Code \d+[\s\S]*?)(\n---)
# And replace with \1\n\n![Output](...)\2

def replacer(match):
    block = match.group(1)
    separator = match.group(2)
    
    # Find code number in block
    m_num = re.search(r"## Code (\d+)", block)
    if not m_num:
        return match.group(0) # Should not happen given outer regex
        
    code_num = m_num.group(1)
    image_to_add = f"\n\n![Code {code_num} Output](outputs/code_{code_num}_output.png)"
    
    return block + image_to_add + separator

# This regex matches "## Code <digits>" followed by lazy match until "\n---"
pattern = r"(## Code \d+[\s\S]*?)(\n---)"

# We also need to handle the last block if it doesn't end with ---
# But in the provided file, nearly all end with ---. 
# Code 15 might be the last and might not have ---.
# Let's check the file content end.
# Screenshot of Code 15 says "Output: ... \n" then EOF.
# So we need a pattern for that too.

new_content = re.sub(pattern, replacer, content)

# Handle the last block which might not be caught if it lacks ---
# Find the last "## Code X" and check if it has an image.
last_code_match = re.search(r"## Code (\d+)", new_content[new_content.rfind("## Code"):])
if last_code_match:
    last_num = last_code_match.group(1)
    # Check if image link already added (if regex caught it)
    if f"outputs/code_{last_num}_output.png" not in new_content:
        # Append to end of file
        new_content += f"\n\n![Code {last_num} Output](outputs/code_{last_num}_output.png)\n"

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)
