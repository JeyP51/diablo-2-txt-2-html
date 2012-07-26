# -*- coding: utf-8 -*-
import csv
import os.path

namesStringTables = ('string.csv','expansionstring.csv','patchstring.csv',)
# Имена нужных столбцов в таблице уникальных предметов
namesColsUITable = ('index','enabled','rarity','lvl req','code',
                               'prop1','par1','min1','max1',
                               'prop2','par2','min2','max2',
                               'prop3','par3','min3','max3',
                               'prop4','par4','min4','max4',
                               'prop5','par5','min5','max5',
                               'prop6','par6','min6','max6',
                               'prop7','par7','min7','max7',
                               'prop8','par8','min8','max8',
                               'prop9','par9','min9','max9',
                               'prop10','par10','min10','max10',
                               'prop11','par11','min11','max11',
                               'prop12','par12','min12','max12',)

srcTxtUniqueItems = open('../txt-sources/ultimative-6/uniqueitems.txt','rb')
tblUniqueItems = []
for row in csv.reader(srcTxtUniqueItems, dialect='excel-tab'):
    tblUniqueItems.append(row)

    
strTblString = open(os.path.join("../string-tables/ultimative-6/rus/",namesStringTables[0]),'r')
tblString = {}
for row in csv.reader(strTblString, dialect='excel'):
    print row
    tblString[row[0]]=row[1]
    
strTblExpString = open(os.path.join("../string-tables/ultimative-6/rus/",namesStringTables[1]),'r')
tblExpString = {}
for row in csv.reader(strTblExpString, dialect='excel'):
    
    tblExpString[row[0]]=row[1]
    
strTblPatchString = open(os.path.join("../string-tables/ultimative-6/rus/",namesStringTables[2]),'r')
tblPatchString = {}
for row in csv.reader(strTblPatchString, dialect='excel'):
    tblPatchString[row[0]]=row[1]

# Первая строка с названиями столбцов
firstRow = tblUniqueItems.pop(0)

# Номера нужных столбцоы в таблице уникальных предметов
numsColsUITable = [firstRow.index(num) for num in firstRow if num in namesColsUITable]

# Убираем из таблицы ненужные столбцы
tblUniqueItems = [[tblUniqueItems[j][i] for i in numsColsUITable] for j in xrange(len(tblUniqueItems))]
tblUniqueItems = [row for row in tblUniqueItems if row[namesColsUITable.index('enabled')] == '1']

print len(tblString)

#for i,value in enumerate(tblUniqueItems):
#    getValue = tblString.get(value[0],'empty_value')
#    if getValue != 'empty_value':
#        tblUniqueItems[i][0] = getValue
#for i,value in enumerate(tblUniqueItems):
#    getValue = tblExpString.get(value[0],'empty_value')
#    if getValue != 'empty_value':
#        tblUniqueItems[i][0] = getValue
#for i,value in enumerate(tblUniqueItems):
#    getValue = tblPatchString.get(value[0],'empty_value')
#    if getValue != 'empty_value':
#        tblUniqueItems[i][0] = getValue
#for row in tblUniqueItems:
#    print row[0].encode('utf-8')