This is the empirical tests for shell sort. And can be made executing just:

```bash
$ chmod +x execute.sh
$ ./execute.sh
```

This will generate the sample arrays with differentes size, starting in 2^10 to 2^25. With uniform distribution, normal distribution with standard deviation of `N * 0.01` for 
repeated numbers in the array and 75% ordered array. 
The output of the executing will be a file with two columns, in the format:
`${arr_size}\\t${time_in_seconds}\\n`

Ready to be plotted in gnuplot.

### Samples
To visualize the samples distributions, you can execute:

```bash
$ python sample_histogram.py [random|repeated|ordered|inverted] [10|11|12|...|25]
```

The greater the file, the more time it will delay to be plotted.

### Dependencies
To execute this, some things is needed:

    * Python
    * Numpy
    * Matplotlib (sample visualization)
