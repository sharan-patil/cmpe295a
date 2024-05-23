import streamlit as st
import folium

from streamlit_folium import st_folium
from streamlit_extras.switch_page_button import switch_page

# st.session_state.update(st.session_state)


#--- Init session_state
if 'active_page' not in st.session_state:
    st.session_state.active_page = 'Home'

st.set_page_config(layout='wide')
st.title('Cattle Vision')

# st.markdown("""
#     <style>
#         .block-container {
#             padding-top: 5rem;
#             padding-bottom: 0rem;
#             padding-left: 10rem;
#             padding-right: 10rem;
#         }
#     </style>
# """, unsafe_allow_html=True)


st.markdown(f"<p style='font-size: 27px;'>Welcome, Sharan. Here's your ranch!</p>",
            unsafe_allow_html=True)

if "selected_camera" not in st.session_state:
    st.session_state.selected_camera = None


st.markdown(f"<p style='font-size: 21px;'>A map of your ranch</p>",
            unsafe_allow_html=True)
m = folium.Map(
    location = [30.884841266378725, -96.90262402599888],
    zoom_start = 15,
    attr = 'Esri', 
    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
    )

folium.Marker(
    location=[30.885, -96.90],
    tooltip='Camera 1',
    icon=folium.Icon(color='blue', icon='fa-camera', prefix='fa')
).add_to(m)

folium.Marker(
    location=[30.885, -96.91],
    tooltip='Camera 2',
    icon=folium.Icon(color='blue', icon='fa-camera', prefix='fa')
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=775)
st.session_state.selected_camera = st_data['last_object_clicked_tooltip']  # 'Camera 1' or 'Camera 2'

if st.session_state.selected_camera is not None:
    switch_page('cameras')




# http://localhost:8501/Contact_Us

# import urllib.parse
# session = st.runtime.get_instance()._session_mgr.list_active_sessions()[0]
# st_base_url = urllib.parse.urlunparse([session.client.request.protocol, session.client.request.host, "", "", "", ""])

# print(st_base_url)