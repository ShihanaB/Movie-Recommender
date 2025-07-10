import streamlit as st
import pandas as pd

st.title("🎬 Movie Recommender System")
sim_df = pd.read_csv('sim_df.csv', index_col=0)

def recommend(movie_title, num_recommendations):
    try:
        sim_scores = sim_df[movie_title].sort_values(ascending=False)[1:num_recommendations+1]
        return sim_scores
    except KeyError:
        return f"Movie '{movie_title}' not found in the database"

movie_list = sim_df.columns.tolist()
selected_movie = st.selectbox("Pick a movie to get recommendations", movie_list)
num_recs = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Recommend"):
    recs = recommend(selected_movie, num_recs)
    st.write(recs)