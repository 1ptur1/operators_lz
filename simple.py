input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
if a == 1 or a == 3 or a == 5 or a == 7 or a == 11 or a == 13 or a == 17 or a == 19 or a == 23:
    t = "Y"
else:
    t = "N"
output_data = open("output.txt","w")
output_data.write(t)
output_data.close()
input_data.close()