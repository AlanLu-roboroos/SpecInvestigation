from sys import argv

inputName = argv[1]
outputLines = int(argv[2])
outputName = argv[3]

with open(inputName, "r") as f:
    data = f.readlines()

interval = int(len(data) / outputLines)

with open(outputName, "w") as f:
    for i in range(0, len(data), interval):
        f.write(data[i])
