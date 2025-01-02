import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import ivtmetrics


st.set_page_config(
    page_title="Beginner's Hypothesis 2025(2y) CholecT50",
    page_icon=":large_blue_circle:",
    layout="wide",
    initial_sidebar_state="expanded"
)
logo_path="media/dsg-logo.png"
logo_image=open(logo_path,"rb").read()

st.sidebar.image(logo_image,use_container_width=True)
st.sidebar.markdown(f"# Join our [Discord Channel](https://discord.gg/xDGk6Wrc)")
if st.sidebar.button("Participate in the Challenge"):
    st.sidebar.markdown("Join the challenge [Here](https://eval.ai/web/challenges/challenge-page/2429/overview)")

if st.sidebar.button(""" Guide for loading datasets 
                  using PyTorch/Tensorflow"""):
    st.sidebar.markdown("Refer to this [GitHub repository](https://github.com/CAMMA-public/cholect45) for more information on Dataloader and train/test/validation splits")



st.write("# Beginner's Hypothesis 2025 (2Y)")
challenge_logo=open("media/challenge_logo.jpeg","rb").read()
st.image(challenge_logo)
st.write("""
## Surgical Action Triplet Post Challenge Phase

### Challenge Background
         
- This Problem statement is inspired from [https://cholectriplet2022.grand-challenge.org/cholectriplet2022/](https://cholectriplet2022.grand-challenge.org/cholectriplet2022/).

- For more in depth detail and clarity go through the official GitHub repository [https://github.com/CAMMA-public/cholectriplet2022](https://github.com/CAMMA-public/cholectriplet2022).

Formalizing surgical activities as triplets of the used instruments, actions performed, and target anatomies 
acted upon provides a better, comprehensive and fine-grained modeling of surgical activities. 
Automatic recognition of these triplet activities directly from surgical videos would facilitate the development of
intra-operative decision support systems that are more helpful, especially for safety, in the operating room (OR).
    
"""
)

st.image("media/ps_image.png")


# Problem statement 
#st.write("### About the Challenge ")
st.write(
  """
       For this challenge participants will develop and compete with algorithms to recognize action triplets as well as localize their 
       region of likelihood in laparoscopic videos without the use of spatial annotation during training. 
       This novel challenge investigates the state-of-the-art on surgical fine-grained activity detection,
       weak supervised learning of action location, and will strengthen this new promising research direction on 
       surgical fine-grained activity modeling in computer-assisted surgery.
  """ 
  
  )

st.image("media/task.png")
st.write("""
    
     The task and the final output of this challenge would be to predict Triplets from video datasets. 
     For each video frames, you will have to detect surgical activities as triplets of {`instruments, verb, target`} where :  
    1. `instrument` is the tool used to perform an action
    2. `verb` is the action performed
    3. `target` is the underlying anatomy/objects acted on
    
    `Refer to the image above for more information.`
      """
      )

st.write("""
   This would basically be divided into 3 major tasks:
    1. Localisation of Instruments and Target in the video
    2. Recognition of Action triplets
    3. Associating action triplets with the corresponding localised bounding boxes
""")

st.divider()

#About the dataset
st.write("""
    ### About the Dataset
""")
st.write("""
    For this challenge you will be provided with a subset of `CholecT50` dataset an endoscopic video dataset that has been annotated with action triplet labels.
    Datasets .zip file can be accessed from [Drive Link](https://drive.google.com/drive/folders/16P1GLCsOLbYYpZilQeuOCMlFpKBrtkXh?usp=sharing).
    - 15 videos including 5 test videos for submission.
    - For Post Challenge Phase Classification, bounding box, and box-triplet association labels of 5 videos will be used for method testing.
""")
st.image("media/annotation_jsonT50.png")
st.write("""

         NOTE: Go through this [GitHub Link](https://github.com/CAMMA-public/cholect50/blob/master/docs/README-Format.md) to better understand the data format and structure. 

The dataset directory structure:

    |──CholecT50
      ├───videos
      │   ├───VID01
      │   │   ├───000000.png
      │   │   ├───
      │   │   └───N.png
      │   ├───
      │   └───VIDN
      │       ├───000000.png
      │       ├───
      │       └───N.png
      ├───labels
      │   ├───VID01.json
      │   ├───
      │   └───VIDNN.json
      ├───label_mapping.txt        
      ├───LICENSE
      └───README.md
""")

st.divider()

st.write("### Rules for submission")
st.write("""
- You must make all submissions public.
- Report each submission JSON file and codes at GitHub Repo to the admins at Discord Channel
- After first submission host your solution/model. (A simple interface that does object and triplet detection)
- For compute and deployment you can use [Lightning AI platform](https://lightning.ai/))
""")
st.divider()

#Evaluation & Submissions
st.write("""
    ### Evaluation & Submissions Guidelines
""")

st.write("""
         
    Submitted methods will be evaluated on three criteria:
    1. Classification AP for action triplet recognition
    2. Localization AP for surgical instrument localization
    3. Detection AP for box-triplet association
         """
)

st.divider()

st.write("""
   Users are to submit a single JSON file for the 5 test videos in the following format:

        MODEL_NAME.json

        {
            VID92: VIDEO_PREDICTION,
            VID96: VIDEO_PREDICTION,
            VID103: VIDEO_PREDICTION,
            VID110: VIDEO_PREDICTION,
            VID111: VIDEO_PREDICTION,
        }
Each VIDEO_PREDICTION should be a dict formated in the following ways:
   
        {
            frame_id:{
            "recognition": [probability of triplet 0,....probability of triplet 99],
            "detection": [
            {"triplet": triplet_id, "instrument": [tool_id, tool_prob,bbox_x, bbox_y, bbox_w, bbox_h]}
            ...
            } ....
        }
""")

st.divider()

st.write("""#### Participate in the [Post Chllenge Track](https://eval.ai/web/challenges/challenge-page/2429/overview) and after each submission, participants need to report the scores along with GitHub Repo updates to the mentor in the Discord Server """)
