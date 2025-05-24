import pandas as pd
import comtradeapicall
import streamlit as st
from utils import read_country_names, read_commodity_names, country_name_to_code, read_country_codes, commodity_name_to_code, country_code_to_name


st.title("Commodity Trade Reseach")

years = [str(num) for num in range(2012, 2026)]
years.reverse()

selected_years = st.multiselect("Years:", options=years, default=years[:3])

selected_commodities = st.multiselect("Commodities:", options=read_commodity_names())


st.status(f"You selected: {selected_commodities}", state='complete')


commodity_codes = [str(commodity_name_to_code(name)) for name in selected_commodities]


st.write("Selected commodity codes:", commodity_codes)


selected_countries = st.multiselect("Countries", options=read_country_names())

country_codes = [str(country_name_to_code(name)) for name in selected_countries]


# Get data button
if st.button(
    "Get Data"
):


    key = "c1ad41944d1947f8924b6d08a399e86e"


    data = comtradeapicall.getFinalData(
        subscription_key=key,
        typeCode="C",
        freqCode="A",
        clCode="HS",
        period=",".join(selected_years),
        reporterCode=",".join([str(num) for num in country_codes]),
        cmdCode=",".join(commodity_codes),
        flowCode="M",
        partnerCode="0",
        partner2Code="0",
        customsCode="C00",
        motCode="0",
        maxRecords=1000,
    )

    # only keep period, qty and netWgt columns
    data = data[["reporterCode","period", "qty", "isQtyEstimated", "netWgt", "isNetWgtEstimated"]]
    
    # replace reporterCodes to country names
    data["reporterCode"] = data["reporterCode"].apply(lambda x: country_code_to_name(int(x)))

    
    data.reset_index(drop=True, inplace=True)



    st.dataframe(data)

    
    
    st.bar_chart(data, x="reporterCode", y="netWgt", color="period", horizontal=True)
    st.bar_chart(data, x="reporterCode", y="qty", color="period", horizontal=True)



