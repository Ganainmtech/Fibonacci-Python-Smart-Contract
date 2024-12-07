from algopy import (arc4, Global, UInt64, urange)

class FibonacciContract(arc4.ARC4Contract):
    n: UInt64  # Input: Which Fibonacci number to compute
    result: UInt64  # Output: Computed Fibonacci result

    @arc4.abimethod(
        allow_actions=["NoOp"],
        create="require",
    )
    def create_fibonacci(self) -> None:
        """
        Initializes the contract.
        """
        pass

    @arc4.abimethod
    def compute_fibonacci(self, n: UInt64) -> UInt64:
        """
        Computes the nth Fibonacci number recursively.
        """
        # Base case for recursion
        if n == 0:
            return UInt64(0)
        elif n == 1:
            return UInt64(1)
        else:
            # Recursive case: fib(n) = fib(n-1) + fib(n-2)
            return self.compute_fibonacci(n - 1) + self.compute_fibonacci(n - 2)

    @arc4.abimethod
    def get_result(self) -> UInt64:
        """
        Retrieves the last computed Fibonacci number.
        """
        return self.result
