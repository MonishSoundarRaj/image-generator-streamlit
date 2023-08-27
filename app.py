import streamlit as st
import replicate as rp

# Have a menu in the main screen to select the model
# Then Show the sidebar for the replicate API key
# Also show the prompt to enter there prompt, then should the loading
# display the image below
# give a download button to users to download the image


# Self initializing
output = rp.run(
    "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
    input={"prompt": "an astronaut riding a rainbow unicorn"},
)

st.image(output)
