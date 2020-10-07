from .augmentations import augment
from .types import Data, Batch, AugmentationProbability, BatchSize

def next(data: Data, augmentation_probability: AugmentationProbability, batch_size: BatchSize) -> Batch:
    '''This function implements the batch generation and augmentation functionality of the package.
    It can be called without using the generator class if required.'''
    data_shuffled = data.sample(frac=1)
    batch = data_shuffled.iloc[0:batch_size]

    return augment(batch, augmentation_probability)
