import argparse
import json
import pandas as pd
import os


### Script command arguments
# Input file
parser = argparse.ArgumentParser()
parser.add_argument(
    '--in',
    dest="input_file",
    type=str,
    required=True
    )

# Output file
parser.add_argument(
    '--out',
    dest="output_file",
    type=str,
    required=True
    )

# Optional array argument
parser.add_argument(
    '--array',
    dest="array",
    type=str,
    required=False
    )

args = parser.parse_args() 


def main():
    json_input = read_file(args.input_file)
    parsed = parse_json(json_input)
    output_csv(parsed)
    print("Done :)")

# Read the initial JSON file
def read_file(input_file):
    with open(input_file, 'r', encoding='utf8') as f:
	    json_input = json.load(f)
    return json_input

# Looping thorugh items in the JSON file
def parse_json(json_input):
    i = 0
    output_list = {}
    # For complex JSON structure
    # Specifying the name of the array containing key data
    if args.array:
        #Converting supplied array path to a list
        array_path = str(args.array).split(".")
        # Iterating through the items in the list
        # and taking the last item as our array name
        for item in array_path:
            json_input = json_input[item]

        # Flatening the array and putting things
        # together in a new dictionary
        for item in json_input:
            i += 1
            updated_list = {}
            flatenned_item = flatten_json(item,updated_list)
            output_list[str(i)] = flatenned_item
    # For simple JSON structure
    # Loop through all items in the array
    else:
        for item in json_input:
            i += 1
            updated_list = {}
            flatenned_item = flatten_json(item,updated_list)
            output_list[str(i)] = flatenned_item

    return output_list

# Flattening the data structure
def flatten_json(item,updated_list,**kwargs):
    for key,value in item.items():
        # Nested dictionaris
        if isinstance(value, dict):
            new_key = (str(kwargs["parent_key"]) + "_" + str(key)) if kwargs else str(key)
            flatten_json(value,updated_list,parent_key=new_key)
        # Lists
        elif isinstance(value, list):
            flat_list = ', '.join(value)
            new_key = (str(kwargs["parent_key"]) + "_" + str(key)) if kwargs else str(key)
            updated_list[new_key] = flat_list
        # When flattened, add to a new list
        else:
            new_key = (str(kwargs["parent_key"]) + "_" + str(key)) if kwargs else str(key)
            updated_list[new_key] = value

    return updated_list

# Saving data in CSV format
def output_csv(parsed):
    # Save temporary json file
    with open(args.input_file + ".tmp", 'w', encoding='utf-8') as f:
        for line in parsed.values():
            f.write(json.dumps(line)+ "\n")

    # Read the temp file into pandas
    with open(args.input_file + ".tmp", encoding='utf-8') as f:
        df = pd.read_json(f, lines=True)

    # Convert json to csv and output to the new file
    df.to_csv(args.output_file, encoding='utf-8', index=False)

    # Remove temp file
    os.remove(args.input_file + ".tmp")

if __name__=="__main__":
    main()
