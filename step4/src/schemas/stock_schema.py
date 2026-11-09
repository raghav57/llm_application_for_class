from pydantic import BaseModel, Field


class StockAnalysis(BaseModel):

    company_name: str = Field(
        description="Full registered name of the company"
    )

    ticker: str = Field(
        description="Stock exchange ticker symbol",
        min_length=1,
        max_length=10
    )

    business_overview: str = Field(
        description="Description of the company's business"
    )

    financial_health: str = Field(
        description="Assessment of the company's financial health"
    )

    valuation: str | None = Field(
        default=None,
        description="Assessment of the company's current valuation, if available"
    )

    investment_risks: str = Field(
        description="Key risks associated with the investment"
    )

    investment_verdict: str = Field(
        default="Not yet evaluated",
        description="Overall investment assessment"
)