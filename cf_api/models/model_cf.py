from typing import List, Optional
from pydantic import BaseModel

class CFRequest(BaseModel):
    """
    Item: items exist in the cart
    n_item: number of item to recommend
    """
    item: List
    n_item: int

class CFResponse(BaseModel):
    """
    input_item: items exist in the cart
    similar_items: recommendions
    """
    input_item: List
    similar_items: Optional[List]
