from pyspark import SparkContext
from pyspark import SparkConf
from operator import add

import math
import time


sc =SparkContext()

TIMETHRESHOLD = 1

trackerPoints = [
		(1512264894, 30, 27),
		(1512264904, 35, 27),
		(1512264914, 39, 30),
		(1512264924, 30, 31),
		(1512264934, 40, 35),
		(1512264944, 300, 27),
		(1512264954, 315, 27),
		(1512264964, 320, 27),
		(1512264974, 317, 27)
	]
	
targetAreas = 	[ 
		((0,0), (30,30)),
		((31,0), (40,40)),
		((315,0), (400,400))
	]



def inArea(elemPoint):
    point = elemPoint[0]
    area = elemPoint[1]

    if point[1] < area[0][0] or point[1] > area[1][0]:
        return (point, 0)
    if point[2] < area[0][1] or point[2] > area[1][1]:
        return (point, 0)

    return (point, 1)



def AreaOfInterestParalelo(dataset, areas):
    
	dataRDD = sc.parallelize(dataset, 4)
	areasRDD = sc.parallelize(areas,4)
	cartesianAreasData = dataRDD.cartesian(areasRDD)


	labeledPoints = cartesianAreasData.map(inArea).reduceByKey(add)


	orderedData = labeledPoints.sortBy(lambda x: x[0][0]).collect()	
	
	FixationGroups = []
	saccadePoint = False
	
	count = -1
	for tupla in orderedData:
		if tupla[1] == 0:
			saccadePoint = True
		else:
			if len(FixationGroups) == 0 or saccadePoint:
				count += 1
				saccadePoint = False
			FixationGroups.append((count,tupla[0]))
			

	fixationsRDD = sc.parallelize(FixationGroups, 4)

	countPoints = sc.parallelize(FixationGroups, 4).map(lambda x: (x[0], 1)).reduceByKey(add)
	somaCoordTime = fixationsRDD.reduceByKey(lambda (tsa, xa, ya),(tsb, xb, yb): ((tsa+tsb, xa+xb, ya+yb)))
	
	
	zippedCentroids = somaCoordTime.join(countPoints)
	filtredDurations = zippedCentroids.filter(lambda (x,y): y[1] > TIMETHRESHOLD)

	centroids = filtredDurations.map(lambda (k,v): (k, v[0][0]/v[1], v[0][1]/v[1], v[0][2]/v[1] ))
	print centroids.collect()

    

AreaOfInterestParalelo(trackerPoints, targetAreas)
