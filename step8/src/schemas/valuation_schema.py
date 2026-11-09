from pydantic import BaseModel, Field


class ValuationAnalysis(BaseModel):
    pe_ratio: float | None = Field(
        default=None,
        description="Price-to-earnings ratio"
    )

    pb_ratio: float | None = Field(
        default=None,
        description="Price-to-book ratio"
    )

    intrinsic_value: float | None = Field(
        default=None,
        description="Estimated intrinsic value per share"
    )

    margin_of_safety: float | None = Field(
        default=None,
        description="Margin of safety expressed as a percentage"
    )

    valuation_assessment: str = Field(
        description="Overall assessment of the stock valuation"
    )