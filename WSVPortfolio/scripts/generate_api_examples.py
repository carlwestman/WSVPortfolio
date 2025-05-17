import os
import json
from borsdata_client.client import BorsdataAPIClient, ReportType, PriceType, CalcGroup, Calc

def main():
    api = BorsdataAPIClient()
    results = {}

    # Instrument Meta
    results['markets'] = api.get_markets().dict()
    results['sectors'] = api.get_sectors().dict()
    results['translation_metadata'] = api.get_translation_metadata(api.api_key).dict()

    # Reports
    example_instrument_id = 1
    results['reports'] = api.get_reports(example_instrument_id, 'year').dict()
    results['reports_compound'] = api.get_reports_compound(example_instrument_id).dict()
    results['reports_metadata'] = api.get_reports_metadata().dict()
    results['reports_array'] = api.get_reports_array(str(example_instrument_id), api.api_key, 'year').dict()

    # StockPrices
    results['stockprices'] = api.get_stockprices(example_instrument_id).dict()
    results['stockprices_last'] = api.get_stockprices_last(api.api_key).dict()
    results['stockprices_global_last'] = api.get_stockprices_global_last(api.api_key).dict()
    results['stockprices_date'] = api.get_stockprices_date(api.api_key, '2023-12-31').dict()
    results['stockprices_global_date'] = api.get_stockprices_global_date(api.api_key, '2023-12-31').dict()
    results['stockprices_array'] = api.get_stockprices_array(str(example_instrument_id), api.api_key).dict()
    results['stock_splits'] = api.get_stock_splits(api.api_key).dict()

    # KPIs
    example_kpi_id = 1
    results['kpi_history'] = api.get_kpi_history(example_instrument_id, example_kpi_id, 'year', 'mean').dict()
    results['kpi_summary'] = api.get_kpi_summary(example_instrument_id, 'year').dict()
    results['kpi_history_alt'] = api.get_kpi_history_alt(example_kpi_id, 'year', 'mean').dict()
    results['kpi_calc'] = api.get_kpi_calc(example_instrument_id, example_kpi_id, 'last', 'high').dict()
    results['kpi_calc_alt'] = api.get_kpi_calc_alt(example_kpi_id, 'last', 'high').dict()
    results['kpi_calc_global'] = api.get_kpi_calc_global(example_kpi_id, 'last', 'high').dict()
    results['kpis_updated'] = api.get_kpis_updated().dict()
    results['kpis_metadata'] = api.get_kpis_metadata().dict()

    # Miscellaneous
    results['branches'] = api.get_branches().dict()
    results['countries'] = api.get_countries().dict()

    # Save to file
    os.makedirs('tests/data', exist_ok=True)
    with open('tests/data/borsdata_api_examples.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
