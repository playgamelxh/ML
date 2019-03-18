# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


if __name__ == "__main__":
    dates = pd.date_range('20181123', periods=6)
    print(dates)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
    print(df)
