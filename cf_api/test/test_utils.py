from os.path import dirname, abspath
import sys

ROOT_DIR = dirname(dirname(abspath(__file__)))
sys.path.append(dirname(ROOT_DIR))

from cf_api.utils.utils import custom_cosine_similarity
from sklearn.metrics.pairwise import cosine_similarity

from numpy import append, zeros, int8
from numpy.random import choice
from random import randint

from unittest import TestCase, main

class TestUtils(TestCase):
    
    def test_custom_cosine_similarity(self):
        # create zeros array
        size = 10236
        first_arr = zeros((size,), dtype=int8)
        second_arr = zeros((size,), dtype=int8)

        # iterate 10 times because randint always choice same number if iterate is more than 10
        for i in range(10):
            # select randomly n item 
            step = randint(1,size)
            first_arr_indexes = choice(size, size=step, replace=False)
            second_arr_indexes = choice(size, size=step, replace=False)

            # replace n item values with 1
            first_arr[first_arr_indexes] = 1
            second_arr[second_arr_indexes] = 1
            
            # calculate similarity
            my_result = custom_cosine_similarity(first_arr, second_arr)
            scikit_result = cosine_similarity([first_arr], [second_arr])[0][0]

            print(f"{str(i+1)}. random choice")
            print(my_result)
            print(scikit_result)
            print("\n")

            self.assertAlmostEqual(my_result, scikit_result)

if __name__ == "__main__":
    main()
