filename = "image.txt"
def ppm_to_basic_image(filename):
    count = 0
    f = open(filename,'r')
    output = open("output_ppm_image.txt", "w")
    for x in range(0, 24):
        output_line = ""
        for y in range(0, 24):
            current = f.readline()
            current = current[1:]
            current = current.split()
            current = current[1]
            binary = bin(int(current))
            binary = int(binary[2:])
            if len(str(binary)) != 8:
                for i in range(0, 8 - len(str(binary))):
                    binary = "0" + str(binary)
            binary = str(binary)[:-2]
            if str(binary)[5] == "1":
                output_line = output_line + "XXX"
            else:
                output_line = output_line + "---"
                count = count + 1
        output.write(f"{output_line}\n")
    print(count)
    f.close()
    output.close()
ppm_to_basic_image(filename)