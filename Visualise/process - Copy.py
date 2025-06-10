import json
import sys


def strippy(lijn):
	erna = lijn.replace("\n","").split(": ")[1]
	if " " in erna:
		erna = erna.split(" ")[0]
	try:
		float(erna)
		if "." in erna:
			return float(erna)
		else:
			return int(erna)
	except ValueError:
		return erna


output = {}

n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i])
else:
	print("A")




with open('process.txt', 'r') as file:
	# Read each line in the file
	began = False

	curr_do = 0

	for line in file:
		if "Type of the Template" in line:
			naam_AELEl = line.replace("\n","").split(": ")[1]

		if began and ": " in line:
			waarde = strippy(line)

			match line.split(": ")[0]:
				case "Do amount":
					curr_do = str(waarde)
					output[curr_do] = [[] for i in range(5)]
				case "DO":
					output[curr_do][0].append(waarde)
				case "S1":
					output[curr_do][1].append(waarde)
				case "S2":
					output[curr_do][2].append(waarde)
				case "DC":
					output[curr_do][3].append(waarde)
				case "Memory":
					output[curr_do][4].append(waarde)

		began = began or ("Begin with DO and time" in line)

t = "	"

s = f'"{naam_AELEl}": ' + "{\n"
for i, j in output.items():
	s += f'{t}"{i}": [\n'
	for k in j:
		s += f'{t}{t}{str(k)},\n'
	s += f'{t}],\n'
s += "},\n"

print(s)
with open("process.txt", "w") as f:
    f.write(s)