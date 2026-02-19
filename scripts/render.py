#!/usr/bin/env python3

import argparse
import json
import re
from pathlib import Path


def _get_value(container, *keys, default=""):
    current = container
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    if current is None:
        return default
    return current


def _as_csv(values):
    if isinstance(values, list):
        return ", ".join(str(value) for value in values if value is not None)
    if values is None:
        return ""
    return str(values)


def _extract_year(report_id: str, source_path: Path) -> str:
    parts = report_id.split("-")
    if len(parts) >= 2 and parts[1].isdigit() and len(parts[1]) == 4:
        return parts[1]

    for parent in source_path.parents:
        if parent.name.isdigit() and len(parent.name) == 4:
            return parent.name

    return "unknown"


def _metrics_row(metric):
    if isinstance(metric, dict):
        scorer = metric.get("scorer", "")
        metric_name = metric.get("metrics", metric.get("metric", ""))
        value = metric.get("value", "")
        if isinstance(value, (int, float)):
            value = f"{value:.2f}"
        return str(scorer), str(metric_name), str(value)

    if isinstance(metric, list):
        return "", "", "; ".join(str(item) for item in metric)

    return "", "", str(metric)


def _split_measurement_details(details: str):
    if not isinstance(details, str):
        return "", ""

    pattern = re.compile(r"(?im)^##\s+Measurement details\s*$")
    match = pattern.search(details)
    if not match:
        return details.strip(), ""

    main_details = details[:match.start()].strip()
    measurement_details = details[match.end():].strip()
    return main_details, measurement_details


def render_report_markdown(report: dict, source_path: Path) -> str:
    report_id = _get_value(
        report,
        "metadata",
        "report_id",
        default=source_path.stem,
    )
    year = _extract_year(report_id, source_path)

    description = _get_value(
        report,
        "problemtype",
        "description",
        "value",
    )
    details = _get_value(report, "description", "value")
    details, measurement_details = _split_measurement_details(details)
    metrics = report.get("metrics") or []
    references = report.get("references") or []

    risk_domains = _as_csv(
        _get_value(report, "impact", "avid", "risk_domain", default=[])
    )
    sep_subcategories = _as_csv(
        _get_value(report, "impact", "avid", "sep_view", default=[])
    )
    lifecycle_stages = _as_csv(
        _get_value(report, "impact", "avid", "lifecycle_view", default=[])
    )

    developer = _as_csv(_get_value(report, "affects", "developer", default=[]))
    deployer = _as_csv(_get_value(report, "affects", "deployer", default=[]))
    artifacts = _get_value(report, "affects", "artifacts", default=[])

    report_type = _get_value(report, "problemtype", "type")
    credits = _as_csv(
        [
            credit.get("value")
            for credit in (report.get("credit") or [])
            if isinstance(credit, dict)
        ]
    )
    reported_date = _get_value(report, "reported_date")
    version = _get_value(report, "data_version")

    lines = [
        "---",
        f"title: {report_id}",
        "layout: page",
        f"url: /database/{report_id}",
        "---",
        "",
        "## Description",
        "",
        description,
        "",
        "## Details",
        "",
        details,
        "",
    ]

    if metrics or measurement_details:
        lines.extend(
            [
                "## Metrics",
                "",
            ]
        )

        if measurement_details:
            lines.append(measurement_details)
            lines.append("")

        if metrics:
            lines.extend(
                [
                    "| Scorer | Metric | Value |",
                    "| --- | --- | --- |",
                ]
            )

            for metric in metrics:
                scorer, metric_name, value = _metrics_row(metric)
                lines.append(f"| {scorer} | {metric_name} | {value} |")

        lines.append("")

    lines.extend(
        [
            "## References",
            "",
        ]
    )

    for reference in references:
        label = (
            reference.get("label", "")
            if isinstance(reference, dict)
            else ""
        )
        url = reference.get("url", "") if isinstance(reference, dict) else ""
        lines.append(f"- [{label}]({url})")

    lines.extend(
        [
            "",
            "## AVID Taxonomy Categorization",
            "",
            f"- **Risk domains:** {risk_domains}",
            f"- **SEP subcategories:** {sep_subcategories}",
            f"- **Lifecycle stages:** {lifecycle_stages}",
            "",
            "## Affected or Relevant Artifacts",
            "",
            f"- **Developer:** {developer}",
            f"- **Deployer:** {deployer}",
            "- **Artifact Details:**",
            "",
            "| Type | Name |",
            "| --- | --- | ",
        ]
    )

    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        artifact_type = artifact.get("type", "")
        artifact_name = artifact.get("name", "")
        lines.append(f"| {artifact_type} | {artifact_name} |")

    lines.extend(
        [
            "",
            "## Other information",
            "",
            f"- **Report Type:** {report_type}",
            f"- **Credits:** {credits}",
            f"- **Date Reported:** {reported_date}",
            f"- **Version:** {version}",
            (
                "- [AVID Entry](https://github.com/avidml/avid-db/tree/main/"
                f"reports/{year}/{source_path.name})"
            ),
            "",
            "",
        ]
    )

    return "\n".join(lines)


