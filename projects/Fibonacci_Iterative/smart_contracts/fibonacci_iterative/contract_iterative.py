from algopy import ( arc4, Global, UInt64, urange)

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
        Computes the nth Fibonacci number iteratively.
        """
        # assert n <= 20  # Example limit for n to avoid exceeding the opcode budget

        # Initialise Fibonacci values
        a = UInt64(0)
        b = UInt64(1)

        # Compute Fibonacci iteratively using urange
        for i in urange(n):
            a, b = b, a + b

        self.result = a  # Store the result in the contract state
        return a


    @arc4.abimethod
    def get_result(self) -> UInt64:
        """
        Retrieves the last computed Fibonacci number.
        """
        return self.result
