import findspark
findspark.init()
from pyspark import SparkConf, SparkContext


def newsInit (line):
    l = line.split("|")
    if len(l) == 3:
        return (int(l[2]),(l[1],int(l[0])))
    else:
        return (3,("",10000000000))

def memesInit(line):
    l = line.split("|")
    if len(l) == 4:
        return (int(l[3]),(l[1],int(l[0])))
    else:
        return(3,("",10000000000))

if __name__ == "__main__":

    conf = SparkConf().setAppName("dataCombiner")
    sc = SparkContext(conf = conf)

    news = sc.textFile("news.data")
    
    memes = sc.textFile("memes_bot3.data")

    newsStart = news.map(newsInit)
    memesStart = memes.map(memesInit)

   # srted = newsStart.sortBy(lambda a : a[0])
   # r = srted.collect()
    merged = memesStart.union(newsStart)
   # r = merged.collect()
    #result = merged.take(500)
    srted = merged.sortBy(lambda a: a[0])
    filtered = srted.filter(lambda a: a[1][1] != 10000000000)
    #r = srted.collect()
    result = filtered.collect()
   # for results in result:
   #     print(results[1])
  #  print result
    
    f1 = open("mnClean.data","w+")
    for results in result:
        f1.write(str(results[1][1]) + "|||" + results[1][0].encode('utf-8') + "\n")

    f1.close()  
