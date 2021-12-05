import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

tab = pd.read_html('https://www.cbr.ru/hd_base/bliquidity/?UniDbQuery.Posted=True&UniDbQuery.From=09.01.2017&UniDbQuery.To=07.10.2021')

print(len(tab))

df = tab[0]

print(df.head)