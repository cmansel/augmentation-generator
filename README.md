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
### Amount augmentation
- A gaussian noise augmentation was chosen for amount, to improve robustness to similar sized transactions.
- The standard deviation has been set so that 68% of samples will be within 20% of the actual amount.
- There is a minimum cap at 10% of the transaction amount to prevent purchases being mislabelled as refunds, and vice versa.

### Description augmentation
- A word shuffling augmentation was chosen for description, to improve robustness to word order. 
- Distinct words are separated by a variety of characters using a regex expression and then shuffled to make a new description, using the same words but in a new order.

## Code style chosen
In line with where react is moving currently I believe that Object Oriented programming should be used at the interface layer with a human, and Functional paradigms should be used below that. In light of this I've implemented my solution a little differently to the example given.
- The next() function is implemented as a class method rather than a function which is called on the class. Creating a class with no methods did not make sense to me as that is essentially just a data structure, so it seemed like using Functional programming with more boilerplate.
- I have implemented the generator class to be used as an interface, but also created a function containing the implementation of the augmentations, should you want to use it within a Functional paradigm.
- This structure is similar to what React is doing at the moment with hooks, blending OO and Functional paradigms.

## Further work
- This repo has linting, typechecking, integration tests and has been dockerised.
- The next step for it would be to add a Continuous Integration pipeline and to potentially publish it as a package, if that was desired.
- Additional augmentations, such as a date augmentation, could be added.
- Additional tests such as unit tests on the lower level functions could be added.