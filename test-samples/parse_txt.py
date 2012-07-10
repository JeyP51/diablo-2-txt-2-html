# -*- coding: utf-8 -*-
import csv
import os.path

namesStringTables = ('expansionstring.txt','patchstring.txt','string.txt',)
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

srcTxtUniqueItems = open('../txt-sources/ultimative-4/uniqueitems.txt','rb')
tblUniqueItems = []
for row in csv.reader(srcTxtUniqueItems, dialect='excel-tab'):
    tblUniqueItems.append(row)

strTblExpString = open(os.path.join("../string-tables/ultimative-4/rus/",namesStringTables[0]),'rb')
tblExpString = []
for row in csv.reader(strTblExpString, dialect='excel-tab'):
    tblExpString.append(row)

# Первая строка с названиями столбцов
firstRow = tblUniqueItems.pop(0)

# Номера нужных столбцоы в таблице уникальных предметов
numsColsUITable = [firstRow.index(num) for num in firstRow if num in namesColsUITable]

# Убираем из таблицы ненужные столбцы
tblUniqueItems = [[tblUniqueItems[j][i] for i in numsColsUITable] for j in xrange(len(tblUniqueItems))]



