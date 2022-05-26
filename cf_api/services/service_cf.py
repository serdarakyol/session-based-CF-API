from pandas import DataFrame
from numpy import zeros, where, argmax, int8
from numpy.random import choice

from collections import Counter

from cf_api.utils.utils import calculate_similarity_parallel

class Recommendation:
    def __init__(self, data:DataFrame) -> None:
        self.data = data
    
    def recommend(self, items:list, n_item:int):
        column_len:int = self.data.columns.shape[0]

        # create current cart
        current_cart = zeros(shape=column_len, dtype=int8)
        for item in items:
            indices = where(self.data.columns == item)
            current_cart[indices] = 1
        
        # convert pandas df to numpy array
        data_matrix = self.data.to_numpy(dtype=int8)

        # store scores (dtype is np.float64)
        scores = calculate_similarity_parallel(
            multiple_item=data_matrix,
            single_item=current_cart
        )

        # find the most n similar items
        similar_items = []
        while len(similar_items) < n_item:
            idx = argmax(scores)
            if current_cart != self.data.index.to_numpy():
                # find which column has 1 value
                item_indexes = where(self.data.iloc[idx].values == 1)
                similar_session_items = self.data.columns[item_indexes]

                # store all of the products from similar sessions
                for item in similar_session_items:
                    similar_items.append(item) 
                scores[idx] = 0

            else:
                scores[idx] = 0

        # find frequency of similar item based onn similar sessions 
        likely_items = Counter(similar_items).most_common(n_item)
        del similar_items

        # recommend if item not in cart
        final_recommendations = []
        for recommend_item in likely_items:
            if recommend_item[0] not in items:
                final_recommendations.append(recommend_item[0])
        
        # if there are not any similar item, randomly recommend
        if len(final_recommendations) == 0:
            final_recommendations = self.data.columns[choice(column_len, size=n_item, replace=False)].to_list()
    
        return final_recommendations
