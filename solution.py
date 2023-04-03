import pandas as pd
import numpy as np


chat_id = 341299061

def solution(x: np.array) -> float:
    fun=lambda x: np.log(x-411)
    x=fun(x)
    return x.mean()
