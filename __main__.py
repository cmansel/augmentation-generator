import pandas as pd
import os
import sys
from src import Generator

pd.options.mode.chained_assignment = None  # This warning is being flagged regardless of the access method used, so it has been disabled.

## THIS IS THE MAIN GENERATOR CLASS EXAMPLE SCRIPT

if __name__ == "__main__":
    # Change working directory to package directory to ensure relative data import works
    augmentation_directory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(augmentation_directory)

    augmentation_data = pd.read_csv('./data/test_data.csv')

    # Get command line inputs
    args = list(sys.argv)

    augmentation_probability = float(args[1])
    batch_size = int(args[2])
    isolated_example_index = int(args[3])
    augmentation_columns = args[4:]


    gen_batch = Generator(data=augmentation_data, augmentation_columns=augmentation_columns, augmentation_probability=augmentation_probability, batch_size=batch_size)

    print('-----------------------------------------------------------')
    print('Batch Examples')
    print('Batch 1')
    print(gen_batch.next())
    print('Batch 2')
    print(gen_batch.next())
    print('Batch 3')
    print(gen_batch.next())
    print('-----------------------------------------------------------')


    gen_isolated = Generator(data=augmentation_data, augmentation_columns=augmentation_columns, augmentation_probability=augmentation_probability, batch_size=len(augmentation_data))

    print('Isolated Example')
    print(gen_isolated.next().loc[isolated_example_index])
    print(gen_isolated.next().loc[isolated_example_index])

    print('-----------------------------------------------------------')

    sys.exit()