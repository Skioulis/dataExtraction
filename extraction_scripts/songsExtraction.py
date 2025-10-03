import pandas as pd

file_Path='../old Data/'
file_Name='randomSongs.csv'

def get_random_songs():
    """
    Fetches a random selection of songs from a dataset and saves them to a new CSV file.
    To work with a smaller dataset for testing purposes.

    Reads a CSV file containing song data, selects a random sample of 100 songs from it,
    and writes the resulting sample into a new CSV file. The function is primarily used
    for creating a smaller random subset of the original dataset.

    Raises:
        FileNotFoundError: If the input CSV file does not exist.
        ValueError: If the dataset contains fewer than 100 rows, causing sampling to fail.

    Returns:
        None
    """
    data = pd.read_csv("../old Data/Τραγούδια.csv")
    new_data = data.sample(n=100)
    new_data.to_csv('../old Data/randomSongs.csv', index=False, header=True)


def get_songs(file_path, file_name):
    data = pd.read_csv(file_path + file_name)
    print(data)
    new_data = data.drop(columns=["Comments"])
    print(new_data)

get_songs(file_Path, file_Name)

