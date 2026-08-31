import streamlit as st
import requests


# PAGE CONFIGURATION
# Configure the Streamlit page.

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="centered"
)

# HEADER
st.title("💱 Currency Converter")
st.caption("Convert currencies using exchange rates from an API.")


# API FUNCTION
# This function gets exchange rates from the API.
#
# Example:
#
# If base currency = INR
#
# API gives:
#
# INR → USD
# INR → EUR
# INR → GBP
# etc.
# ============================================================

def get_exchange_rates(base_currency):

    # API URL
    url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:
        # Send GET request to the API
        response = requests.get(
            url,
            timeout=10
        )

        # Check whether request was successful
        response.raise_for_status()

        # Convert JSON response into Python dictionary
        data = response.json()

        # Return the complete API data
        return data

    except requests.exceptions.RequestException as error:

        # If something goes wrong with the API request
        st.error(f"API request failed: {error}")

        return None
    
# AVAILABLE CURRENCIES
# These currencies will appear in the dropdowns.

currencies = [
    "INR",
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "AUD",
    "CAD",
    "SGD",
    "AED",
    "CNY"
]

# USER INPUT
st.subheader("Enter Conversion Details")


# Create two columns for From and To currency.
col1, col2 = st.columns(2)


# FROM CURRENCY
with col1:

    from_currency = st.selectbox(
        "From Currency",
        currencies
    )

# TO CURRENCY
with col2:

    to_currency = st.selectbox(
        "To Currency",
        currencies,
        index=1
    )

# AMOUNT
amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=100.0,
    step=1.0
)

# CONVERT BUTTON
if st.button("💱 Convert Currency"):
    # Get exchange rate data
    data = get_exchange_rates(from_currency)

    # Continue only if API returned data
    if data:
        # Check API result
        if data.get("result") != "success":

            st.error("Unable to get exchange rates.")

        else:
            # Extract exchange rates
            rates = data["rates"]

            # Get exchange rate for selected currency
            rate = rates[to_currency]

            # Perform currency conversion
            converted_amount = amount * rate

            # Display exchange rate
            st.info(
                f"1 {from_currency} = "
                f"{rate:.4f} {to_currency}"
            )

            # Display final result
            st.success(
                f"{amount:,.2f} {from_currency} = "
                f"{converted_amount:,.2f} {to_currency}"
            )


# HOW THIS PROJECT WORKS

with st.expander("🧠 How does this project work?"):

    st.markdown(
        """
        ### Request Flow

        ```text
        User selects currencies
                ↓
        User enters amount
                ↓
        User clicks Convert
                ↓
        requests.get()
                ↓
        Exchange Rate API
                ↓
        JSON response
                ↓
        response.json()
                ↓
        Python dictionary
                ↓
        Extract exchange rate
                ↓
        amount × exchange rate
                ↓
        Display result
        ```

        ### Important Python Concepts

        **1. requests.get()**

        Sends an HTTP GET request to the API.

        **2. response.raise_for_status()**

        Raises an error if the HTTP request failed.

        **3. response.json()**

        Converts the API's JSON response into a Python dictionary.

        **4. data["rates"]**

        Gets all exchange rates.

        **5. rates[to_currency]**

        Gets the exchange rate for the currency selected by the user.

        **6. amount × rate**

        Performs the actual currency conversion.
        """
    )

#            INTERNET
#               │
#               ▼
#         REST API
#               │
#               │ HTTP GET
#               ▼
#        requests.get()
#               │
#               ▼
#           Response
#               │
#        ┌──────┴──────┐
#        │             │
#  status_code       JSON
#        │             │
#        │       response.json()
#        │             │
#        │             ▼
#        │       Python dict
#        │             │
#        └─────────────┤
#                      ▼
#               Extract data
#                      │
#                      ▼
#                  Calculate
#                      │
#                      ▼
#                  Streamlit
#                      │
#                      ▼
#                    User