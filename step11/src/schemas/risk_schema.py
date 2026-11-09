from pydantic import BaseModel, Field


class RiskAnalysis(BaseModel):
    financial_risks: list[str] = Field(
        description="Key financial risks identified"
    )

    business_risks: list[str] = Field(
        description="Key business and operational risks"
    )

    governance_risks: list[str] = Field(
        description="Key corporate governance risks"
    )

    risk_assessment: str = Field(
        description="Overall assessment of the company's risk profile"
    )