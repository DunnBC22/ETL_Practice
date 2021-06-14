import os
import numpy as np
import pandas as pd

col_names = ['Age', 'Work Class', 'Group Pop',
             'Edu', 'Edu #', 'Marital Status', 'Occupation', 'Relationship', 'Race', 'Sex', 'Cap Gains', 'Cap Loss', 'Hrs/Wk', 'Native Country', 'Under-Over 50K']

data_types = {'Age': np.int32, 'Work Class': str, 'Group Pop': np.int32,
              'Edu': str, 'Edu #': np.int32, 'Marital Status': str, 'Occupation': str, 'Relationship': str, 'Race': str, 'Sex': str, 'Cap Gains': np.int64, 'Cap Loss': np.int64, 'Hrs/Wk': np.int32, 'Native Country': str, 'Under/Over 50K': str}

data = pd.read_csv(
    '~/Desktop/Data Sets - May 2021/Adult Incomes in the United States/adult-data.csv', header=0, names=col_names, dtype=data_types)

print(data.info(), '\n')
print(data.describe(), '\n')

replace_q_mark = ('Work Class', 'Occupation', 'Native Country')

for x in replace_q_mark:
    data[x].replace(' ?', 'Null', inplace=True)

columns_to_create_dict = ('Work Class', 'Edu', 'Marital Status', 'Occupation', 'Race',
                          'Sex', 'Relationship', 'Native Country', 'Under-Over 50K')

resulting_dfs = []

for x in columns_to_create_dict:
    d = data[x].unique()
    data_dict = dict(enumerate(d.flatten(), 1))
    reversed_data_dict = dict([(value, key)
                              for key, value in data_dict.items()])
    # replace the values with the keys (.replace method)
    data[x].replace(reversed_data_dict, inplace=True)
    # create dataframes/tables from dictionary
    resulting_dfs.append(data_dict)

output_columns = list(columns_to_create_dict)
i = 0

for x in resulting_dfs:
    print(output_file := pd.DataFrame.from_dict(
        x, orient='index'))
    # Write all of this updated info to a 'new' file
    file_name = os.path.join(
        r'~/Desktop/Data Sets - May 2021/Adult Incomes in the United States/new/' + output_columns[i] + '.csv')
    output_file.to_csv(file_name, index_label='Index',
                       header=[output_columns[i]])
    i += 1

del(data['Edu #'])

print(data.head(25), '\n')
print(data.info(), '\n')

data.to_csv(
    '~/Desktop/Data Sets - May 2021/Adult Incomes in the United States/new/main.csv', index=False)
