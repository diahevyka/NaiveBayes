# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 11:15:19 2019

@author: Diah Hevyka M
"""

import pandas as pandas

tests = pandas.read_csv("TrainsetTugas1ML.csv")
all = tests.count()

#menghitung semua frekuensi
age = tests['age'].value_counts()
workclass = tests['workclass'].value_counts()
education = tests['education'].value_counts()
marital_status = tests['marital-status'].value_counts()
occupation = tests['occupation'].value_counts()
relationship = tests['relationship'].value_counts()
hours_per_week = tests['hours-per-week'].value_counts()
income = tests['income'].value_counts()

#Probabilitas income p(h)
def klasifikasi(income):    
    income_klasifikasi = []
    for i in income:
        income_klasifikasi.append(i / all[8])
    return income_klasifikasi

pH = pandas.DataFrame({
        "Income" : income.index,
        #"Fraction" : income + " / " + all[8],
        "Probability" : klasifikasi(income)
})
print(pH)



#Probability atribut

'''
#proability age
young = age[0] / all[1]
adult = age[1] / all[1]
old= age[2] / all[1]

#probability workclass
private = workclass[0] / all[2]
self_emp_not_inc = workclass[1] / all[2]
local_gov = workclass[2] / all[2]

#probability education
bachelor = education[0] / all[3]
hs_grad = education[1] / all[3]
some_college = education[2] / all[3]

#probability marital_status
married_civ_spouse = marital_status[0] / all[4]
never_married = marital_status[1] / all[4]
divorced = marital_status[2] / all[4]

#probability occupation
exec_managerial = occupation[0] / all[5]
craft_repair = occupation[1] / all[5]
prof_specialty = occupation[2] / all[5]

#probability relationship
husband = relationship[0] / all[6]
not_in_family = relationship[1] / all[6]
own_child = relationship[3] / all[6]

#probability hours_per_week
normal = hours_per_week[0] / all[7]
low = hours_per_week[1] / all[7]
many = hours_per_Week[2] / all[7]
'''

#hitung probability artribut
