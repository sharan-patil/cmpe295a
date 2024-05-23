import streamlit as st

camera = st.session_state.selected_camera
CAMERA_1_FEED = 'images/sample_cows.jpg'
CAMERA_2_FEED = 'images/sample_empty.jpg'
CAMERA_1_DETECTION = 'images/sample_cows_detection.png'


st.title(f'Displaying the latest feed from {camera}')
if camera == 'Camera 1':
    st.image(CAMERA_1_FEED, caption='Latest camera feed')
elif camera == 'Camera 2':
    st.image(CAMERA_2_FEED, caption='Latest camera feed')

if st.button('Scan image'):
    if camera == 'Camera 1':
        st.image(CAMERA_1_DETECTION, caption='Scanned latest camera feed')
        st.toast('Scanning complete! 15 cows detected!')
        st.toast('A predator is detected!')
        st.write('The predator was last seen with Camera 1 at location [30.884841266378725, -96.90262402599888]')
    elif camera == 'Camera 2':
        st.toast('No cattle or predators detected!')
