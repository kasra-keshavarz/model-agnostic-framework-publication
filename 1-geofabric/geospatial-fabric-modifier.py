#!/usr/bin/env python3
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: meshflow
#     language: python
#     name: meshflow
# ---

# # Geospatial fabric preparation

# In this Notebook, we process the CAMELS-SPAT geospatial fabrics of the "headwater" type catchments. This script is heavily based on `HydrAnT` Python package which focuses on correcting geospatial fabrics to be ready for futher hydrological modelling applications.

# +
# import necessary libraries
# built-in libraries
import os
import argparse

# third-party libraries
import geopandas as gpd

def main():
    # MODIFY THE PATH ACCORDINGLY
    repo_path = '/work/comphyd_lab/data/_to-be-moved/camels-spat-upload/shapefiles/headwater/shapes-distributed/'

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process geospatial fabric data.")
    parser.add_argument('--fabric_code', type=str, required=True, help="Code of the basin to be processed")
    parser.add_argument('--output_root_path', type=str, required=False, default=os.path.join(os.getcwd(), '..', '5-outputs', 'shapefiles', 'headwater', 'shapes-distributed'), help="Root output directory for processed files")
    args = parser.parse_args()

    # Code of the basin to be processed
    fabric_code = args.fabric_code

    # Output path for the processed files
    output_root_path = args.output_root_path
    output_path = os.path.join(output_root_path)

    # Reading files
    riv = gpd.read_file(os.path.join(repo_path, fabric_code, f'{fabric_code}_distributed_river.shp'))
    cat = gpd.read_file(os.path.join(repo_path, fabric_code, f'{fabric_code}_distributed_basin.shp'))

    # columns for further manipulation
    riv_cols = set(riv.columns) - set(['COMID', 'geometry'])

    # assign the corresponding COMID value
    if not riv.loc[0, 'COMID']:
        riv.loc[0, 'COMID'] = cat.loc[0, 'COMID']
        riv['COMID'] = cat['COMID'].astype('Int64')

    # assign other values to zero
    for col in riv_cols:
        riv.loc[0, col] = 0
        riv[col] = riv[col].astype('Int64')

    # assign `order` to 1
    riv.loc[0, 'order'] = 1
    riv['order'] = riv['order'].astype('Int64')

    # assign the geometry to a point
    if riv.loc[0, 'geometry'] is None:
        riv.loc[0, 'geometry'] = gpd.points_from_xy([0], [0])[0]

    # saving both files
    # first creating directory based on the subbasin fabric code
    os.makedirs(output_path, exist_ok=True)

    # saving both files
    riv.to_file(os.path.join(output_path, f'{fabric_code}_distributed_river.shp'), index=False)
    cat.to_file(os.path.join(output_path, f'{fabric_code}_distributed_basin.shp'), index=False)

if __name__ == "__main__":
    main()
