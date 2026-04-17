import streamlit as st
import io
import os

# -------- MODULES --------
from modules.parser import extract_text, extract_images
from modules.extractor import extract_data
from modules.analyzer import analyze
from modules.section_builder import build_sections
from modules.report_generator import generate_ddr
from modules.image_mapper import map_images
from modules.merger import merge_data

# -------- PDF --------
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="DDR Generator", layout="wide")
st.title("🏗️ AI DDR Report Generator")

inspection = st.file_uploader("Upload Inspection PDF", type="pdf")
thermal = st.file_uploader("Upload Thermal PDF", type="pdf")


# ---------------- PDF FUNCTION ----------------
def generate_pdf(ddr_text, images):

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    # ---- TEXT ----
    for line in ddr_text.split("\n"):
        if line.strip():
            content.append(Paragraph(line, styles["Normal"]))
            content.append(Spacer(1, 6))

    content.append(Spacer(1, 15))

    # ---- IMAGES (SAFE) ----
    for img in images:
        try:
            path = img.get("path", "")

            # skip invalid
            if not path or not os.path.exists(path):
                continue

            # only safe formats
            if not path.lower().endswith((".png", ".jpg", ".jpeg")):
                continue

            content.append(Paragraph(img.get("label", "Image"), styles["Heading3"]))
            content.append(Image(path, width=300, height=200))
            content.append(Spacer(1, 10))

        except:
            continue  # never break PDF

    doc.build(content)
    buffer.seek(0)

    return buffer


# ---------------- MAIN ----------------
if st.button("Generate DDR Report"):

    if inspection and thermal:

        try:
            # ---- Save PDFs ----
            with open("inspection.pdf", "wb") as f:
                f.write(inspection.read())

            with open("thermal.pdf", "wb") as f:
                f.write(thermal.read())

            # ---- STEP 1: TEXT ----
            text = extract_text("inspection.pdf") + extract_text("thermal.pdf")

            # ---- STEP 2: EXTRACT ----
            data = extract_data(text)

            # ---- STEP 3: ANALYZE ----
            analysis = analyze(data, text)
            data.update(analysis)

            # ---- STEP 4: MERGE ----
            data["merged_areas"] = merge_data(data)

            # ---- STEP 5: BUILD SECTIONS ----
            sections = build_sections(data, text)

            # ---- STEP 6: GENERATE DDR ----
            ddr = generate_ddr(sections)

            # ---- DISPLAY DDR ----
            st.subheader("📄 Generated DDR")
            st.write(ddr)

            # ---- STEP 7: EXTRACT IMAGES ----
            insp_imgs = extract_images("inspection.pdf", "outputs/inspection")
            therm_imgs = extract_images("thermal.pdf", "outputs/thermal")

            mapped = map_images(insp_imgs, therm_imgs, data)

            # ---- SHOW IMAGES ----
            st.subheader("🖼️ Extracted Images")
            for img in mapped:
                try:
                    st.image(img["path"], width=400)
                except:
                    continue

            # ---- STEP 8: PDF ----
            pdf_file = generate_pdf(ddr, mapped)

            st.download_button(
                label="📄 Download DDR Report",
                data=pdf_file,
                file_name="DDR_Report.pdf",
                mime="application/pdf"
            )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please upload both PDFs")