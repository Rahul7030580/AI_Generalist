from modules.cause_engine import infer_causes

def analyze(data, raw_text):

    result = {}

    area_map = data.get("area_map", {})

    total_issues = sum(len(v) for v in area_map.values())

    # severity logic (dynamic)
    if total_issues > 8:
        severity = "High"
    elif total_issues > 4:
        severity = "Moderate"
    else:
        severity = "Low"

    result["severity"] = severity

    # ---- cause engine ----
    result["root_causes"] = infer_causes(area_map, raw_text)

    return result