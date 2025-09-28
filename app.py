import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Database Connection
conn = mysql.connector.connect(
    host= "mysql-3686de6f-khalidkheiri-d15f.j.aivencloud.com",
    port= 21612,
    user= "avnadmin",
    password= "AVNS_HG4Jt8RVgOtxKCqsoZV",
    database= "socialmedia"
)

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM facebookmetrics")
result=mycursor.fetchall()

df = pd.DataFrame(result)
st.dataframe(df)

col1, col2 = st.columns(2, gap="small")
col1.metric("Followers", value=result[-1][1])

fig = plt.figure()
plt.plot(range(len(result)), df[1])
col2.write(fig)
