# Fibonacci Sequence Generator

## Overview

The Fibonacci Sequence Generator is a Python program that generates and prints Fibonacci sequences based on different step sizes. The Fibonacci sequence is a well-known mathematical pattern introduced by Italian mathematician Fibonacci in the 13th century. It begins with 0 and 1, and each subsequent number is the sum of the previous two.

The program provides two functions, `Fibonacci_2_steps` and `Fibonacci_3_steps`, which generate Fibonacci sequences with 2 and 3 steps, respectively. The step size determines how many previous numbers are considered when calculating the next number in the sequence.

## Features

1. **Fibonacci Sequence Generation**: Generates and prints Fibonacci sequences with 2 and 3 steps.

2. **Timer Decorator**: Measures and prints the runtime of each sequence generation using a decorator.

3. **Progress Bar (TQDM)**: Utilizes the TQDM library to display a progress bar during sequence generation.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/fibonacci-sequence-generator.git
   cd fibonacci-sequence-generator
   ```

2. **Install Dependencies:**

   ```bash
   pip install tqdm
   ```

3. **Run the Program:**

   ```bash
   python fibonacci_sequence_generator.py
   ```

4. **Follow On-screen Prompts:**

   - Choose between generating Fibonacci sequences with 2 or 3 steps.
   - Enter the desired length of the sequence.

## Example

```python
if __name__ == "__main__":
    Fibonacci_3_steps(50)
```

This example generates a Fibonacci sequence with a step size of 3 and a length of 50, showcasing the program's capabilities.

## Dependencies

- Python 3.x
- TQDM library (`pip install tqdm`)

## Contribution Guidelines

If you'd like to contribute to the project, follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure code quality.
4. Submit a pull request with a clear explanation of the changes.

## License

This project is licensed under the MIT License 

## Acknowledgments

- The Fibonacci sequence, a timeless mathematical pattern, has inspired various mathematical and artistic endeavors throughout history.
