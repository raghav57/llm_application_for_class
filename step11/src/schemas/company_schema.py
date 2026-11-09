from pydantic import BaseModel, Field


class CompanyInfo(BaseModel):
    company_name: str = Field(
        description="Full registered name of the company"
    )

    ticker: str = Field(
        min_length=1,
        max_length=10,
        description="Stock exchange ticker symbol"
    )

    sector: str = Field(
        description="Business sector in which the company operates"
    )

    industry: str = Field(
        description="Specific industry of the company"
    )