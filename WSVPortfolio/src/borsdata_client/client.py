"""
Base client for Borsdata API.
"""
import requests
import os
from typing import Optional, TYPE_CHECKING
from typing_extensions import Literal, TypeAlias

# --- Type Aliases for API enums ---
ReportType: TypeAlias = Literal["year", "r12", "quarter"]
PriceType: TypeAlias = Literal["mean", "low", "high"]
CalcGroup: TypeAlias = Literal["last", "1year", "3year", "7year", "10year", "15year"]
Calc: TypeAlias = Literal[
    "high", "latest", "low", "mean", "sum", "cagr", "psh", "trend", "over", "under", "diff", "rank", "point", "default", "return", "stabil", "quarter", "pricehigh", "pricelow", "brank", "ShortSum", "ShortCountry", "ShortIndustry"
]

if TYPE_CHECKING:
    from .models import (
        MarketsRespV1, SectorsRespV1, TranslationMetadataRespV1, ReportsRespV1, ReportsCompoundRespV1, ReportMetadataRespV1, ReportsArrayRespV1,
        StockPricesRespV1, StockPricesLastRespV1, StockPricesGlobalLastRespV1, StockPricesDateRespV1, StockPricesGlobalDateRespV1, StockPricesArrayRespV1, StockSplitRespV1,
        KpisHistoryRespV1, KpisSummaryRespV1, KpisHistoryArrayRespV1, KpisRespV1, KpisAllCompRespV1, KpisCalcUpdatedRespV1, KpiMetadataRespV1,
        BranchesRespV1, CountriesRespV1
    )