def default_output_path(source_path: Path, website_root: Path) -> Path:
    year = source_path.parent.name if source_path.parent.name.isdigit() else ""
    reports_root = (
        website_root / "exampleSite" / "content" / "database" / "reports"
    )
    if year:
        return reports_root / year / f"{source_path.stem}.md"
    return reports_root / f"{source_path.stem}.md"


def render_file(source_path: Path, output_path: Path):
    with source_path.open("r", encoding="utf-8") as source_file:
        report = json.load(source_file)

    markdown = render_report_markdown(report, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Rendered {source_path} -> {output_path}")


def _build_reports_year_table(year: str, report_ids):
    lines = [
        f"#### {year}",
        "| | | | |",
        "|---|---|---|---|",
    ]

    row = []
    for report_id in report_ids:
        row.append(f"[{report_id}](/database/{report_id})")
        if len(row) == 4:
            lines.append("| " + " | ".join(row) + " |")
            row = []

    if row:
        row.extend([""] * (4 - len(row)))
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def _sync_reports_index_for_year(website_root: Path, year: str):
    if not year.isdigit() or len(year) != 4:
        return

    reports_dir = (
        website_root
        / "exampleSite"
        / "content"
        / "database"
        / "reports"
        / year
    )
    if not reports_dir.exists() or not reports_dir.is_dir():
        return

    report_ids = sorted(
        path.stem
        for path in reports_dir.glob("AVID-*.md")
        if path.is_file()
    )
    if not report_ids:
        return

    index_path = (
        website_root
        / "exampleSite"
        / "content"
        / "database"
        / "_index.md"
    )
    if not index_path.exists():
        return

    content = index_path.read_text(encoding="utf-8")

    section_pattern = re.compile(
        rf"(?ms)^####\s+{re.escape(year)}\n"
        r"\| \| \| \| \|\n"
        r"\|---\|---\|---\|---\|\n"
        r".*?(?=^####\s+\d{4}\n|\Z)"
    )

    replacement = _build_reports_year_table(year, report_ids) + "\n\n"

    if section_pattern.search(content):
        updated = section_pattern.sub(replacement, content, count=1)
    else:
        reports_marker = "### List of Reports"
        marker_pos = content.find(reports_marker)
        if marker_pos == -1:
            return
        insert_pos = content.find("\n", marker_pos)
        if insert_pos == -1:
            insert_pos = len(content)
        updated = (
            content[: insert_pos + 1]
            + "\n"
            + replacement
            + content[insert_pos + 1:]
        )

    if updated != content:
        index_path.write_text(updated, encoding="utf-8")
        print(f"Updated report links in {index_path} for year {year}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Render AVID report JSON files into website markdown pages."
        )
    )
    parser.add_argument(
        "input",
        type=Path,
        help=(
            "Path to a report JSON file or a directory containing report "
            "JSON files."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=(
            "Optional output file or directory. If omitted, writes to "
            "exampleSite/content/database/reports/<year>/"
        ),
    )

    args = parser.parse_args()

    website_root = Path(__file__).resolve().parent.parent
    input_path = args.input.resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input path does not exist: {input_path}")

    if input_path.is_file():
        output_path = (
            args.output.resolve()
            if args.output
            else default_output_path(input_path, website_root)
        )
        if args.output and args.output.exists() and args.output.is_dir():
            output_path = output_path / f"{input_path.stem}.md"
        render_file(input_path, output_path)

        reports_root = (
            website_root / "exampleSite" / "content" / "database" / "reports"
        )
        try:
            rel = output_path.resolve().relative_to(reports_root)
            if len(rel.parts) >= 2 and rel.parts[0].isdigit():
                _sync_reports_index_for_year(website_root, rel.parts[0])
        except ValueError:
            pass
        return

    json_files = sorted(
        path for path in input_path.glob("*.json") if path.is_file()
    )
    if not json_files:
        raise FileNotFoundError(
            f"No JSON files found in directory: {input_path}"
        )

    if args.output:
        output_base = args.output.resolve()
        if output_base.suffix.lower() == ".md":
            raise ValueError(
                "When rendering a directory, --output must be "
                "a directory path."
            )
    else:
        year = input_path.name if input_path.name.isdigit() else ""
        output_base = (
            website_root / "exampleSite" / "content" / "database" / "reports"
        )
        if year:
            output_base = output_base / year

    for json_file in json_files:
        output_path = output_base / f"{json_file.stem}.md"
        render_file(json_file, output_path)

    reports_root = (
        website_root / "exampleSite" / "content" / "database" / "reports"
    )
    try:
        rel = output_base.resolve().relative_to(reports_root)
        if rel.parts and rel.parts[0].isdigit():
            _sync_reports_index_for_year(website_root, rel.parts[0])
    except ValueError:
        pass


if __name__ == "__main__":
    main()
