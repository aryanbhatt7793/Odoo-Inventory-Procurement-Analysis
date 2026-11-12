
from pathlib import Path
import markdown

root = Path(__file__).resolve().parent

documents = [
    ("Project Summary", "12_Final_Report/Project_Summary.md"),
    ("Business Requirements", "08_BRD/Business_Requirements.md"),
    ("Process Analysis", "09_Process_Maps/AS_IS_TO_BE_Process.md"),
    ("Gap Analysis", "10_Gap_Analysis/Gap_Analysis.md"),
    ("UAT Test Cases", "11_UAT_Testing/UAT_Test_Cases.md"),
]

sections = []

for title, filename in documents:
    path = root / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing document: {filename}")

    content = path.read_text(encoding="utf-8")
    html = markdown.markdown(
        content,
        extensions=["tables", "fenced_code"]
    )
    sections.append(f'<section><h1>{title}</h1>{html}</section>')

page = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Apex Components - ERP Case Study</title>
<style>
body {{
    font-family: Arial, sans-serif;
    color: #263238;
    max-width: 900px;
    margin: 40px auto;
    padding: 20px;
    line-height: 1.55;
}}
h1 {{ color: #253b70; border-bottom: 2px solid #253b70; padding-bottom: 8px; }}
h2 {{ color: #315b83; margin-top: 25px; }}
table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
th, td {{ border: 1px solid #cbd5e1; padding: 8px; text-align: left; }}
th {{ background: #eaf0f7; }}
section {{ margin-bottom: 45px; }}
@media print {{
    body {{ max-width: none; margin: 12mm; padding: 0; }}
    section {{ page-break-before: always; }}
    section:first-of-type {{ page-break-before: auto; }}
    h1, h2 {{ page-break-after: avoid; }}
    table {{ page-break-inside: avoid; }}
}}
</style>
</head>
<body>
{''.join(sections)}
</body>
</html>"""

output = root / "Apex_Components_Project_Report.html"
output.write_text(page, encoding="utf-8")

print(f"Report created: {output}")
