import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.subheader("Hi, I am Marion :wave:")
st.title("I am a CCS student from Grade 10 Fortitude")
st.write("I'm going to tell you fact about Countries in Asia. ")

st.write("For more info click the link. ")


st.write("[Learn more >](https://www.topuniversities.com/blog/10-surprising-facts-about-asia)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Philippine fact")
        st.write("##")
        st.write(
            """
            - Philippines, an island country of Southeast Asia in the western Pacific Ocean.
            It is an archipelago consisting of more than 7,000 islands and islets lying about 500 miles
            (800 km) off the coast of Vietnam.

            - Manila is the capital, but nearby Quezon City is the country’s most populous city.
            Both are part of the National Capital Region (Metro Manila), located on Luzon,
            the largest island. The second largest island of the Philippines is Mindanao, in the southeast.

            - The Philippines takes its name from Philip II, who was king of Spain during the Spanish
            colonization of the islands in the 16th century.
            """

        )



st.write("For more info click the link. ")


st.write("[Learn more >](https://www.topuniversities.com/blog/10-surprising-facts-about-asia)")




with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Singapore fact")
        st.write("##")
        st.write(
            """
            - A total of 27 Singlish words have made it to the Oxford dictionary.

            - Contrary to popular belief, Singapore is not a single island, but 63 in all; comprising of other offshore islands also, 
            such as Sentosa Island, Pulau Ubin, Sisters’ Island and St John’s island among others.

            - The mythical creature Merlion, the ambassador of Singapore, is a half lion and a half fish. The lion comes from the first 
            sighting, and the fish represents the traditional fishing occupation of the city.
            """

        )

st.write("For more info click the link. ")


st.write("[Learn more >](https://www.holidify.com/pages/facts-about-singapore-2099.html)")
