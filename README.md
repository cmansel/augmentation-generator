# augmentation_generator

## How to run using docker
To run the tests and the example script with defaults of:
augmentation_probability = 1,
batch_size = 5,
isolated_example = 29
```
cd augmentation_generator
docker build . --tag augmentation_generator
docker run augmentation_generator
```

To run the example script with different values run
```
docker run augmentation_generator ./run_with_tests.sh <augmentation_probability> <batch_size> <isolated_example>
```

So with no augmentations, a batch size of 10 and isolating row 30
```
docker run augmentation_generator ./run_with_tests.sh 0 10 30
```


## How to run without docker
- Install the requirements located in the requirements folder

### Running the tests and example script
From within the augmentation_generator directory, to run with default parameters
```
./run_with_tests.sh 1 5 29
```

### Running the example script only
From outside the augmentation generator directory, to run with default parameters
```
python augmentation_generator 1 5 29
```


## Augmentations chosen
### Number augmentation
- A gaussian noise augmentation was chosen for numbers, to improve robustness to similar sized numbers.
- The standard deviation has been set so that 68% of samples will be within 20% of the actual value.
- There is a minimum cap at 10% of the true value to prevent the sign of the number changing, leading to potential misclassifications.

### Shuffle augmentation
- A word shuffling augmentation was chosen for strings, to improve robustness to word order. 
- Distinct words are separated by a variety of characters using a regex expression and then shuffled to make a new description, using the same words but in a new order.