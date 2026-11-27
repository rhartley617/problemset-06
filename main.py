import random, time
import tabulate

def ssort(L):
    for i in range(len(L)):
        #print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L


def qsort(a, pivot_fn):
    ## TO DO
    # Use an explicit stack to avoid Python's recursion limit.
    result = []
    stack = [list(a)]

    while stack:
        values = stack.pop()
        if isinstance(values, tuple):
            result.extend(values[0])
            continue
        if len(values) <= 1:
            result.extend(values)
            continue

        pivot = pivot_fn(values)
        less = [x for x in values if x < pivot]
        equal = [x for x in values if x == pivot]
        greater = [x for x in values if x > pivot]

        # Stack order is reversed so the smaller values are processed first.
        # Equal values can be emitted directly without further partitioning.
        stack.append(greater)
        stack.append((equal,))
        stack.append(less)


    return result
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = lambda a: qsort(a, lambda values: values[0])
    qsort_random_pivot = lambda a: qsort(a, random.choice)
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist.copy()),
            time_search(qsort_random_pivot, mylist.copy()),
            time_search(ssort, mylist.copy())
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'ssort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())


random.seed()
test_print()
