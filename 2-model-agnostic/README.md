# Introduction
This directory automates the "model-agnostic" part of setting up
hydrological models, specifically, running `datatool`, `gistool`, and
`easymore` to extract necessary information to set up various hydrological
models. Below the detail of each workflow is explained:

Modify any segment of the `JSON` file as needed. Get familiar with 
the various tools downloaded and called with this tool first. Visit
the link of each tool!


# Workflows
1. datatool
  https://www.github.com/kasra-keshavarz/datatool

  This workflow simply prepares meteorological datasets by subsetting
  geographical and temporal extents. 

2. gistool
  https://www.github.com/kasra-keshavarz/gistool

  This workflow simply prepares geospatial datasets, such as landcover
  and soil maps, for hydrological modelling purposes. Preparation is
  done by geographical (and if applicable, temporal) subsetting of the
  original datasets, as well as calculating zonal statistics for the
  geofabrics of interest.

3. easymore
  https://github.com/ShervanGharari/EASYMORE

  This workflow calculates aerial average of meteorological datasets
  (in this setup, using the outputs of datatool) for computational
  elements of hydrological models. In the current setup, sub-basins
  are the targets.

4. orchestrator.sh
  https://github.com/kasra-keshavarz/agnostic-orchestrator

  Workflow to execute all mentioned workflows above in a hierarchical
  manner to minimize user interaction with the workflows themself.

5. model-orchestration.json
  https://github.com/kasra-keshavarz/agnostic-orchestrator

  Global configuration file to execute model-agnostic workflows on
  Digital Research Alliance of Canada (DRA)'s Graham HPC in an attempt
  to minimize user interactions with the workflows mentioned above.

  The run the "agnostic orchestrator", you need to simply provide the
  input JSON file to the Bash script. Please make sure all the necessary
  modules and Python environment are loaded beforehand:
  ```console
  (scienv) foo@gra-login1: 2-agnostic$ ./model-agnostic.sh model-agnostic.json
  ```
