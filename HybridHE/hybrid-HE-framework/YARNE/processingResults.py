import glob
import json
import re
import matplotlib.pyplot as plt

def nadublepnt(lijn):
    erna = lijn.replace("\n","").split(": ")[1]
    try:
        float(erna)
        if "." in erna:
            return float(erna)
        else:
            return int(erna)
    except ValueError:
        return erna

All_info = {}
info_useful = {}

for file_path in glob.glob("output/*.txt"):
    if ".output" in file_path:
        info_useful[file_path] = {
            "name_template": 0,
            "pre_ram": 0,
            "post_ram": 0,
            "transfer_size": 0,
            "time_X": [],
            "time_Y":[],
            "time":[],
        }
        with open(file_path, "r") as fh:
            lines = fh.readlines()

            Do_time_started = False
            for line in lines:
                print(line)
                if not Do_time_started:
                    if "Type of the Template" in line:
                        info_useful[file_path]["name_template"] = nadublepnt(line)
                    if "Ram before" in line:
                        info_useful[file_path]["pre_ram"] = nadublepnt(line)
                    if "Ram After" in line:
                        info_useful[file_path]["post_ram"] = nadublepnt(line)
                    if "Begin with DO" in line:
                        Do_time_started = True
                    # Hier in de protocol nog output
                else:
                    if "Do amount" in line:
                        info_useful[file_path]["time_X"].append(nadublepnt(line))
                    elif "Average time" in line:
                        info_useful[file_path]["time_Y"].append(nadublepnt(line))
                    elif line == "\n":
                        pass
                    else:
                        info_useful[file_path]["time"].append([int(x) for x in line.replace("\n","").split(",")])


        print(json.dumps(info_useful, indent = 4))


        for index, inhoud in info_useful.items():

            plt.figure()
            plt.plot(inhoud["time_X"], inhoud["time_Y"])

            box_dict = {}
            for t in range(len(inhoud["time_X"])):
                box_dict[str(inhoud["time_X"][t])] = inhoud["time"][t]

            plt.figure()
            plt.boxplot(box_dict.values(), tick_labels = box_dict.keys())

            plt.show()


        continue
    else:
        continue
        All_info[file_path] = []
        with open(file_path, "r") as fh:
            info = {
                "Test": -1,
                "sizes_RAM": [],
                "unhandled": [],
            }

            lines = fh.readlines()
            for line in lines:
                if line.startswith("Runtime Size:"):
                    result = re.search(r"Runtime Size: (\d+) kB = ([\d\.]+) gB \(([A-Za-z\d\- ]+)\)", line)
                    info["sizes_RAM"].append((result.group(1), result.group(2), result.group(3)))

                elif line.startswith("Test "):
                    All_info[file_path].append(info)

                    info = {
                        "Test": re.search(r"Test (\d+)", line).group(1),
                        "sizes_RAM": [],
                        "unhandled": [],
                    }
                else:
                    info["unhandled"].append(line)
                    if any([a in line for a in ["Begonnen!", "Testcase not found..."]]):
                        pass
                    elif line == "\n":
                        pass
                    else:
                        #print("UNHANDLED", line)
                        pass

        All_info[file_path].append(info)


for index_file, fil_info in All_info.items():
    for info in fil_info:
        max_ram_value = 0
        max_ram = ("0","0","")
        for ram in info["sizes_RAM"]:
            if int(ram[0]) > max_ram_value:
                max_ram_value = int(ram[0])
                max_ram = ram

        info["max_ram"] = max_ram







print(json.dumps(All_info, indent = 4))




## Spline tussen 100, 250, en 500 ofzo, dan met wat normaal-noise
