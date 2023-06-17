import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="IPL 2022 Analysis",page_icon="📈",layout="wide")
data = pd.read_csv("Book_ipl22_ver_33.csv")

#animation loader
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
#animation url
lottie_coding=load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_d4ldfuu6.json")


#Sidebar Navigation
nav=st.sidebar.radio("Navigation",["Home","Analysis","Summary"])

if nav=="Home":

    #Header section
    with st.container():
        st.subheader("A Complete Analysis Of")
        st.title("Indian Premier League 2022")

    with st.container():
        st.write("---")
        left_column,right_column=st.columns(2)
    with left_column:
        st.header("Introduction")
        st.write("The Indian Premier League (IPL) is one of the biggest T20 cricket tournaments in the world. The tournament has grown exponentially in popularity since its inception in 2008, attracting top international players, coaches, and support staff. The purpose of this report is to analyze the data from the IPL 2022 season to gain insights into team and player performance. The data analysis will cover various aspects such as batting, bowling, fielding, team performance, and overall trends observed in the tournament. This report will provide valuable insights into the strategies and tactics used by the teams and players, which can be useful for future IPL seasons. The findings of this report can help teams and players make informed decisions, improve their performance, and ultimately, enhance the overall quality of the tournament.")
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")
    with st.container():
        st.header("Complete Analysis report")
        st.dataframe(data)

if nav=="Analysis":

    st.header("Complete Analysis of IPL 2022")

    st.image("ipl.webp")
    #options
    st.subheader("What you want to know ?")
    option=st.selectbox("",["Number of matches won by each team","Number of matches won by defending and chasing","Top scorers of the league","Top scorers of the league along with scores","Player of the match award","Best bowlers of the league"])

    if option=="Number of matches won by each team":
        #to show no.of matches won by each team in ipl
        with st.container():
            st.subheader("Number of matches won by each team in IPL 2022")
            figure = px.bar(data, x=data["match_winner"],
                    title="Number of Matches Won in IPL 2022")
            st.write(figure)
        with st.container():
            st.subheader("")
        st.write("Gujrat is leading the tournament by winning eight matches. It is an achievement as a new team for Gujrat in IPL")
    
    #to show analysis of no of matches won by defending or chasing
    if option=="Number of matches won by defending and chasing":
        with st.container():
            st.subheader("Analysis of number of matches won by defending or chasing")    
            data["won_by"] = data["won_by"].map({"Wickets": "Chasing", "Runs": "Defending"})
            won_by = data["won_by"].value_counts()
            label = won_by.index
            counts = won_by.values
            colors = ['gold','lightgreen']

            fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
            fig.update_layout(title_text='Number of Matches Won By Defending Or Chasing')
            fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,marker=dict(colors=colors, line=dict(color='black', width=3)))
            st.write(fig)
            st.write("Here it is analyzed whether most of the teams won by defending(batting first) or chasing(batting second).")
            st.write("So, currently, 24 matches are won while chasing the target, and 22 matches are won while defending the target")

    #to show top scorers 
    if option=="Top scorers of the league":
        with st.container():
            st.subheader("Top Scorers of most of the matches of IPL 2022")
            figure = px.bar(data, x=data["top_scorer"],title="Top Scorers in IPL 2022")
            st.write(figure)
            st.write("Currently, Jos Buttler has been a top scorer in 5 matches. He is looking in great touch.")

    #to show top scorers with scores
    if option=="Top scorers of the league along with scores":
        with st.container():
            st.subheader("Top Scorers of IPL 2022 along with scores")
            figure = px.bar(data, x=data["top_scorer"], y = data["highscore"], color = data["highscore"],title="Top Scorers in IPL 2022")
            st.write(figure)
            st.write("So till now, Jos Buttler has scored three centuries, and KL Rahul has scored two centuries.")

    #to show analysis of player of the match
    if option=="Player of the match award":
        with st.container():
            st.subheader("Player of the match award")
            figure = px.bar(data, x = data["player_of_the_match"], title="Most Player of the Match Awards")
            st.write(figure)
            st.write("So Kuldeep Yadav is leading in the list of players of the match awards with four matches. It is a great tournament for Kuldeep Yadav this year.")

    # to show best bowlers
    if option=="Best bowlers of the league":
        with st.container():
            st.subheader("Best Bowlers of IPL 2022")
            figure = px.bar(data, x=data["best_bowling"],title="Best Bowlers in IPL 2022")
            st.write(figure)
            st.write(" Yuzvendra Chahal having the best bowling figures in four matches. So this is a great tournament for Yuzvendra Chahal this year too.")



#Summary
if nav=="Summary":
    st.subheader("Summary of Complete Analysis")
    st.write("The 2022 season of IPL was different in so many ways. From the inclusion of two new teams to getting a new champion of IPL after 5 years, the 2022 season can be described as one of the best. Now to give a small recap of the whole season we will give you all the major details from this 2022 edition of Tata IPL.")
    st.write("1.First and most important thing from the IPL 2022 was the Gujarat Titans lifting the trophy of IPL in their first season. It was local boy Hardik Pandya who led Gujarat Titans to victory in their first season.")
    st.write("2.Second thing which can be drawn from IPL 2022 is the performance of the Rajasthan Royals. After having a fantastic auction Rajasthan Royals did not disappoint their fans and finished as runners-up in IPL 2022. They were so close to giving tribute to legend Shane Warne.")
    st.write("3.Talking about the most number of wins in IPL 2022. It was championed by Gujarat Titans who had the most number of wins in IPL 2022 which was 12. They finished at the top after the League stage with 10 wins and won 2 plays off matches.")
    st.write("4.Talking about the most number of losses so it was two IPL giants Mumbai Indians and Chennai Super Kings who shared this unwanted record. They both lost 10 matches.")
    st.write("5.Team with the highest win percentage is none other than the champions, Gujarat Titans who ended the tournament with a win percentage of 75%.")
    st.write("6.Orange cap holder was none other than Rajasthan’s opener Jos Buttler who has had his best IPL season so far and not only for him but his form and performance were one of the best in the history of IPL. Jos made 863 runs in IPL 2022.")
    st.write("7.Purple cap holder was again from the Rajasthan Royals and it was none other than Yuzvendra Chahal who was playing his first season for the Royals. Yuzi took 27 wickets this season and also took one hattrick against Kolkata Knight Riders.")
    st.write("8.Highest total of the tournament was by Rajasthan Royals who made 222/2 against Delhi Capitals. It was Jos Buttler who played a stunning knock of 116 runs.")
    st.write("9.lowest score of the tournament was by Royal Challengers Bangalore against Sunrisers Hyderabad where Bangalore got all out on just 68 runs.")
    st.write("10.Most valuable player of the season was Jos Buttler who made 4 centuries and 4 half-centuries in this season. He equalized the record of Virat Kohli of having the most number of centuries in a single IPL season. Jos finished with 375 points on the most valuable player list.")