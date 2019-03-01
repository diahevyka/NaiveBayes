# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 11:15:19 2019

@author: Diah Hevyka M
"""

import pandas as pd

train = pd.read_csv("TrainsetTugas1ML.csv")
test = pd.read_csv("TestsetTugas1ML.csv")

all = train.count()

#menghitung semua frekuensi
income = train['income'].value_counts()

#Probabilitas income p(h)
def klasifikasi(income):    
    income_klasifikasi = []
    for i in income:
        income_klasifikasi.append(i / all[8])
    return income_klasifikasi

pH = pd.DataFrame({
    "Income" : income.index,
    #"Fraction" : income + " / " + all[8],
    "Probability" : klasifikasi(income)
})
#print(pH)

atribut = train.columns[1:-1]
atribut = atribut.drop(['relationship'])
#print(atribut)

def naivebayes(atribut, train):
    hasil = {}
    for kelas, kelasdata  in train.groupby("income"):
        hasil.update({kelas: {} })
        for attr in atribut:
            hasil[kelas].update({attr: {} })
            for a,b in kelasdata.groupby(attr):
                penyebut = len(kelasdata)
                pembilang = len(b)
                hasil[kelas][attr].update({ a: pembilang / penyebut })
    return hasil

result = []

hasil = naivebayes(atribut, train)

for index,value in test.iterrows():
    #print(value["age"])
    outcome = []
    for kelas, data in train.groupby("income"):
        pC = 1
        for atr in atribut:
            nilai = value[atr]
            pC *= hasil[kelas][atr][nilai]
        prob = pC * pH.loc[pH["Income"] == kelas].Probability.values
        outcome.append([prob, kelas])
    if (outcome[0][0] > outcome[1][0]):
        result.append(outcome[0][1])
    else:
        result.append(outcome[1][1])
print(result)

pd.DataFrame(result).to_csv("TebakanTugas1ML.csv", index=False, header=False)            