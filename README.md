# PPM_debugging_tools.py
Takes a text file in PPM format where each line starts with a space, and then 3 decimal values seperated by spaces, representing the RGB value of a pixel. This file then produces output files of many helpful formats.

# PPM_to_special_pixel_v2.py
PPM_to_special_pixel_v2.py takes an input .txt file and outputs 2 files,
The output file ppm_to_565_binary.txt contains a 565 packed RGB representation of each pixel, where each pixel is on a new line.
The output file ppm_to_special_pixel_output.txt contains the strings Special or not Special on a new line, depending on whether a pixel is special,
A pixel is defined a special if its 5th most significant bit contains a 1,
Also the 87th special pixel is highlighted for debugging reasons.

# PPM_to_assembly_labels.py
PPM_to_assembly_labels.py takes an input .txt file and outputs 1 file,
The output file ppm_to_assembly_labels.txt converts the input file into packed 565 RGB format,
Each line in the output file is in the format .data 0xAAAA where AAAA is the packed 565 RGB value,
This is used to copy and paste into a simplecpuv1d assembly program.
Some hex values clash with opcodes in the cpu so these are replaced manually but does not effect assembly testing.

# PPM_to_basic_image.py
PPM_to_basic_image.py takes an input .txt file and outputs 1 file,
The output file output_ppm_image.txt is a image representation of PPM_to_special_pixel,
When a pixel is special it is represented by the string "XXX",
When a pixel is not special it is represented by the string "---",
The image generated is 24x24 size, therefore the input .txt must contain exactly 564 lines.
As well as this, PPM_to_basic_image.py prints the number of special pixels to the console.
