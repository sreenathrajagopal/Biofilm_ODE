library(doMC)
registerDoMC(4)

var <- c('study')

foreach(x=var) %dopar% {
	setwd(x)
	y = list.files()
	for (k in y){
		source(k)
		write.table(out,gsub(".R$",'.csv',k),sep=",")
	}
	setwd("..")
}


