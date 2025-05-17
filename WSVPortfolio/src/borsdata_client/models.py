from pydantic import BaseModel, Field
from typing import Optional, List

class ReportV1(BaseModel):
    year: int
    period: int
    revenues: Optional[float] = None
    gross_Income: Optional[float] = None
    operating_Income: float
    profit_Before_Tax: float
    profit_To_Equity_Holders: Optional[float] = None
    earnings_Per_Share: float
    number_Of_Shares: float
    dividend: float
    intangible_Assets: Optional[float] = None
    tangible_Assets: Optional[float] = None
    financial_Assets: Optional[float] = None
    non_Current_Assets: float
    cash_And_Equivalents: Optional[float] = None
    current_Assets: float
    total_Assets: float
    total_Equity: float
    non_Current_Liabilities: Optional[float] = None
    current_Liabilities: Optional[float] = None
    total_Liabilities_And_Equity: float
    net_Debt: Optional[float] = None
    cash_Flow_From_Operating_Activities: Optional[float] = None
    cash_Flow_From_Investing_Activities: Optional[float] = None
    cash_Flow_From_Financing_Activities: Optional[float] = None
    cash_Flow_For_The_Year: Optional[float] = None
    free_Cash_Flow: Optional[float] = None
    stock_Price_Average: float
    stock_Price_High: float
    stock_Price_Low: float
    report_Start_Date: Optional[str] = None
    report_End_Date: Optional[str] = None
    broken_Fiscal_Year: Optional[bool] = None
    currency: Optional[str] = None
    currency_Ratio: Optional[float] = None
    net_Sales: Optional[float] = None
    report_Date: Optional[str] = None

class InstrumentV1(BaseModel):
    insId: int
    name: Optional[str] = None
    urlName: Optional[str] = None
    instrument: int
    isin: Optional[str] = None
    ticker: Optional[str] = None
    yahoo: Optional[str] = None
    sectorId: Optional[int] = None
    marketId: int
    branchId: Optional[int] = None
    countryId: Optional[int] = None
    listingDate: Optional[str] = None
    stockPriceCurrency: Optional[str] = None
    reportCurrency: Optional[str] = None

class KpiV1(BaseModel):
    i: int
    n: Optional[float] = None
    s: Optional[str] = None

class StockPriceV1(BaseModel):
    d: Optional[str] = None
    h: Optional[float] = None
    l: Optional[float] = None
    c: float
    o: Optional[float] = None
    v: Optional[int] = None

class BranchV1(BaseModel):
    id: int
    name: Optional[str] = None
    sectorId: int

class BranchesRespV1(BaseModel):
    branches: Optional[List[BranchV1]] = None

class BuybackRowV1(BaseModel):
    change: int
    changeProc: float
    price: float
    currency: Optional[str] = None
    shares: int
    sharesProc: float
    date: str

class BuybackRespV1(BaseModel):
    insId: int
    values: Optional[List[BuybackRowV1]] = None
    error: Optional[str] = None

class CompaniesCalenderV1(BaseModel):
    insId: int
    values: Optional[List['ReportCalenderDateResp']] = None
    error: Optional[str] = None

class CompaniesCalenderArrayRespV1(BaseModel):
    list: Optional[List[CompaniesCalenderV1]] = None

class CompanyDescriptionV1(BaseModel):
    insId: int
    languageCode: Optional[str] = None
    text: Optional[str] = None
    error: Optional[str] = None

class CompaniesDescriptionArrayRespV1(BaseModel):
    list: Optional[List[CompanyDescriptionV1]] = None

class DividendsDateV1(BaseModel):
    amountPaid: Optional[float] = None
    currencyShortName: Optional[str] = None
    distributionFrequency: Optional[int] = None
    excludingDate: Optional[str] = None
    dividendType: int

class CompaniesDividendsV1(BaseModel):
    insId: int
    values: Optional[List[DividendsDateV1]] = None
    error: Optional[str] = None

class CompaniesDividendArrayRespV1(BaseModel):
    list: Optional[List[CompaniesDividendsV1]] = None

class CountryV1(BaseModel):
    id: int
    name: Optional[str] = None

class CountriesRespV1(BaseModel):
    countries: Optional[List[CountryV1]] = None

class InsiderRowV1(BaseModel):
    misc: bool
    ownerName: Optional[str] = None
    ownerPosition: Optional[str] = None
    equityProgram: bool
    shares: int
    price: float
    amount: float
    currency: Optional[str] = None
    transactionType: int
    verificationDate: str
    transactionDate: Optional[str] = None

class InsiderRespV1(BaseModel):
    insId: int
    values: Optional[List[InsiderRowV1]] = None
    error: Optional[str] = None

