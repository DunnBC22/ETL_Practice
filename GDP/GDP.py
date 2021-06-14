import pandas as pd
from Manipulations import Manipulations


def main():
    data = pd.read_csv('~/Desktop/GDP among World/GDP.csv')

    col_to_remove = ('Anthem', 'Government', 'Population Rank',
                     'World Percentage', 'Growth Rate', 'Capital City')
    col_with_dollar_sign = ('GDP Per Capita', 'GDP (IMF)', 'GDP (UN)')
    col_with_commas = ('Area', 'Land Area')
    col_with_percent_sign = ('2020 World Percentage',
                             '2020 Population Rank', '2020 Growth Rate')
    currency_convert = ('GDP (IMF)', 'GDP (UN)')
    fact_tables_to_create = ['Region', 'Subregion']

    for x in col_to_remove:
        Manipulations.remove_column(data, x)

    for x in col_with_dollar_sign:
        data[x] = Manipulations.remove_dollar_sign(data, x)

    for x in col_with_commas:
        data[x] = Manipulations.remove_the_commas(data, x)

    for x in col_with_percent_sign:
        data[x] = Manipulations.remove_trailing_percent_sign(data, x)

    data = Manipulations.strip_whitespace(data)

    # fact table creation for the two columns
    for x in fact_tables_to_create:
        data[x] = Manipulations.convert_to_dim_table(data, x)

    for x in currency_convert:
        data[x] = Manipulations.add_appropriate_num_of_zeros(data, x)
        #col = col.apply(lambda x: x[:-3])
        data[x] = data[x].map(lambda x: int(x) if isinstance(x, int) else x)

    # Make sure to output the main file (put this function after the following function)
    pd.set_option("max_colwidth", 20)
    output_file_name = r'~/Desktop/GDP among world/new/Main.csv'
    data.to_csv(output_file_name, index=False)

    print(data.head(25))
    print(data.info())


if __name__ == '__main__':
    main()
    quit()
