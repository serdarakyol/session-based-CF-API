import pandas as pd
from numpy import zeros, where, argmax, int8, isnan
from collections import Counter

from cf_api.utils.utils import calculate_similarity_parallel

class Recommendation:
    def __init__(self, data:pd.DataFrame) -> None:
        self.data = data
    
    def recommend(self, items:list, n_item:int):
        column_len:int = self.data.columns.shape[0]

        # create current cart
        current_cart = zeros(shape=column_len, dtype=int8)
        for item in items:
            index = where(self.data.columns == item)
            current_cart[index] = 1
        
        # convert pandas df to numpy array
        data_matrix = self.data.to_numpy(dtype=int8)

        print("current_cart ==> ", type(current_cart[0]))
        print("data_matrix ==> ", type(data_matrix[0][0]))
        print(isnan(current_cart).any())
        print(isnan(data_matrix[0]).any())
        # store scores (dtype is np.float32)
        scores = calculate_similarity_parallel(
            multiple_item=data_matrix,
            single_item=current_cart
        )
        # get recommendation
        similar_sessions = []
        while len(similar_sessions) < n_item:
            idx = argmax(scores)
            if current_cart != self.data.index.to_numpy():
                temp = {
                    "session_id": self.data.index[idx],
                    "similarity": scores[idx],
                    "items": []
                }
                # find which column has 1 value
                item_indexes = where(self.data.iloc[idx].values == 1)
                items = self.data.columns[item_indexes]
                for item in items:
                    temp["items"].append(item)
                similar_sessions.append(temp)
                scores[idx] = 0
                #i += 1
            else:
                scores[idx] = 0

        all_items = [item for ses in similar_sessions for item in ses["items"]]
        likely_items = Counter(all_items).most_common(n_item)
        print(likely_items)
        return likely_items