class HoldingsInsiderTableArrayRespV1(BaseModel):
    list: Optional[List[InsiderRespV1]] = None

class ShortsRespV1(BaseModel):
    insId: int
    shortsProc: Optional[float] = None
    shortsHolders: Optional[float] = None
    shortsAvgProc: Optional[float] = None
    shortsMilj: Optional[float] = None
    shortsAvgMilj: Optional[float] = None
    lastTransactionDate: Optional[str] = None
    dtcSum: Optional[float] = None
    dtcAvg: Optional[float] = None
    trend1w: Optional[float] = None
    trend1m: Optional[float] = None
    trend3m: Optional[float] = None
    trend6m: Optional[float] = None
    error: Optional[str] = None

class HoldingsShortsTableRespV1(BaseModel):
    list: Optional[List[ShortsRespV1]] = None

class MarketV1(BaseModel):
    id: int
    name: Optional[str] = None
    countryId: Optional[int] = None
    isIndex: Optional[bool] = None
    exchangeName: Optional[str] = None

class MarketsRespV1(BaseModel):
    markets: Optional[List[MarketV1]] = None

class ProblemDetails(BaseModel):
    type: Optional[str] = None
    title: Optional[str] = None
    status: Optional[int] = None
    detail: Optional[str] = None
    instance: Optional[str] = None

class ReportCalenderDateResp(BaseModel):
    releaseDate: str
    reportType: Optional[str] = None

class ReportMetadataV1(BaseModel):
    reportPropery: Optional[str] = None
    nameSv: Optional[str] = None
    nameEn: Optional[str] = None
    format: Optional[str] = None

class ReportMetadataRespV1(BaseModel):
    reportMetadatas: Optional[List[ReportMetadataV1]] = None

class ReportsRespV1(BaseModel):
    instrument: int
    reports: Optional[List[ReportV1]] = None

class ReportsCompoundRespV1(BaseModel):
    instrument: int
    reportsYear: Optional[List[ReportV1]] = None
    reportsQuarter: Optional[List[ReportV1]] = None
    reportsR12: Optional[List[ReportV1]] = None

class ReportsCombineRespV1(BaseModel):
    instrument: int
    error: Optional[str] = None
    reportsYear: Optional[List[ReportV1]] = None
    reportsQuarter: Optional[List[ReportV1]] = None
    reportsR12: Optional[List[ReportV1]] = None

class ReportsArrayRespV1(BaseModel):
    reportList: Optional[List[ReportsCombineRespV1]] = None

class SectorV1(BaseModel):
    id: int
    name: Optional[str] = None

class SectorsRespV1(BaseModel):
    sectors: Optional[List[SectorV1]] = None

class StockPriceDateV1(BaseModel):
    i: int
    d: Optional[str] = None
    h: Optional[float] = None
    l: Optional[float] = None
    c: float
    o: Optional[float] = None
    v: Optional[int] = None

class StockPriceFullV1(BaseModel):
    i: int
    d: Optional[str] = None
    h: Optional[float] = None
    l: Optional[float] = None
    c: float
    o: Optional[float] = None
    v: Optional[int] = None

class StockPricesArrayRespListV1(BaseModel):
    instrument: int
    error: Optional[str] = None
    stockPricesList: Optional[List[StockPriceV1]] = None

class StockPricesArrayRespV1(BaseModel):
    stockPricesArrayList: Optional[List[StockPricesArrayRespListV1]] = None

class StockPricesDateRespV1(BaseModel):
    stockPricesList: Optional[List[StockPriceDateV1]] = None

class StockPricesGlobalDateRespV1(BaseModel):
    stockPricesList: Optional[List[StockPriceDateV1]] = None

class StockPricesGlobalLastRespV1(BaseModel):
    stockPricesList: Optional[List[StockPriceFullV1]] = None

class StockPricesLastRespV1(BaseModel):
    stockPricesList: Optional[List[StockPriceFullV1]] = None

class StockPricesRespV1(BaseModel):
    instrument: int
    stockPricesList: Optional[List[StockPriceV1]] = None

class StockSplitV1(BaseModel):
    instrumentId: int
    splitType: Optional[str] = None
    ratio: Optional[str] = None
    splitDate: str

class StockSplitRespV1(BaseModel):
    stockSplitList: Optional[List[StockSplitV1]] = None

class TranslationMetadataV1(BaseModel):
    nameSv: Optional[str] = None
    nameEn: Optional[str] = None
    translationKey: Optional[str] = None

class TranslationMetadataRespV1(BaseModel):
    translationMetadatas: Optional[List[TranslationMetadataV1]] = None

# Add more models as needed for other schemas
