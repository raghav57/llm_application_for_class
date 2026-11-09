from pydantic import BaseModel

from src.schemas.company_schema import CompanyInfo
from src.schemas.financial_schema import FinancialMetrics
from src.schemas.valuation_schema import ValuationAnalysis
from src.schemas.risk_schema import RiskAnalysis
from src.schemas.verdict_schema import InvestmentVerdict


class StockAnalysis(BaseModel):
    company: CompanyInfo
    financials: FinancialMetrics
    valuation: ValuationAnalysis
    risks: RiskAnalysis
    verdict: InvestmentVerdict
    historical_financials: list[FinancialMetrics] = []