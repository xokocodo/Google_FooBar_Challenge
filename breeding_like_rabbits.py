# This method calculates R(n) for any m >= 0
def r_of_n(m):
    # Memoization
    # Create table, if it doesn't already exist
    if not hasattr(r_of_n, 'table'):
        # These are the "seed values" for the R(n) sequence
        r_of_n.table = {0: 1, 1: 1, 2: 2}
    val = r_of_n.table.get(m)
    # If the value has slready been calculated, return the previous value
    if val:
        return val
    
    # Use the sequence definition to recursively calculate R(n)
    # If odd...
    if m % 2:
        # R(2n+1) = R(n-1) + R(n) + 1
        # therefore...
        # R(m) = R( (m-1)/2 ) + R( (m-1)/2 - 1 ) + 1   [for odd m]
        result = r_of_n((m-1)/2) + r_of_n((m-1)/2 - 1) + 1
    # If even...
    else:
        # R(2n+1) = R(n) + R(n+1) + n
        # therefore...
        # R(m) = R(m/2) + R(m/2 + 1) + 1  [for even m]
        result = r_of_n(m/2) + r_of_n(m/2 + 1) + m/2
    # Add the result to the table for future use
    r_of_n.table[m] = result
    return result

# This method calculates the R(n) for the even sequence
def r_e(n):
    return r_of_n(2*n)

# This method calculates the R(n) for the odd sequence
def r_o(n):
    return r_of_n(2*n+1)

# Generic Binary Search Using function f to get and expected value exp
def bin_search(exp, min, max, f=None):
    # if there are only 3 possible values left, just check them all
    if (max - min) < 2:
        for i in range(min, max+1):
            # if the result is correct, return the value
            if f(i) == exp:
                return i
        # Otherwise, no correct answer was found
        return None

    # Determine the middle of the list of remaining posssible values
    # Note: if there are an even number of values, this chooses the lower
    # of the middle values
    mid = (min + max) / 2
    k = f(mid)

    # If the result is too small, pick the range above the selected value
    if k < exp:
        return bin_search(exp, mid, max, f=f)
    # If the result is too large, pick the range above the selected value
    elif k > exp:
        return bin_search(exp, min, mid, f=f)
    # If the result is correct, return the mid value
    else:
        return mid
    
def answer(str_S):

    # n is str_S converted to an integer
    n = int(str_S, 10)
    
    # The range of possible answers is constrained by the desired R(n)
    # Since R(n) >= n for all n, we can always say that the desired n
    # must be less than or equal to the given R(n)
    # Since we are splitting R(n) into two sperate sequences, one odd
    # and one even, we only need to check for n half (rounded up) of R(n)
    m = n/2 + 1
    
    a = None

    # Check both sequences (even and odd) seperately using a binary search
    # Odd...
    o = bin_search(n, 0, m, f=r_o)
    # Even...
    e = bin_search(n, 0, m, f=r_e)

    # Since the odd sequence will always be less than the even sequence for any n
    # (This is due to the odd sequence adding 1 and the even sequence adding n)
    # We know that the odd sequence's occurance of R(n) would occur for a higher n
    # Thus if there is a hit for the odd sequence, that is the correct answer.
    # If not, check the even sequence, and if there is a hit that is the right answer.
    # Otherwise there is not hit at all.
    if o:
        # Note: must multiply by two and add 1 to convert the result from odd sequence
        # to its corresponding position in the combined sequence. 
        a = o * 2 + 1
    elif e:
        # Note: must multiply by two to convert the result from even sequence
        # to its corresponding position in the combined sequence. 
        a = e * 2  

    # Turn the integer (or None) back into a string and return
    return "%s" % a
