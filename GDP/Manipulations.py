import os
import pandas as pd
from decimal import Decimal


class Manipulations:
    def remove_column(dataframe, column):
        '''if the column exists, delete it; otherwise ignore this function'''
        del dataframe[column]
        return dataframe

    def remove_trailing_percent_sign(dataframe, column):
        return dataframe[column].replace(
            regex=r'%', value='')

    def remove_the_commas(dataframe, column):
        return dataframe[column].replace(
            regex=r',', value='')

    def remove_dollar_sign(dataframe, column):
        return dataframe[column].replace(
            regex=r'\$', value='')

    def add_appropriate_num_of_zeros(dataframe, column):
        col = dataframe[column]
        ltl = col.apply(lambda x: x[-2:])
        col = col.apply(lambda x: x[:-3])
        col = pd.to_numeric(col, errors='coerce')
        print()
        lil_enum = enumerate(ltl)
        for idx, val in lil_enum:
            if (val == 'Bn'):
                col[idx] = col[idx]*1000000000
            elif (val == 'Mn'):
                col[idx] = col[idx]*1000000
            elif (val == 'Tn'):
                col[idx] = col[idx]*1000000000000
        return col.apply(lambda x: format(x, "-20,.0f"))

    def strip_whitespace(data_frame):
        return data_frame.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    def convert_to_dim_table(dataframe, column):
        '''replace the values in the column and call a
        method to create the dictionary to make into a table'''
        unique_vals = dataframe[column].unique()
        orig_dict = dict(enumerate(unique_vals, 1))
        reversed_dict = dict([(value, index)
                              for (index, value) in orig_dict.items()])
        dataframe[column].replace(reversed_dict, inplace=True)

        output_file_data = pd.DataFrame.from_dict(orig_dict, orient='index')
        file_name = os.path.join(
            r'~/Desktop/GDP among world/new/' + column + '.csv')
        output_file_data.to_csv(file_name, index_label='Index', header=column)
        return dataframe[column]
