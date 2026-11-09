# Step 1 
from src.schemas.company_schema import CompanyInfo
from src.schemas.stock_schema import StockAnalysis
from src.schemas.financial_schema import FinancialMetrics
from src.schemas.risk_schema import RiskAnalysis
from src.schemas.verdict_schema import InvestmentVerdict
from src.schemas.valuation_schema import ValuationAnalysis
from pydantic import ValidationError


company = CompanyInfo(
    company_name="Tata Consultancy Services",
    ticker="TCS",
    sector="Information Technology",
    industry="IT Services"
)

print(company)
print(company.model_dump())

# Step 2

stock = StockAnalysis(
    company={
        "company_name": "Tata Consultancy Services",
        "ticker": "TCS",
        "sector": "Information Technology",
        "industry": "IT Services"
    },

    financials={
        "revenue": 25000.0,
        "net_profit": 5000.0,
        "total_debt": 1000.0,
        "operating_cash_flow": 6000.0,
        "return_on_equity": 25.0
    },

    valuation={
        "pe_ratio": 28.5,
        "pb_ratio": 12.0,
        "intrinsic_value": 4200.0,
        "margin_of_safety": 15.0,
        "valuation_assessment": "Reasonably valued"
    },

    risks={
        "financial_risks": ["Currency fluctuations"],
        "business_risks": ["Increasing competition"],
        "governance_risks": ["Potential governance concerns"],
        "risk_assessment": "Moderate risk"
    },

    verdict={
        "recommendation": "Buy",
        "investment_thesis": "Strong profitability and healthy cash generation",
        "confidence_score": 85.0,
        "investment_horizon": "5 years"
    }
)

print("\nCOMPLETE STOCK ANALYSIS:")
print(stock)
print(stock.model_dump())

print(stock.company)
print(stock)
print(stock.model_dump())

financials = FinancialMetrics(
    revenue=25000.0,
    net_profit=5000.0,
    total_debt=1000.0,
    operating_cash_flow=6000.0,
    return_on_equity=25.0
)

print("\nFinancial Metrics:")
print(financials)
print(financials.model_dump())


risks = RiskAnalysis(
    financial_risks=[
        "High debt levels",
        "Declining profit margins"
    ],
    business_risks=[
        "Increasing competition",
        "Customer concentration"
    ],
    governance_risks=[
        "Weak board oversight"
    ],
    risk_assessment="Moderate risk"
)

print("\nRisk Analysis:")
print(risks)
print(risks.model_dump())

verdict = InvestmentVerdict(
    recommendation="Buy",
    investment_thesis=(
        "Strong revenue growth, healthy profitability "
        "and manageable debt levels."
    ),
    confidence_score=85.0,
    investment_horizon="5 years"
)

print("\nInvestment Verdict:")
print(verdict)
print(verdict.model_dump())


# -----------------------------------------
# STEP 5.5 - Creating Nested Objects
# -----------------------------------------

company_obj = CompanyInfo(
    company_name="Infosys Limited",
    ticker="INFY",
    sector="Information Technology",
    industry="IT Services"
)

financials_obj = FinancialMetrics(
    revenue=160000.0,
    net_profit=26000.0,
    total_debt=5000.0,
    operating_cash_flow=30000.0,
    return_on_equity=30.0
)

valuation_obj = ValuationAnalysis(
    pe_ratio=25.0,
    pb_ratio=8.0,
    intrinsic_value=1800.0,
    margin_of_safety=12.0,
    valuation_assessment="Reasonably valued"
)

risks_obj = RiskAnalysis(
    financial_risks=["Currency fluctuations"],
    business_risks=["Global IT spending slowdown"],
    governance_risks=["Management succession risk"],
    risk_assessment="Moderate risk"
)

verdict_obj = InvestmentVerdict(
    recommendation="Buy",
    investment_thesis="Strong profitability and cash generation",
    confidence_score=82.0,
    investment_horizon="5 years"
)

# -----------------------------------------
# STEP 5.5.2 - Building Parent Object
# -----------------------------------------

nested_stock = StockAnalysis(
    company=company_obj,
    financials=financials_obj,
    valuation=valuation_obj,
    risks=risks_obj,
    verdict=verdict_obj
)

print("\nNESTED STOCK ANALYSIS:")
print(nested_stock)

print("\nCOMPANY OBJECT TYPE:")
print(type(nested_stock.company))

print("\nFINANCIAL OBJECT TYPE:")
print(type(nested_stock.financials))

print("\nVALUATION OBJECT TYPE:")
print(type(nested_stock.valuation))

# -----------------------------------------
# STEP 5.6.1 - Nested Validation
# -----------------------------------------

# invalid_stock = StockAnalysis(
#     company={
#         "company_name": "Infosys Limited",
#         "ticker": "INFY",
#         "sector": "Information Technology",
#         "industry": "IT Services"
#     },

#     financials={
#         "revenue": -160000.0,
#         "net_profit": 26000.0,
#         "total_debt": 5000.0,
#         "operating_cash_flow": 30000.0,
#         "return_on_equity": 30.0
#     },

#     valuation={
#         "valuation_assessment": "Reasonably valued"
#     },

#     risks={
#         "financial_risks": ["Currency fluctuations"],
#         "business_risks": ["Competition"],
#         "governance_risks": ["Governance concerns"],
#         "risk_assessment": "Moderate risk"
#     },

