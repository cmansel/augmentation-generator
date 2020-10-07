import re
import numpy as np # type: ignore
from .types import AugmentationProbability, Batch

def augment(batch: Batch, augmentation_probability: AugmentationProbability) -> Batch:
    '''Sample from a bernoulli distribution with the probability given to decide
    whether to apply each augmentation. If the amount or description bernoulli sample
    comes back true, then the respective augmentation is applied to the batch of data.'''
    if sample_bernoulli(augmentation_probability):
        batch.amount = batch.amount.map(number_augmentation)

    if sample_bernoulli(augmentation_probability):
        batch.description = batch.description.map(shuffle_augmentation)

    return batch

def sample_bernoulli(augmentation_probability: AugmentationProbability) -> bool:
    '''This function samples from a bernoulli distribution to run a trial with augmentation
    probability of success.'''
    return bool(np.random.binomial(size=1, n=1, p=augmentation_probability)[0])

def number_augmentation(number: float) -> float:
    '''This function injects gaussian noise into the numerical value. The standard deviation is
    set so that 68% of samples will be within 20% of the actual value. There is a minimum cap at
    10% to prevent the number changing sign.'''
    absolute_value = abs(number)
    sign_number = np.sign(number)
    minimum_allowed_value = absolute_value * 0.1

    absolute_value_with_noise = np.random.normal(absolute_value, absolute_value * 0.2)

    return sign_number * max(minimum_allowed_value, absolute_value_with_noise)

def shuffle_augmentation(string: str) -> str:
    '''This function shuffles the words in the string to make the classifier more robust
    to strings with similar words. The words are counted as separate if separated by any of a selection
    of characters shown in the regex expression below.'''
    string_split = re.split(',| |_|-', string) # The regex expression is the string in this line
    np.random.shuffle(string_split)

    separator = " "
    string_shuffled = separator.join(string_split)

    return string_shuffled
