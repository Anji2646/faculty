import streamlit as st
st.image("logo2.jpeg", width=300)

#st.sidebar.title("EEE Faculty Profile")
#st.sidebar.title("Acadamics")
col1, col2 = st.columns(2)
with col1:
    st.write('FAculty profile')
    st.image("015.jpg", width=150)
with col2:
    st.write('Faculty Details')
    st.subheader("Dr. Saiprakash")
# Faculty Details
st.write("**Position:** Assistant Professor ")
st.write("**Department:** Department of Electrical and Electronics Engineering")
st.write("**Research Areas:** Power Electronics,Solar PV systems, Machine Learning, Data Science")

#with st.sidebar:
    #st.write("Name of the faculty")
    


# Faculty Profile Page Layout
st.title("Faculty profile ")

# Faculty Name


# Display Profile Image
  # Replace with actual image URL or file path



# Contact Information
st.write("**Email:** c.saiprakash@sru.edu.in")
st.write("**Phone:** 6301126022")

# Additional Information Section
st.write("### About")
st.write("""
Dr. Saiprakash is a renowned researcher in the field of Solar PV system, Artificial Intelligence, with over 10 years of experience in teaching and research. 
His research interests include Solar fault analysis, machine learnig, AI applications in solar PV performance analysis.
""")

st.write("### Publications")
st.write("""
- C. Saiprakash, A. Mohapatra, B. Nayak, and S. R. Ghatak, **Analysis of partial shading effect on energy output of different solar PV array configurations, Mater. Today Proc., no.39, pp. 1905-1909, 2021.
- C. Saiprakash, A. Mohapatra, A. Manna and A. Nandi, **Hybrid Array Configurations to Reduce Mismatch Loss of a PV Array under Partial Shading Conditions.
""")

# Social Media Links (optional)
st.write("### Connect")
st.write("[LinkedIn](https://www.linkedin.com/in/dr-chidurala-saiprakash-reddy-257a30b1/?originalSubdomain=in)")
st.write("[Google Scholar](https://scholar.google.co.in/citations?user=u8Uo4ZIAAAAJ&hl=en)")
