#!/usr/bin/env python

def Model(gene,perc,model,nam,control='control.csv'):
    import pandas as pd
    y = control
    with open(y) as myfile:
        headRow = next(myfile)
    columns = [x.strip('\n').strip('"') for x in headRow.split(',')]
    columns.insert(0,"count")
    data = pd.read_csv(y, names=columns, skiprows=1)
    
    var = gene
    for i in columns:
        if var+"_Amount" in i:
            var_name = i
    test = data[var_name][100]
    file_in = open(model)
    x = file_in.readlines()
    var5 = float(perc)*float(test)
    i = 0
    while i < len(x):
        if var+"_InitialConcentration =" in x[i]:
            x[i] = "\n"
        elif var_name+"_Dt =" in x[i]:
            x[i] = var_name+"_Dt = "+"0"+"\n"
        elif var_name+" =" in x[i] and "," in x[i]:
            x[i] = var_name+" = "+str(var5)+","+"\n"
        elif var_name+" =" in x[i]:
            x[i] = var_name+" = "+str(var5)+"\n"    
        elif var_name.split("_Amount")[0]+"_Concentration =" in x[i]:
            x[i] = var_name.split("_Amount")[0]+"_Concentration = "+str(var5)+"\n"
        i = i +1 

    name = nam+".R"
    file_out = open(name,"w")
    for i in x:
        file_out.write(i)
    file_out.close()
    file_in.close()





