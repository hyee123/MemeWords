import findspark
findspark.init()
from pyspark import SparkConf, SparkContext
import random

def initMapper (line):
    l = line.split(",")
    if len(l) > 4:
        return (1,l[1],l[3])
    else:
        return(9,"empty","empty")

if __name__ == "__main__":
    random.seed(7)
    conf = SparkConf().setAppName("NewsDataConverter")
    sc = SparkContext(conf = conf)
    l1 = sc.textFile("uci-news-aggregator.csv")

    l2 = l1.map(initMapper)
    randomInserted  = l2.mapValues(lambda x : (x,random.randint(1,10000000)))
    
    subspace = randomInserted.sample(False,0.085,5)
#    l3 = subspace.take(10000)
#    l4 = subspace.collect()
#    for l in l3:
#        print l 
    result = subspace.collect()
    f1 = open("news.data","w+")
    for results in result:
        f1.write(str(results[0]).encode('utf-8') + "|" + results[1][0].encode('utf-8') + "|" + str(results[1][1]).encode('utf-8') + "\n")

    f1.close()
        

