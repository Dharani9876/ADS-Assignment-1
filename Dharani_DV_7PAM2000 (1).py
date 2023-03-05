import warnings
warnings.filterwarnings("ignore")
import pandas as pds, matplotlib.pyplot as mplb, numpy as ny, os
import matplotlib
font = {'family' : 'Times New Roman',
            'weight' : 'bold',
            'size'   : 15}
matplotlib.rc('font', **font)

def ReadData():
    alf=os.listdir()
    csvfl=[]
    for a in alf:
        if ".csv" in a and "expenditure" in a:
            fl=pds.read_csv(a)
            mn=a.split("-")[-2].capitalize()
            fullmn=[mn for x in range(len(fl))]
            fl.insert(2,'Month',fullmn)
            csvfl.append(fl)
    expnd=pds.concat(csvfl)
    return expnd
data=ReadData()
data.fillna("Undefined")
data.head(2)
data['Cost Centre']=data['Cost Centre'].fillna(data['Cost Centre'].mean())
def LinePlot(var):
    uniqvar=data[var].unique().tolist()
    for x in uniqvar:
        if type(x)!=str:
            uniqvar.remove(x)
    expnmn=[]
    expnmx=[]
    expnmin=[]
    for ex in uniqvar:
        expnmn.append(data[data[var]==ex]['Cost Centre'].mean())
        expnmx.append(data[data[var]==ex]['Cost Centre'].max())
        expnmin.append(data[data[var]==ex]['Cost Centre'].min())
    mplb.figure(figsize=(8,4))
    rngmn=[i for i in range(len(data[var].unique()))]
    mplb.title("Expense by {}".format(var),fontsize=25,color="b")
    mplb.plot(expnmn,"--xy",label="Average Expense")
    mplb.plot(expnmx,"--*g",label="Maximum Expense")
    mplb.plot(expnmin,"--vr",label="Minimum Expense")
    mplb.xlabel("{}".format(var),fontsize=20,color="b")
    mplb.xticks(rngmn,data[var].unique(),rotation=90)
    mplb.ylabel("Expense",fontsize=20,color="b")
    mplb.legend(loc='best')
    mplb.grid()
    mplb.show()
LinePlot('Month')
LinePlot('Supplier')
def PieChart(ct,num):
    mplb.figure(figsize=(7,7))
    mplb.title("Transaction by Month for Expenditures",fontsize=20,color="b")
    mplb.pie(num,labels=ct,autopct='%1.1f%%')
    mplb.grid()
    mplb.show()
trmnth=data.Month.value_counts()
trmnthcat=trmnth.index.tolist()
trmnthval=trmnth.tolist()
PieChart(trmnthcat,trmnthval)
def CostbyVar(var):
    var_un=data[var].unique().tolist()
    for x in var_un:
        if type(x)!=str:
            var_un.remove(x)
    eadtsm=[]
    for ex in var_un:
        eadtsm.append(sum(data[data[var]==ex]['Cost Centre'].tolist())/len(data[data[var]==ex]['Cost Centre'].tolist()))
    mplb.figure(figsize=(7,7))
    mplb.title("Average Costing by {}".format(var),fontsize=25,color="b")
    mplb.barh(var_un,eadtsm,alpha=0.6,color="b")
    mplb.xlabel("{}".format(var),fontsize=20,color="b")
    mplb.ylabel("Costing",fontsize=20,color="b")
    mplb.xticks(rotation=90)
    mplb.grid()
    mplb.show()
CostbyVar("Expense type")
CostbyVar("Expense area")
CostbyVar('Supplier')