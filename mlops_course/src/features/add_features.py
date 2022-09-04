import pandas as pd
import numpy as np
import click


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def add_features(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Make additional features
    :param input_path:
    :param output_path:
    :return:
    """
    df = pd.read_csv(input_path)
    # Replace "date" with numeric features for year and month.
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['month'] = pd.to_datetime(df['date']).dt.month
    df.drop('date', axis=1, inplace=True)
    # Apartment floor in relation to total number of floors.
    df['level_to_levels'] = df['level'] / df['levels']
    # Average size of room in the apartment.
    df['area_to_rooms'] = (df['area'] / df['rooms']).abs()
    # Fix division by zero.
    df.loc[df['area_to_rooms'] == np.inf, 'area_to_rooms'] = \
        df.loc[df['area_to_rooms'] == np.inf, 'area']

    df.to_csv(output_path)

if __name__ == "__main__":
    add_features()