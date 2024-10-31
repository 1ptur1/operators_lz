input_data = open("input.txt","r")
data = input_data.read()
n = int(data)
d = 0
while n != 0:
    if n % 3 == 0:
        n -= 3
    elif n% 3 == 1:
        n -=1
    else:
        n -=2
    d +=1
d = str(d)
output_data = open("output.txt","w")
output_data.write(d)
output_data.close()
input_data.close()