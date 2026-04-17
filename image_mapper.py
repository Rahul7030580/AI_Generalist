def map_images(inspection_imgs, thermal_imgs, data):

    mapped = []

    areas = list(data.get("area_map", {}).keys())

    # assign images dynamically
    for i, img in enumerate(inspection_imgs):
        area = areas[i % len(areas)] if areas else "General"

        mapped.append({
            "label": f"Image {i+1}",
            "path": img,
            "area": area,
            "type": "inspection"
        })

    for i, img in enumerate(thermal_imgs):
        area = areas[i % len(areas)] if areas else "General"

        mapped.append({
            "label": f"Thermal {i+1}",
            "path": img,
            "area": area,
            "type": "thermal"
        })

    return mapped