import streamlit as st
from text_extract import *
from llm import *

st.title("Testing Instructions App")

uploaded_images = st.file_uploader(label = "Upload your screenshots here.",type=['png','jpeg','jpg'],accept_multiple_files=True)

if uploaded_images:

    with st.expander("Preview Images",icon="⚙️"):

        for img in uploaded_images:
            st.image(img,caption = img.name)

additional_info = st.text_area(label = "Additional Content (Optional)")

if st.button(label = "Submit Images",):
    if uploaded_images:

        # image_index = st.slider(label = "Peview : Your uploaded Images",min_value=0,max_value=len(uploaded_images)-1,value=0,step=1)
        # # Display the selected image
        # st.image(uploaded_images[image_index], caption=f'Image {image_index + 1}')

        placeholder = st.empty()
        placeholder.text("Generating Instructions for your app...")
        context = []
        for img in uploaded_images:

            img_context = text_extractor(image=img)
            context.extend(img_context)

        if additional_info:
            context.append(additional_info)
        
        context = join_context(context)
        llm_response = get_instructions_from_context(context)
        placeholder.success("Done!")
        st.write(llm_response)

    else:
        st.warning("ERROR : Please upload at least one image.")