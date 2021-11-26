# Biofilm_ODE
The ODE model is built for studying the biofilm formation in E. coli, considering the key enzymes involved in the formation of the same.

# Run.R

	Run.R is a script that has been built to read an ODE model built in the R environment and run the simulation for stipulated time. This result is later exported into a csv file. The result file includes the change in amount of each of the key species in the model.

	## Installation

	This script requires the user to install R programming language.
	The following libraries are essential for running the script post the installation of R.
	1. deSolve library and its associated dependancy

	The model file must be present in the same directory as the script as the same is passed as an argument to the script.

	## USAGE

	Rscript Run.R control.R

	## Input
	control.R (The model for which the simulation is attempted, Example for wildtype is presented)

	## Output

	control.csv


# model_build.py
	 model_build.py is a script containing the function designed to parse the R ODE model and construct models of Knock out and Over expression as per user's discretion.

	## Installation

	This script requires the User to install Python Programming Language.
	The following libraries are reuired for running the script.
	1. Pandas

	
	The Files passed on as the argument should be present in the same directory in which the function is called.

	## Usage

	from model_build import Model
	Model('CsrA',0.25,'control.R','CsrA_75_KO','control.csv')

	## Inputs
	Argument 1 - The species to be augmented in the Model (Case sensitive ensure the first letter is capital so the the protein is selected for perturbation)
	Argument 2 - The multiplier to the control value of the species towards which the user wants to observe the changes (decimal notation). For example, 75% reduction in CsrA, the user uses a multiplier of 0.25 asking the program to reduce the species from control condition to 75% reduced presence in the system
	Argument 3 -  The wild type ODE model
	Argument 4 - Custom name that can be given to save the model created (Output file name)
	Argument 5 - The control run data obtained as a csv from the earlier script is used to obtain the control condition Amount of the species perturbed.

# bulk_build.py
	Bulk_build.py is a script containing a function to parse the R ODE model and construct automatically a graded KO model building models corresponding to 50%,75% and 99% Knockdowns of species selected.

	## Installation

	This script requires the User to install Python Programming Language.
	The following libraries are required for running the script.
	1. Pandas

	## Usage

	from bulk_build import Model_Graded
	Model_Graded(gene,model,control_result)

	## Inputs
	Argument 1 - The species to be augmented in the Model (Case sensitive ensure the first letter is capital so the the protein is selected for perturbation)
	Argument 2 -  The wild type ODE model
	Argument 3 - The control run data(WILD TYPE) obtained as a csv from the earlier script is used to obtain the control condition Amount of the species perturbed.

# image_bulk.py
	image_bulk.py is a script containing a function to read all the csv files within the directory containing the Bulk perturbation model files and their corresponding result file post simulations for each of the model.
	
	## Installation

	This script requires the User to install Python Programming Language.
	The following libraries are rqeuired for running the script.
	1. Pandas
	2. Plotly


	## Usage
	from image_bulk import Image_Bulk
	Image_Bulk(title_name,species_perturbed,species_plotted)

	## Inputs
	Argument 1 - The title for the plot being generated
	Argument 2 - The species that has been perturbed. NOTE - The function should be called inside the folder containing the perturbation results
	Argument 3 - The species whose Amount is plotted with respect to time to observe the impact of the perturbation on the specific target.

# image.py
	image.py is a script containing a function to read a csv files of interest and develop a plot of a particular species Amount with respect to time.	
	## Installation

	This script requires the User to install Python Programming Language.
	The following libraries are required for running the script.
	1. Pandas
	2. Plotly


	## Usage
	from image import Image
	Image(title_name,species_perturbed,species_plotted,result_file)

	## Inputs
	Argument 1 - The title for the plot being generated
	Argument 2 - The species that has been perturbed. NOTE - The function should be called inside the folder containing the perturbation results
	Argument 3 - The species whose Amount is plotted with respect to time to observe the impact of the perturbation on the specific target.
	Argument 4 - The csv file that contains the data to be read and plotted.

#script.R 
	script.R is a script containing a function to read the files created by the bulk_build.py script and run each of the model and build the results for the same.

	##Usage 
	Edit the "var" variable in in the script.R to define the species being perturbed.
	Use the command below from the home directory where the directory of the species being perturbed is present.
	Rscript script.R 

# bulk_build_oe.py
	Bulk_build.py is a script containing a function to parse the R ODE model and construct automatically a graded OE/KO model building models corresponding to 2X,4X OE and 99% Knockdown of species selected.

	## Installation

	This script requires the User to install Python Programming Language.
	The following libraries are reuired for running the script.
	1. Pandas

	## Usage

	from bulk_build import Model_Graded
	Model_Graded(gene,model,control_result)

	## Inputs
	Argument 1 - The species to be augmented in the Model (Case sensitive ensure the first letter is capital so the the protein is selected for perturbation)
	Argument 2 -  The wild type ODE model
	Argument 3 - The control run data(WILD TYPE) obtained as a csv from the earlier script is used to obtain the control condition Amount of the species perturbed.


# Rawdata_studies
	The folder contains the raw data for the studies presented in the manuscript. Each folder contains the model file pertaining to the perturbation and the corresponding result.
