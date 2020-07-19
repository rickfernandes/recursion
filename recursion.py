
# Fibonacci sequence starting with 1,1
def fib(n):
	# By using <= on the if statement, I'm covering the case where n == 0
	# the index stars at 0
	return 1 if n<= 1 else fib(n-1) + fib(n-2)
	# The code above is the same as:
	# if n <=1:
	#	return 1
	#return fib(n-1) + fib(n-2)

# Function to pretty print the fibonacci sequence with N elements
def fibSeq(N):
	# In python you can construct an array with the for below
	# it's just a cleaner way to do so
	return [fib(n) for n in range(N)]
	# The code above is the same as:
	# fib_array = []
	# for n in range(N):
	# 	fib_array.append(fib(n))
	# return fib_array

# Quick sort simplified method
def qsort(arr): 
	# Not pythonic to have return on the same line as if
	# but I'm using to shorten the code
    if len(arr) <= 1: return arr
    else:
    	# the code below breaks the array in 3:
    	#	- numbers lower than index 0 value
    	#	- index 0 value
    	#	- numbers higher than index 0 value
    	# then quick sort the 3 arrays above and merge the sorted arrays
    	# You can use \ to split lines, to make your code more readable
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])

# Main
def main():
	print(f"Fibonacci with 10 elements {fibSeq(10)}")
	array = [0,8,4,7,2,9,1,3,6,8,0,1,0]
	print(f"Unsorted array: {array}")
	print(f"Sorted array: {qsort(array)}")


if __name__ == '__main__':
	main()