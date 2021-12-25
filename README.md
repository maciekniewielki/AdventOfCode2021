# Advent of code 2021
My Advent of Code 2021 solutions. For more information about AoC please visit https://adventofcode.com/

# Python solutions
At the time of writing these scripts I was using Python 3.8.1. In some scripts I use external libraries like `numpy` (for operations on vectors/matrices) and `networkx` (for graphs). The solutions are usually not very optimized and some can take up to 5 minutes to run.

## Running
The solutions are using a shared Common library, used usually for the IO operations. If you'd like to run a script, please:

1. Add the `Python` folder to the PYTHONPATH environment variable
2. Run the specified day from inside this day's folder (so it can find the input file)

Alternatively, the `run_day.py` script can do that for you. Just run it with the first argument as the day number like this
```
python run_day.py 5
```

# No day 23?
I did it by hand by playing around with chess pieces. I will update with the proper algorithm once I have some time.