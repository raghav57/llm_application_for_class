from pydantic import BaseModel, Field


class FinancialMetrics(BaseModel):
    revenue: float = Field(
        gt=0,
        description="Annual revenue in the reporting currency"
    )

    net_profit: float = Field(
        description="Annual net profit"
    )

    total_debt: float = Field(
        ge=0,
        description="Total outstanding debt"
    )

    operating_cash_flow: float = Field(
        description="Cash generated from operating activities"
    )

    return_on_equity: float = Field(
        description="Return on equity expressed as a percentage"
    )