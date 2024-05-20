import os
import time
from datetime import datetime


def process_file(csv_file):
    variables = read_csv(FOLDER_DIR + "/" + csv_file)
    output_result(output_file, csv_file, variables)

def read_csv(csv_file):
    variables = []
    with open(csv_file) as file:
        for line in file:
            if not line.startswith(';') and line.strip():
                variable = line.replace(',', '.').strip()
                variables.append(variable)
    return variables

def output_result(output_file, csv_file, variables):
    points = ','.join(variables)
    cam_name = csv_file.replace('.csv', '')
    cam = "(Enabled:= TRUE, Loaded:= FALSE, Name:= '" + csv_file.replace('.csv', '') + "', Points:=[" + points + "]),"
    with open(output_file, 'a') as output:
        output.write('\n')
        if cam_name.endswith('A'):
            output.write('// ' + cam_name.replace('A','') + '\n')
        output.write(cam)
        print("Cam " + csv_file + " of " + str(len(variables)) + " points, written in " + output_file)


# MAIN PRG
print("Program started")
time.sleep(1)

try:
    FOLDER_DIR = "./Cams"
    output_file = datetime.now().strftime("%Y-%m-%d_%H-%M") + " Output.txt"
    with open(output_file, 'w') as new_file:
        new_file.write('')

    csv_files = [file for file in os.listdir(FOLDER_DIR) if file.endswith('.csv')]
    for csv_file in csv_files:
        process_file(csv_file)

except Exception as error:
    print("An error occurred:", error)
    if os.path.exists(output_file):
        print("deleting output file")
        os.remove(output_file)

time.sleep(100000)
