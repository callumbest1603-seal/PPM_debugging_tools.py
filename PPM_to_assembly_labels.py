filename = "image.txt"
def ppm_to_assembly_labels(filename):
    f = open(filename, "r")
    output_assembly_labels = open("ppm_to_assembly_labels.txt", "w")
    for line in f:
        line = line[1:]
        rgb_array = line.split()
        red = bin(int(rgb_array[0]))[2:]
        if len(red) != 8:
            for i in range(8 - len(red)):
                red = "0" + red
        red = red[:-3]
        green = bin(int(rgb_array[1]))[2:]
        if len(green) != 8:
            for i in range(8 - len(green)):
                green = "0" + green
        green = green[:-2]
        blue = bin(int(rgb_array[2]))[2:]
        if len(blue) != 8:
            for i in range(8 - len(blue)):
                blue = "0" + blue
        blue = blue[:-3]
        binary_pixel = red + green + blue
        if str(binary_pixel) == "0100001000001011":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000110000001011":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000101111001010":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000101101001001":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000101101001000":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000101111101010":
            output_assembly_labels.write(f".data 0x0020\n")
        elif str(binary_pixel) == "0111001100001011":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0110101100001011":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000101100001000":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000101110001010":
            output_assembly_labels.write(f".data 0x0000\n")
        elif str(binary_pixel) == "0000101110001001":
            output_assembly_labels.write(f".data 0x0000\n")
        else:
            binary_pixel = int(binary_pixel, 2)
            binary_pixel = f"{binary_pixel:04X}"
            output_assembly_labels.write(f".data 0x{binary_pixel}\n")
    f.close()
    output_assembly_labels.close()
ppm_to_assembly_labels(filename)