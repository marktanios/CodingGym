import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

if __name__ == '__main__':
    conf = SparkConf().setAppName("Trade Republic App")
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, 1)

    quotesInputStream = ssc.socketTextStream("localhost", 8080)

    #print(quotesInputStream.pprint())

    newQuotesStream = quotesInputStream.filter(lambda keyValue: keyValue[1] == "ADD")
    newQuotesStream = newQuotesStream.map(lambda keyValue: print("Hiiii" + keyValue[1]))

    newQuotesStream.pprint()

    ssc.start()  # Start the computation
    ssc.awaitTermination()  # Wait for the computation to terminate

    #newQuotesStream.print()

