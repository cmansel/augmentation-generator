# Augmentation Generator
[![cmansel](https://circleci.com/gh/cmansel/augmentation-generator.svg?style=shield)](<https://app.circleci.com/pipelines/github/cmansel/augmentation-generator>)

This package generates augmented data from an existing dataset.

Specifically, an augmentation generator can be created which produces batches of augmented data from an original dataset. Float columns in the data can be injected with gaussian noise, string columns can be shuffled.

### Noise augmentation for floats
- A gaussian noise augmentation was chosen for numbers, to improve robustness to similar sized numbers.
- The standard deviation has been set so that 68% of samples will be within 20% of the actual value.
- There is a minimum cap at 10% of the true value to prevent the sign of the number changing, leading to potential misclassifications.

### Shuffle augmentation for strings
- A word shuffling augmentation was chosen for strings, to improve robustness to word order. 
- Distinct words are separated by a variety of characters using a regex expression and then shuffled to make a new description, using the same words but in a new order.


## How to run using docker
To run the tests and the example script with defaults of:
augmentation_probability = 1,
batch_size = 5,
isolated_example = 29,
augmentation_columns = ['amount', 'description']
```
docker build . --tag augmentation_generator
docker run augmentation_generator
```

To run the example script with different values run
```
docker run augmentation_generator ./run_with_tests.sh <augmentation_probability> <batch_size> <isolated_example> <augmentation_column_1> <augmentation_column_2> ... <augmentation_column_n>
```

So with no probability of augmentation, a batch size of 10, isolating row 30, but selecting description as the column to augment
```
docker run augmentation_generator ./run_with_tests.sh 0 10 30 description
```

## How to run without docker
- Install the requirements located in the requirements folder

### Running the tests and example script
From within the augmentation_generator directory, to run with default parameters
```
./run_with_tests.sh 1 5 29 amount description
```

### Running the example script only
From outside the augmentation generator directory, to run with default parameters
```
python augmentation_generator 1 5 29 amount description
```