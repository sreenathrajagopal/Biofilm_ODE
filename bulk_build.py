#!/usr/bin/env python
# coding: utf-8


def Model_Graded(gene,model,control='control.csv'):
    import os
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
    
    os.mkdir(var)
    file_in = open(model)
    x = file_in.readlines()
    var5 = float(test)
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

    name = var+"/"+var+"_control.R"
    file_out = open(name,"w")
    for i in x:
        file_out.write(i)
    file_out.close()
    file_in.close()
    
    file_in = open(model)
    x = file_in.readlines()
    var5 = 0.5*float(test)
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

    name = var+"/"+var+"_50.R"
    file_out = open(name,"w")
    for i in x:
        file_out.write(i)
    file_out.close()
    file_in.close()
    
    file_in = open(model)
    x = file_in.readlines()
    var5 = 0.25*float(test)
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

    name = var+"/"+var+"_75.R"
    file_out = open(name,"w")
    for i in x:
        file_out.write(i)
    file_out.close()
    file_in.close()
    
    file_in = open(model)
    x = file_in.readlines()
    var5 = 0.01*float(test)
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

    name = var+"/"+var+"_KO.R"
    file_out = open(name,"w")
    for i in x:
        file_out.write(i)
    file_out.close()
    file_in.close()


