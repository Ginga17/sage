import os
import csv


# Quick and dirty functions to combine together data in multiple csv files into 1
# The data was generated from buildGraph

# Path to the folder containing CSV files
folder_path = 'outputDir'

def getAllData(rowPos, colPos):
    vals = []
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            # Construct the full path to the CSV file
            file_path = os.path.join(folder_path, filename)
            
            # Open the CSV file
            with open(file_path, 'r') as csvfile:
                # Create CSV reader
                reader = csv.reader(csvfile)
                i = 0
                # Loop through each row in the CSV file
                for row in reader:
                    if i == rowPos:
                        print(row[1])
                        vals.append(row[colPos])
                    i+=1
    return vals

# columns from 1 to 4:
# vertex_cover_sntd,vertex_cover_ntd,vertex_cover_cliquer,vertex_cover_milp
def getAllDataForAlgo(outputFilename, column):
    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)
    
        for i in range(1,5):
            data = getAllData(i, column)
            writer.writerow(data)


def getMemAllData(rowPos, colPos):
    folder_path = 'outputMemoryFinal'
    vals = []
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            # Construct the full path to the CSV file
            file_path = os.path.join(folder_path, filename)
            
            # Open the CSV file
            with open(file_path, 'r') as csvfile:
                # Create CSV reader
                reader = csv.reader(csvfile)
                i = 0
                # Loop through each row in the CSV file
                for row in reader:
                    if i == rowPos:
                        print(row[1])
                        vals.append(row[colPos])
                    i+=1
    return vals

def getAllDataForAlgo(outputFilename, column):
    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        


        for i in range(1,5):
            data = getMemAllData(i, column)
            writer.writerow(data)

    def replace_comma_with_semicolon(file_path):
        try:
            # Open the file in read mode
            with open(file_path, 'r') as file:
                content = file.read()

            # Replace commas with semicolons
            modified_content = content.replace(',', ';')

            # Open the file in write mode and write the modified content
            with open(file_path, 'w') as file:
                file.write(modified_content)

            print("Replacement successful.")

        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")
        except Exception as e:
            print(f"An error occurred: {e}")
    replace_comma_with_semicolon(outputFilename)

      
def getNodeCounts(rowPos, colPos):
    folder_path = 'nodesOrderEdges'

    vals = []
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            # Construct the full path to the CSV file
            file_path = os.path.join(folder_path, filename)
            
            # Open the CSV file
            with open(file_path, 'r') as csvfile:
                # Create CSV reader
                reader = csv.reader(csvfile)
                i = 0
                # Loop through each row in the CSV file
                for row in reader:
                    if i == rowPos:
                        print(row[1])
                        vals.append(row[colPos])
                    i+=1
    return vals

def getNodeCountData(outputFilename, column):
    with open(outputFilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        


        for i in range(1,5):
            data = getNodeCounts(i, column)
            writer.writerow(data)

    def replace_comma_with_semicolon(file_path):
        try:
            # Open the file in read mode
            with open(file_path, 'r') as file:
                content = file.read()

            # Replace commas with semicolons
            modified_content = content.replace(',', ';')

            # Open the file in write mode and write the modified content
            with open(file_path, 'w') as file:
                file.write(modified_content)

            print("Replacement successful.")

        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")
        except Exception as e:
            print(f"An error occurred: {e}")
    replace_comma_with_semicolon(outputFilename)



            
getNodeCountData("nodeCountSemiNTD.csv",1)
getNodeCountData("nodeCountNTD.csv",3)
getAllDataForAlgo("summarySemiNTDMem.csv",1)
getAllDataForAlgo("summaryNTDMem.csv",2)
    