class BorsdataAPIClient:
    def __init__(self, base_url: str = "https://apiservice.borsdata.se", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        if api_key is None:
            api_key = os.environ.get("BORSDATA_API_KEY")
            if not api_key:
                raise RuntimeError("BORSDATA_API_KEY environment variable must be set or api_key provided.")
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def _get(self, path: str, params: Optional[dict] = None):
        url = f"{self.base_url}{path}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # --- Instrument Meta ---
    def get_markets(self) -> 'MarketsRespV1':
        """Returns all Markets."""
        from .models import MarketsRespV1
        return MarketsRespV1.parse_obj(self._get("/v1/markets"))

    def get_sectors(self) -> 'SectorsRespV1':
        """Returns all Sectors."""
        from .models import SectorsRespV1
        return SectorsRespV1.parse_obj(self._get("/v1/sectors"))

    def get_translation_metadata(self, authKey: str) -> 'TranslationMetadataRespV1':
        """Returns translations for bransch, sector, country. Requires API key."""
        from .models import TranslationMetadataRespV1
        return TranslationMetadataRespV1.parse_obj(self._get("/v1/translationmetadata", params={"authKey": authKey}))

    # --- Reports ---
    def get_reports(self, instrument_id: int, reporttype: ReportType) -> 'ReportsRespV1':
        """Returns Reports for Instrument. Report Type (year, r12, quarter)."""
        from .models import ReportsRespV1
        return ReportsRespV1.parse_obj(self._get(f"/v1/instruments/{instrument_id}/reports/{reporttype}"))

    def get_reports_compound(self, instrument_id: int) -> 'ReportsCompoundRespV1':
        """Returns Reports for one Instrument. All Reports Type included (year, r12, quarter)."""
        from .models import ReportsCompoundRespV1
        return ReportsCompoundRespV1.parse_obj(self._get(f"/v1/instruments/{instrument_id}/reports"))

    def get_reports_metadata(self) -> 'ReportMetadataRespV1':
        """Returns Report metadata."""
        from .models import ReportMetadataRespV1
        return ReportMetadataRespV1.parse_obj(self._get("/v1/instruments/reports/metadata"))

    def get_reports_array(self, instList: str, authKey: str, reporttype: Optional[ReportType] = None, from_date: str = None, to_date: str = None) -> 'ReportsArrayRespV1':
        """Returns Reports for list of instruments. instList is comma-separated IDs. Optionally filter by reporttype."""
        from .models import ReportsArrayRespV1
        params = {"instList": instList, "authKey": authKey}
        if reporttype:
            params["reporttype"] = reporttype
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        return ReportsArrayRespV1.parse_obj(self._get("/v1/instruments/reports", params=params))

    # --- StockPrices ---
    def get_stockprices(self, instrument_id: int) -> 'StockPricesRespV1':
        """Returns StockPrice for Instrument. 10 year default."""
        from .models import StockPricesRespV1
        return StockPricesRespV1.parse_obj(self._get(f"/v1/instruments/{instrument_id}/stockprices"))

    def get_stockprices_last(self, authKey: str) -> 'StockPricesLastRespV1':
        """Returns Last StockPrices for all Instruments. Only Nordic(Pro)."""
        from .models import StockPricesLastRespV1
        return StockPricesLastRespV1.parse_obj(self._get("/v1/instruments/stockprices/last", params={"authKey": authKey}))

    def get_stockprices_global_last(self, authKey: str) -> 'StockPricesGlobalLastRespV1':
        """Returns Last/Latest StockPrices for all Global Instruments. Only Global(Pro+)."""
        from .models import StockPricesGlobalLastRespV1
        return StockPricesGlobalLastRespV1.parse_obj(self._get("/v1/instruments/stockprices/global/last", params={"authKey": authKey}))

    def get_stockprices_date(self, authKey: str, date: str) -> 'StockPricesDateRespV1':
        """Returns one StockPrice for each Instrument for a specific date. Only Nordic(Pro)."""
        from .models import StockPricesDateRespV1
        return StockPricesDateRespV1.parse_obj(self._get("/v1/instruments/stockprices/date", params={"authKey": authKey, "date": date}))

    def get_stockprices_global_date(self, authKey: str, date: str) -> 'StockPricesGlobalDateRespV1':
        """Returns one StockPrice for each global Instrument for a specific date. Only Global(Pro+)."""
        from .models import StockPricesGlobalDateRespV1
        return StockPricesGlobalDateRespV1.parse_obj(self._get("/v1/instruments/stockprices/global/date", params={"authKey": authKey, "date": date}))

    def get_stockprices_array(self, instList: str, authKey: str, from_date: str = None, to_date: str = None) -> 'StockPricesArrayRespV1':
        """Returns StockPrice for list of Instruments. instList is comma-separated IDs."""
        from .models import StockPricesArrayRespV1
        params = {"instList": instList, "authKey": authKey}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        return StockPricesArrayRespV1.parse_obj(self._get("/v1/instruments/stockprices", params=params))

    def get_stock_splits(self, authKey: str, from_date: str = None) -> 'StockSplitRespV1':
        """Returns Stock Splits for Nordic Instruments. Max 1 Year."""
        from .models import StockSplitRespV1
        params = {"authKey": authKey}
        if from_date:
            params["from"] = from_date
        return StockSplitRespV1.parse_obj(self._get("/v1/instruments/StockSplits", params=params))

    # --- KPIs ---
    def get_kpi_history(self, insid: int, kpiId: int, reporttype: ReportType, pricetype: PriceType) -> 'KpisHistoryRespV1':
        """Returns KPI history for an instrument."""
        from .models import KpisHistoryRespV1
        return KpisHistoryRespV1.parse_obj(self._get(f"/v1/instruments/{insid}/kpis/{kpiId}/{reporttype}/{pricetype}/history"))

    def get_kpi_summary(self, insid: int, reporttype: ReportType) -> 'KpisSummaryRespV1':
        """Returns KPI summary for an instrument."""
        from .models import KpisSummaryRespV1
        return KpisSummaryRespV1.parse_obj(self._get(f"/v1/instruments/{insid}/kpis/{reporttype}/summary"))

    def get_kpi_history_alt(self, kpiId: int, reporttype: ReportType, pricetype: PriceType) -> 'KpisHistoryArrayRespV1':
        """Returns KPI history for all instruments for a KPI."""
        from .models import KpisHistoryArrayRespV1
        return KpisHistoryArrayRespV1.parse_obj(self._get(f"/v1/instruments/kpis/{kpiId}/{reporttype}/{pricetype}/history"))

    def get_kpi_calc(self, insid: int, kpiId: int, calcGroup: CalcGroup, calc: Calc) -> 'KpisRespV1':
        """Returns calculated KPI for an instrument."""
        from .models import KpisRespV1
        return KpisRespV1.parse_obj(self._get(f"/v1/instruments/{insid}/kpis/{kpiId}/{calcGroup}/{calc}"))

    def get_kpi_calc_alt(self, kpiId: int, calcGroup: CalcGroup, calc: Calc) -> 'KpisAllCompRespV1':
        """Returns calculated KPI for all instruments for a KPI."""
        from .models import KpisAllCompRespV1
        return KpisAllCompRespV1.parse_obj(self._get(f"/v1/instruments/kpis/{kpiId}/{calcGroup}/{calc}"))

    def get_kpi_calc_global(self, kpiId: int, calcGroup: CalcGroup, calc: Calc) -> 'KpisAllCompRespV1':
        """Returns calculated KPI for all global instruments for a KPI."""
        from .models import KpisAllCompRespV1
        return KpisAllCompRespV1.parse_obj(self._get(f"/v1/instruments/global/kpis/{kpiId}/{calcGroup}/{calc}"))

    def get_kpis_updated(self) -> 'KpisCalcUpdatedRespV1':
        """Returns updated KPIs."""
        from .models import KpisCalcUpdatedRespV1
        return KpisCalcUpdatedRespV1.parse_obj(self._get("/v1/instruments/kpis/updated"))

    def get_kpis_metadata(self) -> 'KpiMetadataRespV1':
        """Returns KPI metadata."""
        from .models import KpiMetadataRespV1
        return KpiMetadataRespV1.parse_obj(self._get("/v1/instruments/kpis/metadata"))

    # --- Miscellaneous ---
    def get_branches(self) -> 'BranchesRespV1':
        """Returns all Branches."""
        from .models import BranchesRespV1
        return BranchesRespV1.parse_obj(self._get("/v1/branches"))

    def get_countries(self) -> 'CountriesRespV1':
        """Returns all Countries."""
        from .models import CountriesRespV1
        return CountriesRespV1.parse_obj(self._get("/v1/countries"))
