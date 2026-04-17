def build_sections(data, raw_text):

    sections = {}

    merged = data.get("merged_areas", {})
    causes = data.get("root_causes", [])
    severity = data.get("severity", "Moderate")

    # 1
    sections["introduction"] = (
        "This report presents findings from a detailed inspection conducted to identify "
        "leakage, dampness, and structural concerns within the property."
    )

    # 2
    sections["general"] = "General property details are Not Available."

    # 3 🔥 FIXED OBSERVATIONS
    obs_lines = []

    for area, issues in merged.items():
        obs_lines.append(f"{area}:")
        for issue in issues:
            obs_lines.append(f"- {issue}")

    sections["observations"] = "\n".join(obs_lines)

    # 4
    sections["causes"] = "\n".join(causes) if causes else "Not Available"

    # 5
    sections["severity"] = f"{severity} severity based on spread of issues."

    # 6
    sections["recommendations"] = "Repair defects, waterproof affected areas, fix leakage sources."

    # 7
    sections["thermal"] = "Thermal data Not Available."

    # 8
    sections["limitations"] = "Based on visible inspection only."

    return sections