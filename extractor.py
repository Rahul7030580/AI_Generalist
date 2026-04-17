import re
from collections import defaultdict

def normalize_text(text):
    return text.lower()


def extract_data(text):

    text = normalize_text(text)

    data = {
        "area_map": defaultdict(set),
        "raw_sentences": []
    }

    # split sentences
    sentences = re.split(r"[.\n]", text)

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue

        data["raw_sentences"].append(sent)

        # detect possible area (flexible)
        area_match = re.findall(r"(hall|bedroom|kitchen|bathroom|parking|external|wall|balcony|terrace)", sent)

        # detect issue words (not fixed list — pattern based)
        issue_match = re.findall(r"(damp\w*|leak\w*|seep\w*|crack\w*|moist\w*|efflorescence)", sent)

        for area in area_match:
            for issue in issue_match:
                data["area_map"][area.title()].add(issue)

    # convert sets → list
    data["area_map"] = {k: list(v) for k, v in data["area_map"].items()}

    return data