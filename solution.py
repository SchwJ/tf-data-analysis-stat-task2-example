import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 5191217616 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    # было
    # alpha = 1 - p
    # loc = x.mean()
    # scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    # return loc - scale * norm.ppf(1 - alpha / 2), loc - scale * norm.ppf(alpha / 2)

    # стало

    alpha = 1 - p
    max = np.max(x)
    return max, (max - 0.017) / alpha ** (1/len(x)) + 0.017
