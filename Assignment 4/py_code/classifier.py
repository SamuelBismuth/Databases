# All this code is based on our lecturer slide.
# Here only some modifications are done.

import findspark
from pyspark import SparkContext
import numpy as np

findspark.init("/home/sam/Hardware/pyspark")
sc = SparkContext("local[*]", "Simple App")

# The next input data is based on our lecturer slides.
# We have two class : the spam class (0) and the real class (1).

input_data = sc.parallelize([["buy it paying later ! click me !", 0],
                             ["you won 10000 dollars ! click here !", 0],
                             ["will see you later", 1],
                             ["will you want to meet later ?", 1],
                             ["I'm waiting for you", 1]])

'''input_data = sc.parallelize([["hello there", 0],
                             ["hi there", 0],
                             ["go home", 1],
                             ["see you", 1],
                             ["good bye to you", 1]])'''

# Number of words.
pk = input_data.map(lambda tup: (tup[1], len(tup[0].split()))).reduceByKey(lambda a, b: a + b).collectAsMap()
# Total number of words.
p_tot = sum(pk.values())

# For every word, how many time it appears in his own class.
pki = input_data \
    .flatMap(lambda tup: list(list([(tup[1], w) for w in tup[0].split()]))) \
    .map(lambda tup: ((tup[0], tup[1]), 1)) \
    .reduceByKey(lambda a, b: a + b).collectAsMap()
pkd = input_data \
    .flatMap(lambda tup: set(set([(w, 1) for w in tup[0].split()]))).collectAsMap()
p_totD = len(pkd.keys())

# Once again, the test is based on our lecturer slides.

query = "are you paying too much ? click now !"
class_probs = [(pk[k])  # Number of words in query
               / (float(p_tot))  # Total number of words
               * np.prod(
    np.array([(pki.get((k, i), 0) + 1) /  # For every word, how many time it appears in his own class.
              (float(pk[k]) + p_totD)  # Number of messages per class.
              for i in query.split()]))  # All the words of the new query.
               for k in range(0, 2)]

if __name__ == "__main__":
    print('{0:.17f}'.format(class_probs[0]) + " and " + '{0:.17f}'.format(class_probs[1]))
    print(class_probs)
    y_star = np.argmax(np.array(class_probs))
    print("class: ", y_star)
