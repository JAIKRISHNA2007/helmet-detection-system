
# app.py
import tempfile
import cv2
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Helmet Detection", page_icon="🪖", layout="wide")

@st.cache_resource
def load_model():
    return YOLO("models/best.pt")

model = load_model()

st.sidebar.title("Helmet Detection")
mode = st.sidebar.radio("Select Mode", ["Image", "Video", "Webcam"])
conf = st.sidebar.slider("Confidence",0.05,1.0,0.25,0.05)

st.title("🪖 Helmet Detection System")

if mode=="Image":
    img_file=st.file_uploader("Upload Image",type=["jpg","jpeg","png"])
    if img_file:
        image=Image.open(img_file)
        c1,c2=st.columns(2)
        with c1:
            st.image(image,caption="Uploaded",use_container_width=True)
        if st.button("Detect"):
            results=model.predict(image,conf=conf,verbose=False)
            img=results[0].plot()
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

            counts={"helmet":0,"motor":0,"no-helmet":0,"person":0}
            for cls in results[0].boxes.cls:
                name=model.names[int(cls)]
                if name in counts:
                    counts[name]+=1

            with c2:
                st.image(img,caption="Detection",use_container_width=True)

            a,b,c,d=st.columns(4)
            a.metric("Helmet",counts["helmet"])
            b.metric("Motor",counts["motor"])
            c.metric("Person",counts["person"])
            d.metric("No Helmet",counts["no-helmet"])

            if counts["no-helmet"]>0:
                st.error("Helmet violation detected")
            else:
                st.success("No helmet violation detected")

elif mode=="Video":
    video=st.file_uploader("Upload MP4",type=["mp4","avi","mov"])
    if video and st.button("Process Video"):
        tfile=tempfile.NamedTemporaryFile(delete=False,suffix=".mp4")
        tfile.write(video.read())

        cap=cv2.VideoCapture(tfile.name)
        width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps=cap.get(cv2.CAP_PROP_FPS)

        out_path=tempfile.NamedTemporaryFile(delete=False,suffix=".mp4").name
        writer=cv2.VideoWriter(out_path,cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))

        frame_area=st.empty()
        progress=st.progress(0)

        total=max(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),1)
        frame=0

        while True:
            ret,img=cap.read()
            if not ret:
                break
            res=model.predict(img,conf=conf,verbose=False)
            ann=res[0].plot()
            writer.write(ann)
            frame_area.image(cv2.cvtColor(ann,cv2.COLOR_BGR2RGB),channels="RGB")
            frame+=1
            progress.progress(min(frame/total,1.0))

        cap.release()
        writer.release()

        st.success("Video Processed")
        with open(out_path,"rb") as f:
            st.download_button("Download Processed Video",f,"output_video.mp4","video/mp4")

else:
    import av
    from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

    st.subheader("📷 Live Webcam Detection")

    class Processor(VideoProcessorBase):
        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")

            results = model.predict(
                img,
                conf=conf,
                verbose=False
            )

            annotated = results[0].plot()

            return av.VideoFrame.from_ndarray(
                annotated,
                format="bgr24"
            )

    webrtc_streamer(
        key="helmet-webcam",
        video_processor_factory=Processor,
        media_stream_constraints={
            "video": True,
            "audio": False
        },
        async_processing=True
    )