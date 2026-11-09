from pydantic import BaseModel, Field
from typing import Literal


class FinancialHealth(BaseModel):
    profitability: str = Field(
        description="Assessment of the company's profitability"
    )

    debt_position: str = Field(
        description="Assessment of the company's debt and leverage"
    )

    cash_flow: str = Field(
        description="Assessment of operating cash flow and free cash flow"
    )

    revenue_growth: str = Field(
        description="Assessment of the company's revenue growth"
    )


class ValuationAssessment(BaseModel):
    intrinsic_value_estimate: float | None = Field(
        default=None,
        description="Estimated intrinsic value per share, if sufficient data exists"
    )

    market_price: float | None = Field(
        default=None,
        description="Market price per share, if provided or verified"
    )

    margin_of_safety: float | None = Field(
        default=None,
        description="Estimated margin of safety as a percentage, if calculable"
    )

    valuation_commentary: str = Field(
        description="Explanation of the company's valuation"
    )


class StockAnalysis(BaseModel):
    company_name: str = Field(
        description="Name of the company being analysed"
    )

    ticker: str | None = Field(
        default=None,
        description="Stock ticker symbol, if known"
    )

    business_overview: str = Field(
        description="Brief explanation of the company's business model"
    )

    financial_health: FinancialHealth

    valuation: ValuationAssessment

    strengths: list[str] = Field(
        description="Important positive investment characteristics"
    )

    risks: list[str] = Field(
        description="Important business, financial and valuation risks"
    )

    overall_assessment: str = Field(
        description="Balanced summary of the investment characteristics"
    )

    assessment_category: Literal[
        "potential_value",
        "mixed_signals",
        "potential_value_trap",
        "insufficient_data"
    ]

    data_limitations: list[str] = Field(
        description="Missing information, assumptions and limitations"
    )