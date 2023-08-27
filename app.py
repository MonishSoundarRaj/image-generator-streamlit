import streamlit as st
import replicate as rp
import os
import requests

st.markdown("<h1 style='color: #041359; font-family: sans-serif; text-align: center'>IMAGINATE HUB</h1>", unsafe_allow_html=True)

with st.expander("**Prompt & Result Sample**"):
    col1, col2 = st.columns(2) 
    st.write("#### Model: Stable Diffusion")
    st.markdown("<h5>Prompt Entered: 'a vision of paradise. unreal engine'</h5>", unsafe_allow_html=True)
    st.write("##### Result:")
    st.image("./generated_image.png")

with st.form("model_selection_form"):
    st.markdown("<h4 style='text-align: center'>Choose a model from the dropdown to begin</h4>", unsafe_allow_html=True)
    option = st.selectbox("**Select the model you want to use**", (None, "Stable Diffusion", "Anything-v4.0", "Waifu Diffusion", "Vintedios Diffusion"), index=0)
    st.form_submit_button("Select Model")

if option is not None:
    st.sidebar.markdown("<h2 style='text-align: center;'>CONTROL BAR</h2>", unsafe_allow_html=True)
    user_API_key = st.sidebar.text_input(label="Enter your replicate API key:", type="password")
    st.sidebar.markdown("<h4><a href='https://gist.github.com/MonishSoundarRaj/76d1d6ef9a806d879ef4357ae5111f00'>How to get replicate API key?</a></h4>", unsafe_allow_html=True)
    
    st.sidebar.write("More options coming soon to change image generation parameters.")
    
    with st.form("Enter_Prompt_form"):
        prompt = st.text_area("Enter Image Generation Prompt")
        prompt_submit = st.form_submit_button("Submit Prompt")
        
    if prompt_submit:
        if user_API_key:
            st.success("Your prompt has been submitted successfully.")
            with st.spinner("We are working on your image"):
                model_selected = None
                if option == "Stable Diffusion":
                    model_selected = "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4"
                elif option == "Anything-v4.0":
                    model_selected = "cjwbw/anything-v4.0:42a996d39a96aedc57b2e0aa8105dea39c9c89d9d266caf6bb4327a1c191b061"
                elif option == "Waifu Diffusion":
                    model_selected = "cjwbw/waifu-diffusion:25d2f75ecda0c0bed34c806b7b70319a53a1bccad3ade1a7496524f013f48983"
                else:
                    model_selected = "22-hours/vintedois-diffusion:28cea91bdfced0e2dc7fda466cc0a46501c0edc84905b2120ea02e0707b967fd"
                
                os.environ["REPLICATE_API_TOKEN"] = user_API_key
                
                output = rp.run(
                    model_selected,
                    input={"prompt": prompt},
                )
            
                st.image(output)
                
                st.success(f"You can download the image by going here: {output[0]}" )
                
                # response = requests.get(output[0])
                # img_bytes = response.content
                # st.warning("If you click on download below the image will be downloaded and the page will refresh")
                # st.download_button("Download Image", data=img_bytes, file_name="generated_image.png", mime="image/png") 
        else:
            st.write("Enter your key in the sidebar.")
            
    else:
        pass




