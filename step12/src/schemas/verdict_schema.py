from pydantic import BaseModel, Field


class InvestmentVerdict(BaseModel):
    recommendation: str = Field(
        description="Investment recommendation: Buy, Hold or Avoid"
    )

    investment_thesis: str = Field(
        description="Core reasoning behind the investment recommendation"
    )

    confidence_score: float = Field(
        ge=0,
        le=100,
        description="Confidence in the investment assessment, from 0 to 100"
    )

    investment_horizon: str = Field(
        description="Suggested investment holding period"
    )