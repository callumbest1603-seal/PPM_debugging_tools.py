filename = "image.txt"
def PPM_to_special_pixel_v2(filename):
    count = 0
    f = open(filename, "r")
    output_special_pixel = open("ppm_to_special_pixel_output.txt", "w")
    output_binary_pixel = open("ppm_to_565_binary.txt", "w")
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
        print(binary_pixel)
        if binary_pixel[10] == "1":
            count = count + 1
            if count == 87:
                output_special_pixel.write(f"Special-87th--------------------------------------------------------------\n")
            else:
                output_special_pixel.write(f"Special\n")
        else:
            output_special_pixel.write(f"Not Special\n")
        output_binary_pixel.write(f"{binary_pixel}\n")
    f.close()
    output_special_pixel.close()
    output_binary_pixel.close()
PPM_to_special_pixel_v2(filename)