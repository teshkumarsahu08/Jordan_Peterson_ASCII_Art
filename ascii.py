import os
from PIL import Image

# Character palette: Darkest to Lightest
ASCII_CHARS = "@#%*+=-:. "

def generate_ascii_final(target_name):
    # 1. Check if the file exists using a loop
    files_in_folder = os.listdir(".")
    found_file = False
    
    for file in files_in_folder:
        if file.lower() == target_name.lower():
            found_file = True
            break
    
    if found_file == False:
        print(f"Error: {target_name} not found.")
        return

    try:
        # 2. Load and Resize
        img = Image.open(target_name)
        width = 100
        # Calculate height with 0.5 aspect ratio correction
        height = int((img.height / img.width) * width * 0.5)
        img = img.resize((width, height))
        img = img.convert("L") # Grayscale
        
        # Load pixels into a coordinate-accessible map
        pixel_map = img.load()
        num_chars = len(ASCII_CHARS)
        bucket_size = 256 / num_chars

        # 3. Outer loop for rows (Y-axis)
        for y in range(height):
            line = ""
            
            # 4. Inner loop for columns (X-axis)
            for x in range(width):
                pixel_value = pixel_map[x, y]
                
                # 5. Conditional loop to determine which character to use
                char_to_add = ASCII_CHARS[-1] # Default to lightest
                for i in range(num_chars):
                    # Check if pixel brightness falls within the current bucket
                    if pixel_value < (i + 1) * bucket_size:
                        char_to_add = ASCII_CHARS[i]
                        break
                
                line += char_to_add
            
            # 6. Print the row only if it contains data
            if len(line) > 0:
                print(line)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the final loop-based version
generate_ascii_final("person.png")