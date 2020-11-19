import sys
import os
import unittest
from typing import Any
import pandas as pd

pd.options.mode.chained_assignment = None  # This warning is being flagged regardless of the access method used, so it has been disabled.

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import Generator

augmentation_test_data = pd.read_csv('./data/test_data.csv')

class GeneratorTests(unittest.TestCase):
    def test_batch(self: Any) -> Any:
        augmentation_probability = 1
        batch_size = 5

        gen_batch = Generator(data=augmentation_test_data, augmentation_columns=['amount', 'description'], augmentation_probability=augmentation_probability, batch_size=batch_size)

        batch_one = gen_batch.next()
        batch_two = gen_batch.next()

        self.assertEqual(len(batch_one), batch_size)
        self.assertEqual(len(batch_two), batch_size)

    def test_no_augmentation(self: Any) -> Any:
        augmentation_probability = 0
        batch_size = len(augmentation_test_data)

        gen_batch = Generator(data=augmentation_test_data, augmentation_columns=['amount', 'description'], augmentation_probability=augmentation_probability, batch_size=batch_size)

        batch = gen_batch.next()

        self.assertEqual(len(batch), batch_size)
        self.assertEqual(augmentation_test_data.loc[29, 'amount'], batch.loc[29, 'amount'])
        self.assertEqual(augmentation_test_data.loc[29, 'description'], batch.loc[29, 'description'])

        self.assertEqual(augmentation_test_data.loc[72, 'amount'], batch.loc[72, 'amount'])
        self.assertEqual(augmentation_test_data.loc[72, 'description'], batch.loc[72, 'description'])

    def test_augmentation(self: Any) -> Any:
        augmentation_probability = 1
        batch_size = len(augmentation_test_data)

        gen_batch = Generator(data=augmentation_test_data, augmentation_columns=['amount', 'description'], augmentation_probability=augmentation_probability, batch_size=batch_size)

        batch = gen_batch.next()

        self.assertNotEqual(augmentation_test_data.loc[29, 'amount'], batch.loc[29, 'amount'])
        self.assertEqual(sorted(augmentation_test_data.loc[29, 'description'].split()), sorted(batch.loc[29, 'description'].split()))

        self.assertNotEqual(augmentation_test_data.loc[72, 'amount'], batch.loc[72, 'amount'])
        self.assertEqual(sorted(augmentation_test_data.loc[72, 'description'].split()), sorted(batch.loc[72, 'description'].split()))

if __name__ == '__main__':
    unittest.main()
