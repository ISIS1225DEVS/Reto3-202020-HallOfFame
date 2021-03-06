"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 .
 """

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def AccidentsSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.AccidentsSize(analyzer)


def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)

def getAccidentsByDate(analyzer, Date):
    """
    Retorna el total de crimenes en un rango de fechas
    """
    dic={}
    for i in range(1,5):
        num=getAccidentsBySeverity(analyzer,Date,i)
        dic[i]=num
    return dic

def getAccidentsBySeverity(analyzer, Date,
                         Severity):
    """
    Retorna el total de crimenes de un tipo especifico en una
    fecha determinada
    """
    Date = datetime.datetime.strptime(Date, '%Y-%m-%d')
    return model.getAccidentsBySeverity(analyzer, Date.date(),Severity)

def getAccidentsBeforeDate(analyzer, Date):
    Date=datetime.datetime.strptime(Date, '%Y-%m-%d')
    return model.getAccidentsBeforeDate(analyzer, Date)


def getAccidentsbyrange(analyzer, inicialdate, finaldate):
    inicialdate = datetime.datetime.strptime(inicialdate, '%Y-%m-%d')
    finaldate = datetime.datetime.strptime(finaldate, '%Y-%m-%d')
    dic = model.getAccidentsbyrange(analyzer, inicialdate.date(), finaldate.date())
    total= dic[1]+dic[2] + dic[3]+ dic[4]
    maximo =()
    mayor = 0
    for i in range(1,5):
        if dic[i]>mayor:
            mayor = dic[i]
            maximo = (i)
    return (dic,total, maximo, mayor)

def getAccidentsByState(analyzer,initialDate,finalDate):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    info = model.getAccidentsByState(analyzer,initialDate.date(),finalDate.date())
    State = info[0]["State"]
    count = info[0]["Count"]
    date = datetime.date.isoformat(info[1])
    return (State, count, date)
    
    
def getAccidentsByTime(analyzer,initialTime,finalTime):
    initialTime = "1111-11-11 "+ initialTime+":00"
    finalTime = "1111-11-11 "+ finalTime+":00"
    return model.getAccidentsByTime(analyzer,initialTime,finalTime)

def getAccidentsBylocation(analyzer,latitud,longitud,radio):
    return model.getAccidentsBylocation(analyzer,latitud,longitud,radio)

