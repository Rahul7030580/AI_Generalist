import fitz  # PyMuPDF
import os
import hashlib


# -------- TEXT EXTRACTION --------
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


# -------- IMAGE EXTRACTION (DEDUP) --------
def extract_images(pdf_path, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    doc = fitz.open(pdf_path)

    image_paths = []
    seen_hashes = set()

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # 🔥 remove duplicates
            img_hash = hashlib.md5(image_bytes).hexdigest()
            if img_hash in seen_hashes:
                continue

            seen_hashes.add(img_hash)

            image_ext = base_image["ext"]
            image_name = f"img_{page_index}_{img_index}.{image_ext}"
            image_path = os.path.join(output_folder, image_name)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    return image_paths