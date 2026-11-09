class TokenCounter:

    def __init__(self):

        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_requests = 0

    # --------------------------------
    # Record token usage
    # --------------------------------

    def record_usage(self, input_tokens, output_tokens):

        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens

        self.total_requests += 1

    # --------------------------------
    # Calculate total tokens
    # --------------------------------

    def get_total_tokens(self):

        return (
            self.total_input_tokens
            + self.total_output_tokens
        )

    # --------------------------------
    # Display usage
    # --------------------------------

    def display_usage(self):

        print("\nTOKEN USAGE")
        print("-" * 40)

        print("Total Requests:", self.total_requests)

        print(
            "Input Tokens:",
            self.total_input_tokens
        )

        print(
            "Output Tokens:",
            self.total_output_tokens
        )

        print(
            "Total Tokens:",
            self.get_total_tokens()
        )

        print("-" * 40)