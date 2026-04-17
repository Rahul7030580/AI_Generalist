import re

def infer_causes(area_map, raw_text):

    causes = set()
    text = raw_text.lower()

    # pattern-based reasoning (NOT hardcoded mapping)

    if re.search(r"tile|joint|gap|grout", text):
        causes.add("Water ingress through tile joints leading to seepage via capillary action")

    if re.search(r"crack|fracture", text):
        causes.add("Water ingress through cracks in walls or structural elements")

    if re.search(r"damp|moist|efflorescence", text):
        causes.add("Moisture intrusion due to prolonged water exposure and inadequate waterproofing")

    if re.search(r"leak|plumbing|pipe", text):
        causes.add("Leakage from plumbing systems causing continuous moisture exposure")

    if re.search(r"terrace|slope|ponding", text):
        causes.add("Improper slope or drainage leading to water accumulation")

    if re.search(r"thermal|temperature", text):
        causes.add("Thermal variations indicating moisture presence within structural components")

    return list(causes)