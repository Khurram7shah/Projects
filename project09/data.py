# # import streamlit as st 
# # import pandas as pd
# # import matplotlib.pyplot as plt

 
# # st.title ("Simple Data Dashbord")
# # uploaded_file = st.file_uploader("Choose a CSV file",type="cvs")

# # if uploaded_file  is not None:
# #     df = pd.read_csv(uploaded_file)
    
    
# #     st.subheader("Data preview")
# #     st.write(df.head())
    
# #     st.subheader("Data Summary")
# #     st.write(df.describe())
    
# #     st.subheader("Filter Data")
# #     columns=df.columns.list()
# #     selected_column=st.selectbox("Select colum")
    
    
    
    
    
    
    
    
    
    
    
    
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("Simple Data Dashboard")

# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Data Preview")
#     st.write(df.head())

#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.subheader("Filter Data")
#     columns = df.columns.tolist()
#     selected_column = st.selectbox("Select column to filter by", columns)
#     unique_values = df[selected_column].unique()
#     selected_value = st.selectbox("Select value", unique_values)

#     filtered_df = df[df[selected_column] == selected_value]
#     st.write(filtered_df)

#     st.subheader("Plot Data")
#     x_column = st.selectbox("Select x-axis column", columns)
#     y_column = st.selectbox("Select y-axis column", columns)

#     if st.button("Generate Plot"):
#         st.line_chart(filtered_df.set_index(x_column)[y_column])
# else:
#     st.write("Waiting on file upload...")










import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Simple Data Dashboard")

# File Upload
uploaded_file = st.file_uploader("📂 Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display Data Preview
    st.subheader("🔍 Data Preview")
    st.write(df.head())

    # Display Data Summary
    st.subheader("📊 Data Summary")
    st.write(df.describe())

    # Filter Data
    st.subheader("🔎 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("📌 Select column to filter by", columns)

    if selected_column:
        unique_values = df[selected_column].dropna().unique()
        selected_value = st.selectbox("📌 Select value", unique_values)

        # Filter DataFrame
        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

    # Plot Data
    st.subheader("📈 Plot Data")
    
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if not numeric_columns:
        st.warning("⚠️ No numeric columns found for plotting.")
    else:
        x_column = st.selectbox("📌 Select x-axis column", df.columns)
        y_column = st.selectbox("📌 Select y-axis column", numeric_columns)

        if st.button("📊 Generate Plot"):
            try:
                # Ensure x-axis column is suitable for indexing
                df[x_column] = pd.to_datetime(df[x_column], errors='ignore')

                # Drop NaN values to prevent errors
                chart_data = filtered_df.dropna(subset=[x_column, y_column])

                # Generate Line Chart
                st.line_chart(chart_data.set_index(x_column)[y_column])

            except Exception as e:
                st.error(f"❌ Error generating chart: {e}")

else:
    st.info("📂 Please upload a CSV file to get started.")
