"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    st.sidebar.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/CompanyLogo.png",
                     use_column_width=True)

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","History Of Movies","Data Exploration", "Our Products and Services", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "History Of Movies":
        st.sidebar.video("https://www.youtube.com/watch?v=dKrVegVI0Us")
        st.sidebar.video("https://www.youtube.com/watch?v=TcMBFSGVi1c")
        st.sidebar.video("https://www.youtube.com/watch?v=tg52up16eq0")


        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/HistoryOfMovies.png", use_column_width=True)

        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B1%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B2%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B3%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B4%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B5%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B6%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B7%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B8%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B9%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B10%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B11%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B12%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B13%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B14%5D.jpg", use_column_width=True)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/movies/timelineoffilmandtechnology-170905072010%5B15%5D.jpg", use_column_width=True)

        st.info("Slidedeck courtesy from Slideshare (Mike Gunn), https://www.slideshare.net/MikeGunn/timeline-of-the-history-of-film-and-technology?from_action=save ")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


    # Data Exploration Page
    if page_selection == "Data Exploration":

        st.sidebar.video("https://www.youtube.com/watch?v=555oiY9RWM4")
        st.sidebar.video("https://www.youtube.com/watch?v=WTAg7aolyCY")
        st.sidebar.video("https://www.youtube.com/watch?v=naQr0uTrH_s")

        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/DataExploration.png", use_column_width=True)
        st.header("Movie Ratings")
        st.subheader("Number Of Ratings")
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/NumberOfRatings.PNG", use_column_width=True)

        st.subheader("Total Number Of Ratings")
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/TotalNumberOfRatings.PNG", use_column_width=True)

        st.subheader("Mean Rating")
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/MeanRating.PNG", use_column_width=True)

        st.header("Frequency of Genres")
        #st.subheader("Number Of Ratings")
        st.image("https://github.com/ASMaharaj/unsupervised-predict-streamlit-template/blob/developing/resources/images/FrequencyOfGenres.PNG", use_column_width=True)

        st.header("Word Clouds")
        st.subheader("Directors")
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/DirectorsWordCloud.PNG", use_column_width=True)

        st.subheader("Genre")
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/GenreWordCloud.PNG", use_column_width=True)

        st.subheader("Tag")
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/TagWordCloud.PNG", use_column_width=True)


    # Our Products and Services Page
    if page_selection == "Our Products and Services":

        st.sidebar.video("https://www.youtube.com/watch?v=QIt6ewZkeE0")
        st.sidebar.video("https://www.youtube.com/watch?v=PbMl6DjhJ1I")
        st.sidebar.video("https://www.youtube.com/watch?v=9oeGoQGt7Aos")

        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/OurProductsServices.png", use_column_width=True)


        # OneFlix products offered
        st.title("Products and Services offered")
        st.markdown("""
                        - Work with stakeholders in any organisation to identify opportunities for leveraging company data to drive business solutions.
                        - Assess the effectiveness and accuracy of new data sources and data gathering techniques.
                        - Mine and analyze data from company databases to drive optimization and improvement of product development, marketing techniques and business strategies.
                        - Intelligent Dash-boarding
                        - Distributed computing
                        - Story-telling and visualisation of big data
                        - Develop custom data models and algorithms to apply to data sets.
                        - Use predictive modeling to increase and optimize customer experiences, revenue generation, ad targeting and other business outcomes.
                        - Develop company A/B testing framework and test model quality.
                        - Coordinate with different functional teams to implement models and monitor outcomes.
                        - Develop processes and tools to monitor and analyze model performance and data accuracy.
                    """)

        # Create a contact us widget
        st.header("Contact Us")
        st.markdown("If you wish to contact us please enter your details below and we will get back to as soon as possible")
        st.text_input("Full Name")
        st.text_input("Contact Number", "Optional")
        st.text_input("Email Address")
        st.text_area("Enter a message")

        def func():
            st.write("Submitted, Thank You")
            return
        if st.button("Send"):
            func()

    # About Us Page
    if page_selection == "About Us":

        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/AboutUs.png",
        use_column_width=True)

        # table of contents on the sidebar
        st.sidebar.title("Table of contents")
        st.sidebar.info("The table of contents is interactive")
        class Toc3:
            def __init__(self):
                self._items = []
                self._placeholder = None

            def title(self, text):
                self._markdown(text, "h1")

            def header(self, text):
                self._markdown(text, "h2", " " * 2)

            def subheader(self, text):
                self._markdown(text, "h3", " " * 4)

            def placeholder(self, sidebar = False ):
                self._placeholder = st.sidebar

            def generate(self):
                if self._placeholder:
                    self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)

            def _markdown(self, text, level, space=""):
                key = "".join(filter(str.isalnum, text)).lower()

                st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
                self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


        toc3 = Toc3()

        toc3.placeholder()


        # Our Company background story
        toc3.title("OUR STORY")
        st.markdown("""
                    NetFlieks started in the Summer of 2018.

                    A group of individuals came together with the same vision:
                            Create recommender systems for content that users would find interesting.

                    A concept now brought to perfection by NetFlieks creators.

                    Today, NetFlieks are helping users in selecting various content that peaks their interests and exposing them to sources and sites that they would normally overlook which
                    could be of interest for them.

                    NetFlieks features a variety of recommender systems that users can make use of, using a broad spectrum of data preprocessing techniques and parameters.
                    Simply put: There's content for every user, mindset and style.
                    """)

        # Content creators who worked on this assignment
        toc3.title("MEET THE TEAM")

        toc3.header("Armaan Singh Maharaj")
        #st.markdown("")
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/Armaan.jpeg",
        caption = "Have you ever seen me and Batman in the same room😉", use_column_width =True)

        toc3.header("Primrose Mukhethwa Ramukhuvhathi")
        st.markdown("""
                    A tree hugger, love of nature and an environmentalist at heart who is fascinated by numbers . And recently have fallen for Machine Learning.
                    """)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/primrose.jpg", caption= "", use_column_width=True)

        toc3.header("Abednego Pakaree")
        st.markdown("""
                    Applying logic to life!
                    """)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/AB.jpg", caption = "", use_column_width=True)

        toc3.header("Khathutshelo Netsianda")
        st.markdown("""
                     I am a data science/machine learning student. i am interested in developing intelligent algorithm to solve the world's problems
                    """)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/khathutshelo.jpg", caption="", use_column_width=True)

        toc3.header("Ntokozo Nkanyane")

        toc3.header("Tsundukani Makhubela")
        st.markdown("""
                    AI enthusiast & I dream in Python.
                    """)
        st.image("https://raw.githubusercontent.com/ASMaharaj/unsupervised-predict-streamlit-template/developing/resources/images/Tsundukani.png", caption="Introvert, a bit eccentric🙃", use_column_width=True)

        toc3.generate()

        st.sidebar.video("https://www.youtube.com/watch?v=e3Nl_TCQXuw")
        st.sidebar.video("https://www.youtube.com/watch?v=Skpu5HaVkOc")
        st.sidebar.video("https://www.youtube.com/watch?v=xNWSGRD5CzU")



if __name__ == '__main__':
    main()
