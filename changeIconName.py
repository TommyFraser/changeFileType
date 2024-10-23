import os
import cairosvg

#folder path
folder_path = "C:\Python\icons\Cisco icons"


# #list all files in the directory
# files = os.listdir(folder_path)


# # print the listof files
# for file in files:
#     print(file)


# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.svg'):
        svg_file = os.path.join(folder_path, filename)
        png_file = os.path.join(folder_path, filename.replace('.svg', '.png'))
        
        # Convert SVG to PNG with a transparent background
        cairosvg.svg2png(url=svg_file, write_to=png_file)

print("Conversion completed!")