import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
import plotly.express as px
from bson.decimal128 import Decimal128


st.set_page_config(layout="wide")
selected=option_menu("Main Menu",['HOME','DATA EXPLORE',"Contact us"])


if selected=="HOME":
    st.title(":green[Welcome] :violet[to] :red[jeevitha's] :grey[Airbnb] :blue[Analysis]")
    st.markdown(":green[vacation rental American Company]")
    st.divider()
    col1,col2=st.columns(2)
    col3,col4=st.columns(2)
    col5,col6=st.columns(2)

    with col1:
        st.subheader("""**Airbnb is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia.**""")
        st.divider()
        st.divider()

    with col2:
        st.image(r"C:\Users\Prajee\Downloads\airbnb-678x381.jpg")
        st.caption("***Headquarters at 888 Brannan Street, in San Francisco, California, United States***")

    with col3:
        st.image(r"C:\Users\Prajee\Downloads\957-9571167_airbnb-png.png")
        st.caption("***Airbnb is a shortened version of its original name, AirBedandBreakfast.com***")

    with col4:
         st.subheader("""**The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents,and for a lack of regulation**""")       
         st.divider()
         st.divider()

    with col5:
        st.subheader("**Lodging, Hospitality, Homestay, Travel Industry, Property management and Tourism**")
        st.subheader("**Number of employees- 6,907 (2023) Revenue(Decrease) US$5.99 billion (2023)**")

    with col6:
        st.image(r"C:\Users\Prajee\Downloads\5e67688b-757d-44d6-8b4b-1e91dc6fe49f.webp") 
        st.caption("***Area served - Worldwide***") 

    st.divider() 

   

elif selected=="DATA EXPLORE":
  
    df=pd.read_csv(r"C:\Users\Prajee\OneDrive\Desktop\airbnb\Airbnb.csv")
    country = st.sidebar.multiselect('Select a country',sorted(df['country'].unique()),sorted(df['country'].unique()))
    prop = st.sidebar.multiselect('Select Property_Type',sorted(df['Property_Type'].unique()),sorted(df['Property_Type'].unique()))
    room = st.sidebar.multiselect('Select Room_Type',sorted(df['Room_Type'].unique()),sorted(df['Room_Type'].unique()))

    query=f'country in {country} & Room_Type in {room} & Property_Type	 in {prop}'
    col1,col2=st.columns([1,1],gap='small')

    with col1:
        df1=df.query(query).groupby(["Property_Type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig=px.bar(df1,title="Top 10  Property_Type	 with Count",
                   x="Property_Type",y="count",
                   orientation="v",color="Property_Type",
                   color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)

        df1= df.query(query).groupby(["Room_Type"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.pie(df1,
                             title=' Room_Type With Count',
                             values='count',names="Room_Type")
        fig.update_traces(textposition='inside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True)    
        
              
        df1= df.query(query).groupby(["Cancellation_Policy"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.line(df1,
                             title='Cancellation_Policy With Count',
                             x='Cancellation_Policy',y='count',text='count',markers=True)
        fig.update_traces(textposition="top center")                    
        st.plotly_chart(fig,use_container_width=True)
        
        
        df1= df.query(query).groupby(["Number_Of_Reviews"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
        fig = px.bar(df1,
                             title=' Number_Of_Reviews With Count',
                             x="Number_Of_Reviews",y="count",
                             text="count", orientation='v',
                             color='count',color_continuous_scale=px.colors.sequential.Darkmint_r)
        fig.update_traces( textposition='outside')
        st.plotly_chart(fig,use_container_width=True)

        with col2: 
      
            df1= df1= df.query(query).groupby('Property_Type',as_index=False)['Minimum_Nights'].mean()
            fig = px.pie(df1,
                                title='Minimum_Nights With Property_Type',
                                values="Minimum_Nights",names="Property_Type")
            fig.update_traces(textposition='inside', textinfo='value+label')
            st.plotly_chart(fig,use_container_width=True) 
            
            
            df1= df1= df.query(query).groupby(["Maximum_Nights"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
            fig = px.pie(df1,
                                title='Maximum_Nights With Count',
                                values='count',names="Maximum_Nights")
            fig.update_traces(textposition='inside')
            fig.update_layout(uniformtext_minsize=12)
            st.plotly_chart(fig,use_container_width=True)
            
            
            df1= df1= df.query(query).groupby(["Host_Neighbourhood"]).size().reset_index(name="count").sort_values(by='count',ascending=False)[:10]
            fig = px.bar(df1,
                                title='Host Neighbourhood With Count',
                                x="Host_Neighbourhood", y="count",
                                orientation='v',color='count',
                                color_continuous_scale=px.colors.sequential.Bluered_r)
            st.plotly_chart(fig,use_container_width=True)
            
        
        df1= df1= df.query(query).groupby("Property_Type",as_index=False)['Price'].mean().sort_values(by='Price',ascending=False)[:10]
        fig = px.bar(df1,
                            title=' Property With Mean Price ',
                            x="Property_Type",y="Price",
                            text="Price", orientation='v',
                            color='Property_Type',color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 
        
           
        


elif selected=="Contact us":
    st.subheader(":grey[Airbnb Data Visualization]")
    st.markdown("""***I Created this Airbnb Data Analysis Project Using "Python" to perform Data Cleansing, Understand Dataset,.
                Since 2008, guests and hosts have used Airbnb to expand on travelling possibilities and present more unique,
                personalized way of experiencing the world. This dataset describes the listing activity and metrics in Amsterdam,
                Netherland for 2019.The objective of the project is to perform data visualization techniques to understand the insight of the data.
                ***""")

    col1,col2=st.columns(2)
    with col1:
        st.title(":red[Contact Us]")
        st.caption(":orange[:red[Note]:---fill all mandatory fields---]")

        Name=st.text_input("Name*")
        Mobile=st.text_input("Mobile*")
        Email=st.text_input("Email*")
        Message=st.text_input("Message(optional)")


        if st.button("SUBMIT", " background-color: #512bba"):
            st.success('''Thank you for your Message, We will get back to you soon''')

        
    with col2:
        st.subheader("***Jeevitha Malan***:heart")
        st.caption("***:red[Mobile]:-9600303340,:orange[E-Mail]-jeevitham338@gmail.com***")