#!/bin/bash

# input values
root_path="$1"
model="$2"

# Path to the directory containing the shapefiles
shapefiles_path="/work/comphyd_lab/data/_to-be-moved/camels-spat-upload/shapefiles/headwater/shapes-distributed"

# Get all directory names (just the basenames)
mapfile -t new_names < <(find "$shapefiles_path" -maxdepth 1 -type d -printf "%f\n" | sort | tail -n +2)  # tail skips the '.' directory

# Loop through each name
for new_name in "${new_names[@]}"; do
    # Create the directory if it doesn't exist
    mkdir -p "$root_path/$new_name"

    # Process the JSON file with sed to replace all occurrences
    if [[ -z "$root_path/$model/${model}.json" ]]; then
      sed "s/CATCHMENT/$new_name/g" "$root_path/${model}/${model}.json" > "$root_path/$new_name/${model}.json"
    fi
    if [[ -z "$root_path/$model/${model}.slurm" ]]; then
      sed "s/CATCHMENT/$new_name/g" "$root_path/${model}/${model}.slurm" > "$root_path/$new_name/${model}.slurm"
    fi

    echo "Created $root_path/$new_name/$model"
done
