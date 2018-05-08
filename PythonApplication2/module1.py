import sys

def func():
	print("Inside func()")

def fib(num):
    print("Inside fib()")

if __name__ == "__main__":
    sys.exit(int(fib() or 0))