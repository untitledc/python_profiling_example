# -*- coding: utf-8 -*-

import cProfile
import csv

import numpy as np
import pandas as pd

N_COL = 100
N_ROW = 500
CSV_FN = 'm.csv'


def gen_random_matrix():
    return np.random.rand(N_ROW, N_COL) * 10


def gen_header():
    header = []
    for c in range(N_COL):
        header.append('f{}'.format(c))
    return header


def write_csv(matrix, header):
    with open(CSV_FN, 'w') as f_out:
        writer = csv.DictWriter(f_out, header)
        writer.writeheader()
        for row in matrix:
            writer.writerow(dict(zip(header, row)))


def to_dataframe(filename):
    return pd.read_csv(filename)


def plus_one(df):
    for r in df.index:
        for c in df.columns:
            df.at[r, c] += 1


def main():
    matrix = gen_random_matrix()
    header = gen_header()
    write_csv(matrix, header)
    df_0 = to_dataframe(CSV_FN)
    plus_one(df_0)


if __name__ == '__main__':
    pr = cProfile.Profile()

    pr.enable()
    main()
    pr.disable()

    pr.dump_stats('example.prof')
    pr.print_stats()

