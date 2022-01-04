import numpy as np


class AutoBins:
    r"""
    Automatically create bins for ploting histogram.

    Params:
        - ls (int): minimum number of data in a bin.
        - ps (int):
    """
    def __init__(self, ls: int = 3, ps: int = 30):
        self.ls = ls
        self.ps = ps

    def get_len_step(self, arr: np.ndarray) -> int:
        r"""
        How many bins can be used when data follow uniform distribution.
        """
        return len(arr) // self.ls

    def get_power_step(self, arr: np.ndarray) -> int:
        r"""
        Use the magnitude of # samples to prevent `get_len_step` gives
        too many bins when data is huge.
        """
        if len(arr) == 0:
            return np.nan
        p = np.log10(len(arr))
        return int(p*self.ps)

    def get_mean_diff_step(self, arr: np.ndarray) -> int:
        r"""
        Calculate the mean of neighboring unique value difference.
        """
        if len(arr) == 0:
            return np.nan
        u, c = np.unique(arr, return_counts=True)
        if len(u) == 1:
            return np.nan

        d = np.diff(u)
        w = c[1:]*c[:-1]
        _diff_mean = np.average(d, weights=w)
        _min = int(min(arr))
        _max = int(max(arr))
        return int((_max-_min)/_diff_mean)

    def __call__(self, arr: np.ndarray) -> np.ndarray:
        arr = arr[~np.isnan(arr)]
        if len(arr) == 0:
            return None
        _min = int(min(arr))
        _max = int(max(arr))
        if _min == _max:
            return np.linspace(_min-0.5, _max+0.5, 11)
        _n = np.nanmin([
            self.get_len_step(arr),
            self.get_mean_diff_step(arr),
            self.get_power_step(arr)
        ])
        _max += (_max-_min)/_n
        _n = int(max(_n, 2)) + 1
        return np.linspace(_min, _max, _n)
