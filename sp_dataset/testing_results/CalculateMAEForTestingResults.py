import glob

import pandas
from sklearn.metrics import mean_squared_error,mean_absolute_error,median_absolute_error
from statistics import mean,median
# from UtilFunctions import *
import os
fopSEETestingResults=''


lstConfigurations=['within_project/','cross_project/within_repo/','cross_project/cross_repo/']
fpSummary=fopSEETestingResults+'summary.txt'
strHeader='Name\tNumOfTest\tMAE'
f1=open(fpSummary,'w')
f1.write('')
f1.close()
for i in range(0,len(lstConfigurations)):
    configItem=lstConfigurations[i]
    fopProjects=fopSEETestingResults+configItem
    lstFopSetting=glob.glob(fopProjects+'**/')
    for j in range(0,len(lstFopSetting)):
        arrFopSetting=lstFopSetting[j].split('/')
        nameOfSetting=arrFopSetting[len(arrFopSetting)-2]
        lstCsvFiles=glob.glob((lstFopSetting[j]+'*.csv'))
        lstMAEOfSetting=[]
        lstOnlyMAE=[]
        for k in range(0,len(lstCsvFiles)):
            fpCsvItem=lstCsvFiles[k]
            nameOfProject=os.path.basename(fpCsvItem)
            dfInput=pandas.read_csv(fpCsvItem)
            lstItemExpected=dfInput['storypoint'].tolist()
            lstItemRawPrediction = dfInput['raw predictions'].tolist()
            maeScore=mean_absolute_error(lstItemExpected,lstItemRawPrediction)
            lstMAEOfSetting.append([nameOfProject,len(lstItemExpected),maeScore])
            lstOnlyMAE.append(maeScore)

        meanMAE=mean(lstOnlyMAE)
        medianMAE=median(sorted(lstOnlyMAE))

        f1 = open(fpSummary, 'a')
        f1.write('Setting {} {}\nAverage MAE\t{}\nMedian MAE\t{}\n\n'.format(configItem,nameOfSetting,meanMAE,medianMAE))
        f1.write(strHeader+'\n')
        for k in range(0,len(lstMAEOfSetting)):
            f1.write('{}\t{}\t{}\n'.format(lstMAEOfSetting[k][0],lstMAEOfSetting[k][1],lstMAEOfSetting[k][2]))
        f1.write('\n\n\n')
        f1.close()






