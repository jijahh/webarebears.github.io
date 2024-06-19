import pandas as pd
import stat
import scipy.stats as stats
import numpy as np

upperSecondary2021 = pd.read_csv(r'CS 132\proj\Upper Secondary 2021.csv')
upperSecondary2020 = pd.read_csv(r'CS 132\proj\Upper Secondary 2020.csv')
upperSecondary2019 = pd.read_csv(r'CS 132\proj\Upper Secondary 2019.csv')
upperSecondary2018 = pd.read_csv(r'CS 132\proj\Upper Secondary 2018.csv')
upperSecondary2017 = pd.read_csv(r'CS 132\proj\Upper Secondary 2017.csv')
lowerSecondary2021 = pd.read_csv(r'CS 132\proj\Lower Secondary 2021.csv')
lowerSecondary2020 = pd.read_csv(r'CS 132\proj\Lower Secondary 2020.csv')
lowerSecondary2019 = pd.read_csv(r'CS 132\proj\Lower Secondary 2019.csv')
lowerSecondary2018 = pd.read_csv(r'CS 132\proj\Lower Secondary 2018.csv')
lowerSecondary2017 = pd.read_csv(r'CS 132\proj\Lower Secondary 2017.csv')
primary2017 = pd.read_csv(r'CS 132\proj\Primary 2017.csv')
primary2018 = pd.read_csv(r'CS 132\proj\Primary 2018.csv')
primary2019 = pd.read_csv(r'CS 132\proj\Primary 2019.csv')
primary2020 = pd.read_csv(r'CS 132\proj\Primary 2020.csv')
primary2021 = pd.read_csv(r'CS 132\proj\Primary 2021.csv')
localteachers = pd.read_csv(r'CS 132\proj\Teachers (Local).csv')
enrolmentTeachers = pd.read_csv(r'CS 132\proj\Enrollment + Teachers Data.csv')
localEnrolment = pd.read_csv(r'CS 132\proj\Enrollment (Local).csv')
localEnrolmentMinimized = pd.read_csv(
    r'CS 132\proj\Enrollment (Local - Minimized).csv')
primaryLocal = pd.read_csv(r'CS 132\proj\Primary Local.csv')
upperLocal = pd.read_csv(r'CS 132\proj\Upper Local.csv')
lowerLocal = pd.read_csv(r'CS 132\proj\Lower Local.csv')
globalUpperConcat = pd.concat([upperSecondary2021, upperSecondary2020,
                              upperSecondary2019, upperSecondary2018, upperSecondary2017])
globalLowerConcat = pd.concat([lowerSecondary2017, lowerSecondary2018,
                              lowerSecondary2019, lowerSecondary2020, lowerSecondary2021])
globalPrimaryConcat = pd.concat(
    [primary2017, primary2018, primary2019, primary2020, primary2021])
globalConcat = pd.concat(
    [globalUpperConcat, globalLowerConcat, globalPrimaryConcat])


def printOutput(T, p, localMean, globalMean):
    if p <= 0.05:
        print('Reject H0')
    else:
        print('Accept H0')
    print('T:', T)
    print('P:', p)
    print('Local Mean:', localMean)
    print('Global Mean:', globalMean)


Tglobal, pglobal = stats.ttest_ind(
    enrolmentTeachers['Ratio'], globalConcat['Ratio'])
globalMean = globalConcat['Ratio'].mean()
localMean = enrolmentTeachers['Ratio'].mean()
Tprimary, pprimary = stats.ttest_ind(
    primaryLocal['Ratio'], globalPrimaryConcat['Ratio'])
globalPrimaryMean = globalPrimaryConcat['Ratio'].mean()
localPrimaryMean = primaryLocal['Ratio'].mean()
Tupper, pupper = stats.ttest_ind(
    upperLocal['Ratio'], globalUpperConcat['Ratio'])
globalUpperMean = globalUpperConcat['Ratio'].mean()
localUpperMean = upperLocal['Ratio'].mean()
Tlower, plower = stats.ttest_ind(
    lowerLocal['Ratio'], globalLowerConcat['Ratio'])
globalLowerMean = globalLowerConcat['Ratio'].mean()
localLowerMean = lowerLocal['Ratio'].mean()
print("----Global Output (First Research Question):----")
printOutput(Tglobal, pglobal, localMean, globalMean)
print("----Per year level (Second Research Question):----")
print("Primary Level:")
printOutput(Tprimary, pprimary, localPrimaryMean, globalPrimaryMean)
print("Upper Secondary Level:")
printOutput(Tupper, pupper, localUpperMean, globalUpperMean)
print("Lower Secondary Level:")
printOutput(Tlower, plower, localLowerMean, globalLowerMean)
