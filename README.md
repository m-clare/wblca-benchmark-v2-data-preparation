# CLF WBLCA Benchmark Study v2 - Data Preparation
This repository contains code that was developed and used to produce a dataset associated with the CLF WBLCA Benchmark Study V2 and referenced by the Data Descriptor paper titled "A Harmonized Dataset of High-Resolution Whole Building Life Cycle Assessment Results in North America". The code can be used to clean, prepare, and harmonize WBLCA data. 

The dataset produced from this code is available at: https://github.com/Life-Cycle-Lab/wblca-benchmark-v2-data

## What is the CLF WBLCA Benchmark Study v2?
In 2017, the CLF published the Embodied Carbon Benchmark Study for North American buildings. Since then, the practice of whole-building life cycle assessment (WBLCA) has grown rapidly in the AEC industry, and it’s become clear that more robust and reliable benchmarks are critical for advancing work in this field. The new CLF WBLCA Benchmark Study (Version 2) is built upon research and insights from the 2017 study. The project expanded our research methodology, included more comprehensive data collection, and resulted in a high-resolution dataset of harmonized WBLCA model results and project design characteristics for nearly 300 buildings across the United States and Canada. Outcomes from this project are aimed to enable designers and decision-makers to set reliable embodied carbon targets and understand the potential for reduction throughout the design and construction processes.

## Philosophy
The code provided by this repository processes data for the CLF WBLCA Benchmark Study v2 in three distinct ways. 

![Process for repository processing](https://github.com/Life-Cycle-Lab/wblca-benchmark-v2-data-preparation/blob/main/figures/process/Data%20Preparation%20Detailed%20Breakdown.png)


1. It processes project metadata into a machine readable format that can be analyzed along with environmental impacts.
2. It processes Tally LCA and One Click LCA outputs into a harmonized output with re-classified building elements and materials. 
3. The code finalizes the project metadata and LCA results into two types of data records: a general metadata record with pertinent impacts, and a more in depth collection of impacts per material modeled.

In this way, a novel, harmonized data record can be created by any user with project metadata and LCA results from Tally LCA or One Click LCA. 

## Repository Structure
The repository references Cookiecutter Data Science, a project structure for data analysis such as this study. Cookiecutter Data Science has many useful opinions about structuring a project, and this repository attempts to follow the structure as much as possible. 

The repository is composed of five directories which contain the contents of the code used in the CLF WBLCA Benchmark Study v2. These are:
- *wblca_benchmark_v2_data_prep*
- *scripts*
- *data*
- *figures*
- *references*
  
### wblca_benchmark_v2_data_prep
The *wblca_benchmark_v2_data_prep* repository contains the python files that support the data pipelines in the *scripts* directory. This repository is composed of all helper functions that allow for the creation of the data record. These functions clean the datasets, create new columns, map materials and elements, and filter out the requisite data, among other processes.

### scripts
The *scripts* directory contains the python files that form three distinct data pipelines. These files create the project metadata, LCA results, and data record. 

### data
The *data* directory is a placeholder for real data that can be processed using the methods of the CLF WBLCA Benchmark Study v2. There are four main components of the *data* directory:
- *metadata*
- *lca_results*
- *data_record*
- *logs*
*Metadata*, *lca_results*, and *data_record* each holds the raw, interim, and final processed data for each data pipeline. Logs provides key information for all the scripts run in scripts for each of the main processes. 

### figures
The *figures* directory holds any Sankey charts of material mapping created by sankey_viz.py in *scripts/lca_results*.

### references
The *references* directory provides configuration information for each of the scripts. These yaml files provide lists and dictionaries of key processes such as column creation, column renaming, and value replacement, among other processes. 

## How to use repository
To use this repository, users will need to run the three data pipelines provided in the *scripts* directory. The project metadata and LCA results pipelines are not dependent on each other, but the data record pipeline requires that the other two are run first. These pipelines feed directly into the data record directly, so no user input is needed. 

To run the project metadata pipeline, data entry templates should be placed in *data/metadata/raw*. To run the LCA results pipeline, flattened Tally LCA or One Click LCA tool outputs should be placed in their respective folders in *data/lca_results/raw*. From there, run the scripts in the respective folder in order based on numbering. 

To make this process easier, a makefile is provided for easier command line interfacing. See [this guide](https://cookiecutter-data-science.drivendata.org/using-the-template/#changing-the-makefile) for more details on downloading make.

## How to cite
This code is supplementary to the following works. Please cite both the Data Descriptor and the specific data version used:
- **Data Descriptor:** Benke, B., Chafart, M., Shen, Y., Ashtiani, M., Carlisle, S., and Simonen, K.  *A Harmonized Dataset of High-Resolution Whole Building Life Cycle Assessment Results in North America.* In Review. Preprint available at [*Data Descriptor preprint DOI here, when ready*].
- **Dataset:** Refer to the latest version on Figshare https://doi.org/10.6084/m9.figshare.28462145.v1

## Project Background 
In 2017, the Carbon Leadership Forum (CLF) published the Embodied Carbon Benchmark Study for North American buildings. Since then, the practice of whole-building life cycle assessment (WBLCA) has grown rapidly in the AEC industry, and it’s become clear that more robust and reliable benchmarks are critical for advancing work in this field. The new CLF WBLCA Benchmark Study (Version 2) is built upon research and insights from the 2017 study. The project expanded our research methodology, included more comprehensive data collection, and resulted in a high-resolution dataset of harmonized WBLCA model results and project design characteristics for nearly 300 buildings across the United States and Canada. Outcomes from this project are aimed to enable designers and decision-makers to set reliable embodied carbon targets and understand the potential for reduction throughout the design and construction processes.

## Additional Resources
- [WBLCA Benchmark Study V2 Project Page - Carbon Leadership Forum](https://carbonleadershipforum.org/clf-wblca-v2/)
- [WBLCA Benchmark Study V2 Project Page - Life Cycle Lab at University of Washington](https://www.lifecyclelab.org/projects/)
- Data Descriptor (link TBD)
- [California Carbon Report](https://carbonleadershipforum.org/california-carbon/)
- [Data Entry Template](https://hdl.handle.net/1773/51286)
- [Data Collection User Guide](https://hdl.handle.net/1773/51285)
- Benchmark Study Dashboard (TBD)

## Acknowledgements
We would like to thank the Alfred P. Sloan Foundation, the ClimateWorks Foundation, and the Breakthrough Energy Foundation for supporting this research project. 

We thank this study’s participating design practitioners (data contributors) who provided substantial time and effort in recording and submitting building project data and sharing feedback with the research team. These companies included: Arrowstreet Architects, Arup, BranchPattern, Brightworks Sustainability, Buro Happold, BVH Architecture, DCI Engineers, EHDD, Ellenzweig, Gensler, GGLO, Glumac, Group 14 Engineering, Ha/f Climate Design, HOK, KieranTimberlake, KPFF Consulting Engineers, Lake|Flato, LMN Architects, Mahlum Architects, Mead & Hunt, Inc., Mithun, Perkins&Will, reLoad Sustainable Design Inc., SERA Architects, Stok, The Green Engineer Inc., The Miller Hull Partnership, LLP., Walter P Moore, and ZGF Architects LLP.