#     verdict={
#         "recommendation": "Buy",
#         "investment_thesis": "Strong profitability",
#         "confidence_score": 82.0,
#         "investment_horizon": "5 years"
#     }
# )

# -----------------------------------------
# STEP 5.6.2 - Multiple Nested Errors
# -----------------------------------------

# invalid_stock_multiple = StockAnalysis(
#     company={
#         "company_name": "Infosys Limited",
#         "ticker": "INFY",
#         "sector": "Information Technology",
#         "industry": "IT Services"
#     },

#     financials={
#         "revenue": -160000.0,
#         "net_profit": 26000.0,
#         "total_debt": -5000.0,
#         "operating_cash_flow": 30000.0,
#         "return_on_equity": 30.0
#     },

#     valuation={
#         "pe_ratio": 25.0,
#         "valuation_assessment": "Reasonably valued"
#     },

#     risks={
#         "financial_risks": ["Currency fluctuations"],
#         "business_risks": ["Competition"],
#         "governance_risks": ["Governance concerns"],
#         "risk_assessment": "Moderate risk"
#     },

#     verdict={
#         "recommendation": "Buy",
#         "investment_thesis": "Strong profitability",
#         "confidence_score": 120.0,
#         "investment_horizon": "5 years"
#     }
# )


# -----------------------------------------
# STEP 5.7 - Handling Validation Errors
# -----------------------------------------

try:
    invalid_stock_multiple = StockAnalysis(
        company={
            "company_name": "Infosys Limited",
            "ticker": "INFY",
            "sector": "Information Technology",
            "industry": "IT Services"
        },

        financials={
            "revenue": -160000.0,
            "net_profit": 26000.0,
            "total_debt": -5000.0,
            "operating_cash_flow": 30000.0,
            "return_on_equity": 30.0
        },

        valuation={
            "pe_ratio": 25.0,
            "valuation_assessment": "Reasonably valued"
        },

        risks={
            "financial_risks": ["Currency fluctuations"],
            "business_risks": ["Competition"],
            "governance_risks": ["Governance concerns"],
            "risk_assessment": "Moderate risk"
        },

        verdict={
            "recommendation": "Buy",
            "investment_thesis": "Strong profitability",
            "confidence_score": 120.0,
            "investment_horizon": "5 years"
        }
    )

except ValidationError as e:
    print("\nVALIDATION FAILED!")
    print(e)


# -----------------------------------------
# STEP 5.8 - Lists of Nested Models
# -----------------------------------------

historical_data = StockAnalysis(
    company=company_obj,
    financials=financials_obj,
    valuation=valuation_obj,
    risks=risks_obj,
    verdict=verdict_obj,

    historical_financials=[
        FinancialMetrics(
            revenue=120000.0,
            net_profit=18000.0,
            total_debt=8000.0,
            operating_cash_flow=22000.0,
            return_on_equity=22.0
        ),

        FinancialMetrics(
            revenue=140000.0,
            net_profit=22000.0,
            total_debt=6500.0,
            operating_cash_flow=26000.0,
            return_on_equity=26.0
        ),

        FinancialMetrics(
            revenue=160000.0,
            net_profit=26000.0,
            total_debt=5000.0,
            operating_cash_flow=30000.0,
            return_on_equity=30.0
        )
    ]
)

print("\nHISTORICAL FINANCIAL DATA:")

for financial_year in historical_data.historical_financials:
    print(financial_year)


# -----------------------------------------
# STEP 5.9 - Serialization
# -----------------------------------------

print("\nSERIALIZATION: PYTHON DICTIONARY")

stock_dictionary = historical_data.model_dump()

print(stock_dictionary)


print("\nSERIALIZATION: JSON")

stock_json = historical_data.model_dump_json(indent=4)

print(stock_json)

# -----------------------------------------
# STEP 5.9.2 - JSON to Pydantic Object
# -----------------------------------------

reconstructed_stock = StockAnalysis.model_validate_json(stock_json)

print("\nRECONSTRUCTED STOCK OBJECT:")
print(reconstructed_stock)

print("\nRECONSTRUCTED OBJECT TYPE:")
print(type(reconstructed_stock))

print("\nRECONSTRUCTED COMPANY TYPE:")
print(type(reconstructed_stock.company))

print("\nRECONSTRUCTED FINANCIAL HISTORY:")
print(type(reconstructed_stock.historical_financials[0]))


# -----------------------------------------
# STEP 5.10 - Final Schema Test
# -----------------------------------------

print("\nFINAL VALUE INVESTING COPILOT SCHEMA")

print("Company:", reconstructed_stock.company.company_name)
print("Ticker:", reconstructed_stock.company.ticker)

print("Revenue:", reconstructed_stock.financials.revenue)
print("Net Profit:", reconstructed_stock.financials.net_profit)

print("Valuation:", reconstructed_stock.valuation.valuation_assessment)

print("Risk:", reconstructed_stock.risks.risk_assessment)

print("Recommendation:", reconstructed_stock.verdict.recommendation)

print(
    "Historical Financial Records:",
    len(reconstructed_stock.historical_financials)
)

print("\nFINAL SCHEMA VALIDATION:")
print("Valid:", isinstance(reconstructed_stock, StockAnalysis))