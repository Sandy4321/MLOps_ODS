import pandas as pd
import click


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
@click.argument("region_id", type=click.INT)
def select_region(input_path: str, output_path: str, region_id: int):
    """
    Function selects the listings belonging to a specified city.
    :param input_path:
    :param output_path:
    :param region_id:
    :return:
    """
    df = pd.read_csv(input_path)
    df = df[df['region'] == region_id]
    df.drop('region', axis=1, inplace=True)
    print(f'Selected {len(df)} samples in region {region_id}.')
    df.to_csv(output_path)

if __name__ == "__main__":
    select_region()