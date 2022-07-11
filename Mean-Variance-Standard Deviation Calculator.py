import numpy as np
def calculate(a):
    if len(a)==9:
        arr = np.asarray(a).reshape(-1,3)
        print(arr)
        Dict = dict({
            'mean': [arr.mean(axis=0), arr.mean(axis=1), arr.mean()],
            'variance': [arr.var(axis=0),arr.var(axis=1), arr.var(axis=None)],
            'standard deviation': [arr.std(axis=0), arr.std(axis=1), arr.std()],
            'max': [arr.max(axis=0), arr.max(axis=1), arr.max()],
            'min': [arr.min(axis=0), arr.min(axis=1), arr.min()],
            'sum': [arr.sum(axis=0), arr.sum(axis=1), arr.sum()]
        })
        return Dict
    else:
        print("wrong input")
print(calculate([0,1,2,3,4,5,6,7,8]))