import streamlit as st
import pandas as pd

import yfinance as yf

# 0. page title
st.title("Stock Market Data BI Dashboard")
st.set_page_config(
    page_title="HK Stock Market Data", page_icon=":smiley:", layout="wide"
)

# 1. sidebar
st.sidebar.header("User Input Parameters")
ticker = st.sidebar.text_input("Ticker", "AAPL")
today = pd.Timestamp.now().date()
last_year = today - pd.DateOffset(years=1)
start_date = st.sidebar.date_input("Start Date", last_year)
end_date = st.sidebar.date_input("End Date", today)

# 2. main panel
st.write(f"**Stock Data for **{ticker}** from {start_date} to {end_date}")

# 3. fetch data
data = yf.download(ticker, start=start_date, end=end_date)

if data.empty:
    st.warning("No data found for the given ticker and date range.")
    st.stop()

# 4. tabs
tabs = st.tabs(["Data", "Visualization"])

with tabs[0]:
    st.subheader("Raw Data")
    st.dataframe(data.tail(10))

with tabs[1]:
    st.subheader("Closing Price Chart")
    st.line_chart(data["Close"])

    st.subheader("Volume Chart")
    st.bar_chart(data["Volume"])


# st.text("Hello, Streamlit!")
# st.title("My First Streamlit App")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.write("This is a simple text output.")
# st.write(
#     [
#         "Streamlit",
#         "is",
#         "an",
#         "open-source",
#         "app",
#         "framework",
#         "for",
#         "Machine Learning",
#         "and",
#         "Data Science.",
#         "hahahaha",
#     ]
# )
# st.write(12345)
# st.markdown("This is a **Markdown** text.")
# st.success("This is a success message.")
# st.info("This is an info message.")
# st.warning("This is a warning message.")
# st.error("This is an error message.")

# user_input = st.text_input("Enter your name:")
# st.write("Hello", user_input)

# st.selectbox("Select your favorite color:", ["Red", "Green", "Blue"])
# st.multiselect("Select your favorite fruits:", ["Apple", "Banana", "Cherry", "Date"])
# st.slider("Select a value:", 0, 100, 50)
# st.checkbox("Check this box")
# st.button("Click me")
# st.date_input("Select a date:")

# data = pd.DataFrame(
#     {
#         "Region": ["North", "South", "East", "West", "North", "South"],
#         "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"],
#         "Sales": [12000, 8500, 5300, 14200, 9100, 4800],
#         "Date": [
#             "2026-01-01",
#             "2026-01-02",
#             "2026-01-03",
#             "2026-01-04",
#             "2026-01-05",
#             "2026-01-06",
#         ],
#     }
# )
# region_filter = st.selectbox("Filter by Region", data["Region"].unique())
# filtered_df = data[data["Region"] == region_filter]
# st.dataframe(filtered_df)
