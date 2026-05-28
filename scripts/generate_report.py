import json
import xml.etree.ElementTree as ET

summary = {}

# cppcheck
try:
    tree = ET.parse("reports/cppcheck.xml")
    root = tree.getroot()

    cppcheck_count = len(root.findall(".//error"))
    summary["cppcheck"] = cppcheck_count

except:
    summary["cppcheck"] = 0

# clang-tidy
try:
    with open("reports/clang-tidy.txt") as f:
        lines = f.readlines()

    summary["clang-tidy"] = len(lines)

except:
    summary["clang-tidy"] = 0

# semgrep
try:
    with open("reports/semgrep.sarif") as f:
        data = json.load(f)

    results = data["runs"][0]["results"]
    summary["semgrep"] = len(results)

except:
    summary["semgrep"] = 0

# trivy
try:
    with open("reports/trivy.json") as f:
        data = json.load(f)

    count = 0

    for result in data.get("Results", []):
        count += len(result.get("Vulnerabilities", []))

    summary["trivy"] = count

except:
    summary["trivy"] = 0

# Generate markdown
with open("reports/summary.md", "w") as f:

    f.write("# Security Scan Summary\n\n")
    f.write("| Tool | Issues |\n")
    f.write("|------|--------|\n")

    for tool, issues in summary.items():
        f.write(f"| {tool} | {issues} |\n")

print("Summary report generated.")
