import streamlit as st

def calculate_position_size(portfolio_value, risk_percentage, entry_price, stop_loss_price, rounding_decimals):
    try:
        # Calculate risk amount
        risk_amount = portfolio_value * (risk_percentage / 100)
        
        # Calculate trade risk (difference between entry and stop loss prices)
        trade_risk = abs(entry_price - stop_loss_price)
        
        # Calculate position sizes
        position_size1 = round(risk_amount / trade_risk, rounding_decimals)
        position_size2 = round((risk_amount / trade_risk) / 2, rounding_decimals)
        position_size3 = round((risk_amount / trade_risk) / 4, rounding_decimals)
        
        return position_size1, position_size2, position_size3
    except ValueError:
        return None, None, None

# Streamlit app layout
st.title("Position Size Calculator")

portfolio_value = st.number_input("Portfolio Value ($):", min_value=0.0, value=0.0)
risk_percentage = st.number_input("Risk Percentage (%):", min_value=0.0, max_value=100.0, value=1.0)
entry_price = st.number_input("Entry Price:", min_value=0.0, value=0.0)
stop_loss_price = st.number_input("Stop Loss Price:", min_value=0.0, value=0.0)
rounding_decimals = st.number_input("Rounding Decimal Places:", min_value=0, max_value=10, value=2)

if st.button("Calculate"):
    position_size1, position_size2, position_size3 = calculate_position_size(portfolio_value, risk_percentage, entry_price, stop_loss_price, rounding_decimals)
    
    if position_size1 is not None:
        st.success(f"Position Size Full: {position_size1}")
        st.success(f"Position Size Half: {position_size2}")
        st.success(f"Position Size 1/4: {position_size3}")
    else:
        st.error("Please enter valid numbers for all fields.")

