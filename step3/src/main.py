from src.services.investment_service import InvestmentService


def main():

    copilot = InvestmentService()

    question = input("Ask your Value Investing Copilot: ")

    response = copilot.analyze(question)

    print("\n--- VALUE INVESTING COPILOT ---\n")
    print(response)


if __name__ == "__main__":
    main()