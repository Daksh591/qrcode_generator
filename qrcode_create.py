import qrcode
import webbrowser
import streamlit
streamlit.subheader("QR Code generator")
a = streamlit.text_area("Enter your QRCode data - ")
b = qrcode.make(a)
c = streamlit.text_input("Enter your qrcode save file name","sampleqr.png",placeholder="Enter like - sampleqr.png")
b.save(c)
bu = streamlit.button("See your qrcode")
if bu:
    try:
        webbrowser.open(c)
        streamlit.success("You're QR Code is created")
    except Exception as e:
        streamlit.error("Do not do this mistake")

    streamlit.text("Some more websites listed below: - ")
    streamlit.markdown("[Age Calculator](https://agecalculatordaksh.streamlit.app)")
    streamlit.markdown("[Know you BMI](https://knowbmibody.streamlit.app)")
    streamlit.markdown("[Know your phone number's service provider](https://knowdaksh.streamlit.app/)")

