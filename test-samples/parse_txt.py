# -*- coding: utf-8 -*-
import csv

namesTables = ('expansionstring','patchstring','string',)

srcTxtUniqueItems = open('../txt-sources/ultimative-4/uniqueitems.txt','rb')
tblUniqueItems = csv.reader(srcTxtUniqueItems,dialect='excel-tab')
