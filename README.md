#Image to ASCII Art Generator using Python

🧠 Project Overview

This project converts a human image into ASCII art using Python.
It uses loops, conditional statements, logical buckets, and image processing.
The ASCII output is displayed directly in the terminal.

🎯 Objectives

Understand how digital images store pixel brightness
Apply loops and conditionals for character mapping
Convert grayscale pixel values into ASCII characters
Strengthen Python fundamentals for AIML projet.

🛠️ Technologies Used

Python 3.10+
Pillow (PIL) Library
VS Code / Terminal

⚙️ Working Principle

The image is resized to fit the terminal.
It is converted to grayscale.
Pixel brightness values (0–255) are grouped into buckets.
Each bucket maps to an ASCII character.
Nested loops traverse image rows and columns.

🧩 Algorithm Steps

Check if image file exists using a loop
Load and resize the image
Convert image to grayscale
Divide brightness into equal buckets
Use nested loops to map pixels to ASCII
Print ASCII image row-by-row

📸 Sample Output

Displays a recognizable human face
Dark areas appear dense (@ # %)
Light areas appear sparse (. and spaces)

