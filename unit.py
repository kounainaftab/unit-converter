import streamlit as st

# Define conversion functions
def length_conversion(value, from_unit, to_unit):
    if from_unit == "Meter" and to_unit == "Centimeter":
        return value * 100
    elif from_unit == "Meter" and to_unit == "Kilometer":
        return value / 1000
    elif from_unit == "Centimeter" and to_unit == "Meter":
        return value / 100
    elif from_unit == "Centimeter" and to_unit == "Kilometer":
        return value / 100000
    elif from_unit == "Kilometer" and to_unit == "Meter":
        return value * 1000
    elif from_unit == "Kilometer" and to_unit == "Centimeter":
        return value * 100000

def mass_conversion(value, from_unit, to_unit):
    if from_unit == "Gram" and to_unit == "Kilogram":
        return value / 1000
    elif from_unit == "Gram" and to_unit == "Ton":
        return value / 1000000
    elif from_unit == "Kilogram" and to_unit == "Gram":
        return value * 1000
    elif from_unit == "Kilogram" and to_unit == "Ton":
        return value / 1000
    elif from_unit == "Ton" and to_unit == "Gram":
        return value * 1000000
    elif from_unit == "Ton" and to_unit == "Kilogram":
        return value * 1000

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# Create Streamlit app
st.title("Unit Converter")

# Create tabs
tab_length, tab_mass, tab_temperature = st.tabs(["Length", "Mass", "Temperature"])

# Length tab
with tab_length:
    st.header("Length Conversion")
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From:", ["Meter", "Centimeter", "Kilometer"])
    to_unit = st.selectbox("To:", ["Meter", "Centimeter", "Kilometer"])
    if st.button("Convert"):
        result = length_conversion(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result} {to_unit}")

# Mass tab
with tab_mass:
    st.header("Mass Conversion")
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From:", ["Gram", "Kilogram", "Ton"])
    to_unit = st.selectbox("To:", ["Gram", "Kilogram", "Ton"])
    if st.button("Convert"):
        result = mass_conversion(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result} {to_unit}")

# Temperature tab
with tab_temperature:
    st.header("Temperature Conversion")
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = temperature_conversion(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} = {result}{to_unit}")