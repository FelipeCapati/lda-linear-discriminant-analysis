import pandas as pd
import numpy as np
from enum import Enum


class LdaType(Enum):
    One = 1
    Two = 2
    Three = 3


class LDA:
    def __init__(self):
        self.eig_pairs = None
        self.w = None
        self.data = None
        self.target_column_name = None

    @staticmethod
    def __get_sw_from_df_data(data: pd.DataFrame, target_column_name: str) -> pd.DataFrame:
        sw = None
        once = True
        target_classes = np.unique(data[target_column_name].values)
        for target_class in target_classes:
            if once:
                target_slice = data.loc[data[target_column_name] == target_class].drop(columns=[target_column_name])
                diff = target_slice - target_slice.mean().to_frame().T.values
                sw = diff.T.dot(diff)
                once = False
            else:
                target_slice = data.loc[data[target_column_name] == target_class].drop(columns=[target_column_name])
                diff = target_slice - target_slice.mean().to_frame().T.values
                sw = sw + diff.T.dot(diff)
        return sw

    @staticmethod
    def __get_sb_from_df_data(data: pd.DataFrame, target_column_name: str) -> pd.DataFrame:
        sb = None
        once = True
        target_classes = np.unique(data[target_column_name].values)
        for target_class in target_classes:
            if once:
                once = False
                overall_mean = data.drop(columns=[target_column_name]).mean().to_frame().T
                target_slice = data.loc[data[target_column_name] == target_class].drop(columns=[target_column_name])
                target_mean = target_slice.mean().to_frame().T.values
                n = len(target_slice)
                diff = overall_mean - target_mean
                sb = n * diff.T.dot(diff)
            else:
                overall_mean = data.drop(columns=[target_column_name]).mean().to_frame().T
                target_slice = data.loc[data[target_column_name] == target_class].drop(columns=[target_column_name])
                target_mean = target_slice.mean().to_frame().T.values
                n = len(target_slice)
                diff = overall_mean - target_mean
                sb = sb + n * diff.T.dot(diff)
        return sb

    @staticmethod
    def _get_sorted_eigen_pairs(sw: pd.DataFrame, sb: pd.DataFrame) -> list:
        eigen_values, eigen_vectors = np.linalg.eig(np.linalg.inv(sw.values).dot(sb.values))
        eigen_pairs = [(np.abs(eigen_values[i]), eigen_vectors[:, i]) for i in range(len(eigen_values))]
        eigen_pairs = sorted(eigen_pairs, key=lambda k: k[0], reverse=True)

        return eigen_pairs

    def fit(self, data: pd.DataFrame, target_column_name: str, log: bool = False):
        self.data = data
        self.target_column_name = target_column_name
        sw = self.__get_sw_from_df_data(data=self.data, target_column_name=self.target_column_name)
        sb = self.__get_sb_from_df_data(data=self.data, target_column_name=self.target_column_name)
        self.eig_pairs = self._get_sorted_eigen_pairs(sw=sw, sb=sb)

        if log:
            print(self.eig_pairs)

        return self.eig_pairs

    def conversion(self, type:LdaType):
        if self.eig_pairs is None:
            raise Exception("[LDA][Error] - Run First Fit method")

        shape = len(self.data.columns) - 1

        if type == LdaType.One:
            self.w = np.hstack((self.eig_pairs[0][1].reshape(shape, 1)))
        if type == LdaType.Two:
            self.w = np.hstack((self.eig_pairs[0][1].reshape(shape, 1), self.eig_pairs[1][1].reshape(shape, 1)))
        if type == LdaType.Three:
            self.w = np.hstack((self.eig_pairs[0][1].reshape(shape, 1), self.eig_pairs[1][1].reshape(shape, 1), self.eig_pairs[2][1].reshape(shape, 1)))

        return self.data.drop(columns=[self.target_column_name]).dot(self.w)
