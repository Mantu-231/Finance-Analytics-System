import streamlit as st
import requests
import plotly.express as px


API_URL = "https://finance-analytics-system.onrender.com"


st.set_page_config(
    page_title="Finance Analytics Dashboard",
    page_icon="💰",
    layout="wide"
)


st.title("💰 Finance Analytics Dashboard")


# Token storage
if "token" not in st.session_state:
    st.session_state.token = None



# ================= LOGIN =================

if st.session_state.token is None:

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):

        # OAuth2 login requires form data
        response = requests.post(
            f"{API_URL}/login",
            data={
                "username": email,
                "password": password
            }
        )


        if response.status_code == 200:

            data = response.json()

            st.session_state.token = data["access_token"]

            st.success("Login successful")

            st.rerun()


        else:

            st.error(
                f"Login failed: {response.text}"
            )


    st.stop()



# ================= AUTH HEADER =================

headers = {
    "Authorization": f"Bearer {st.session_state.token}"
}



# ================= ANALYTICS =================

st.subheader("📊 Financial Summary")


analytics_response = requests.get(
    f"{API_URL}/analytics",
    headers=headers
)


if analytics_response.status_code == 200:

    analytics = analytics_response.json()


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Total Income",
        analytics["total_income"]
    )


    col2.metric(
        "Total Expense",
        analytics["total_expense"]
    )


    col3.metric(
        "Savings",
        analytics["savings"]
    )


else:

    st.error(
        analytics_response.text
    )



# ================= TRANSACTIONS =================

st.subheader("💳 Transactions")


transaction_response = requests.get(
    f"{API_URL}/transactions",
    headers=headers
)


if transaction_response.status_code == 200:

    transactions = transaction_response.json()


    if transactions:

        st.dataframe(
            transactions
        )


        fig = px.pie(
            transactions,
            names="category",
            values="amount",
            title="Expense Category"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    else:

        st.info(
            "No transactions found"
        )


else:

    st.error(
        transaction_response.text
    )



# ================= ADD TRANSACTION =================

st.subheader("➕ Add Transaction")


amount = st.number_input(
    "Amount",
    min_value=0.0
)


category = st.text_input(
    "Category"
)


transaction_type = st.selectbox(
    "Transaction Type",
    [
        "Income",
        "Expense"
    ]
)


transaction_date = st.text_input(
    "Date",
    "2026-08-03"
)



if st.button("Add Transaction"):


    response = requests.post(
        f"{API_URL}/transactions",
        headers=headers,
        json={
            "amount": amount,
            "category": category,
            "transaction_type": transaction_type,
            "transaction_date": transaction_date
        }
    )


    if response.status_code == 200:

        st.success(
            "Transaction added successfully"
        )

        st.rerun()


    else:

        st.error(
            response.text
        )



# ================= LOGOUT =================

st.sidebar.title("Account")


if st.sidebar.button("Logout"):

    st.session_state.token = None

    st.rerun()