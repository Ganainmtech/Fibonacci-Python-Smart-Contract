from algopy import (arc4, Global, UInt64)
# Fibonacci smart contract using ARC4
class FibonacciContract(arc4.ARC4Contract):
    # State variable for the Fibonacci input
    n: UInt64  # Stores which Fibonacci number to compute

    @arc4.abimethod(
        allow_actions=["NoOp"],  # Callable only during a NoOp transaction
        create="require",  
    )
    def create_fibonacci(self) -> None:
        """
        Contract initialisation.
        """
        pass

    @arc4.abimethod
    def compute_fibonacci(self, n: UInt64) -> UInt64:
        """
        Compute the nth Fibonacci number recursively.
        """
        # Base cases: return 0 or 1 directly
        if n == 0:
            return UInt64(0)
        elif n == 1:
            return UInt64(1)
        else:
            # Recursive case: fib(n) = fib(n-1) + fib(n-2)
            return self.compute_fibonacci(n - 1) + self.compute_fibonacci(n - 2)
