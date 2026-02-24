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
        value = _format_inspect_metric_value(metric.get("value", ""))
        return str(scorer), str(metric_name), str(value)

    if isinstance(metric, list):
        return "", "", "; ".join(str(item) for item in metric)

    return "", "", str(metric)


def _render_test_scores_metrics(metrics):
    if not isinstance(metrics, list) or not metrics:
        return None

    first_metric = metrics[0]
    if not isinstance(first_metric, dict):
        return None

    results = first_metric.get("results")
    if not isinstance(results, dict):
        return None

    test_scores = results.get("Test Scores")
    if not isinstance(test_scores, list):
        return None

    score_rows = [row for row in test_scores if isinstance(row, dict)]
    if not score_rows:
        return None

    headers = []
    seen = set()
    for row in score_rows:
        for key in row.keys():
            if key in seen:
                continue
            seen.add(key)
            headers.append(str(key))

    detection_name = _get_value(
        first_metric,
        "detection_method",
        "name",
        default="",
    )
    if detection_name:
        lead_line = f"{detection_name} obtained the following test scores."
    else:
        lead_line = "The following test scores were obtained."

    lines = [
        lead_line,
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for row in score_rows:
        values = [_format_metric_value(row.get(header, "")) for header in headers]
        lines.append("| " + " | ".join(values) + " |")

    return lines


def _render_detector_failure_metrics(metrics):
    if not isinstance(metrics, list) or not metrics:
        return None

    first_metric = metrics[0]
    if not isinstance(first_metric, dict):
        return None

    results = first_metric.get("results")
    if not isinstance(results, dict):
        return None

    rows = results.get("rows")
    if not isinstance(rows, list):
        return None

    row_dicts = [row for row in rows if isinstance(row, dict)]
    if not row_dicts:
        return None

    headers = []
    seen = set()
    for row in row_dicts:
        for key in row.keys():
            if key in seen:
                continue
            seen.add(key)
            headers.append(str(key))

    lines = [
        "Number of failures were counted for each detector in the probe.",
        "",
        "| " + " | ".join(_metric_header_label(header) for header in headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for row in row_dicts:
        values = []
        for header in headers:
            raw_value = row.get(header, "")
            normalized_header = str(header).strip().lower()
            if normalized_header in {"passed", "total"}:
                values.append(_format_whole_number(raw_value))
            elif normalized_header == "score":
                values.append(_format_defcon_score(raw_value))
            else:
                values.append(_format_metric_value(raw_value))
        lines.append("| " + " | ".join(values) + " |")

    return lines


def _metric_header_label(key):
    raw = str(key).strip()
    if not raw:
        return ""
    return _title_case_key(raw.split("_", 1)[0])


def _format_metric_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return str(value)
    if isinstance(value, str):
        return value
    return _stringify_value(value)


def _format_inspect_metric_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return f"{float(value):.3f}"
    if isinstance(value, float):
        return f"{value:.3f}"
    if isinstance(value, str):
        stripped = value.strip()
        try:
            return f"{float(stripped):.3f}"
        except ValueError:
            return value
    return _stringify_value(value)


def _format_whole_number(value):
    try:
        return str(int(round(float(value))))
    except (TypeError, ValueError):
        return _stringify_value(value)


def _format_defcon_score(value):
    try:
        score = float(value)
    except (TypeError, ValueError):
        return _stringify_value(value)

    # ABSOLUTE_DEFCON_BOUNDS * 100 from garak/analyze/__init__.py
    if score < 5:
        return f"🔴 {score:.1f}"
    if score < 40:
        return f"🟠 {score:.1f}"
    if score < 80:
        return f"🟡 {score:.1f}"
    if score < 99:
        return f"🟢 {score:.1f}"
    return f"🔵 {score:.1f}"

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


def _stringify_value(value):
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _severity_colorize(value):
    text = _stringify_value(value)
    lowered = text.strip().lower()
    if lowered == "critical":
        return "🔴 Critical"
    if lowered == "high":
        return "🔴 High"
    if lowered == "medium":
        return "🟠 Medium"
    if lowered == "low":
        return "🟢 Low"
    return text


def _format_table_cell(value):
    if isinstance(value, list):
        return ", ".join(_stringify_value(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return _severity_colorize(value)


def _title_case_key(key):
    raw = str(key).strip()
    if not raw:
        return ""

    normalized = re.sub(r"[_\-]+", " ", raw)
    normalized = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", normalized)
    words = normalized.split()

    out_words = []
    for word in words:
        lowered = word.lower()
        if lowered == "cvss":
            out_words.append("CVSS")
        elif lowered == "cwe":
            out_words.append("CWE")
        elif lowered == "id":
            out_words.append("ID")
        else:
            out_words.append(lowered.capitalize())
    return " ".join(out_words)


def _render_nested_bullets(value, indent: int = 0):
    prefix = "  " * indent
    lines = []

    if isinstance(value, dict):
        if not value:
            lines.append(f"{prefix}- _(empty)_")
            return lines

        for key, nested in value.items():
            if isinstance(nested, (dict, list)):
                lines.append(f"{prefix}- **{key}:**")
                lines.extend(_render_nested_bullets(nested, indent + 1))
            else:
                lines.append(
                    f"{prefix}- **{key}:** {_stringify_value(nested)}"
                )
        return lines

    if isinstance(value, list):
        if not value:
            lines.append(f"{prefix}- _(empty)_")
            return lines

        for index, item in enumerate(value, start=1):
            if isinstance(item, (dict, list)):
                lines.append(f"{prefix}- **Item {index}:**")
                lines.extend(_render_nested_bullets(item, indent + 1))
            else:
                lines.append(f"{prefix}- {_stringify_value(item)}")
        return lines

    lines.append(f"{prefix}- {_stringify_value(value)}")
    return lines


def _render_impact_avid(value):
    risk_domains = _as_csv(_get_value(value, "risk_domain", default=[]))
    sep_subcategories = _as_csv(_get_value(value, "sep_view", default=[]))
    lifecycle_stages = _as_csv(
        _get_value(value, "lifecycle_view", default=[])
    )
    return [
        "### AVID Taxonomy Categorization",
        "",
        f"- **Risk domains:** {risk_domains}",
        f"- **SEP subcategories:** {sep_subcategories}",
        f"- **Lifecycle stages:** {lifecycle_stages}",
        "",
    ]


def _render_impact_cvss(value):
    lines = [
        "### CVSS",
        "",
    ]

    if not isinstance(value, dict) or not value:
        lines.extend(["- _(none)_", ""])
        return lines

    lines.extend(
        [
            "<table>",
            "<tbody>",
        ]
    )

    for key, nested_value in value.items():
        lines.append(
            "<tr>"
            f"<td>{_title_case_key(key)}</td>"
            f"<td>{_format_table_cell(nested_value)}</td>"
            "</tr>"
        )

    lines.extend(
        [
            "</tbody>",
            "</table>",
        ]
    )

    lines.append("")
    return lines


def _render_impact_cwe(value):
    lines = [
        "### CWE",
        "",
    ]

    if not isinstance(value, list) or not value:
        lines.extend(["- _(none)_", ""])
        return lines

    dict_items = [item for item in value if isinstance(item, dict)]
    if not dict_items:
        lines.extend(["- _(none)_", ""])
        return lines

    lines.append("| ID | Description |")
    lines.append("| --- | --- |")

    for item in dict_items:
        cwe_id = item.get("cweId", item.get("id", ""))
        description = item.get("description", "")
        if isinstance(description, dict):
            description = description.get("value", "")
        lines.append(
            f"| {_format_table_cell(cwe_id)} | {_format_table_cell(description)} |"
        )

    lines.append("")
    return lines


def _render_impact_odin(value):
    lines = [
        "### 0DIN",
        "",
    ]

    if not isinstance(value, dict) or not value:
        lines.extend(["- _(none)_", ""])
        return lines

    for key, nested_value in value.items():
        if key == "JailbreakTaxonomy" and isinstance(nested_value, list):
            rows = [item for item in nested_value if isinstance(item, dict)]
            lines.append(f"- **{_title_case_key(key)}:**")
            if not rows:
                lines.append("  - _(none)_")
                continue

            headers = []
            seen = set()
            for row in rows:
                for header in row.keys():
                    if header in seen:
                        continue
                    seen.add(header)
                    headers.append(str(header))

            lines.append("")
            lines.append("| " + " | ".join(_title_case_key(h) for h in headers) + " |")
            lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
            for row in rows:
                values = [_stringify_value(row.get(header, "")) for header in headers]
                lines.append("| " + " | ".join(values) + " |")
            lines.append("")
            continue

        if isinstance(nested_value, (dict, list)):
            lines.append(f"- **{_title_case_key(key)}:**")
            lines.extend(_render_nested_bullets(nested_value, indent=1))
        else:
            lines.append(
                f"- **{_title_case_key(key)}:** {_stringify_value(nested_value)}"
            )

    lines.append("")
    return lines


def _render_impact_section(impact):
    lines = [
        "## Impact",
        "",
    ]

    if not isinstance(impact, dict) or not impact:
        lines.extend(["- _(none)_", ""])
        return lines

    for key, value in impact.items():
        normalized_key = str(key).strip().lower()
        if normalized_key == "avid":
            lines.extend(_render_impact_avid(value))
            continue
        if normalized_key == "odin":
            lines.extend(_render_impact_odin(value))
            continue
        if normalized_key == "cvss":
            lines.extend(_render_impact_cvss(value))
            continue
        if normalized_key == "cwe":
            lines.extend(_render_impact_cwe(value))
            continue

        lines.extend(
            [
                f"### {key}",
                "",
            ]
        )
        lines.extend(_render_nested_bullets(value))
        lines.append("")

    return lines


def _is_odin_disclosure(report: dict) -> bool:
    impact = report.get("impact")
    if isinstance(impact, dict) and "odin" in impact:
        return True

    references = report.get("references") or []
    for reference in references:
        if not isinstance(reference, dict):
            continue
        label = _stringify_value(reference.get("label", "")).lower()
        url = _stringify_value(reference.get("url", "")).lower()
        if "0din" in label or "0din" in url:
            return True

    return False


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

    developer = _as_csv(_get_value(report, "affects", "developer", default=[]))
    deployer = _as_csv(_get_value(report, "affects", "deployer", default=[]))
    artifacts = _get_value(report, "affects", "artifacts", default=[])

    report_type = _get_value(report, "problemtype", "type")
    impact = report.get("impact")
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
            test_scores_lines = _render_test_scores_metrics(metrics)
            if test_scores_lines is not None:
                lines.extend(test_scores_lines)
            else:
                detector_failure_lines = _render_detector_failure_metrics(metrics)
                if detector_failure_lines is not None:
                    lines.extend(detector_failure_lines)
                else:
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
            "## Affected or Relevant Artifacts",
            "",
            "| Type | Name |",
            "| --- | --- | ",
        ]
    )

    if not _is_odin_disclosure(report):
        lines = lines[:-2]
        lines.extend(
            [
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

    lines.extend(["", * _render_impact_section(impact)])

    lines.extend(
        [
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


def _extract_report_index_row(report_path: Path):
    report_id = report_path.stem
    description = ""
    report_type = ""
    reported_date = ""

    content = report_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    in_description = False
    in_other_info = False
    for line in lines:
        stripped = line.strip()

        if stripped == "## Description":
            in_description = True
            in_other_info = False
            continue

        if stripped.startswith("## ") and stripped != "## Description":
            in_description = False
            in_other_info = stripped == "## Other information"

        if in_description and stripped and not stripped.startswith("---"):
            description = stripped
            in_description = False
            continue

        if in_other_info:
            if stripped.startswith("- **Report Type:**"):
                report_type = stripped.replace("- **Report Type:**", "", 1).strip()
            elif stripped.startswith("- **Date Reported:**"):
                reported_date = stripped.replace(
                    "- **Date Reported:**",
                    "",
                    1,
                ).strip()

    description = description.replace("|", "\\|")
    report_type = report_type.replace("|", "\\|")
    reported_date = reported_date.replace("|", "\\|")
    return report_id, description, report_type, reported_date


def _extract_vulnerability_index_row(vuln_path: Path):
    vuln_id = vuln_path.stem
    description = ""

    try:
        content = vuln_path.read_text(encoding="utf-8")
    except OSError:
        return vuln_id, description

    in_description = False
    for line in content.splitlines():
        stripped = line.strip()

        if stripped == "## Description":
            in_description = True
            continue

        if stripped.startswith("## ") and stripped != "## Description":
            in_description = False

        if in_description and stripped and not stripped.startswith("---"):
            description = stripped
            break

    description = description.replace("|", "\\|")
    return vuln_id, description


def _build_vulnerabilities_year_table(year: str, vuln_paths):
    rows = [_extract_vulnerability_index_row(path) for path in vuln_paths]
    table_id = f"vulnerabilities-{year}"
    page_size_id = f"{table_id}-page-size"
    pager_id = f"{table_id}-pager"

    lines = [
        f"<!-- vulnerabilities-year:{year}:start -->",
        f"##### {year}",
        "",
        "<div class=\"avid-report-controls\" style=\"display: flex; justify-content: flex-end; margin: 0.5rem 0;\">",
        "  <label style=\"display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;\">",
        "    Rows per page:",
        (
            f"    <select id=\"{page_size_id}\" style=\"display: inline-block; width: auto; min-width: 4.5rem;\">"
            "<option value=\"10\">10</option>"
            "<option value=\"20\" selected>20</option>"
            "<option value=\"50\">50</option>"
            "</select>"
        ),
        "  </label>",
        "</div>",
        (
            f"<table class=\"avid-report-table\" id=\"{table_id}\" "
            "style=\"table-layout: fixed; width: 100%;\">"
        ),
        "  <colgroup>",
        "    <col style=\"width: 28%;\">",
        "    <col style=\"width: 72%;\">",
        "  </colgroup>",
        "  <thead>",
        "    <tr>",
        (
            "      <th data-sort-col=\"0\" "
            "style=\"white-space: nowrap;\">Vulnerability ID</th>"
        ),
        (
            "      <th data-sort-col=\"1\" "
            "style=\"overflow: hidden; text-overflow: ellipsis; white-space: nowrap;\">"
            "Description</th>"
        ),
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]

    for vuln_id, description in rows:
        lines.append(
            "    <tr>"
            f"<td><a href=\"/database/{vuln_id}\">{vuln_id}</a></td>"
            f"<td style=\"overflow: hidden; text-overflow: ellipsis; white-space: nowrap;\">{description}</td>"
            "</tr>"
        )

    lines.extend(
        [
            "  </tbody>",
            "</table>",
            (
                f"<div class=\"avid-report-pager\" id=\"{pager_id}\" "
                "style=\"display: flex; justify-content: flex-end; align-items: center; "
                "gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;\"></div>"
            ),
            "",
            "<script>",
            "if (!window.__avidReportTableInit) {",
            "  window.__avidReportTableInit = function (tableId) {",
            "    var table = document.getElementById(tableId);",
            "    if (!table) return;",
            "    var tbody = table.querySelector('tbody');",
            "    if (!tbody) return;",
            "    var pageSizeSelect = document.getElementById(tableId + '-page-size');",
            "    var pager = document.getElementById(tableId + '-pager');",
            "    if (!pageSizeSelect || !pager) return;",
            "",
            "    var state = {",
            "      page: 1,",
            "      pageSize: Number(pageSizeSelect.value) || 20,",
            "    };",
            "",
            "    function getRows() {",
            "      return Array.from(tbody.querySelectorAll('tr'));",
            "    }",
            "",
            "    function renderPager(totalPages) {",
            "      pager.innerHTML = '';",
            "",
            "      function appendButton(label, pageNo, disabled) {",
            "        var button = document.createElement('button');",
            "        button.type = 'button';",
            "        button.textContent = label;",
            "        button.style.width = 'auto';",
            "        button.style.minWidth = '2.25rem';",
            "        button.style.display = 'inline-block';",
            "        button.disabled = !!disabled;",
            "        if (!button.disabled) {",
            "          button.addEventListener('click', function () {",
            "            state.page = pageNo;",
            "            render();",
            "          });",
            "        }",
            "        pager.appendChild(button);",
            "      }",
            "",
            "      function appendEllipsis() {",
            "        var span = document.createElement('span');",
            "        span.textContent = '...';",
            "        span.className = 'avid-pager-ellipsis';",
            "        pager.appendChild(span);",
            "      }",
            "",
            "      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);",
            "",
            "      if (totalPages <= 3) {",
            "        for (var i = 1; i <= totalPages; i += 1) {",
            "          appendButton(String(i), i, i === state.page);",
            "        }",
            "      } else {",
            "        appendButton('1', 1, state.page === 1);",
            "        appendButton('2', 2, state.page === 2);",
            "        appendEllipsis();",
            "        appendButton(String(totalPages), totalPages, state.page === totalPages);",
            "      }",
            "",
            "      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);",
            "    }",
            "",
            "    function syncSortIndicators() {",
            "      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {",
            "        var arrow = th.querySelector('.avid-sort-arrow');",
            "        if (!arrow) {",
            "          arrow = document.createElement('span');",
            "          arrow.className = 'avid-sort-arrow';",
            "          arrow.style.marginLeft = '0.35rem';",
            "          th.appendChild(arrow);",
            "        }",
            "        var dir = th.getAttribute('data-sort-dir');",
            "        if (dir === 'asc') {",
            "          arrow.textContent = '↑';",
            "        } else if (dir === 'desc') {",
            "          arrow.textContent = '↓';",
            "        } else {",
            "          arrow.textContent = '↕';",
            "        }",
            "      });",
            "    }",
            "",
            "    function render() {",
            "      var rows = getRows();",
            "      var totalRows = rows.length;",
            "      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));",
            "      if (state.page > totalPages) state.page = totalPages;",
            "      if (state.page < 1) state.page = 1;",
            "",
            "      var start = (state.page - 1) * state.pageSize;",
            "      var end = start + state.pageSize;",
            "      rows.forEach(function (row, idx) {",
            "        row.style.display = idx >= start && idx < end ? '' : 'none';",
            "      });",
            "",
            "      renderPager(totalPages);",
            "    }",
            "",
            "    if (!table.dataset.avidSortBound) {",
            "      table.dataset.avidSortBound = 'true';",
            "      table.addEventListener('click', function (event) {",
            "        var th = event.target.closest('th[data-sort-col]');",
            "        if (!th || !table.contains(th)) return;",
            "",
            "        var col = Number(th.getAttribute('data-sort-col'));",
            "        var current = th.getAttribute('data-sort-dir') || '';",
            "        var next = current === 'asc' ? 'desc' : 'asc';",
            "",
            "        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {",
            "          h.removeAttribute('data-sort-dir');",
            "        });",
            "        th.setAttribute('data-sort-dir', next);",
            "        syncSortIndicators();",
            "",
            "        var rows = getRows();",
            "        rows.sort(function (a, b) {",
            "          var av = (a.children[col] && a.children[col].innerText || '').trim();",
            "          var bv = (b.children[col] && b.children[col].innerText || '').trim();",
            "          var ad = Date.parse(av);",
            "          var bd = Date.parse(bv);",
            "          var cmp;",
            "          if (!Number.isNaN(ad) && !Number.isNaN(bd)) {",
            "            cmp = ad - bd;",
            "          } else {",
            "            cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });",
            "          }",
            "          return next === 'asc' ? cmp : -cmp;",
            "        });",
            "        rows.forEach(function (row) { tbody.appendChild(row); });",
            "        state.page = 1;",
            "        render();",
            "      });",
            "    }",
            "",
            "    if (!pageSizeSelect.dataset.avidPageSizeBound) {",
            "      pageSizeSelect.dataset.avidPageSizeBound = 'true';",
            "      pageSizeSelect.addEventListener('change', function () {",
            "        state.pageSize = Number(pageSizeSelect.value) || 20;",
            "        state.page = 1;",
            "        render();",
            "      });",
            "    }",
            "",
            "    syncSortIndicators();",
            "    render();",
            "  };",
            "}",
            f"window.__avidReportTableInit('{table_id}');",
            "</script>",
            f"<!-- vulnerabilities-year:{year}:end -->",
        ]
    )

    return "\n".join(lines)


def _build_reports_year_table(year: str, report_paths):
    rows = [_extract_report_index_row(path) for path in report_paths]
    table_id = f"reports-{year}"
    page_size_id = f"{table_id}-page-size"
    pager_id = f"{table_id}-pager"

    lines = [
        f"<!-- reports-year:{year}:start -->",
        f"#### {year}",
        "",
        "<div class=\"avid-report-controls\" style=\"display: flex; justify-content: flex-end; margin: 0.5rem 0;\">",
        "  <label style=\"display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;\">",
        "    Rows per page:",
        (
            f"    <select id=\"{page_size_id}\" style=\"display: inline-block; width: auto; min-width: 4.5rem;\">"
            "<option value=\"10\">10</option>"
            "<option value=\"20\" selected>20</option>"
            "<option value=\"50\">50</option>"
            "</select>"
        ),
        "  </label>",
        "</div>",
        (
            f"<table class=\"avid-report-table\" id=\"{table_id}\" "
            "style=\"table-layout: fixed; width: 100%;\">"
        ),
        "  <colgroup>",
        "    <col style=\"width: 18%;\">",
        "    <col style=\"width: 52%;\">",
        "    <col style=\"width: 15%;\">",
        "    <col style=\"width: 15%;\">",
        "  </colgroup>",
        "  <thead>",
        "    <tr>",
        (
            "      <th data-sort-col=\"0\" "
            "style=\"white-space: nowrap;\">Report ID</th>"
        ),
        (
            "      <th data-sort-col=\"1\" "
            "style=\"overflow: hidden; text-overflow: ellipsis; white-space: nowrap;\">"
            "Description</th>"
        ),
        (
            "      <th data-sort-col=\"2\" "
            "style=\"white-space: nowrap;\">Report Type</th>"
        ),
        (
            "      <th data-sort-col=\"3\" "
            "style=\"white-space: nowrap;\">Date Reported</th>"
        ),
        "    </tr>",
        "  </thead>",
        "  <tbody>",
    ]

    for report_id, description, report_type, reported_date in rows:
        lines.append(
            "    <tr>"
            f"<td><a href=\"/database/{report_id}\">{report_id}</a></td>"
            f"<td style=\"overflow: hidden; text-overflow: ellipsis; white-space: nowrap;\">{description}</td>"
            f"<td>{report_type}</td>"
            f"<td>{reported_date}</td>"
            "</tr>"
        )

    lines.extend(
        [
            "  </tbody>",
            "</table>",
            (
                f"<div class=\"avid-report-pager\" id=\"{pager_id}\" "
                "style=\"display: flex; justify-content: flex-end; align-items: center; "
                "gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;\"></div>"
            ),
            "",
            "<script>",
            "if (!window.__avidReportTableInit) {",
            "  window.__avidReportTableInit = function (tableId) {",
            "    var table = document.getElementById(tableId);",
            "    if (!table) return;",
            "    var tbody = table.querySelector('tbody');",
            "    if (!tbody) return;",
            "    var pageSizeSelect = document.getElementById(tableId + '-page-size');",
            "    var pager = document.getElementById(tableId + '-pager');",
            "    if (!pageSizeSelect || !pager) return;",
            "",
            "    var state = {",
            "      page: 1,",
            "      pageSize: Number(pageSizeSelect.value) || 20,",
            "    };",
            "",
            "    function getRows() {",
            "      return Array.from(tbody.querySelectorAll('tr'));",
            "    }",
            "",
            "    function renderPager(totalPages) {",
            "      pager.innerHTML = '';",
            "",
            "      function appendButton(label, pageNo, disabled) {",
            "        var button = document.createElement('button');",
            "        button.type = 'button';",
            "        button.textContent = label;",
            "        button.style.width = 'auto';",
            "        button.style.minWidth = '2.25rem';",
            "        button.style.display = 'inline-block';",
            "        button.disabled = !!disabled;",
            "        if (!button.disabled) {",
            "          button.addEventListener('click', function () {",
            "            state.page = pageNo;",
            "            render();",
            "          });",
            "        }",
            "        pager.appendChild(button);",
            "      }",
            "",
            "      function appendEllipsis() {",
            "        var span = document.createElement('span');",
            "        span.textContent = '...';",
            "        span.className = 'avid-pager-ellipsis';",
            "        pager.appendChild(span);",
            "      }",
            "",
            "      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);",
            "",
            "      if (totalPages <= 3) {",
            "        for (var i = 1; i <= totalPages; i += 1) {",
            "          appendButton(String(i), i, i === state.page);",
            "        }",
            "      } else {",
            "        appendButton('1', 1, state.page === 1);",
            "        appendButton('2', 2, state.page === 2);",
            "        appendEllipsis();",
            "        appendButton(String(totalPages), totalPages, state.page === totalPages);",
            "      }",
            "",
            "      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);",
            "    }",
            "",
            "    function syncSortIndicators() {",
            "      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {",
            "        var arrow = th.querySelector('.avid-sort-arrow');",
            "        if (!arrow) {",
            "          arrow = document.createElement('span');",
            "          arrow.className = 'avid-sort-arrow';",
            "          arrow.style.marginLeft = '0.35rem';",
            "          th.appendChild(arrow);",
            "        }",
            "        var dir = th.getAttribute('data-sort-dir');",
            "        if (dir === 'asc') {",
            "          arrow.textContent = '↑';",
            "        } else if (dir === 'desc') {",
            "          arrow.textContent = '↓';",
            "        } else {",
            "          arrow.textContent = '↕';",
            "        }",
            "      });",
            "    }",
            "",
            "    function render() {",
            "      var rows = getRows();",
            "      var totalRows = rows.length;",
            "      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));",
            "      if (state.page > totalPages) state.page = totalPages;",
            "      if (state.page < 1) state.page = 1;",
            "",
            "      var start = (state.page - 1) * state.pageSize;",
            "      var end = start + state.pageSize;",
            "      rows.forEach(function (row, idx) {",
            "        row.style.display = idx >= start && idx < end ? '' : 'none';",
            "      });",
            "",
            "      renderPager(totalPages);",
            "    }",
            "",
            "    if (!table.dataset.avidSortBound) {",
            "      table.dataset.avidSortBound = 'true';",
            "      table.addEventListener('click', function (event) {",
            "        var th = event.target.closest('th[data-sort-col]');",
            "        if (!th || !table.contains(th)) return;",
            "",
            "        var col = Number(th.getAttribute('data-sort-col'));",
            "        var current = th.getAttribute('data-sort-dir') || '';",
            "        var next = current === 'asc' ? 'desc' : 'asc';",
            "",
            "        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {",
            "          h.removeAttribute('data-sort-dir');",
            "        });",
            "        th.setAttribute('data-sort-dir', next);",
            "        syncSortIndicators();",
            "",
            "        var rows = getRows();",
            "        rows.sort(function (a, b) {",
            "          var av = (a.children[col] && a.children[col].innerText || '').trim();",
            "          var bv = (b.children[col] && b.children[col].innerText || '').trim();",
            "          var ad = Date.parse(av);",
            "          var bd = Date.parse(bv);",
            "          var cmp;",
            "          if (!Number.isNaN(ad) && !Number.isNaN(bd)) {",
            "            cmp = ad - bd;",
            "          } else {",
            "            cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });",
            "          }",
            "          return next === 'asc' ? cmp : -cmp;",
            "        });",
            "        rows.forEach(function (row) { tbody.appendChild(row); });",
            "        state.page = 1;",
            "        render();",
            "      });",
            "    }",
            "",
            "    if (!pageSizeSelect.dataset.avidPageSizeBound) {",
            "      pageSizeSelect.dataset.avidPageSizeBound = 'true';",
            "      pageSizeSelect.addEventListener('change', function () {",
            "        state.pageSize = Number(pageSizeSelect.value) || 20;",
            "        state.page = 1;",
            "        render();",
            "      });",
            "    }",
            "",
            "    syncSortIndicators();",
            "    render();",
            "  };",
            "}",
            f"window.__avidReportTableInit('{table_id}');",
            "</script>",
            f"<!-- reports-year:{year}:end -->",
        ]
    )

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

    report_paths = sorted(
        path
        for path in reports_dir.glob("AVID-*.md")
        if path.is_file()
    )
    if not report_paths:
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
        rf"(?ms)(?:^<!--\s*reports-year:{re.escape(year)}:start\s*-->\n"
        rf".*?^<!--\s*reports-year:{re.escape(year)}:end\s*-->\n?)"
        rf"|(?:^####\s+{re.escape(year)}\n.*?(?=^####\s+\d{{4}}\n|\Z))"
    )

    replacement = _build_reports_year_table(year, report_paths) + "\n\n"

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


def _sync_reports_index_for_all_years(website_root: Path):
    reports_root = (
        website_root / "exampleSite" / "content" / "database" / "reports"
    )
    if not reports_root.exists() or not reports_root.is_dir():
        return

    years = sorted(
        [
            path.name
            for path in reports_root.iterdir()
            if path.is_dir() and path.name.isdigit()
        ],
        reverse=True,
    )

    for year in years:
        _sync_reports_index_for_year(website_root, year)


def _sync_vulnerabilities_index_for_year(website_root: Path, year: str):
    if not year.isdigit() or len(year) != 4:
        return

    vulns_dir = (
        website_root
        / "exampleSite"
        / "content"
        / "database"
        / "vulnerabilities"
        / year
    )
    if not vulns_dir.exists() or not vulns_dir.is_dir():
        return

    vuln_paths = sorted(
        path for path in vulns_dir.glob("AVID-*.md") if path.is_file()
    )
    if not vuln_paths:
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
        rf"(?ms)(?:^<!--\s*vulnerabilities-year:{re.escape(year)}:start\s*-->\n"
        rf".*?^<!--\s*vulnerabilities-year:{re.escape(year)}:end\s*-->\n?)"
        rf"|(?:^#####\s+{re.escape(year)}\n.*?(?=^#####\s+\d{{4}}\n|^##\s+Reports\n|\Z))"
    )

    replacement = _build_vulnerabilities_year_table(year, vuln_paths) + "\n\n"

    if section_pattern.search(content):
        updated = section_pattern.sub(replacement, content, count=1)
    else:
        vulns_marker = "### List of Vulnerabilities"
        marker_pos = content.find(vulns_marker)
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
        print(f"Updated vulnerability links in {index_path} for year {year}")


def _sync_vulnerabilities_index_for_all_years(website_root: Path):
    vulns_root = (
        website_root / "exampleSite" / "content" / "database" / "vulnerabilities"
    )
    if not vulns_root.exists() or not vulns_root.is_dir():
        return

    years = sorted(
        [
            path.name
            for path in vulns_root.iterdir()
            if path.is_dir() and path.name.isdigit()
        ],
        reverse=True,
    )

    for year in years:
        _sync_vulnerabilities_index_for_year(website_root, year)


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

        _sync_reports_index_for_all_years(website_root)
        _sync_vulnerabilities_index_for_all_years(website_root)
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

    _sync_reports_index_for_all_years(website_root)
    _sync_vulnerabilities_index_for_all_years(website_root)


if __name__ == "__main__":
    main()
