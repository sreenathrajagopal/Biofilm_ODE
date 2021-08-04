args <- commandArgs(trailingOnly = TRUE) # COMMAND LINE ARGUMENTS AQUIRED
model <- args[1]
model_name <- unlist(strsplit(model,"[.]"))
source(model) #Source the ODE model and run for the simulation time
name <- paste(model_name[1],".csv",sep="")
write.table(out,name,sep=',') # export the result into a csv file
