def merge_data(data):

    merged = {}

    area_map = data.get("area_map", {})

    # ensure all standard areas exist
    standard_areas = ["Hall", "Bedroom", "Kitchen", "Bathroom", "Parking", "External"]

    for area in standard_areas:
        issues = area_map.get(area, [])

        if not issues:
            merged[area] = ["Not Available"]
        else:
            merged[area] = list(set(issues))  # remove duplicates

    return merged