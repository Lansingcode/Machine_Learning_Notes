# -*- coding:utf-8 -*-

from time import ctime
import pandas as pd
import numpy as np


# from sklearn.feature_selection import chi2

def chi2(A):
    ''' Compute the Chi-Square value '''
    m, k = A.shape  # 行数 列数

    R = A.sum(axis=1)  # 行求和结果
    C = A.sum(axis=0)  # 列求和结果
    N = A.sum()  # 总和

    res = 0
    for i in range(m):
        for j in range(k):
            Eij = 1.0 * R[i] * C[j] / N
            if Eij != 0:
                res = 1.0 * res + (A[i][j] - Eij) ** 2 / Eij
    return res


def chi_merge(fea_count, dis_count):
    while fea_count.shape[0] > dis_count:
        chi_list = []
        for i in range(fea_count.shape[0] - 1):
            chi_value = chi2(fea_count.iloc[i:i + 2].values)
            chi_list.append([fea_count.index[i], chi_value])

        chi_min_index = np.argmin(np.array(chi_list)[:, 1])
        if chi_min_index == len(chi_list) - 1:
            current_fea = chi_list[chi_min_index][0]
            fea_count.loc[current_fea] = fea_count.loc[current_fea:].sum(axis=0)
            fea_count = fea_count.loc[:current_fea].copy()
        else:
            current_fea = chi_list[chi_min_index][0]
            next_fea = chi_list[chi_min_index + 1][0]
            fea_count.loc[current_fea] = fea_count.loc[current_fea] + fea_count.loc[next_fea]
            fea_count.drop([next_fea], inplace=True)
            chi_list.remove(chi_list[chi_min_index + 1])
    print fea_count


def discrete(path):
    df = pd.read_csv(path, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
    target_name = df.columns[-1]
    fea_names = df.columns[0:-1]
    dis_count = 13
    for f in fea_names:
        fea_count = df[[f, target_name]].copy().groupby([f, target_name]).size().unstack().fillna(0.0)
        chi_merge(fea_count, dis_count)


if __name__ == '__main__':
    print('Start: ' + ctime())
    discrete('iris.csv')
    print('End: ' + ctime())
