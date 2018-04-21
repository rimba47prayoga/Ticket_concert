from enum import Enum
from datetime import date
from datetime import datetime
from dateutil.parser import parse
from django.db import connection
from django.http import HttpResponse
import json
class CriteriaSearch(Enum):
    Equal = 1
    BeginWith = 2
    EndWith = 3
    NotEqual = 4
    Greater = 5
    Less = 6
    LessOrEqual = 7
    GreaterOrEqual = 8
    Like = 9
    In = 10
    NotIn = 11
    Beetween = 12

class DataType(Enum):
      BigInt = 1; Boolean = 2;Char = 3;DateTime = 4; Decimal = 5; Float = 6; Image = 7; Integer = 8;
      Money = 9; NChar = 10; NVarChar = 11; VarChar = 12; Variant=13;

class Data(Enum):
    Success = 1
    Exists = 2
    Empty = 3

class ResolveCriteria:
    __query = "";
    def __init__(self,criteria=CriteriaSearch.Like,typeofData=DataType.VarChar,columnKey='',value=None):
        self.criteria = criteria
        self.typeofData = typeofData
        self.valueData = value
        self.colKey = columnKey
    def DefaultModel(self):
        filterfield = self.colKey + '__istarswith'
        if self.criteria==CriteriaSearch.Beetween:
            if self.typeofData==DataType.Boolean or self.typeofData==DataType.Char or self.typeofData==DataType.NChar or self.typeofData==DataType.NVarChar \
                or self.typeofData==DataType.VarChar:
                    raise ValueError('value type is in valid')
            if self.typeofData==DataType.DateTime:
                if ',' in str(self.valueData):
                    strValueKeys = str(self.valueData).split(',')
                    filterfield = self.colKey + '__range'
                    startDate = datetime.strptime(self.valueData[0],'Y-m-d')
                    #StartDateRange = (  # The start_date with the minimum possible time
                    #datetime.combine(startDate, datetime.min.time()),
                    ## The start_date with the maximum possible time
                    #datetime.combine(StatDateRange, datetime.max.time())
                    #)
                    endDate = datetime.strptime(self.valueData[1],'Y-m-d')
                    #endDateRange = (  # The start_date with the minimum possible time
                    #datetime.combine(endDate, datetime.min.time()),
                    ## The start_date with the maximum possible time
                    #datetime.combine(endDate, datetime.max.time())
                    #)
                    return {filterfield:[startDate,endDate]}
            elif self.typeofData==DataType.BigInt or self.typeofData==DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Integer or self.typeofData==DataType.Money:
                return {filterfield:[self.valueData[0],self.valueData[1]]}
            else:
                raise ValueError('value type is in valid')
        elif self.criteria==CriteriaSearch.BeginWith:
            if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                return {filterfield:self.valueData}
            else:
                raise ValueError('value type is in valid')
        elif self.criteria==CriteriaSearch.EndWith:
            if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                filterfield = self.colKey + '__iendswith'
            else:
                raise ValueError('value type is in valid')
            return {filterfield:self.valueData}

    def Sql(self):
        if self.criteria==CriteriaSearch.Beetween:
            if self.typeofData==DataType.Boolean or self.typeofData==DataType.Char or self.typeofData==DataType.NChar or self.typeofData==DataType.NVarChar \
                or self.typeofData==DataType.VarChar:
                    raise ValueError('value type is in valid')
            elif self.typeofData==DataType.Integer or self.typeofData==DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                    or self.typeofData==DataType.BigInt:
                values = str(self.valueData).split('-')
                val1 =  values[0];val2 = ''
                ResolveCriteria.__query = " = " + str(val1)
                if len(values) >1:
                    val2 = values[1]
                    ResolveCriteria.__query = " BETWEEN " + str(val1) + " AND " + str(val2)
            if self.typeofData==DataType.DateTime:
                values = str(self.valueData).split('-')
                startDate = values[0]
                strstartDate = str(parse(startDate).strftime("%Y-%m-%d"))#jadinya string datetime
                endDate = strstartDate + " 23:59:59'"
                strEndDate = endDate
                ResolveCriteria.__query = " BETWEEN '" + strstartDate + "'" + " AND '" + strEndDate
                if len(values) > 1:
                    endDate = values[1]
                    strEndDate = str(parse(endDate).strftime("%Y-%m-%d"))#jadinya string datetime
                    #str(parse(self.valueData).strftime("%Y-%m-%d"))#jadinya string datetime
                    ResolveCriteria.__query =  """ >=  STR_TO_DATE('""" + strstartDate + """','%Y-%m-%d') AND  """ + self.colKey + """ <= STR_TO_DATE('""" + strEndDate + """','%Y-%m-%d')"""

        elif self.criteria==CriteriaSearch.BeginWith:
            ResolveCriteria.__query= " LIKE '{0!s}%'".format(str(self.valueData))
        elif self.criteria==CriteriaSearch.EndWith:
                ResolveCriteria.__query= " LIKE '{0!s}%'".format(str(self.valueData))
        elif self.criteria == CriteriaSearch.Equal:
            if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                ResolveCriteria.__query = " = '{0}'".format(self.valueData)
            elif self.typeofData==DataType.Integer or self.typeofData==DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                    or self.typeofData==DataType.BigInt:
                ResolveCriteria.__query = ' = {0}'.format(self.valueData)
            elif self.typeofData==DataType.DateTime:
                strDate = str(parse(self.valueData).strftime("%Y-%m-%d"))#jadinya string datetime
                ResolveCriteria.__query = " BETWEEN '" + strDate + "'" + " AND '" + strDate + " 23:59:59'"
                #ResolveCriteria.__query = """ = STR_TO_DATE('""" + str(self.valueData) + """','%Y-%m-%d')"""
        elif self.criteria==CriteriaSearch.Greater:
            if self.typeofData==DataType.Integer or self.typeofData==DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                or self.typeofData==DataType.BigInt:
                ResolveCriteria.__query = ' > {0}'.format(float(self.valueData))
            elif self.typeofData==DataType.DateTime:
                strDate = str(parse(self.valueData).strftime("%Y-%m-%d"))#jadinya string datetime
                ResolveCriteria.__query = """ > STR_TO_DATE('""" + strDate + """','%Y-%m-%d')"""
        elif self.criteria==CriteriaSearch.GreaterOrEqual:
            if self.typeofData==DataType.Integer or self.typeofData== DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                or self.typeofData==DataType.BigInt:
                ResolveCriteria.__query = ' > {0}'.format(float(self.valueData))
            elif self.typeofData==DataType.DateTime:
                #format data yang di masukan di valueData mesti dijadikan tahun-bulan-tanggal sebelum di proses
                strDate = str(parse(self.valueData).strftime("%Y-%m-%d"))#jadinya string datetime
                ResolveCriteria.__query = """ >= STR_TO_DATE('""" + strDate + """','%Y-%m-%d')"""
        elif self.criteria==CriteriaSearch.In:
            rowFilter = " IN('"
            if ',' in str(self.valueData):
                if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                    strValueKeys = str(self.valueData).split(',')
                    for i in range(len(strValueKeys)):
                        rowFilter += strValueKeys[i] + "'"
                        if i < len(strValueKeys) -1:
                            rowFilter += ","
                    rowFilter += ")"
                    ResolveCriteria.__query = rowFilter
                elif self.typeofData==DataType.Integer or self.typeofData==DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                    or self.typeofData==DataType.BigInt:
                    rowFilter = " IN("
                    strValueKeys = str(self.valueData).split(',')
                    for i in range(len(strValueKeys)):
                        rowFilter += strValueKeys[i] + ""
                        if i < len(strValueKeys) -1:
                            rowFilter += ","
                    rowFilter += ")"
                elif self.typeofData==DataType.DateTime:
                    rowFilter = " IN("
                    strValueKeys = str(self.valueData).split(',')
                    for i in range(len(strValueKeys)):
                        strDate = str(parse(strValueKeys[i]).strftime("%Y-%m-%d"))#jadinya string datetime
                        rowFilter += """STR_TO_DATE('""" + strDate + """','%Y-%m-%d')"""
                        if i < len(strValueKeys) -1:
                            rowFilter += ","
                    rowFilter += ")"
                    ResolveCriteria.__query = rowFilter
            if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                ResolveCriteria.__query = " IN ('{0!s}')".format(str(self.valueData))
            elif self.typeofData==DataType.DateTime:
            #format data yang di masukan di valueData mesti dijadikan tahun-bulan-tanggal sebelum di proses
                ResolveCriteria.__query = parse(self.valueData).strftime("""' IN('%Y-%m-%d')""")
        elif self.criteria==CriteriaSearch.NotIn:
            rowFilter = " NOT IN('"
            if ',' in str(self.valueData):
                if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                    strValueKeys = str(self.valueData).split(',')
                    for i in range(len(strValueKeys)):
                        rowFilter += strValueKeys[i] + "'"
                        if i < len(strValueKeys) -1:
                            rowFilter += ","
                    rowFilter += ")"
                    ResolveCriteria.__query = rowFilter
                elif self.typeofData==DataType.Integer or self.typeofData==DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                    or self.typeofData==DataType.BigInt:
                    rowFilter = " NOT IN("
                    strValueKeys = str(self.valueData).split(',')
                    for i in range(len(strValueKeys)):
                        rowFilter += strValueKeys[i] + ""
                        if i < len(strValueKeys) -1:
                            rowFilter += ","
                    rowFilter += ")"
                elif self.typeofData==DataType.DateTime:
                    rowFilter = """ NOT IN("""
                    strValueKeys = str(self.valueData).split(',')

                    for i in range(len(strValueKeys)):
                         #"""STR_TO_DATE('""" + strValueKeys + """','%Y-%m-%d')"""
                        strDate = str(parse(strValueKeys[i]).strftime("%Y-%m-%d"))#jadinya string datetime
                        rowFilter += """STR_TO_DATE('""" + strDate + """','%Y-%m-%d')"""
                        if i < len(strValueKeys) -1:
                            rowFilter += ","
                    rowFilter += ")"
                    ResolveCriteria.__query = rowFilter
            if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                ResolveCriteria.__query = " NOT IN ('{0!s}')".format(str(self.valueData))
            elif self.typeofData==DataType.DateTime:
            #format data yang di masukan di valueData mesti dijadikan tahun-bulan-tanggal sebelum di proses
                strDate = str(parse(self.valueData).strftime("%Y-%m-%d"))#jadinya string datetime
                ResolveCriteria.__query = """ NOT IN(STR_TO_DATE('""" + strDate + """','%Y-%m-%d'))"""
        elif self.criteria==CriteriaSearch.Less:
            if self.typeofData==DataType.Integer or self.typeofData== DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                or self.typeofData==DataType.BigInt:
                ResolveCriteria.__query = ' < {0}'.format(float(self.valueData))
            elif self.typeofData==DataType.DateTime:
                strDate = str(parse(self.valueData).strftime("%Y-%m-%d"))#jadinya string datetime
                ResolveCriteria.__query = """ < STR_TO_DATE('""" + strDate + """','%Y-%m-%d')"""
        elif self.criteria==CriteriaSearch.LessOrEqual:
            if self.typeofData==DataType.Integer or self.typeofData== DataType.Decimal or self.typeofData==DataType.Float or self.typeofData==DataType.Money \
                or self.typeofData==DataType.BigInt:
                ResolveCriteria.__query = ' <= {0}'.format(float(self.valueData))
            elif self.typeofData==DataType.DateTime:
                strDate = str(parse(self.valueData).strftime("%Y-%m-%d"))#jadinya string datetime
                ResolveCriteria.__query = """ <= STR_TO_DATE('""" + strDate + """','%Y-%m-%d')"""
                #ResolveCriteria.__query = ' <= {%Y-%m-%d}'.format(datetime((str(self.valueData)[0:3]),str(self.valueData)[5:6],str(self.valueData)[7:8]))
        elif self.criteria==CriteriaSearch.Like:
            ResolveCriteria.__query = " LIKE '%{0!s}%'".format(str(self.valueData))
        elif self.criteria==CriteriaSearch.NotEqual:
            if self.typeofData==DataType.Char or self.typeofData==DataType.VarChar or self.typeofData==DataType.NVarChar:
                ResolveCriteria.__query = " <> '{0}'".format(str(self.valueData))
            elif self.typeofData==DataType.Integer:
                ResolveCriteria.__query = ' <> {0}'.format(self.valueData)
        return ResolveCriteria.__query

    def getDataType(strDataType):
        if strDataType == 'int':
            return DataType.Integer
        elif strDataType=='varchar':
            return DataType.VarChar
        elif strDataType == 'bigint':
            return DataType.BigInt
        elif strDataType == 'boolean':
            return DataType.Boolean
        elif strDataType == 'char':
            return DataType.Char
        elif strDataType == 'datetime':
            return DataType.DateTime
        elif strDataType == 'decimal':
            return DataType.Decimal
        elif strDataType == 'float':
            return DataType.Float
        elif strDataType == 'image':
            return DataType.Image
        elif strDataType == 'money':
            return DataType.Money
        elif strDataType == 'nchar':
            return DataType.Char
        elif strDataType =='nvarchar':
            return DataType.NVarChar
        else :
            return DataType.VarChar

    def getCriteriaSearch(strCriteria):
        if strCriteria == 'equal':
            return CriteriaSearch.Equal
        elif strCriteria == 'beginwith':
            return CriteriaSearch.BeginWith
        elif strCriteria == 'endwith':
            return CriteriaSearch.EndWith
        elif strCriteria == 'notequal':
            return CriteriaSearch.NotEqual
        elif strCriteria == 'greater':
            return CriteriaSearch.Greater
        elif strCriteria == 'less':
            return CriteriaSearch.Less
        elif strCriteria == 'lessorequal':
            return CriteriaSearch.LessOrEqual
        elif strCriteria == 'greaterorequal':
            return CriteriaSearch.GreaterOrEqual
        elif strCriteria == 'like':
            return CriteriaSearch.Like
        elif strCriteria == 'in':
            return CriteriaSearch.In
        elif strCriteria == 'notin':
            return CriteriaSearch.NotIn
        elif strCriteria == 'between':
            return CriteriaSearch.Beetween
        else:
            return CriteriaSearch.Like
from functools import wraps
from django.core.exceptions import PermissionDenied
class decorators:
    def ajax_required(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if request.is_ajax():
                return view(request, *args, **kwargs)
            else:
                raise PermissionDenied()
        return _wrapped_view
class query:
    def dictfetchall(cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
class commonFunct:
    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")
                

