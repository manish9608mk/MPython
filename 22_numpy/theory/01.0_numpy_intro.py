'''
NUMPY — INTRODUCTION
--------------------


WHAT IS NUMPY?
--------------

NumPy = Numerical Python.

NumPy is a Python library used mainly for:

- Numerical computation
- Working with arrays and matrices
- Mathematical operations
- Statistics
- Linear algebra
- Data manipulation
- Machine Learning
- Artificial Intelligence
- Data Science


WHY SHOULD I LEARN NUMPY?
--------------------------

Python already has lists.

Example:

    numbers = [1, 2, 3, 4]

We can store numbers in a list, so why do we need NumPy?

Because NumPy is designed specifically for numerical
computations.

With a Python list:

    numbers = [1, 2, 3, 4]

    result = [x * 2 for x in numbers]

With NumPy:

    import numpy as np

    arr = np.array([1, 2, 3, 4])

    result = arr * 2

    print(result)

    Output:

    [2 4 6 8]


The important difference is:

Python list:

    We usually think in terms of loops.

NumPy:

    We can operate on the whole array.

This is called:

    VECTORIZATION


WHAT IS VECTORIZATION?
----------------------

Vectorization means performing an operation on an entire
array instead of manually writing a loop for every element.

Example:

    arr = np.array([1, 2, 3, 4])

    arr * 2

NumPy automatically applies the operation to every element.

Result:

    [2 4 6 8]


Instead of thinking:

    "How do I loop through every element?"

Think:

    "What operation do I want to perform on this array?"

This way of thinking becomes very important in:

- Data Science
- Machine Learning
- AI
- Scientific computing


WHAT IS THE MOST IMPORTANT NUMPY OBJECT?
----------------------------------------

The most important object in NumPy is:

    ndarray

ndarray means:

    N-dimensional array

Example:

    import numpy as np

    arr = np.array([10, 20, 30, 40])

    print(arr)

    Output:

    [10 20 30 40]

Here:

    arr

is a NumPy ndarray.


WHY IS NUMPY IMPORTANT FOR AI / ML?
-----------------------------------

Most Machine Learning data is numerical.

For example:

    Age     Salary     Experience

    22      40000      1
    25      60000      3
    28      80000      5

This can be represented as:

    [[22, 40000, 1],
     [25, 60000, 3],
     [28, 80000, 5]]

This is a 2D NumPy array.

Machine Learning frequently requires:

- Mathematical calculations
- Feature manipulation
- Matrix multiplication
- Mean
- Standard deviation
- Normalization
- Distance calculations
- Random number generation
- Linear algebra

NumPy provides efficient tools for these operations.


WHEN WILL I USE NUMPY?
----------------------

Use NumPy when working with numerical data.

Common situations:

1. Numerical data

2. Large collections of numbers

3. Vectors

4. Matrices

5. Mathematical calculations

6. Statistical calculations

7. Machine Learning

8. Data preprocessing

9. Computer Vision

10. Scientific computing


REAL-WORLD EXAMPLES
-------------------

Image:

    Image
      ↓
    Pixel values
      ↓
    NumPy array

ML dataset:

    Dataset
      ↓
    Numerical features
      ↓
    NumPy array

ML model:

    Features
      ↓
    Matrix
      ↓
    Mathematical operations
      ↓
    Prediction

Sensor data:

    Temperature readings
      ↓
    NumPy array
      ↓
    Statistical analysis

Computer Vision:

    Image
      ↓
    Pixel matrix
      ↓
    NumPy operations


NUMPY VS PYTHON LIST
--------------------

Python List:

    numbers = [1, 2, 3, 4]

NumPy Array:

    arr = np.array([1, 2, 3, 4])


PYTHON LIST

- General-purpose data structure
- Very flexible
- Can contain different data types
- Good for general programming
- Does not provide the same numerical operations as NumPy


NUMPY ARRAY

- Designed for numerical data
- Usually stores one data type
- Supports vectorized operations
- Supports multidimensional arrays
- Efficient for numerical computation
- Provides mathematical operations
- Provides linear algebra functionality


IMPORTANT NUMPY MENTAL MODEL
----------------------------

Think about NumPy like this:

    NumPy
      ↓
    ndarray
      ↓
    Dimensions
      ↓
    Numerical operations
      ↓
    Mathematics
      ↓
    Machine Learning


ARRAY DIMENSIONS
----------------

1D ARRAY

A one-dimensional array looks like:

    [1, 2, 3, 4]

You can think of it as a vector.

    1D → Vector


2D ARRAY

A two-dimensional array looks like:

    [[1, 2],
     [3, 4]]

You can think of it as a matrix.

    2D → Matrix


3D ARRAY

Example:

    [[[1, 2],
      [3, 4]],

     [[5, 6],
      [7, 8]]]

3D and higher-dimensional arrays are useful for
more complex data.

For example:

    Images
    Videos
    Batches of ML data


NUMPY TOPICS I MUST LEARN
-------------------------


PHASE 1 — FOUNDATION
--------------------

First understand the basic NumPy array.

Topics:

1. Import NumPy

    import numpy as np


2. ndarray

Understand:

    np.ndarray


3. Creating arrays

Learn:

    np.array()
    np.zeros()
    np.ones()
    np.full()
    np.empty()
    np.arange()
    np.linspace()


4. Array properties

Learn:

    arr.ndim
    arr.shape
    arr.size
    arr.dtype
    arr.itemsize


IMPORTANT:

Do not just memorize these properties.

Understand what each one tells you about
your array.


PHASE 2 — INDEXING & SHAPES
---------------------------

After creating arrays, learn how to access
and manipulate their structure.

Topics:

5. Indexing

Example:

    arr[0]
    arr[1]


6. Slicing

Example:

    arr[1:4]


7. 2D indexing

Example:

    arr[0, 1]


8. Selecting rows

Example:

    arr[0]


9. Selecting columns

Example:

    arr[:, 0]


10. Negative indexing

Example:

    arr[-1]


11. Reshape

Learn:

    reshape()

Example:

    arr.reshape(2, 3)


12. Flatten

Learn:

    flatten()
    ravel()


13. Transpose

Learn:

    .T
    transpose()


IMPORTANT QUESTION:

If I have an array:

    [[1, 2, 3],
     [4, 5, 6]]

I should understand:

    shape
    rows
    columns
    indexing
    slicing

before moving forward.


PHASE 3 — ARRAY OPERATIONS
--------------------------

Now learn how to perform calculations
on arrays.

13. Arithmetic operations

    +
    -
    *
    /
    //

Example:

    arr + 10
    arr * 2


14. Element-wise operations

Example:

    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])

    a + b

    Output:

    [11 22 33]


15. Comparison operations

Learn:

    >
    <
    >=
    <=
    ==
    !=


Example:

    arr > 10


16. Aggregation

Learn:

    np.sum()
    np.mean()
    np.min()
    np.max()
    np.std()
    np.var()


Example:

    arr = np.array([10, 20, 30])

    np.mean(arr)

    Output:

    20


17. Axis

Learn:

    axis=0
    axis=1


IMPORTANT:

Do not memorize:

    axis=0
    axis=1

Understand what happens when an operation
is performed across rows or columns.

Axis becomes extremely important when working
with datasets.


PHASE 4 — CORE NUMPY POWER
--------------------------

These concepts make NumPy much more powerful.

18. Vectorization

Understand:

    array operation
        ↓
    no unnecessary Python loop


19. Broadcasting

Broadcasting allows NumPy to perform operations
between arrays of compatible shapes.

Example:

    arr = np.array([1, 2, 3])

    arr + 10

Result:

    [11 12 13]

The scalar 10 is effectively applied to
each element.


20. Boolean masking

Example:

    arr = np.array([10, 20, 30, 40])

    arr[arr > 20]

Result:

    [30 40]

This is extremely useful for filtering data.


21. Conditional operations

Learn:

    np.where()


Example:

    np.where(arr > 20, 1, 0)


22. Filtering data

Learn how to select only the data
that satisfies a condition.


23. Replacing values

Learn how to modify values based on conditions.


PHASE 5 — ARRAY MANIPULATION
----------------------------

Learn how to combine and split arrays.

24. concatenate()

Used to join arrays.


25. stack()

Used to combine arrays along a new axis.


26. vstack()

Vertical stacking.


27. hstack()

Horizontal stacking.


28. split()

Split an array into multiple arrays.


29. repeat()

Repeat elements.


30. unique()

Find unique values.

Example:

    arr = np.array([1, 2, 2, 3, 3, 3])

    np.unique(arr)

    Output:

    [1 2 3]


PHASE 6 — SEARCHING & SORTING
-----------------------------

Learn how to search and order numerical data.

31. np.sort()

Sort values.


32. np.argsort()

Returns the indices that would sort the array.

This is very useful when you need the
original positions after sorting.


33. np.argmax()

Returns the index of the maximum value.


34. np.argmin()

Returns the index of the minimum value.


35. np.where()

Find positions where a condition is true.


36. np.unique()

Find unique values.


PHASE 7 — RANDOM
----------------

Random numbers are important in:

- Machine Learning
- Simulations
- Testing
- Data generation
- Model initialization


37. Random numbers

Learn:

    np.random.rand()
    np.random.randn()
    np.random.randint()


38. Random seed

Learn:

    np.random.seed()


WHY IS SEED IMPORTANT?

Suppose you generate random data.

Without a fixed seed:

    Run 1 → different result
    Run 2 → different result

With a fixed seed:

    Run 1 → same result
    Run 2 → same result

This is called:

    REPRODUCIBILITY

Reproducibility is important when debugging,
testing, and experimenting with ML models.


PHASE 8 — LINEAR ALGEBRA
------------------------

VERY IMPORTANT FOR AI / ML.

You don't need to become a mathematician,
but you must understand the basic concepts.


39. Vectors

Example:

    [1, 2, 3]


40. Matrices

Example:

    [[1, 2],
     [3, 4]]


41. Matrix multiplication

Learn:

    np.dot()

and:

    @


Example:

    A @ B


Understand WHY matrix multiplication is used
in Machine Learning.

For example:

    Input features
          ↓
    Matrix multiplication
          ↓
    Weights
          ↓
    Prediction


42. Transpose

Learn:

    A.T


43. Inverse

Learn:

    np.linalg.inv()


Understand the mathematical meaning.

Do not just memorize the function.


44. Determinant

Learn:

    np.linalg.det()


45. Norm

Learn:

    np.linalg.norm()


Norms are useful for:

- Distance
- Magnitude
- Optimization
- Machine Learning


46. Basic linear algebra operations

Understand:

    vectors
    matrices
    dot product
    matrix multiplication
    transpose
    magnitude
    distance


PHASE 9 — DATA HANDLING
-----------------------

Real-world data is not always clean.

47. Data types

Understand:

    dtype


48. astype()

Used to convert the data type.

Example:

    arr.astype(float)


49. NaN

Understand:

    np.nan

NaN means:

    Not a Number

It is commonly used to represent missing numerical data.


50. Detect missing values

Learn:

    np.isnan()


51. Copy vs View

This is VERY important.

Understand:

    copy()

versus

    view()

Why?

Because modifying a view can sometimes also
affect the original array.

You should understand NumPy's memory behavior
instead of blindly using copy() everywhere.


PHASE 10 — FILE HANDLING
------------------------

Learn how NumPy arrays can be stored and loaded.

52. Save arrays

    np.save()


53. Load arrays

    np.load()


54. Save/load multiple arrays

Understand when NumPy's own file formats
are useful.


WHAT SHOULD I BE ABLE TO DO AFTER NUMPY?
----------------------------------------

Do NOT measure your NumPy knowledge by:

    "How many functions can I memorize?"

Instead, I should be able to solve problems such as:

1. Create and manipulate arrays.

2. Understand array dimensions.

3. Understand shape.

4. Access specific elements.

5. Extract rows and columns.

6. Slice arrays.

7. Reshape arrays.

8. Flatten arrays.

9. Perform calculations on arrays.

10. Filter data using conditions.

11. Use boolean masking.

12. Use broadcasting.

13. Use vectorization.

14. Calculate statistics.

15. Normalize numerical data.

16. Handle missing values.

17. Sort and search data.

18. Generate reproducible random data.

19. Perform matrix multiplication.

20. Work with vectors and matrices.

21. Understand axis.

22. Understand copy vs view.

23. Manipulate real-world numerical datasets.


PROJECTS TO BECOME PROFICIENT
-----------------------------

Don't learn NumPy only through small examples.

Build projects.

Projects will force you to understand:

    arrays
    shape
    indexing
    slicing
    axis
    filtering
    aggregation
    broadcasting
    vectorization


PROJECT 1 — NUMPY DATA ANALYZER
-------------------------------

Create a program that analyzes student marks.

Example:

    marks = np.array([75, 82, 91, 65, 88])

Calculate:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation
- Percentage
- Pass/fail students

Learn:

    arrays
    statistics
    filtering
    aggregation


PROJECT 2 — STUDENT PERFORMANCE ANALYZER
-----------------------------------------

Create a 2D NumPy array.

Rows = students

Columns = subjects

Example:

    marks = np.array([
        [80, 75, 90],
        [65, 70, 72],
        [90, 88, 95]
    ])


Calculate:

- Average of each student
- Average of each subject
- Highest score
- Lowest score
- Pass/fail
- Student ranking
- Subject performance

Main concepts:

    shape
    axis
    aggregation
    indexing
    sorting


PROJECT 3 — SALES DATA ANALYZER
-------------------------------

Create numerical sales data.

Example:

    sales = np.array([
        [100, 200, 150],
        [120, 180, 170],
        [200, 250, 300]
    ])

Think:

    rows    → months
    columns → products


Calculate:

- Total sales
- Average sales
- Best month
- Best product
- Minimum sales
- Maximum sales
- Product-wise totals
- Month-wise totals

Main concepts:

    axis
    aggregation
    indexing
    filtering
    sorting


PROJECT 4 — IMAGE PROCESSING BASICS
------------------------------------

Understand that an image can be represented
as numerical data.

Concept:

    Image
      ↓
    Pixels
      ↓
    NumPy array
      ↓
    Matrix operations


Practice:

- Inspect image shape
- Crop an image
- Flip an image
- Change brightness
- Normalize pixel values
- Modify pixel values

Main concepts:

    arrays
    shape
    slicing
    indexing
    arithmetic


PROJECT 5 — ML DATA PREPROCESSING
---------------------------------

Create a small numerical dataset.

Practice:

- Selecting features
- Selecting rows
- Filtering
- Handling missing values
- Normalization
- Standardization
- Reshaping
- Splitting data

Example mental model:

    Raw data
       ↓
    NumPy array
       ↓
    Clean data
       ↓
    Transform data
       ↓
    ML model


PROJECT 6 — LINEAR REGRESSION FROM SCRATCH
------------------------------------------

Build a very small linear regression implementation
using NumPy.

Understand:

    X
    ↓
    weights
    ↓
    prediction
    ↓
    error
    ↓
    update


The goal is not to build a production ML model.

The goal is to understand how numerical operations
actually happen inside Machine Learning.

This is much more valuable than simply memorizing
NumPy functions.


PROJECT 7 — NUMPY ML MINI PROJECT
---------------------------------

Create a small dataset such as:

    house size
    bedrooms
    age
    price


Use NumPy to:

- Store the data
- Inspect the shape
- Select features
- Filter rows
- Normalize values
- Calculate statistics
- Perform matrix operations

Then later connect this project to:

    Scikit-learn


This creates a bridge between:

    NumPy
       ↓
    Machine Learning


INTERVIEW PREPARATION
---------------------

For NumPy interviews, I should understand:

1. What is NumPy?

2. Why use NumPy instead of Python lists?

3. What is ndarray?

4. What is vectorization?

5. Why is vectorization useful?

6. What is broadcasting?

7. What is shape?

8. What is ndim?

9. What is size?

10. What is dtype?

11. What is axis?

12. Difference between 1D and 2D arrays.

13. Difference between reshape() and flatten().

14. Difference between flatten() and ravel().

15. What is boolean indexing?

16. What is np.where()?

17. What is copy vs view?

18. How does NumPy handle data types?

19. What is broadcasting?

20. What is matrix multiplication?

21. Difference between * and @.

22. What is np.dot()?

23. What is np.argmax()?

24. What is np.argmin()?

25. What is np.argsort()?

26. How does random seed work?

27. How do you handle NaN values?

28. What is normalization?

29. How do you calculate mean/std?

30. Why are NumPy arrays useful in Machine Learning?


REAL-WORLD THINKING
-------------------

When I see numerical data, don't immediately
start writing code.

First ask:

    1. Is this data naturally represented as an array?

    2. What is the shape?

    3. How many dimensions are there?

    4. What does each row represent?

    5. What does each column represent?

    6. Do I need every element?

    7. Do I need only specific rows?

    8. Do I need only specific columns?

    9. Can I use slicing?

    10. Can I use boolean masking?

    11. Can vectorization replace a loop?

    12. Can broadcasting solve the problem?

    13. Do I need aggregation?

    14. Which axis should I use?

    15. Do I need matrix multiplication?

    16. Do I need normalization?

    17. Are there missing values?

    18. Do I need a copy or a view?


This way of thinking is more important than
memorizing NumPy functions.


WHEN SHOULD I USE A PYTHON LOOP?
--------------------------------

Don't think:

    "NumPy means never use loops."

That is incorrect.

Use NumPy vectorization when the operation can
naturally be applied to an entire array.

Example:

    arr * 2

is better than manually looping just to multiply
every value.

But sometimes a loop is still appropriate,
especially when the logic is complicated or
cannot be naturally vectorized.


NUMPY IN A REAL ML PIPELINE
---------------------------

A simplified ML workflow can look like:

    Raw Dataset
         ↓
    NumPy / Pandas
         ↓
    Clean Data
         ↓
    Select Features
         ↓
    Transform Data
         ↓
    Normalize / Standardize
         ↓
    Train/Test Split
         ↓
    Machine Learning Model
         ↓
    Prediction
         ↓
    Evaluation


NUMPY IN COMPUTER VISION
------------------------

A simplified computer vision workflow:

    Image
      ↓
    Pixel values
      ↓
    NumPy array
      ↓
    Shape
      ↓
    Crop / Resize / Transform
      ↓
    Normalize
      ↓
    ML / Deep Learning model


NUMPY IN DEEP LEARNING
----------------------

Deep learning frameworks such as:

    PyTorch
    TensorFlow

use concepts that are closely related to
NumPy arrays.

Understanding NumPy makes it easier to understand:

    tensors
    shapes
    dimensions
    matrix multiplication
    broadcasting
    vectorized operations


NUMPY LEARNING PRIORITY
-----------------------

MUST MASTER:

    ndarray
    shape
    ndim
    size
    dtype
    indexing
    slicing
    2D arrays
    reshape
    axis
    arithmetic operations
    aggregation
    vectorization
    broadcasting
    boolean masking
    np.where()
    copy vs view


SHOULD KNOW WELL:

    concatenate
    stack
    vstack
    hstack
    sort
    argsort
    argmax
    argmin
    unique
    random
    random seed
    astype
    NaN handling


IMPORTANT FOR AI / ML:

    vectors
    matrices
    dot product
    matrix multiplication
    transpose
    norms
    normalization
    standardization
    basic linear algebra


LEARN LATER:

    advanced NumPy internals
    advanced memory layout
    specialized numerical routines
    rarely used functions


The goal is NOT:

    "Know every NumPy function."

The goal is:

    "Given numerical data, I can choose the
     correct NumPy operation and solve the problem."


FINAL GOAL
----------

After learning NumPy, I should be comfortable with:

    Python
      ↓
    NumPy arrays
      ↓
    Numerical operations
      ↓
    Vectors
      ↓
    Matrices
      ↓
    Statistics
      ↓
    Linear Algebra
      ↓
    Data preprocessing
      ↓
    Machine Learning


NUMPY IS NOT THE END GOAL
-------------------------

NumPy is a foundation for:

    NumPy
      ↓
    Pandas
      ↓
    Data Analysis
      ↓
    Matplotlib / Seaborn
      ↓
    Statistics
      ↓
    Scikit-learn
      ↓
    Machine Learning
      ↓
    Deep Learning
      ↓
    AI / Computer Vision / NLP


LEARNING RULE
-------------

Don't memorize NumPy.

For every topic ask:

    1. WHAT is it?

    2. WHY do we need it?

    3. HOW does it work?

    4. WHEN should I use it?

    5. WHAT problem does it solve?

    6. Can I solve a small real-world problem with it?


If I can explain the concept, write the code,
and use it to solve a real problem,

then I actually understand NumPy.


NUMPY LEARNING MINDSET
----------------------

                 NUMPY
                   │
        ┌──────────┴──────────┐
        ↓                     ↓
   Fundamentals          ML Mathematics
        │                     │
    ndarray                Vectors
    shape                  Matrices
    indexing               Dot product
    slicing                Matrix multiplication
    reshape                Norms
    axis                   Statistics
    broadcasting           Randomness
    masking
        │                     │
        └──────────┬──────────┘
                   ↓
              ML PROBLEMS
                   ↓
           REAL-WORLD PROJECTS
                   ↓
                ML / AI


THE FINAL TEST
--------------

Before saying:

    "I know NumPy."

I should be able to take an unfamiliar numerical
dataset and answer:

    What is its shape?

    What does each dimension represent?

    How do I select the required data?

    How do I filter it?

    How do I calculate statistics?

    How do I reshape it?

    Can I vectorize the operation?

    Can broadcasting help?

    How do I handle missing values?

    How do I normalize the data?

    Do I need matrix multiplication?

    Can I explain why I chose that operation?


If I can do these things confidently,

I have a strong practical NumPy foundation.
'''