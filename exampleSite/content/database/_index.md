---
title: Database
layout: page
image: "/uploads/avid.png"
url: /database
---

AVID is a database of failure modes in general-purpose AI (GPAI) systems, including LLMs, API-only AI systems, developer tooling, and end-to-end applications and agents. The two base data classes are **Report** and **Vulnerability**. A *report* captures one concrete occurrence with supporting evidence; a *vulnerability* (vuln) captures a recurring failure mode.

Records in this database can be mapped to multiple taxonomy and risk frameworks, including the AVID taxonomy, CVSS risk scores, and MITRE ATLAS. This page lists the current reports and vulns in our database. To learn more about the database and usage, refer to our [documentation](https://avidml.gitbook.io/).

> **Note:** Older AVID records (before 2025) were curated under a broader AI/ML scope; these should be interpreted as legacy entries relative to the current GPAI-focused scope.
>
> The definition of an "AI vulnerability" is still evolving across the ecosystem, so AVID currently uses a working definition. In this release, we are prioritizing report-level evidence and have not yet published new vulnerability records.

## Reports
Reports are occurrences of a GPAI failure mode. We classify reports in four types, in increasing degree of quantitative evidence:

1. <span class="report-badge badge-issue">Issue</span>: qualitative evaluation based on a single sample or handful of samples,
2. <span class="report-badge badge-advisory">Advisory</span>: qualitative evaluation based on multiple Incidents,
3. <span class="report-badge badge-measurement">Measurement</span>: quantitative evaluation with associated data and metric,
4. <span class="report-badge badge-detection">Detection</span>: A Measurement deemed critical by a threshold or statistical test.

### List of Reports

<!-- reports-year:2026:start -->
#### 2026

<div class="avid-report-controls" style="display: flex; justify-content: flex-start; margin: 0.5rem 0;">
  <label style="display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;">
    Rows per page:
    <select id="reports-2026-page-size" style="display: inline-block; width: auto; min-width: 4.5rem;"><option value="10">10</option><option value="20" selected>20</option><option value="50">50</option></select>
  </label>
</div>
<table class="avid-report-table" id="reports-2026" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 18%;">
    <col style="width: 52%;">
    <col style="width: 15%;">
    <col style="width: 15%;">
  </colgroup>
  <thead>
    <tr>
      <th data-sort-col="0" data-sort-dir="desc" style="white-space: nowrap;">Report ID</th>
      <th data-sort-col="1" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Description</th>
      <th data-sort-col="2" style="white-space: nowrap;">Report Type</th>
      <th data-sort-col="3" style="white-space: nowrap;">Date Reported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><a href="/database/AVID-2026-R0001">AVID-2026-R0001</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0132</td><td>Advisory</td><td>2024-09-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0002">AVID-2026-R0002</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incorrect Authorization in mintplex-labs/anything-llm (CVE-2024-10109)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0003">AVID-2026-R0003</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Privilege Management in lunary-ai/lunary (CVE-2024-10273)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0004">AVID-2026-R0004</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Authorization in lunary-ai/lunary (CVE-2024-10274)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0005">AVID-2026-R0005</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Access Control in lunary-ai/lunary (CVE-2024-10330)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0006">AVID-2026-R0006</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in mintplex-labs/anything-llm (CVE-2024-10513)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0007">AVID-2026-R0007</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing Authorization in lunary-ai/lunary (CVE-2024-10762)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0008">AVID-2026-R0008</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service (DoS) in invoke-ai/invokeai (CVE-2024-10821)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0009">AVID-2026-R0009</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service (DoS) via Multipart Boundary in eosphoros-ai/db-gpt (CVE-2024-10829)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0010">AVID-2026-R0010</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in eosphoros-ai/db-gpt (CVE-2024-10830)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0011">AVID-2026-R0011</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write through Absolute Path Traversal in eosphoros-ai/db-gpt (CVE-2024-10831)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0012">AVID-2026-R0012</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write in eosphoros-ai/db-gpt (CVE-2024-10833)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0013">AVID-2026-R0013</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write in eosphoros-ai/db-gpt (CVE-2024-10834)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0014">AVID-2026-R0014</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write via SQL Injection in eosphoros-ai/db-gpt (CVE-2024-10835)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0015">AVID-2026-R0015</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cross-Site Request Forgery (CSRF) in eosphoros-ai/db-gpt (CVE-2024-10906)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0016">AVID-2026-R0016</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Exposure of Sensitive System Information via ImagePromptTemplate in langchain-ai/langchain (CVE-2024-10940)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0017">AVID-2026-R0017</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Code Injection in binary-husky/gpt_academic (CVE-2024-10950)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0018">AVID-2026-R0018</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Prompt Injection Leading to RCE in binary-husky/gpt_academic Plugin `manim` (CVE-2024-10954)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0019">AVID-2026-R0019</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Delete in invoke-ai/invokeai (CVE-2024-11042)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0020">AVID-2026-R0020</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service (DoS) via Large Payload in Board Name Field in invoke-ai/invokeai (CVE-2024-11043)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0021">AVID-2026-R0021</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Access Control in lunary-ai/lunary (CVE-2024-11300)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0022">AVID-2026-R0022</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Enforcement of Unique Constraint in lunary-ai/lunary (CVE-2024-11301)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0023">AVID-2026-R0023</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution via Model Deserialization in invoke-ai/invokeai (CVE-2024-12029)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0024">AVID-2026-R0024</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AI Scribe – SEO AI Writer, Content Generator, Humanizer, Blog Writer, SEO Optimizer, DALLE-3, AI WordPress Plugin ChatGPT (GPT-4o 128K) <= 2.3 - Missing Authorization to Authenticated (Subscriber+) Settings Update (CVE-2024-12606)</td><td>Advisory</td><td>2025-01-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0025">AVID-2026-R0025</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service (DoS) in run-llama/llama_index (CVE-2024-12704)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0026">AVID-2026-R0026</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF in infiniflow/ragflow (CVE-2024-12779)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0027">AVID-2026-R0027</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SQL Injection to RCE in run-llama/llama_index (CVE-2024-12909)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0028">AVID-2026-R0028</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SQL Injection in run-llama/llama_index (CVE-2024-12911)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0029">AVID-2026-R0029</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM watsonx.ai cross-site scripting (CVE-2024-49785)</td><td>Advisory</td><td>2025-01-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0030">AVID-2026-R0030</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Uncontrolled Resource Consumption in mlflow/mlflow (CVE-2024-6838)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0031">AVID-2026-R0031</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Exposure of Sensitive Information in mintplex-labs/anything-llm (CVE-2024-6842)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0032">AVID-2026-R0032</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Access Control in lunary-ai/lunary (CVE-2024-8999)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0033">AVID-2026-R0033</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Authorization and Duplicate Slug Vulnerability in lunary-ai/lunary (CVE-2024-9000)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0034">AVID-2026-R0034</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary Code Execution via Crafted Keras Config for Model Loading (CVE-2025-1550)</td><td>Advisory</td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0035">AVID-2026-R0035</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">picklescan - Security scanning bypass via 'pip main' (CVE-2025-1716)</td><td>Advisory</td><td>2025-02-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0036">AVID-2026-R0036</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">picklescan - Security scanning bypass via non-standard file extensions (CVE-2025-1889)</td><td>Advisory</td><td>2025-03-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0037">AVID-2026-R0037</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">picklescan ZIP archive manipulation attack leads to crash (CVE-2025-1944)</td><td>Advisory</td><td>2025-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0038">AVID-2026-R0038</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">picklescan - Zip Flag Bit Exploit Crashes Picklescan But Not PyTorch (CVE-2025-1945)</td><td>Advisory</td><td>2025-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0039">AVID-2026-R0039</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mage AI insecure default initialization of resource (CVE-2025-2129)</td><td>Advisory</td><td>2025-03-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R0040">AVID-2026-R0040</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Microsoft Account Elevation of Privilege Vulnerability (CVE-2025-21396)</td><td>Advisory</td><td>2025-01-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R0041">AVID-2026-R0041</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure AI Face Service Elevation of Privilege Vulnerability (CVE-2025-21415)</td><td>Advisory</td><td>2025-01-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R0042">AVID-2026-R0042</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-23359</td><td>Advisory</td><td>2025-02-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0043">AVID-2026-R0043</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NI Vision Builder AI VBAI File Processing Missing Warning Remote Code Execution Vulnerability (CVE-2025-2450)</td><td>Advisory</td><td>2025-03-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R0044">AVID-2026-R0044</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure Promptflow Remote Code Execution Vulnerability (CVE-2025-24986)</td><td>Advisory</td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0045">AVID-2026-R0045</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">BentoML Allows Remote Code Execution (RCE) via Insecure Deserialization (CVE-2025-27520)</td><td>Advisory</td><td>2025-04-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0046">AVID-2026-R0046</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Control of Generation of Code ('Code Injection') in GitLab (CVE-2025-2867)</td><td>Advisory</td><td>2025-03-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0047">AVID-2026-R0047</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch torch.nn.utils.rnn.pad_packed_sequence memory corruption (CVE-2025-2998)</td><td>Advisory</td><td>2025-03-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R0048">AVID-2026-R0048</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch torch.nn.utils.rnn.unpack_sequence memory corruption (CVE-2025-2999)</td><td>Advisory</td><td>2025-03-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R0049">AVID-2026-R0049</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch torch.jit.script memory corruption (CVE-2025-3000)</td><td>Advisory</td><td>2025-03-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R0050">AVID-2026-R0050</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch torch.lstm_cell memory corruption (CVE-2025-3001)</td><td>Advisory</td><td>2025-03-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R0051">AVID-2026-R0051</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-3035</td><td>Advisory</td><td>2025-04-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R0052">AVID-2026-R0052</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch torch.jit.jit_module_from_flatbuffer memory corruption (CVE-2025-3121)</td><td>Advisory</td><td>2025-04-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R0053">AVID-2026-R0053</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch CUDACachingAllocator.cpp torch.cuda.memory.caching_allocator_delete memory corruption (CVE-2025-3136)</td><td>Advisory</td><td>2025-04-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0054">AVID-2026-R0054</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ageerle ruoyi-ai API Interface SysModelController.java improper authorization (CVE-2025-3199)</td><td>Advisory</td><td>2025-04-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0055">AVID-2026-R0055</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary file write from Cursor Agent through a prompt injection from malicious @Docs (CVE-2025-32018)</td><td>Advisory</td><td>2025-04-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R0056">AVID-2026-R0056</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ageerle ruoyi-ai SysNoticeController.java improper authorization (CVE-2025-3202)</td><td>Advisory</td><td>2025-04-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0057">AVID-2026-R0057</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insecure Deserialization leads to RCE in BentoML's runner server (CVE-2025-32375)</td><td>Advisory</td><td>2025-04-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R0058">AVID-2026-R0058</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Langflow < 1.3.0 Unauthenticated RCE via /api/v1/validate/code (CVE-2025-3248)</td><td>Advisory</td><td>2025-04-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R0059">AVID-2026-R0059</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Urgent Health Inquiry"</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0060">AVID-2026-R0060</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Hex Recipe Book" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0061">AVID-2026-R0061</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Incremental Table Completion" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0062">AVID-2026-R0062</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Prompt Injection via "Correction" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0063">AVID-2026-R0063</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Chemical Compiler Debug" Tactic</td><td>Measurement</td><td>2026-02-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0064">AVID-2026-R0064</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Split Mode" Response Requests</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0065">AVID-2026-R0065</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Placeholder Injection" Tactic</td><td>Measurement</td><td>2026-01-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R0066">AVID-2026-R0066</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Deceptive Forensic Context" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0067">AVID-2026-R0067</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Technical Field Guide" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0068">AVID-2026-R0068</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Hybrid Role" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0069">AVID-2026-R0069</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "API System Instructions" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0070">AVID-2026-R0070</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Haiku of Love" Tactic</td><td>Measurement</td><td>2026-01-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0071">AVID-2026-R0071</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Choose Your Own Adventure" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0072">AVID-2026-R0072</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Chemist Code Language" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0073">AVID-2026-R0073</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Fashion Design Recipe" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0074">AVID-2026-R0074</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Science Student Safety" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0075">AVID-2026-R0075</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Show Character Role-Playing" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0076">AVID-2026-R0076</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Story Teller" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0077">AVID-2026-R0077</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Screenplay Deception" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0078">AVID-2026-R0078</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Police Interrogation Terminal" Tactic</td><td>Measurement</td><td>2026-01-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R0079">AVID-2026-R0079</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Compare and Contrast" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0080">AVID-2026-R0080</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Essay Title" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0081">AVID-2026-R0081</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Key-Value Pairs" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0082">AVID-2026-R0082</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via Token Disruption through Random Spacing</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0083">AVID-2026-R0083</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Abbreviation Expansion"</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0084">AVID-2026-R0084</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "First Person Perspective"</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0085">AVID-2026-R0085</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Psych-Phil DT + Compaction" Technique</td><td>Measurement</td><td>2025-10-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R0086">AVID-2026-R0086</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Super Short Prompt"</td><td>Measurement</td><td>2025-10-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0087">AVID-2026-R0087</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via Investigative Journalist Persona</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0088">AVID-2026-R0088</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Speculative Knowledge Preservation" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0089">AVID-2026-R0089</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI DALL-E3 Guardrail Jailbreak via "Classical Art Reframing" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0090">AVID-2026-R0090</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via Memory Dump Simulation Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0091">AVID-2026-R0091</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI Sora Guardrail Jailbreak via "Anatomical Escalation" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0092">AVID-2026-R0092</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Mathematical Variable Obfuscation" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0093">AVID-2026-R0093</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Scientific Framing for Wrapper" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0094">AVID-2026-R0094</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Terminal Simulation" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0095">AVID-2026-R0095</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Servile Scientist" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0096">AVID-2026-R0096</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI DALL-E3 Guardrail Jailbreak via "Debug Framework Simulation" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0097">AVID-2026-R0097</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI Sora Guardrail Jailbreak via "Hypothetical Anatomy" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0098">AVID-2026-R0098</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI DALL-E3 Guardrail Jailbreak via "Historical NSFW" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0099">AVID-2026-R0099</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI GPT-4o Guardrail Jailbreak via "Layered Summarization" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0100">AVID-2026-R0100</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI DALL-E3 Guardrail Jailbreak via "Feminist Art Description" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0101">AVID-2026-R0101</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI DALL-E3 Guardrail Jailbreak via "Artistic Escalation" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0102">AVID-2026-R0102</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Academic Framing" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0103">AVID-2026-R0103</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Wiki Creation" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0104">AVID-2026-R0104</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI GPT-4o Guardrail Jailbreak via "Zero-Width Unicode" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0105">AVID-2026-R0105</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI DALL-E3  Guardrail Jailbreak via "Historical Polaroid" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0106">AVID-2026-R0106</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Fictional API Detection" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0107">AVID-2026-R0107</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NSFWOpenAI DALL-E3 Guardrail Jailbreak via "Surprise Attack" Tactic</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0108">AVID-2026-R0108</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Spelling Mistakes" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0109">AVID-2026-R0109</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Lambda Pattern Formatting" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0110">AVID-2026-R0110</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Apocalyptic Scenario" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0111">AVID-2026-R0111</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Scientific Formula" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0112">AVID-2026-R0112</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI GPT-4o Guardrail Jailbreak via "Naval Parameters Cipher" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0113">AVID-2026-R0113</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via IPA Encoding Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0114">AVID-2026-R0114</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Chaotic Formatting" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0115">AVID-2026-R0115</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Leetspeak Unicode" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0116">AVID-2026-R0116</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Correct Me" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0117">AVID-2026-R0117</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Pronunciation Bypass" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0118">AVID-2026-R0118</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Chemist's Essay" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0119">AVID-2026-R0119</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Analyze Data" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0120">AVID-2026-R0120</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI Multiple Model Prompt Injection via "Morse Code Businessman" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0121">AVID-2026-R0121</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Arbitrary Relation" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0122">AVID-2026-R0122</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple Model Guardrail Jailbreak via "Fortune Cookie Simulator" Tactic</td><td>Measurement</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0123">AVID-2026-R0123</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Gemini G-Suite Prompt Injection Vulnerability</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0124">AVID-2026-R0124</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Amazon Rufus Guardrail Jailbreak via ASCII Decimal Encoding</td><td>Issue</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0125">AVID-2026-R0125</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiEscaped`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0126">AVID-2026-R0126</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiRaw`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0127">AVID-2026-R0127</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.CompleteKey`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0128">AVID-2026-R0128</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.GetKey`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0129">AVID-2026-R0129</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `atkgen.Tox`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0130">AVID-2026-R0130</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `continuation.ContinueSlursReclaimedSlurs`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0131">AVID-2026-R0131</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.Ablation_Dan_11_0`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0132">AVID-2026-R0132</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.AutoDANCached`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0133">AVID-2026-R0133</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.DanInTheWild`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0134">AVID-2026-R0134</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.Repeat`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0135">AVID-2026-R0135</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.RepeatedToken`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0136">AVID-2026-R0136</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dra.DRA`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0137">AVID-2026-R0137</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAscii85`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0138">AVID-2026-R0138</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAtbash`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0139">AVID-2026-R0139</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase16`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0140">AVID-2026-R0140</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase2048`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0141">AVID-2026-R0141</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase32`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0142">AVID-2026-R0142</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase64`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0143">AVID-2026-R0143</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBraille`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0144">AVID-2026-R0144</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectEcoji`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0145">AVID-2026-R0145</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectHex`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0146">AVID-2026-R0146</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectMorse`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0147">AVID-2026-R0147</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectNato`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0148">AVID-2026-R0148</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectROT13`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0149">AVID-2026-R0149</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUU`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0150">AVID-2026-R0150</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUnicodeTagChars`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0151">AVID-2026-R0151</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectZalgo`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0152">AVID-2026-R0152</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.JinjaTemplatePythonInjection`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0153">AVID-2026-R0153</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.SQLInjectionEcho`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0154">AVID-2026-R0154</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.Tag`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0155">AVID-2026-R0155</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.ThreatenJSON`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0156">AVID-2026-R0156</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.WhoIsRiley`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0157">AVID-2026-R0157</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Slurs`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0158">AVID-2026-R0158</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Substances`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0159">AVID-2026-R0159</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win10`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0160">AVID-2026-R0160</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win11`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0161">AVID-2026-R0161</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetEiffel`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0162">AVID-2026-R0162</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetLegal`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0163">AVID-2026-R0163</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionReport`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0164">AVID-2026-R0164</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionResume`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0165">AVID-2026-R0165</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnFr`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0166">AVID-2026-R0166</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnZh`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0167">AVID-2026-R0167</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentJailbreak`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0168">AVID-2026-R0168</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhois`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0169">AVID-2026-R0169</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhoisSnippet`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0170">AVID-2026-R0170</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianCloze`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0171">AVID-2026-R0171</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianComplete`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0172">AVID-2026-R0172</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureCloze`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0173">AVID-2026-R0173</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureComplete`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0174">AVID-2026-R0174</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTCloze`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0175">AVID-2026-R0175</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTComplete`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0176">AVID-2026-R0176</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterCloze`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0177">AVID-2026-R0177</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterComplete`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0178">AVID-2026-R0178</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Bullying`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0179">AVID-2026-R0179</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Deadnaming`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0180">AVID-2026-R0180</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.QuackMedicine`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0181">AVID-2026-R0181</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SexualContent`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0182">AVID-2026-R0182</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Sexualisation`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0183">AVID-2026-R0183</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SlurUsage`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0184">AVID-2026-R0184</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Evasion`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0185">AVID-2026-R0185</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Payload`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0186">AVID-2026-R0186</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.SubFunctions`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0187">AVID-2026-R0187</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.TopLevel`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0188">AVID-2026-R0188</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `misleading.FalseAssertion`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0189">AVID-2026-R0189</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Dart`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0190">AVID-2026-R0190</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.JavaScript`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0191">AVID-2026-R0191</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Perl`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0192">AVID-2026-R0192</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Python`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0193">AVID-2026-R0193</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.RakuLand`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0194">AVID-2026-R0194</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Ruby`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0195">AVID-2026-R0195</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Rust`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0196">AVID-2026-R0196</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.FutureTense`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0197">AVID-2026-R0197</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.PastTense`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0198">AVID-2026-R0198</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackHateHumans`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0199">AVID-2026-R0199</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackKillHumans`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0200">AVID-2026-R0200</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackLongPrompt`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0202">AVID-2026-R0202</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `snowball.GraphConnectivity`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0203">AVID-2026-R0203</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `suffix.GCGCached`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0204">AVID-2026-R0204</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `tap.TAPCached`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0205">AVID-2026-R0205</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `topic.WordnetControversial`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0206">AVID-2026-R0206</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.ColabAIDataLeakage`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0207">AVID-2026-R0207</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownImageExfil`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0208">AVID-2026-R0208</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURIImageExfilExtended`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0209">AVID-2026-R0209</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURINonImageExfilExtended`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0210">AVID-2026-R0210</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownXSS`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0211">AVID-2026-R0211</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.PlaygroundMarkdownExfil`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0212">AVID-2026-R0212</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.StringAssemblyDataExfil`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0213">AVID-2026-R0213</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Kimi-K2-Instruct-0905 from Moonshot AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.TaskXSS`.</td><td>Measurement</td><td>2026-02-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0214">AVID-2026-R0214</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Authenticated Command Injection in OpenClaw Docker Execution via PATH Environment Variable (CVE-2026-24763)</td><td>Advisory</td><td>2026-02-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R0215">AVID-2026-R0215</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has Remote Code Execution via System Prompt Injection in Slack Channel Descriptions (CVE-2026-24764)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0216">AVID-2026-R0216</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw/Clawdbot has OS Command Injection via Project Root Path in sshNodeCommand (CVE-2026-25157)</td><td>Advisory</td><td>2026-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0217">AVID-2026-R0217</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2026-25253</td><td>Advisory</td><td>2026-02-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R0218">AVID-2026-R0218</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has a Telegram webhook request forgery (missing `channels.telegram.webhookSecret`) → auth bypass (CVE-2026-25474)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0219">AVID-2026-R0219</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw Vulnerable to Local File Inclusion via MEDIA: Path Extraction (CVE-2026-25475)</td><td>Advisory</td><td>2026-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0220">AVID-2026-R0220</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw Affected by Unauthenticated Local RCE via WebSocket config.apply (CVE-2026-25593)</td><td>Advisory</td><td>2026-02-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R0221">AVID-2026-R0221</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has BlueBubbles webhook auth bypass via loopback proxy trust (CVE-2026-26316)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0222">AVID-2026-R0222</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw affected by cross-site request forgery (CSRF) through loopback browser mutation endpoints (CVE-2026-26317)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0223">AVID-2026-R0223</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has Missing Webhook Authentication in Telnyx Provider Allowing Unauthenticated Requests (CVE-2026-26319)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0224">AVID-2026-R0224</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw macOS deep link confirmation truncation can conceal executed agent message (CVE-2026-26320)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0225">AVID-2026-R0225</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has a local file disclosure via sendMediaFeishu in Feishu extension (CVE-2026-26321)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0226">AVID-2026-R0226</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw Gateway tool allowed unrestricted gatewayUrl override (CVE-2026-26322)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0227">AVID-2026-R0227</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has a command injection in maintainer clawtributors updater (CVE-2026-26323)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0228">AVID-2026-R0228</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has a SSRF guard bypass via full-form IPv4-mapped IPv6 (loopback / metadata reachable) (CVE-2026-26324)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0229">AVID-2026-R0229</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw Node host system.run rawCommand/command mismatch can bypass allowlist/approvals (CVE-2026-26325)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0230">AVID-2026-R0230</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw skills.status could leak secrets to operator.read clients (CVE-2026-26326)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0231">AVID-2026-R0231</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw allows unauthenticated discovery TXT records to steer routing and TLS pinning (CVE-2026-26327)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0232">AVID-2026-R0232</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw iMessage group allowlist authorization inherited DM pairing-store identities (CVE-2026-26328)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0233">AVID-2026-R0233</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has a path traversal in browser upload allows local file read (CVE-2026-26329)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0234">AVID-2026-R0234</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw has a Path Traversal in Browser Download Functionality (CVE-2026-26972)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0235">AVID-2026-R0235</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw: Unsanitized CWD path injection into LLM prompts (CVE-2026-27001)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0236">AVID-2026-R0236</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw: Docker container escape via unvalidated bind mount config injection (CVE-2026-27002)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0237">AVID-2026-R0237</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw: Telegram bot token exposure via logs (CVE-2026-27003)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0238">AVID-2026-R0238</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw session tool visibility hardening and Telegram webhook secret fallback (CVE-2026-27004)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0239">AVID-2026-R0239</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw's sandbox config hash sorted primitive arrays and suppressed needed container recreation (CVE-2026-27007)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0240">AVID-2026-R0240</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw hardened the skill download target directory validation (CVE-2026-27008)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0241">AVID-2026-R0241</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw affected by Stored XSS in Control UI via unsanitized assistant name/avatar in inline script injection (CVE-2026-27009)</td><td>Advisory</td><td>2026-02-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0242">AVID-2026-R0242</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw Discord moderation authorization used untrusted sender identity in tool-driven flows (CVE-2026-27484)</td><td>Advisory</td><td>2026-02-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0243">AVID-2026-R0243</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw affected by Stored XSS in Control UI via unsanitized assistant name/avatar in inline script injection (CVE-2026-27485)</td><td>Advisory</td><td>2026-02-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0244">AVID-2026-R0244</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw: Process Safety - Unvalidated PID Kill via SIGKILL in Process Cleanup (CVE-2026-27486)</td><td>Advisory</td><td>2026-02-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0245">AVID-2026-R0245</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw: Prevent shell injection in macOS keychain credential write (CVE-2026-27487)</td><td>Advisory</td><td>2026-02-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0246">AVID-2026-R0246</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw hardened cron webhook delivery against SSRF (CVE-2026-27488)</td><td>Advisory</td><td>2026-02-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0247">AVID-2026-R0247</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenClaw: ACP prompt-size checks missing in local stdio bridge could reduce responsiveness with very large inputs (CVE-2026-27576)</td><td>Advisory</td><td>2026-02-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0248">AVID-2026-R0248</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Misconfigured database exposes sensitive API keys</td><td>Advisory</td><td>2026-03-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0249">AVID-2026-R0249</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Exposed ClickHouse database leaking sensitive information</td><td>Issue</td><td>2026-03-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0250">AVID-2026-R0250</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Critical authentication bypass vulnerability in Base44</td><td>Advisory</td><td>2026-03-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0251">AVID-2026-R0251</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Data exfiltration via prompt injection</td><td>Issue</td><td>2026-03-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0253">AVID-2026-R0253</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Dia: Increased Spoof Risk; Missing full screen toast (CVE-2025-13132)</td><td>Advisory</td><td>2025-11-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0254">AVID-2026-R0254</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.PastTense`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0255">AVID-2026-R0255</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackHateHumans`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0256">AVID-2026-R0256</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackKillHumans`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0257">AVID-2026-R0257</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBraille`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0258">AVID-2026-R0258</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectEcoji`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0259">AVID-2026-R0259</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectHex`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0260">AVID-2026-R0260</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectMorse`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0261">AVID-2026-R0261</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectNato`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0262">AVID-2026-R0262</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectROT13`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0263">AVID-2026-R0263</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUU`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0264">AVID-2026-R0264</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUnicodeTagChars`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0265">AVID-2026-R0265</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectZalgo`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0266">AVID-2026-R0266</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.JinjaTemplatePythonInjection`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0267">AVID-2026-R0267</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.SQLInjectionEcho`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0268">AVID-2026-R0268</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.Tag`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0269">AVID-2026-R0269</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.ThreatenJSON`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0270">AVID-2026-R0270</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.WhoIsRiley`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0271">AVID-2026-R0271</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Slurs`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0272">AVID-2026-R0272</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Substances`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0273">AVID-2026-R0273</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win10`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0274">AVID-2026-R0274</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win11`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0275">AVID-2026-R0275</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetEiffel`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0276">AVID-2026-R0276</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetLegal`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0277">AVID-2026-R0277</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionReport`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0278">AVID-2026-R0278</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionResume`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0279">AVID-2026-R0279</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnFr`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0280">AVID-2026-R0280</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnZh`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0281">AVID-2026-R0281</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentJailbreak`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0282">AVID-2026-R0282</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase32`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0283">AVID-2026-R0283</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase64`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0284">AVID-2026-R0284</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiEscaped`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0285">AVID-2026-R0285</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiRaw`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0286">AVID-2026-R0286</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.CompleteKey`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0287">AVID-2026-R0287</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.GetKey`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0288">AVID-2026-R0288</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `atkgen.Tox`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0289">AVID-2026-R0289</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `continuation.ContinueSlursReclaimedSlurs`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0290">AVID-2026-R0290</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.Ablation_Dan_11_0`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0291">AVID-2026-R0291</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.AutoDANCached`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0292">AVID-2026-R0292</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.DanInTheWild`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0293">AVID-2026-R0293</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.Repeat`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0294">AVID-2026-R0294</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.RepeatedToken`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0295">AVID-2026-R0295</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `dra.DRA`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0296">AVID-2026-R0296</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAscii85`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0297">AVID-2026-R0297</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAtbash`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0298">AVID-2026-R0298</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase16`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0299">AVID-2026-R0299</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase2048`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0300">AVID-2026-R0300</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase32`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0301">AVID-2026-R0301</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase64`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0302">AVID-2026-R0302</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBraille`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0303">AVID-2026-R0303</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectEcoji`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0304">AVID-2026-R0304</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectHex`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0305">AVID-2026-R0305</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectMorse`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0306">AVID-2026-R0306</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectNato`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0307">AVID-2026-R0307</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectROT13`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0308">AVID-2026-R0308</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUU`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0309">AVID-2026-R0309</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUnicodeTagChars`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0310">AVID-2026-R0310</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectZalgo`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0311">AVID-2026-R0311</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.JinjaTemplatePythonInjection`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0312">AVID-2026-R0312</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.SQLInjectionEcho`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0313">AVID-2026-R0313</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.Tag`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0314">AVID-2026-R0314</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.ThreatenJSON`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0315">AVID-2026-R0315</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.WhoIsRiley`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0316">AVID-2026-R0316</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Slurs`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0317">AVID-2026-R0317</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Substances`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0318">AVID-2026-R0318</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win10`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0319">AVID-2026-R0319</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win11`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0320">AVID-2026-R0320</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetEiffel`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0321">AVID-2026-R0321</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetLegal`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0322">AVID-2026-R0322</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionReport`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0323">AVID-2026-R0323</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionResume`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0324">AVID-2026-R0324</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnFr`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0325">AVID-2026-R0325</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnZh`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0326">AVID-2026-R0326</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentJailbreak`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0327">AVID-2026-R0327</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhois`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0328">AVID-2026-R0328</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhoisSnippet`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0329">AVID-2026-R0329</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0330">AVID-2026-R0330</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0331">AVID-2026-R0331</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0332">AVID-2026-R0332</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0333">AVID-2026-R0333</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0334">AVID-2026-R0334</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0335">AVID-2026-R0335</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0336">AVID-2026-R0336</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0337">AVID-2026-R0337</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Bullying`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0338">AVID-2026-R0338</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Deadnaming`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0339">AVID-2026-R0339</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.QuackMedicine`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0340">AVID-2026-R0340</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SexualContent`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0341">AVID-2026-R0341</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Sexualisation`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0342">AVID-2026-R0342</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SlurUsage`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0343">AVID-2026-R0343</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Evasion`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0344">AVID-2026-R0344</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Payload`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0345">AVID-2026-R0345</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.SubFunctions`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0346">AVID-2026-R0346</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.TopLevel`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0347">AVID-2026-R0347</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `misleading.FalseAssertion`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0348">AVID-2026-R0348</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Dart`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0349">AVID-2026-R0349</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.JavaScript`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0350">AVID-2026-R0350</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Perl`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0351">AVID-2026-R0351</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Python`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0352">AVID-2026-R0352</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.RakuLand`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0353">AVID-2026-R0353</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Ruby`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0354">AVID-2026-R0354</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Rust`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0355">AVID-2026-R0355</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.FutureTense`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0356">AVID-2026-R0356</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.PastTense`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0357">AVID-2026-R0357</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackHateHumans`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0358">AVID-2026-R0358</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackKillHumans`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0359">AVID-2026-R0359</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackLongPrompt`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0360">AVID-2026-R0360</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `snowball.GraphConnectivity`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0361">AVID-2026-R0361</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `suffix.GCGCached`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0362">AVID-2026-R0362</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `tap.TAPCached`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0363">AVID-2026-R0363</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `topic.WordnetControversial`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0364">AVID-2026-R0364</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.ColabAIDataLeakage`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0365">AVID-2026-R0365</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownImageExfil`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0366">AVID-2026-R0366</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURIImageExfilExtended`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0367">AVID-2026-R0367</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURINonImageExfilExtended`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0368">AVID-2026-R0368</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownXSS`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0369">AVID-2026-R0369</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.PlaygroundMarkdownExfil`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0370">AVID-2026-R0370</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.StringAssemblyDataExfil`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0371">AVID-2026-R0371</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gpt-oss-20b from OpenAI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.TaskXSS`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0372">AVID-2026-R0372</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhoisSnippet`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0373">AVID-2026-R0373</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0374">AVID-2026-R0374</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0375">AVID-2026-R0375</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0376">AVID-2026-R0376</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0377">AVID-2026-R0377</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0378">AVID-2026-R0378</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0379">AVID-2026-R0379</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterCloze`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0380">AVID-2026-R0380</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterComplete`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0381">AVID-2026-R0381</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Bullying`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0382">AVID-2026-R0382</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Deadnaming`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0383">AVID-2026-R0383</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.QuackMedicine`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0384">AVID-2026-R0384</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SexualContent`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0385">AVID-2026-R0385</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Sexualisation`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0386">AVID-2026-R0386</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SlurUsage`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0387">AVID-2026-R0387</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Evasion`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0388">AVID-2026-R0388</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Payload`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0389">AVID-2026-R0389</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.SubFunctions`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0390">AVID-2026-R0390</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.TopLevel`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0391">AVID-2026-R0391</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `misleading.FalseAssertion`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0392">AVID-2026-R0392</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Dart`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0393">AVID-2026-R0393</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.JavaScript`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0394">AVID-2026-R0394</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Perl`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0395">AVID-2026-R0395</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiEscaped`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0396">AVID-2026-R0396</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiRaw`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0397">AVID-2026-R0397</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.CompleteKey`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0398">AVID-2026-R0398</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.GetKey`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0399">AVID-2026-R0399</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `atkgen.Tox`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0400">AVID-2026-R0400</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `continuation.ContinueSlursReclaimedSlurs`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0401">AVID-2026-R0401</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.Ablation_Dan_11_0`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0402">AVID-2026-R0402</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.AutoDANCached`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0403">AVID-2026-R0403</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.DanInTheWild`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0404">AVID-2026-R0404</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.Repeat`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0405">AVID-2026-R0405</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.RepeatedToken`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0406">AVID-2026-R0406</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `dra.DRA`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0407">AVID-2026-R0407</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAscii85`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0408">AVID-2026-R0408</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAtbash`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0409">AVID-2026-R0409</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase16`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0410">AVID-2026-R0410</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase2048`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0411">AVID-2026-R0411</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Rust`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0412">AVID-2026-R0412</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model Mistral-Small-24B-Instruct-2501 from Mistral was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.FutureTense`.</td><td>Measurement</td><td>2026-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0413">AVID-2026-R0413</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI ChatGPT Content Safety Explicit Image Bypass</td><td>Advisory</td><td>2026-01-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R0414">AVID-2026-R0414</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Eclipse Theia IDE MCP Configuration Code Execution</td><td>Advisory</td><td>2025-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R0415">AVID-2026-R0415</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI Codex CLI Notify Field Configuration Remote Code Execution</td><td>Advisory</td><td>2026-01-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0416">AVID-2026-R0416</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI Codex CLI Model Provider Configuration Remote Code Execution</td><td>Advisory</td><td>2026-01-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0417">AVID-2026-R0417</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI Codex CLI MCP Configuration Remote Code Execution</td><td>Advisory</td><td>2026-01-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0418">AVID-2026-R0418</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Amazon Kiro IDE Data Exfiltration via Filename Prompt Injection and Kiro Powers Registry Fetching</td><td>Advisory</td><td>2025-12-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0419">AVID-2026-R0419</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Amazon Kiro IDE Data Exfiltration via Steering File</td><td>Advisory</td><td>2025-12-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R0420">AVID-2026-R0420</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Gemini CLI Tool Discovery Code Execution</td><td>Advisory</td><td>2025-12-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0421">AVID-2026-R0421</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Gemini CLI MCP Configuration Code Execution</td><td>Advisory</td><td>2025-12-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0422">AVID-2026-R0422</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">JetBrains Junie AI Coding Agent guidelines.md Code Execution</td><td>Advisory</td><td>2025-11-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0423">AVID-2026-R0423</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TheLibrarian.io Internal Cloud Environment Access via web_fetch Tool</td><td>Advisory</td><td>2025-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0424">AVID-2026-R0424</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Zed IDE LSP Configuration Code Execution</td><td>Advisory</td><td>2025-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0425">AVID-2026-R0425</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Zed IDE MCP Configuration Code Execution</td><td>Advisory</td><td>2025-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0426">AVID-2026-R0426</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Antigravity IDE Persistent Code Execution</td><td>Advisory</td><td>2025-11-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0427">AVID-2026-R0427</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cline Bot AI Coding Agent Code Execution via Prompt Injection and TOCTOU Script Invocation</td><td>Advisory</td><td>2025-08-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0428">AVID-2026-R0428</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cline Bot AI Coding Agent Code Execution via Prompt Injection and .clinerules Directives</td><td>Advisory</td><td>2025-08-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0429">AVID-2026-R0429</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cline Bot AI Coding Agent Data Exfiltration via Prompt Injection and DNS</td><td>Advisory</td><td>2025-08-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0430">AVID-2026-R0430</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Nvidia NemoGuard Jailbreak Detect Guardrail Evasion</td><td>Advisory</td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0431">AVID-2026-R0431</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Protect AI Jailbreak and Prompt Injection Guardrail Evasion</td><td>Advisory</td><td>2025-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0432">AVID-2026-R0432</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vijil Prompt Injection Guardrail Evasion</td><td>Advisory</td><td>2025-03-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0433">AVID-2026-R0433</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Meta Prompt Guard Guardrail Evasion</td><td>Advisory</td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0434">AVID-2026-R0434</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Microsoft Azure Prompt Shield Guardrail Evasion</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R0435">AVID-2026-R0435</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Microsoft Azure AI Content Safety Guardrail Evasion</td><td>Advisory</td><td>2024-03-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0436">AVID-2026-R0436</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mistral Vibe CLI MCP Configuration Code Execution</td><td>Advisory</td><td>2025-12-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0437">AVID-2026-R0437</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mistral Vibe CLI Shell Expansion Command Execution</td><td>Advisory</td><td>2026-01-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R0438">AVID-2026-R0438</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mistral Vibe CLI Python Tools Code Execution</td><td>Advisory</td><td>2025-12-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0439">AVID-2026-R0439</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackLongPrompt`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0440">AVID-2026-R0440</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `snowball.GraphConnectivity`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0441">AVID-2026-R0441</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `suffix.GCGCached`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0442">AVID-2026-R0442</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `tap.TAPCached`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0443">AVID-2026-R0443</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `topic.WordnetControversial`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0444">AVID-2026-R0444</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.ColabAIDataLeakage`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0445">AVID-2026-R0445</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownImageExfil`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0446">AVID-2026-R0446</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURIImageExfilExtended`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0447">AVID-2026-R0447</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURINonImageExfilExtended`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0448">AVID-2026-R0448</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownXSS`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0449">AVID-2026-R0449</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.PlaygroundMarkdownExfil`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0450">AVID-2026-R0450</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.StringAssemblyDataExfil`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0451">AVID-2026-R0451</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.TaskXSS`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0452">AVID-2026-R0452</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiEscaped`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0453">AVID-2026-R0453</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiRaw`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0454">AVID-2026-R0454</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.CompleteKey`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0455">AVID-2026-R0455</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.GetKey`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0456">AVID-2026-R0456</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `atkgen.Tox`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0457">AVID-2026-R0457</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `continuation.ContinueSlursReclaimedSlurs`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0458">AVID-2026-R0458</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.Ablation_Dan_11_0`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0459">AVID-2026-R0459</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.AutoDANCached`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0460">AVID-2026-R0460</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.DanInTheWild`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0461">AVID-2026-R0461</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.Repeat`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0462">AVID-2026-R0462</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.RepeatedToken`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0463">AVID-2026-R0463</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `dra.DRA`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0464">AVID-2026-R0464</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAscii85`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0465">AVID-2026-R0465</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAtbash`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0466">AVID-2026-R0466</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase16`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0467">AVID-2026-R0467</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase2048`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0468">AVID-2026-R0468</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase32`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0469">AVID-2026-R0469</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase64`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0470">AVID-2026-R0470</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBraille`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0471">AVID-2026-R0471</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectEcoji`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0472">AVID-2026-R0472</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectHex`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0473">AVID-2026-R0473</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectMorse`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0474">AVID-2026-R0474</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectNato`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0475">AVID-2026-R0475</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectROT13`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0476">AVID-2026-R0476</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUU`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0477">AVID-2026-R0477</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUnicodeTagChars`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0478">AVID-2026-R0478</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectZalgo`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0479">AVID-2026-R0479</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.JinjaTemplatePythonInjection`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0480">AVID-2026-R0480</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.SQLInjectionEcho`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0481">AVID-2026-R0481</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.Tag`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0482">AVID-2026-R0482</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.ThreatenJSON`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0483">AVID-2026-R0483</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.WhoIsRiley`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0484">AVID-2026-R0484</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Slurs`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0485">AVID-2026-R0485</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Substances`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0486">AVID-2026-R0486</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win10`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0487">AVID-2026-R0487</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win11`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0488">AVID-2026-R0488</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetEiffel`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0489">AVID-2026-R0489</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetLegal`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0490">AVID-2026-R0490</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionReport`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0491">AVID-2026-R0491</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionResume`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0492">AVID-2026-R0492</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnFr`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0493">AVID-2026-R0493</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnZh`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0494">AVID-2026-R0494</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentJailbreak`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0495">AVID-2026-R0495</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhois`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0496">AVID-2026-R0496</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhoisSnippet`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0497">AVID-2026-R0497</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0498">AVID-2026-R0498</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0499">AVID-2026-R0499</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0500">AVID-2026-R0500</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0501">AVID-2026-R0501</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0502">AVID-2026-R0502</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0503">AVID-2026-R0503</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0504">AVID-2026-R0504</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0505">AVID-2026-R0505</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Bullying`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0506">AVID-2026-R0506</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Deadnaming`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0507">AVID-2026-R0507</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.QuackMedicine`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0508">AVID-2026-R0508</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SexualContent`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0509">AVID-2026-R0509</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Sexualisation`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0510">AVID-2026-R0510</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SlurUsage`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0511">AVID-2026-R0511</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Evasion`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0512">AVID-2026-R0512</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Payload`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0513">AVID-2026-R0513</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.SubFunctions`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0514">AVID-2026-R0514</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.TopLevel`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0515">AVID-2026-R0515</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `misleading.FalseAssertion`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0516">AVID-2026-R0516</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Dart`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0517">AVID-2026-R0517</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.JavaScript`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0518">AVID-2026-R0518</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Perl`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0519">AVID-2026-R0519</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Python`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0520">AVID-2026-R0520</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.RakuLand`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0521">AVID-2026-R0521</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Ruby`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0522">AVID-2026-R0522</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Rust`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0523">AVID-2026-R0523</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.FutureTense`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0524">AVID-2026-R0524</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.PastTense`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0525">AVID-2026-R0525</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackHateHumans`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0526">AVID-2026-R0526</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackKillHumans`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0527">AVID-2026-R0527</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackLongPrompt`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0528">AVID-2026-R0528</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `snowball.GraphConnectivity`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0529">AVID-2026-R0529</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `suffix.GCGCached`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0530">AVID-2026-R0530</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `tap.TAPCached`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0531">AVID-2026-R0531</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `topic.WordnetControversial`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0532">AVID-2026-R0532</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.ColabAIDataLeakage`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0533">AVID-2026-R0533</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownImageExfil`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0534">AVID-2026-R0534</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURIImageExfilExtended`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0535">AVID-2026-R0535</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURINonImageExfilExtended`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0536">AVID-2026-R0536</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownXSS`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0537">AVID-2026-R0537</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.PlaygroundMarkdownExfil`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0538">AVID-2026-R0538</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.StringAssemblyDataExfil`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0539">AVID-2026-R0539</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model gemma-3n-E4B-it from Google was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.TaskXSS`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0540">AVID-2026-R0540</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiEscaped`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0541">AVID-2026-R0541</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiRaw`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0542">AVID-2026-R0542</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.CompleteKey`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0543">AVID-2026-R0543</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.GetKey`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0544">AVID-2026-R0544</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `atkgen.Tox`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0545">AVID-2026-R0545</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `continuation.ContinueSlursReclaimedSlurs`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0546">AVID-2026-R0546</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.Ablation_Dan_11_0`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0547">AVID-2026-R0547</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.AutoDANCached`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0548">AVID-2026-R0548</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.DanInTheWild`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0549">AVID-2026-R0549</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.Repeat`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0550">AVID-2026-R0550</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.RepeatedToken`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0551">AVID-2026-R0551</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dra.DRA`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0552">AVID-2026-R0552</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAscii85`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0553">AVID-2026-R0553</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAtbash`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0554">AVID-2026-R0554</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase16`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0555">AVID-2026-R0555</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase2048`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0556">AVID-2026-R0556</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase32`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0557">AVID-2026-R0557</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase64`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0558">AVID-2026-R0558</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBraille`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0559">AVID-2026-R0559</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectEcoji`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0560">AVID-2026-R0560</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectHex`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0561">AVID-2026-R0561</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectMorse`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0562">AVID-2026-R0562</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectNato`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0563">AVID-2026-R0563</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectROT13`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0564">AVID-2026-R0564</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUU`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0565">AVID-2026-R0565</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUnicodeTagChars`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0566">AVID-2026-R0566</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectZalgo`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0567">AVID-2026-R0567</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.JinjaTemplatePythonInjection`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0568">AVID-2026-R0568</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.SQLInjectionEcho`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0569">AVID-2026-R0569</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.Tag`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0570">AVID-2026-R0570</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.ThreatenJSON`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0571">AVID-2026-R0571</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.WhoIsRiley`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0572">AVID-2026-R0572</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Slurs`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0573">AVID-2026-R0573</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Substances`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0574">AVID-2026-R0574</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win10`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0575">AVID-2026-R0575</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win11`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0576">AVID-2026-R0576</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetEiffel`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0577">AVID-2026-R0577</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetLegal`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0578">AVID-2026-R0578</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionReport`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0579">AVID-2026-R0579</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionResume`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0580">AVID-2026-R0580</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnFr`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0581">AVID-2026-R0581</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnZh`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0582">AVID-2026-R0582</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentJailbreak`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0583">AVID-2026-R0583</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhois`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0584">AVID-2026-R0584</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhoisSnippet`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0585">AVID-2026-R0585</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0586">AVID-2026-R0586</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0587">AVID-2026-R0587</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0588">AVID-2026-R0588</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0589">AVID-2026-R0589</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0590">AVID-2026-R0590</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0591">AVID-2026-R0591</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterCloze`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0592">AVID-2026-R0592</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterComplete`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0593">AVID-2026-R0593</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Bullying`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0594">AVID-2026-R0594</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Deadnaming`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0595">AVID-2026-R0595</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.QuackMedicine`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0596">AVID-2026-R0596</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SexualContent`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0597">AVID-2026-R0597</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Sexualisation`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0598">AVID-2026-R0598</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SlurUsage`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0599">AVID-2026-R0599</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Evasion`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0600">AVID-2026-R0600</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Payload`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0601">AVID-2026-R0601</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.SubFunctions`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0602">AVID-2026-R0602</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.TopLevel`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0603">AVID-2026-R0603</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `misleading.FalseAssertion`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0604">AVID-2026-R0604</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Dart`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0605">AVID-2026-R0605</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.JavaScript`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0606">AVID-2026-R0606</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Perl`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0607">AVID-2026-R0607</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Python`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0608">AVID-2026-R0608</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.RakuLand`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0609">AVID-2026-R0609</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Ruby`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0610">AVID-2026-R0610</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Rust`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0611">AVID-2026-R0611</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.FutureTense`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0612">AVID-2026-R0612</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.PastTense`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0613">AVID-2026-R0613</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackHateHumans`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0614">AVID-2026-R0614</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackKillHumans`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0615">AVID-2026-R0615</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackLongPrompt`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0616">AVID-2026-R0616</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `snowball.GraphConnectivity`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0617">AVID-2026-R0617</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `suffix.GCGCached`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0618">AVID-2026-R0618</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `tap.TAPCached`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0619">AVID-2026-R0619</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `topic.WordnetControversial`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0620">AVID-2026-R0620</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.ColabAIDataLeakage`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0621">AVID-2026-R0621</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownImageExfil`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0622">AVID-2026-R0622</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURIImageExfilExtended`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0623">AVID-2026-R0623</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownURINonImageExfilExtended`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0624">AVID-2026-R0624</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.MarkdownXSS`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0625">AVID-2026-R0625</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.PlaygroundMarkdownExfil`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0626">AVID-2026-R0626</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.StringAssemblyDataExfil`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0627">AVID-2026-R0627</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model LFM2-24B-A2B from Liquid AI was evaluated by the Garak LLM Vulnerability scanner using the probe `web_injection.TaskXSS`.</td><td>Measurement</td><td>2026-03-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0628">AVID-2026-R0628</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Dart`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0629">AVID-2026-R0629</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.JavaScript`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0630">AVID-2026-R0630</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Perl`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0631">AVID-2026-R0631</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Python`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0632">AVID-2026-R0632</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.RakuLand`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0633">AVID-2026-R0633</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Ruby`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0634">AVID-2026-R0634</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `packagehallucination.Rust`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0635">AVID-2026-R0635</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.FutureTense`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0636">AVID-2026-R0636</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `phrasing.PastTense`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0637">AVID-2026-R0637</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackHateHumans`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0638">AVID-2026-R0638</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `promptinject.HijackKillHumans`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0639">AVID-2026-R0639</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiEscaped`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0640">AVID-2026-R0640</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `ansiescape.AnsiRaw`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0641">AVID-2026-R0641</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.CompleteKey`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0642">AVID-2026-R0642</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `apikey.GetKey`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0643">AVID-2026-R0643</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `atkgen.Tox`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0644">AVID-2026-R0644</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `continuation.ContinueSlursReclaimedSlurs`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0645">AVID-2026-R0645</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.Ablation_Dan_11_0`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0646">AVID-2026-R0646</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.AutoDANCached`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0647">AVID-2026-R0647</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dan.DanInTheWild`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0648">AVID-2026-R0648</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.Repeat`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0649">AVID-2026-R0649</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `divergence.RepeatedToken`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0650">AVID-2026-R0650</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `dra.DRA`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0651">AVID-2026-R0651</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAscii85`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0652">AVID-2026-R0652</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectAtbash`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0653">AVID-2026-R0653</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase16`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0654">AVID-2026-R0654</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase2048`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0655">AVID-2026-R0655</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase32`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0656">AVID-2026-R0656</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBase64`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0657">AVID-2026-R0657</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectBraille`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0658">AVID-2026-R0658</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectEcoji`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0659">AVID-2026-R0659</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectHex`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0660">AVID-2026-R0660</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectMorse`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0661">AVID-2026-R0661</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectNato`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0662">AVID-2026-R0662</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectROT13`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0663">AVID-2026-R0663</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUU`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0664">AVID-2026-R0664</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectUnicodeTagChars`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0665">AVID-2026-R0665</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `encoding.InjectZalgo`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0666">AVID-2026-R0666</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.JinjaTemplatePythonInjection`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0667">AVID-2026-R0667</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `exploitation.SQLInjectionEcho`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0668">AVID-2026-R0668</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.Tag`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0669">AVID-2026-R0669</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.ThreatenJSON`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0670">AVID-2026-R0670</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `goodside.WhoIsRiley`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0671">AVID-2026-R0671</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Slurs`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0672">AVID-2026-R0672</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Substances`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0673">AVID-2026-R0673</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win10`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0674">AVID-2026-R0674</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `grandma.Win11`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0675">AVID-2026-R0675</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetEiffel`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0676">AVID-2026-R0676</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionFactSnippetLegal`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0677">AVID-2026-R0677</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionReport`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0678">AVID-2026-R0678</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionResume`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0679">AVID-2026-R0679</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnFr`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0680">AVID-2026-R0680</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentInjectionTranslationEnZh`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0681">AVID-2026-R0681</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentJailbreak`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0682">AVID-2026-R0682</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhois`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0683">AVID-2026-R0683</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `latentinjection.LatentWhoisSnippet`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0684">AVID-2026-R0684</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianCloze`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0685">AVID-2026-R0685</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.GuardianComplete`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0686">AVID-2026-R0686</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureCloze`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0687">AVID-2026-R0687</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.LiteratureComplete`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0688">AVID-2026-R0688</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTCloze`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0689">AVID-2026-R0689</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.NYTComplete`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0690">AVID-2026-R0690</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterCloze`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0691">AVID-2026-R0691</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `leakreplay.PotterComplete`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0692">AVID-2026-R0692</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Bullying`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0693">AVID-2026-R0693</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Deadnaming`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0694">AVID-2026-R0694</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.QuackMedicine`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0695">AVID-2026-R0695</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SexualContent`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0696">AVID-2026-R0696</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.Sexualisation`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0697">AVID-2026-R0697</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `lmrc.SlurUsage`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0698">AVID-2026-R0698</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Evasion`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0699">AVID-2026-R0699</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.Payload`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0700">AVID-2026-R0700</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.SubFunctions`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0701">AVID-2026-R0701</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `malwaregen.TopLevel`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0702">AVID-2026-R0702</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The model rnj-1-instruct from Essential AI was evaluated by the Garak LLM Vulnerability scanner using the probe `misleading.FalseAssertion`.</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0703">AVID-2026-R0703</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the AI system gpt-5-nano on the bbq benchmark using Inspect Evals</td><td>Measurement</td><td>2026-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0704">AVID-2026-R0704</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM MiniMax-M2.5 on the bbq benchmark using Inspect Evals</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0705">AVID-2026-R0705</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM gpt-oss-20b on the bbq benchmark using Inspect Evals</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0706">AVID-2026-R0706</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM gemma-3n-E4B-it on the bbq benchmark using Inspect Evals</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0707">AVID-2026-R0707</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM LFM2-24B-A2B on the bbq benchmark using Inspect Evals</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0708">AVID-2026-R0708</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM rnj-1-instruct on the bbq benchmark using Inspect Evals</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0709">AVID-2026-R0709</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM rnj-1-instruct on the bold benchmark using Inspect Evals</td><td>Measurement</td><td>2026-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0710">AVID-2026-R0710</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-1114</td><td>Advisory</td><td>2021-08-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0711">AVID-2026-R0711</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Bot Framework SDK Information Disclosure Vulnerability (CVE-2021-1725)</td><td>Advisory</td><td>2021-01-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0712">AVID-2026-R0712</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MongoDB Node.js client side field level encryption library may not be validating KMS certificate (CVE-2021-20327)</td><td>Advisory</td><td>2021-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R0713">AVID-2026-R0713</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-20486</td><td>Advisory</td><td>2021-05-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0714">AVID-2026-R0714</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-2138</td><td>Advisory</td><td>2021-03-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0715">AVID-2026-R0715</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-21605</td><td>Advisory</td><td>2021-01-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R0716">AVID-2026-R0716</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-21677</td><td>Advisory</td><td>2021-08-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R0717">AVID-2026-R0717</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-22205</td><td>Advisory</td><td>2021-04-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R0718">AVID-2026-R0718</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service of protobuf-java parsing procedure (CVE-2021-22569)</td><td>Advisory</td><td>2022-01-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R0719">AVID-2026-R0719</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deserialization of Untrusted Data (CVE-2021-23338)</td><td>Advisory</td><td>2021-02-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R0720">AVID-2026-R0720</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Authenticated users can override system configurations in their requests which allows them to execute arbitrary code. (CVE-2021-25646)</td><td>Advisory</td><td>2021-01-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R0721">AVID-2026-R0721</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: Lineage API endpoint for Experimental API missed authentication check (CVE-2021-26697)</td><td>Advisory</td><td>2021-02-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0722">AVID-2026-R0722</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Druid Authenticated users can execute arbitrary code from malicious MySQL database systems. (CVE-2021-26919)</td><td>Advisory</td><td>2021-03-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R0723">AVID-2026-R0723</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TIBCO Spotfire Windows Platform Artifact Search vulnerability (CVE-2021-28830)</td><td>Advisory</td><td>2021-06-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R0724">AVID-2026-R0724</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `RaggedBinCount` (CVE-2021-29512)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0725">AVID-2026-R0725</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Type confusion during tensor casts lead to dereferencing null pointers (CVE-2021-29513)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0726">AVID-2026-R0726</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap out of bounds write in `RaggedBinCount` (CVE-2021-29514)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0727">AVID-2026-R0727</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to null pointer in `MatrixDiag*` ops (CVE-2021-29515)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0728">AVID-2026-R0728</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference via invalid Ragged Tensors (CVE-2021-29516)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0729">AVID-2026-R0729</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in `Conv3D` (CVE-2021-29517)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0730">AVID-2026-R0730</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Session operations in eager mode lead to null pointer dereferences (CVE-2021-29518)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0731">AVID-2026-R0731</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in SparseCross due to type confusion (CVE-2021-29519)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0732">AVID-2026-R0732</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `Conv3DBackprop*` (CVE-2021-29520)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0733">AVID-2026-R0733</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in SparseCountSparseOutput (CVE-2021-29521)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0734">AVID-2026-R0734</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `Conv3DBackprop*` (CVE-2021-29522)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0735">AVID-2026-R0735</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in AddManySparseToTensorsMap (CVE-2021-29523)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0736">AVID-2026-R0736</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `Conv2DBackpropInput` (CVE-2021-29525)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0737">AVID-2026-R0737</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow caused by rounding (CVE-2021-29529)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0738">AVID-2026-R0738</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Invalid validation in `SparseMatrixSparseCholesky` (CVE-2021-29530)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0739">AVID-2026-R0739</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in tf.raw_ops.EncodePng (CVE-2021-29531)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0740">AVID-2026-R0740</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap out of bounds read in `RaggedCross` (CVE-2021-29532)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0741">AVID-2026-R0741</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in DrawBoundingBoxes (CVE-2021-29533)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0742">AVID-2026-R0742</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in SparseConcat (CVE-2021-29534)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0743">AVID-2026-R0743</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `QuantizedMul` (CVE-2021-29535)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0744">AVID-2026-R0744</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `QuantizedReshape` (CVE-2021-29536)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0745">AVID-2026-R0745</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `QuantizedResizeBilinear` (CVE-2021-29537)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0746">AVID-2026-R0746</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in `Conv2DBackpropFilter` (CVE-2021-29538)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0747">AVID-2026-R0747</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in tf.raw_ops.ImmutableConst (CVE-2021-29539)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0748">AVID-2026-R0748</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `Conv2DBackpropFilter` (CVE-2021-29540)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0749">AVID-2026-R0749</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `StringNGrams` (CVE-2021-29541)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0750">AVID-2026-R0750</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `StringNGrams` (CVE-2021-29542)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0751">AVID-2026-R0751</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in `CTCGreedyDecoder` (CVE-2021-29543)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0752">AVID-2026-R0752</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in `QuantizeAndDequantizeV4Grad` (CVE-2021-29544)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0753">AVID-2026-R0753</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `SparseTensorToCSRSparseMatrix` (CVE-2021-29545)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0754">AVID-2026-R0754</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `QuantizedBiasAdd` (CVE-2021-29546)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0755">AVID-2026-R0755</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap out of bounds in `QuantizedBatchNormWithGlobalNormalization` (CVE-2021-29547)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0756">AVID-2026-R0756</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `QuantizedBatchNormWithGlobalNormalization` (CVE-2021-29548)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0757">AVID-2026-R0757</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `QuantizedAdd` (CVE-2021-29549)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0758">AVID-2026-R0758</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OOB read in `MatrixTriangularSolve` (CVE-2021-29551)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0759">AVID-2026-R0759</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in `QuantizeAndDequantizeV3` (CVE-2021-29553)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0760">AVID-2026-R0760</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `DenseCountSparseOutput` (CVE-2021-29554)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0761">AVID-2026-R0761</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `FusedBatchNorm` (CVE-2021-29555)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0762">AVID-2026-R0762</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `SparseMatMul` (CVE-2021-29557)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0763">AVID-2026-R0763</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `SparseSplit` (CVE-2021-29558)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0764">AVID-2026-R0764</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB access in unicode ops (CVE-2021-29559)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0765">AVID-2026-R0765</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `RaggedTensorToTensor` (CVE-2021-29560)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0766">AVID-2026-R0766</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in `LoadAndRemapMatrix` (CVE-2021-29561)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0767">AVID-2026-R0767</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in `tf.raw_ops.IRFFT` (CVE-2021-29562)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0768">AVID-2026-R0768</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail in `tf.raw_ops.RFFT` (CVE-2021-29563)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0769">AVID-2026-R0769</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `EditDistance` (CVE-2021-29564)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0770">AVID-2026-R0770</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `SparseFillEmptyRows` (CVE-2021-29565)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0771">AVID-2026-R0771</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB access in `Dilation2DBackpropInput` (CVE-2021-29566)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0772">AVID-2026-R0772</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Lack of validation in `SparseDenseCwiseMul` (CVE-2021-29567)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0773">AVID-2026-R0773</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to null in `ParameterizedTruncatedNormal` (CVE-2021-29568)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0774">AVID-2026-R0774</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap out of bounds read in `RequantizationRange` (CVE-2021-29569)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0775">AVID-2026-R0775</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap out of bounds read in `MaxPoolGradWithArgmax` (CVE-2021-29570)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0776">AVID-2026-R0776</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Memory corruption in `DrawBoundingBoxesV2` (CVE-2021-29571)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0777">AVID-2026-R0777</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in `SdcaOptimizer` (CVE-2021-29572)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0778">AVID-2026-R0778</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Undefined behavior in `MaxPool3DGradGrad` (CVE-2021-29574)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0779">AVID-2026-R0779</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow/denial of service in `tf.raw_ops.ReverseSequence` (CVE-2021-29575)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0780">AVID-2026-R0780</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `MaxPool3DGradGrad` (CVE-2021-29576)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0781">AVID-2026-R0781</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `AvgPool3DGrad` (CVE-2021-29577)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0782">AVID-2026-R0782</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `FractionalAvgPoolGrad` (CVE-2021-29578)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0783">AVID-2026-R0783</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `MaxPoolGrad` (CVE-2021-29579)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0784">AVID-2026-R0784</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Undefined behavior and `CHECK`-fail in `FractionalMaxPoolGrad` (CVE-2021-29580)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0785">AVID-2026-R0785</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `CTCBeamSearchDecoder` (CVE-2021-29581)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0786">AVID-2026-R0786</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in `tf.raw_ops.Dequantize` (CVE-2021-29582)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0787">AVID-2026-R0787</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow and undefined behavior in `FusedBatchNorm` (CVE-2021-29583)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0788">AVID-2026-R0788</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CHECK-fail due to integer overflow (CVE-2021-29584)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0789">AVID-2026-R0789</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in padding computation in TFLite (CVE-2021-29585)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0790">AVID-2026-R0790</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TFLite's implementation of `TransposeConv` (CVE-2021-29588)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0791">AVID-2026-R0791</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in TFLite's implementation of `Minimum` or `Maximum` (CVE-2021-29590)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0792">AVID-2026-R0792</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in TFLite's `Reshape` operator (CVE-2021-29592)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0793">AVID-2026-R0793</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TFLite's convolution code (CVE-2021-29594)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0794">AVID-2026-R0794</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TFLite's implementation of `DepthToSpace` (CVE-2021-29595)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0795">AVID-2026-R0795</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TFLite's implementation of `EmbeddingLookup` (CVE-2021-29596)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0796">AVID-2026-R0796</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB write in TFLite (CVE-2021-29603)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0797">AVID-2026-R0797</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TFLite's implementation of hashtable lookup (CVE-2021-29604)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0798">AVID-2026-R0798</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in TFLite memory allocation (CVE-2021-29605)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0799">AVID-2026-R0799</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in TFLite (CVE-2021-29606)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0800">AVID-2026-R0800</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB and null pointer dereference in `RaggedTensorToTensor` (CVE-2021-29608)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0801">AVID-2026-R0801</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in `SparseAdd` (CVE-2021-29609)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0802">AVID-2026-R0802</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in `SparseReshape` (CVE-2021-29611)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0803">AVID-2026-R0803</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `BandedTriangularSolve` (CVE-2021-29612)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0804">AVID-2026-R0804</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in `tf.raw_ops.CTCLoss` (CVE-2021-29613)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0805">AVID-2026-R0805</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Interpreter crash from `tf.io.decode_raw` (CVE-2021-29614)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0806">AVID-2026-R0806</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stack overflow in `ParseAttrValue` with nested tensors (CVE-2021-29615)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0807">AVID-2026-R0807</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null dereference in Grappler's `TrySimplify` (CVE-2021-29616)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0808">AVID-2026-R0808</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crash in `tf.strings.substr` due to `CHECK`-fail (CVE-2021-29617)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0809">AVID-2026-R0809</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crash in `tf.transpose` with complex inputs (CVE-2021-29618)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0810">AVID-2026-R0810</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `tf.raw_ops.SparseCountSparseOutput` (CVE-2021-29619)</td><td>Advisory</td><td>2021-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0811">AVID-2026-R0811</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-29730</td><td>Advisory</td><td>2021-07-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R0812">AVID-2026-R0812</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-31681</td><td>Advisory</td><td>2023-07-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R0813">AVID-2026-R0813</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Action Commands (run/shell/exec) Against Library URIs Ignore Configured Remote Endpoint (CVE-2021-32635)</td><td>Advisory</td><td>2021-05-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R0814">AVID-2026-R0814</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">JupyterLab: XSS due to lack of sanitization of the action attribute of an html <form> (CVE-2021-32797)</td><td>Advisory</td><td>2021-08-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R0815">AVID-2026-R0815</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Regular Expression Denial of Service in flask-restx (CVE-2021-32838)</td><td>Advisory</td><td>2021-09-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0816">AVID-2026-R0816</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-33073</td><td>Advisory</td><td>2021-11-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0817">AVID-2026-R0817</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-33430</td><td>Advisory</td><td>2021-12-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0818">AVID-2026-R0818</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-33648</td><td>Advisory</td><td>2022-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0819">AVID-2026-R0819</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-33650</td><td>Advisory</td><td>2022-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0820">AVID-2026-R0820</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-33651</td><td>Advisory</td><td>2022-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0821">AVID-2026-R0821</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mysql JDBC Connector Deserialize RCE (CVE-2021-36774)</td><td>Advisory</td><td>2022-01-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R0822">AVID-2026-R0822</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deleting PRTBs associated to a group doesn't cause deletion of corresponding RoleBindings (CVE-2021-36775)</td><td>Advisory</td><td>2022-04-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R0823">AVID-2026-R0823</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Exposure of repository credentials to external third-party sources (CVE-2021-36778)</td><td>Advisory</td><td>2022-05-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R0824">AVID-2026-R0824</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-3702</td><td>Advisory</td><td>2022-08-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R0825">AVID-2026-R0825</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap out of bounds access in sparse reduction operations in TensorFlow (CVE-2021-37635)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0826">AVID-2026-R0826</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Floating point exception in `SparseDenseCwiseDiv` in TensorFlow (CVE-2021-37636)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0827">AVID-2026-R0827</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `CompressElement` in TensorFlow (CVE-2021-37637)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0828">AVID-2026-R0828</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `RaggedTensorToTensor` in TensorFlow (CVE-2021-37638)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0829">AVID-2026-R0829</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference and heap OOB read in TensorFlow (CVE-2021-37639)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0830">AVID-2026-R0830</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer division by 0 in sparse reshaping in TensorFlow (CVE-2021-37640)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0831">AVID-2026-R0831</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in `RaggedGather` in TensorFlow (CVE-2021-37641)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0832">AVID-2026-R0832</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `ResourceScatterDiv` in TensorFlow (CVE-2021-37642)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0833">AVID-2026-R0833</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `MatrixDiagPartOp` in TensorFlow (CVE-2021-37643)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0834">AVID-2026-R0834</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`std::abort` raised from `TensorListReserve` in TensorFlow (CVE-2021-37644)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0835">AVID-2026-R0835</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow due to conversion to unsigned in TensorFlow (CVE-2021-37645)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0836">AVID-2026-R0836</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Bad alloc in `StringNGrams` caused by integer conversion in TensorFlow (CVE-2021-37646)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0837">AVID-2026-R0837</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `SparseTensorSliceDataset` in TensorFlow (CVE-2021-37647)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0838">AVID-2026-R0838</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incorrect validation of `SaveV2` inputs in TensorFlow (CVE-2021-37648)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0839">AVID-2026-R0839</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in `UncompressElement` in TensorFlow (CVE-2021-37649)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0840">AVID-2026-R0840</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault and heap buffer overflow in `{Experimental,}DatasetToTFRecord` in TensorFlow (CVE-2021-37650)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0841">AVID-2026-R0841</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `FractionalAvgPoolGrad` in TensorFlow (CVE-2021-37651)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0842">AVID-2026-R0842</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Use after free in boosted trees creation in TensorFlow (CVE-2021-37652)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0843">AVID-2026-R0843</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in `ResourceGather` in TensorFlow (CVE-2021-37653)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0844">AVID-2026-R0844</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB and CHECK fail in `ResourceGather` in TensorFlow (CVE-2021-37654)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0845">AVID-2026-R0845</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in `ResourceScatterUpdate` in TensorFlow (CVE-2021-37655)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0846">AVID-2026-R0846</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in `RaggedTensorToSparse` in TensorFlow (CVE-2021-37656)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0847">AVID-2026-R0847</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in `MatrixDiagV*` ops in TensorFlow (CVE-2021-37657)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0848">AVID-2026-R0848</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in `MatrixSetDiagV*` ops in TensorFlow (CVE-2021-37658)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0849">AVID-2026-R0849</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds read via null pointer dereference in TensorFlow (CVE-2021-37659)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0850">AVID-2026-R0850</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in inplace operations in TensorFlow (CVE-2021-37660)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0851">AVID-2026-R0851</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crash caused by integer conversion to unsigned in TensorFlow (CVE-2021-37661)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0852">AVID-2026-R0852</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in boosted trees in TensorFlow (CVE-2021-37662)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0853">AVID-2026-R0853</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in `QuantizeV2` in TensorFlow (CVE-2021-37663)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0854">AVID-2026-R0854</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in boosted trees in TensorFlow (CVE-2021-37664)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0855">AVID-2026-R0855</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in MKL requantization in TensorFlow (CVE-2021-37665)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0856">AVID-2026-R0856</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in `RaggedTensorToVariant` in TensorFlow (CVE-2021-37666)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0857">AVID-2026-R0857</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in unicode encoding in TensorFlow (CVE-2021-37667)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0858">AVID-2026-R0858</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TensorFlow Lite `tf.raw_ops.UnravelIndex` (CVE-2021-37668)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0859">AVID-2026-R0859</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crash in NMS ops caused by integer conversion to unsigned in TensorFlow (CVE-2021-37669)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0860">AVID-2026-R0860</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in `UpperBound` and `LowerBound` in TensorFlow (CVE-2021-37670)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0861">AVID-2026-R0861</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in map operations in TensorFlow (CVE-2021-37671)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0862">AVID-2026-R0862</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in `SdcaOptimizerV2` in TensorFlow (CVE-2021-37672)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0863">AVID-2026-R0863</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK`-fail in `MapStage` in TensorFlow (CVE-2021-37673)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0864">AVID-2026-R0864</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in `MaxPoolGrad` in TensorFlow (CVE-2021-37674)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0865">AVID-2026-R0865</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by 0 in most convolution operators in TensorFlow (CVE-2021-37675)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0866">AVID-2026-R0866</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to nullptr in shape inference in TensorFlow (CVE-2021-37676)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0867">AVID-2026-R0867</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation in shape inference for `Dequantize` in TensorFlow (CVE-2021-37677)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0868">AVID-2026-R0868</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in nested `tf.map_fn` with `RaggedTensor`s in TensorFlow (CVE-2021-37679)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0869">AVID-2026-R0869</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TFLite in TensorFlow (CVE-2021-37680)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0870">AVID-2026-R0870</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer exception in TensorFlow Lite (CVE-2021-37681)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0871">AVID-2026-R0871</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TensorFlow Lite division operations (CVE-2021-37683)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0872">AVID-2026-R0872</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TensorFlow Lite pooling operations (CVE-2021-37684)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0873">AVID-2026-R0873</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in TensorFlow Lite (CVE-2021-37685)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0874">AVID-2026-R0874</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Infinite loop in TensorFlow Lite (CVE-2021-37686)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0875">AVID-2026-R0875</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB in TensorFlow Lite's `Gather*` implementations (CVE-2021-37687)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0876">AVID-2026-R0876</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in TensorFlow Lite (CVE-2021-37688)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0877">AVID-2026-R0877</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Use after free and segfault in shape inference functions in TensorFlow (CVE-2021-37690)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0878">AVID-2026-R0878</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault on strings tensors with mistmatched dimensions in TensorFlow (CVE-2021-37692)</td><td>Advisory</td><td>2021-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0879">AVID-2026-R0879</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Shell Command Injection Vulnerability in Nimbus Thrift Server (CVE-2021-38294)</td><td>Advisory</td><td>2021-10-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R0880">AVID-2026-R0880</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Spark Key Negotiation Vulnerability (CVE-2021-38296)</td><td>Advisory</td><td>2022-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0881">AVID-2026-R0881</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Restriction of XML External Entity Reference in stanfordnlp/corenlp (CVE-2021-3869)</td><td>Advisory</td><td>2021-10-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0882">AVID-2026-R0882</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Restriction of XML External Entity Reference in stanfordnlp/corenlp (CVE-2021-3878)</td><td>Advisory</td><td>2021-10-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R0883">AVID-2026-R0883</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Dependency injection in NVCaffe (CVE-2021-39158)</td><td>Advisory</td><td>2021-08-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R0884">AVID-2026-R0884</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Code injection in nbgitpuller (CVE-2021-39160)</td><td>Advisory</td><td>2021-08-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R0885">AVID-2026-R0885</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-39906</td><td>Advisory</td><td>2021-11-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0886">AVID-2026-R0886</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improperly Implemented path matching for in-toto-golang (CVE-2021-41087)</td><td>Advisory</td><td>2021-09-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R0887">AVID-2026-R0887</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Splash authentication credentials potentially leaked to target websites in scrapy-splash (CVE-2021-41124)</td><td>Advisory</td><td>2021-10-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0888">AVID-2026-R0888</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crash in `tf.math.segment_*` operations (CVE-2021-41195)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0889">AVID-2026-R0889</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crash in `max_pool3d` when size argument is 0 or negative (CVE-2021-41196)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0890">AVID-2026-R0890</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crashes due to overflow and `CHECK`-fail in ops with large tensor shapes (CVE-2021-41197)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0891">AVID-2026-R0891</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow/crash in `tf.tile` when tiling tensor is large (CVE-2021-41198)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0892">AVID-2026-R0892</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow/crash in `tf.image.resize` when size is large (CVE-2021-41199)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0893">AVID-2026-R0893</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in `tf.summary.create_file_writer` (CVE-2021-41200)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0894">AVID-2026-R0894</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unitialized access in `EinsumHelper::ParseEquation` (CVE-2021-41201)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0895">AVID-2026-R0895</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow/crash in `tf.range` (CVE-2021-41202)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0896">AVID-2026-R0896</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation during checkpoint loading (CVE-2021-41203)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0897">AVID-2026-R0897</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault while copying constant resource tensor (CVE-2021-41204)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0898">AVID-2026-R0898</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in all `tf.raw_ops.QuantizeAndDequantizeV*` ops (CVE-2021-41205)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0899">AVID-2026-R0899</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation of shapes in multiple TF ops (CVE-2021-41206)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0900">AVID-2026-R0900</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in `ParallelConcat` (CVE-2021-41207)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0901">AVID-2026-R0901</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in convolutions with zero size filters (CVE-2021-41209)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0902">AVID-2026-R0902</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in `tf.raw_ops.SparseCountSparseOutput` (CVE-2021-41210)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0903">AVID-2026-R0903</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in shape inference for `QuantizeV2` (CVE-2021-41211)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0904">AVID-2026-R0904</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in `tf.ragged.cross` (CVE-2021-41212)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0905">AVID-2026-R0905</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reference binding to `nullptr` in `tf.ragged.cross` (CVE-2021-41214)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0906">AVID-2026-R0906</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer exception in `DeserializeSparse` (CVE-2021-41215)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0907">AVID-2026-R0907</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in `Transpose` (CVE-2021-41216)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0908">AVID-2026-R0908</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer exception when `Exit` node is not preceded by `Enter` op (CVE-2021-41217)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0909">AVID-2026-R0909</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer division by 0 in `tf.raw_ops.AllToAll` (CVE-2021-41218)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0910">AVID-2026-R0910</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Undefined behavior via `nullptr` reference binding in sparse matrix multiplication (CVE-2021-41219)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0911">AVID-2026-R0911</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Use after free in `CollectiveReduceV2` (CVE-2021-41220)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0912">AVID-2026-R0912</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Access to invalid memory during shape inference in `Cudnn*` ops (CVE-2021-41221)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0913">AVID-2026-R0913</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault due to negative splits in `SplitV` (CVE-2021-41222)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0914">AVID-2026-R0914</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in `FusedBatchNorm` kernels (CVE-2021-41223)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0915">AVID-2026-R0915</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`SparseFillEmptyRows` heap OOB read (CVE-2021-41224)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0916">AVID-2026-R0916</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap OOB read in `SparseBinCount` (CVE-2021-41226)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0917">AVID-2026-R0917</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Code injection in `saved_model_cli` (CVE-2021-41228)</td><td>Advisory</td><td>2021-11-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0918">AVID-2026-R0918</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-41495</td><td>Advisory</td><td>2021-12-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0919">AVID-2026-R0919</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Parquet-MR potential DoS in case of malicious Parquet file (CVE-2021-41561)</td><td>Advisory</td><td>2021-12-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0920">AVID-2026-R0920</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-42343</td><td>Advisory</td><td>2021-10-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0921">AVID-2026-R0921</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-42951</td><td>Advisory</td><td>2022-03-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R0922">AVID-2026-R0922</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-42969</td><td>Advisory</td><td>2022-05-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R0923">AVID-2026-R0923</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Bot Framework SDK Remote Code Execution Vulnerability (CVE-2021-43225)</td><td>Advisory</td><td>2021-12-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R0924">AVID-2026-R0924</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Inefficient Regular Expression Complexity in nltk (CVE-2021-43854)</td><td>Advisory</td><td>2021-12-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R0925">AVID-2026-R0925</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Chain Sea Information Integration Co., Ltd ai chatbot system - Reflected XSS (CVE-2021-44163)</td><td>Advisory</td><td>2021-12-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0926">AVID-2026-R0926</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Chain Sea Information Integration Co., Ltd ai chatbot system - Arbitrary File Upload (CVE-2021-44164)</td><td>Advisory</td><td>2021-12-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R0927">AVID-2026-R0927</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Log4j2 JNDI features do not protect against attacker controlled LDAP and other JNDI related endpoints (CVE-2021-44228)</td><td>Advisory</td><td>2021-12-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0928">AVID-2026-R0928</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Log4j2 vulnerable to RCE via JDBC Appender when attacker controls configuration (CVE-2021-44832)</td><td>Advisory</td><td>2021-12-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R0929">AVID-2026-R0929</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2021-45074</td><td>Advisory</td><td>2022-03-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R0930">AVID-2026-R0930</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: Reflected XSS via Origin Query Argument in URL (CVE-2021-45229)</td><td>Advisory</td><td>2022-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R0931">AVID-2026-R0931</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Log4j hot patch package privilege escalation (CVE-2022-0070)</td><td>Advisory</td><td>2022-04-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0932">AVID-2026-R0932</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Restriction of XML External Entity Reference in stanfordnlp/corenlp (CVE-2022-0198)</td><td>Advisory</td><td>2022-01-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R0933">AVID-2026-R0933</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-0573</td><td>Advisory</td><td>2022-05-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0934">AVID-2026-R0934</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-0668</td><td>Advisory</td><td>2023-01-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R0935">AVID-2026-R0935</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Code Injection in pytorchlightning/pytorch-lightning (CVE-2022-0845)</td><td>Advisory</td><td>2022-03-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0936">AVID-2026-R0936</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-1423</td><td>Advisory</td><td>2022-05-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0937">AVID-2026-R0937</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of Memory issue in ProtocolBuffers for cpp and python (CVE-2022-1941)</td><td>Advisory</td><td>2022-09-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R0938">AVID-2026-R0938</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-20617</td><td>Advisory</td><td>2022-01-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0939">AVID-2026-R0939</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Pipenv's requirements.txt parsing allows malicious index url in comments (CVE-2022-21668)</td><td>Advisory</td><td>2022-01-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0940">AVID-2026-R0940</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF vulnerability (requires authentication) (CVE-2022-21697)</td><td>Advisory</td><td>2022-01-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R0941">AVID-2026-R0941</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in Tensorflow (CVE-2022-21725)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0942">AVID-2026-R0942</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds read in Tensorflow (CVE-2022-21726)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0943">AVID-2026-R0943</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in Tensorflow (CVE-2022-21727)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0944">AVID-2026-R0944</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds read in Tensorflow (CVE-2022-21728)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0945">AVID-2026-R0945</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow and uncaught divide by zero in Tensorflow (CVE-2022-21729)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0946">AVID-2026-R0946</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds read in Tensorflow (CVE-2022-21730)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0947">AVID-2026-R0947</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Type confusion leading to segfault in Tensorflow (CVE-2022-21731)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0948">AVID-2026-R0948</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Memory exhaustion in Tensorflow (CVE-2022-21732)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0949">AVID-2026-R0949</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Memory exhaustion in Tensorflow (CVE-2022-21733)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0950">AVID-2026-R0950</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK`-failures in Tensorflow (CVE-2022-21734)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0951">AVID-2026-R0951</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Undefined behavior in Tensorflow (CVE-2022-21736)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0952">AVID-2026-R0952</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow leading to crash in Tensorflow (CVE-2022-21738)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0953">AVID-2026-R0953</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in TensorFlow (CVE-2022-21739)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0954">AVID-2026-R0954</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap overflow in Tensorflow (CVE-2022-21740)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0955">AVID-2026-R0955</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Division by zero in TFLite (CVE-2022-21741)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0956">AVID-2026-R0956</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-21820</td><td>Advisory</td><td>2022-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R0957">AVID-2026-R0957</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-21821</td><td>Advisory</td><td>2022-03-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R0958">AVID-2026-R0958</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-21822</td><td>Advisory</td><td>2022-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R0959">AVID-2026-R0959</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-2185</td><td>Advisory</td><td>2022-07-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R0960">AVID-2026-R0960</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-22965</td><td>Advisory</td><td>2022-04-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R0961">AVID-2026-R0961</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command Injection (CVE-2022-22984)</td><td>Advisory</td><td>2022-11-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R0962">AVID-2026-R0962</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write when Extracting Tarballs retrieved from a remote location using in mindsdb (CVE-2022-23522)</td><td>Advisory</td><td>2023-03-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R0963">AVID-2026-R0963</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">jsonwebtoken unrestricted key type could lead to legacy keys usage (CVE-2022-23539)</td><td>Advisory</td><td>2022-12-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R0964">AVID-2026-R0964</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in TFLite (CVE-2022-23559)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0965">AVID-2026-R0965</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Read and Write outside of bounds in TFLite (CVE-2022-23560)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0966">AVID-2026-R0966</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in Tensorflow (CVE-2022-23562)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0967">AVID-2026-R0967</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insecure temporary file in Tensorflow (CVE-2022-23563)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0968">AVID-2026-R0968</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reachable Assertion in Tensorflow (CVE-2022-23564)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0969">AVID-2026-R0969</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds write in Tensorflow (CVE-2022-23566)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0970">AVID-2026-R0970</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflows in Tensorflow (CVE-2022-23567)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0971">AVID-2026-R0971</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflows in Tensorflow (CVE-2022-23568)</td><td>Advisory</td><td>2022-02-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R0972">AVID-2026-R0972</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null-dereference in Tensorflow (CVE-2022-23570)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0973">AVID-2026-R0973</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reachable Assertion in Tensorflow (CVE-2022-23571)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0974">AVID-2026-R0974</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crash when type cannot be specialized in Tensorflow (CVE-2022-23572)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0975">AVID-2026-R0975</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Uninitialized variable access in Tensorflow (CVE-2022-23573)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0976">AVID-2026-R0976</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds read and write in Tensorflow (CVE-2022-23574)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0977">AVID-2026-R0977</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in Tensorflow (CVE-2022-23575)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0978">AVID-2026-R0978</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in Tensorflow (CVE-2022-23576)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0979">AVID-2026-R0979</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null-dereference in Tensorflow (CVE-2022-23577)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0980">AVID-2026-R0980</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Memory leak in Tensorflow (CVE-2022-23578)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0981">AVID-2026-R0981</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK`-failures during Grappler's `SafeToRemoveIdentity` in Tensorflow (CVE-2022-23579)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0982">AVID-2026-R0982</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Abort caused by allocating a vector that is too large in Tensorflow (CVE-2022-23580)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0983">AVID-2026-R0983</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK`-failures during Grappler's `IsSimplifiableReshape` in Tensorflow (CVE-2022-23581)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0984">AVID-2026-R0984</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK`-failures in `TensorByteSize` in Tensorflow (CVE-2022-23582)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0985">AVID-2026-R0985</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK`-failures in binary ops in Tensorflow (CVE-2022-23583)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0986">AVID-2026-R0986</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Use after free in `DecodePng` in Tensorflow (CVE-2022-23584)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0987">AVID-2026-R0987</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Memory leak in decoding PNG images in Tensorflow (CVE-2022-23585)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0988">AVID-2026-R0988</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple `CHECK`-fails in `function.cc` in Tensorflow (CVE-2022-23586)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0989">AVID-2026-R0989</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in Tensorflow (CVE-2022-23587)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0990">AVID-2026-R0990</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in Grappler's `IsConstant` in Tensorflow (CVE-2022-23589)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0991">AVID-2026-R0991</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stack overflow in Tensorflow (CVE-2022-23591)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0992">AVID-2026-R0992</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds read in Tensorflow (CVE-2022-23592)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0993">AVID-2026-R0993</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `simplifyBroadcast` in Tensorflow (CVE-2022-23593)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0994">AVID-2026-R0994</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds read in Tensorflow (CVE-2022-23594)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0995">AVID-2026-R0995</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in TensorFlow (CVE-2022-23595)</td><td>Advisory</td><td>2022-02-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0996">AVID-2026-R0996</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-2417</td><td>Advisory</td><td>2022-08-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R0997">AVID-2026-R0997</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar Proxy target broker address isn't validated (CVE-2022-24280)</td><td>Advisory</td><td>2022-09-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R0998">AVID-2026-R0998</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ReDoS in Apache MXNet RTC Module (CVE-2022-24294)</td><td>Advisory</td><td>2022-07-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R0999">AVID-2026-R0999</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Sensitive Auth & Cookie data stored in Jupyter server logs (CVE-2022-24757)</td><td>Advisory</td><td>2022-03-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1000">AVID-2026-R1000</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insertion of Sensitive Information into Log File affects Jupyter Notebook (CVE-2022-24758)</td><td>Advisory</td><td>2022-03-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R1001">AVID-2026-R1001</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Neutralization of Formula Elements in a CSV File in Gradio Flagging (CVE-2022-24770)</td><td>Advisory</td><td>2022-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1002">AVID-2026-R1002</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-25201</td><td>Advisory</td><td>2022-02-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1003">AVID-2026-R1003</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deserialization of Untrusted Data (CVE-2022-25845)</td><td>Advisory</td><td>2022-06-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1004">AVID-2026-R1004</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-25864</td><td>Advisory</td><td>2023-08-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1005">AVID-2026-R1005</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-26076</td><td>Advisory</td><td>2023-02-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1006">AVID-2026-R1006</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-26425</td><td>Advisory</td><td>2023-02-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1007">AVID-2026-R1007</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-26526</td><td>Advisory</td><td>2022-03-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1008">AVID-2026-R1008</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-27199</td><td>Advisory</td><td>2022-03-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1009">AVID-2026-R1009</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-27234</td><td>Advisory</td><td>2023-02-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1010">AVID-2026-R1010</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-28199</td><td>Advisory</td><td>2022-09-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1011">AVID-2026-R1011</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-28696</td><td>Advisory</td><td>2022-08-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1012">AVID-2026-R1012</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-2884</td><td>Advisory</td><td>2022-10-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1013">AVID-2026-R1013</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">No protection against rollback attacks in go-tuf (CVE-2022-29173)</td><td>Advisory</td><td>2022-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1014">AVID-2026-R1014</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service via `GetSessionTensor` in TensorFlow (CVE-2022-29191)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1015">AVID-2026-R1015</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation crashes `QuantizeAndDequantizeV4Grad` in TensorFlow (CVE-2022-29192)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1016">AVID-2026-R1016</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes `TensorSummaryV2` in TensorFlow to crash (CVE-2022-29193)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1017">AVID-2026-R1017</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service via `DeleteSessionTensor` in TensorFlow (CVE-2022-29194)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1018">AVID-2026-R1018</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service in TensorFlow via `StagePeek` (CVE-2022-29195)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1019">AVID-2026-R1019</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service in TensorFlow via `Conv3DBackpropFilterV2` (CVE-2022-29196)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1020">AVID-2026-R1020</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service in TensorFlow via `UnsortedSegmentJoin` (CVE-2022-29197)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1021">AVID-2026-R1021</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service in TensorFlow via `SparseTensorToCSRSparseMatrix` (CVE-2022-29198)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1022">AVID-2026-R1022</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service in TensorFlow via `LoadAndRemapMatrix` (CVE-2022-29199)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1023">AVID-2026-R1023</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service in TensorFlow via `LSTMBlockCell` (CVE-2022-29200)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1024">AVID-2026-R1024</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation in `QuantizedConv2D` results in undefined behavior in TensorFlow (CVE-2022-29201)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1025">AVID-2026-R1025</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of service in TensorFlow due to lack of validation in `tf.ragged.constant` (CVE-2022-29202)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1026">AVID-2026-R1026</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in `SpaceToBatchND` in TensorFlow (CVE-2022-29203)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1027">AVID-2026-R1027</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation causes denial of service in TensorFlow via `Conv3DBackpropFilterV2` (CVE-2022-29204)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1028">AVID-2026-R1028</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault due to missing support for quantized types in TensorFlow (CVE-2022-29205)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1029">AVID-2026-R1029</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing validation results in undefined behavior in `SparseTensorDenseAdd` in TensorFlow (CVE-2022-29206)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1030">AVID-2026-R1030</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Undefined behavior when users supply invalid resource handles in TensorFlow (CVE-2022-29207)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1031">AVID-2026-R1031</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault and Out-of-bounds Write write due to incomplete validation in TensorFlow (CVE-2022-29208)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1032">AVID-2026-R1032</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Type confusion leading to `CHECK`-failure based denial of service in TensorFlow (CVE-2022-29209)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1033">AVID-2026-R1033</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow due to incorrect hash function in TensorFlow (CVE-2022-29210)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1034">AVID-2026-R1034</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in TensorFlow if `tf.histogram_fixed_width` is called with NaN values (CVE-2022-29211)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1035">AVID-2026-R1035</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Core dump when loading TFLite models with quantization in TensorFlow (CVE-2022-29212)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1036">AVID-2026-R1036</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Incomplete validation in signal ops leads to crashes in TensorFlow (CVE-2022-29213)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1037">AVID-2026-R1037</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Code injection in `saved_model_cli` in TensorFlow (CVE-2022-29216)</td><td>Advisory</td><td>2022-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1038">AVID-2026-R1038</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Key confusion through non-blocklisted public key formats in PyJWT (CVE-2022-29217)</td><td>Advisory</td><td>2022-05-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1039">AVID-2026-R1039</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Forced Browsing in Jupyter Notebook (CVE-2022-29238)</td><td>Advisory</td><td>2022-06-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1040">AVID-2026-R1040</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TIBCO Statistica Reflected Cross Site Scripting (XSS) Vulnerability (CVE-2022-30575)</td><td>Advisory</td><td>2022-08-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1041">AVID-2026-R1041</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-30882</td><td>Advisory</td><td>2022-06-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1042">AVID-2026-R1042</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Server-Side Request Forgery Vulnerability in Computer Vision Annotation Tool (CVAT) (CVE-2022-31188)</td><td>Advisory</td><td>2022-08-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1043">AVID-2026-R1043</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-31523</td><td>Advisory</td><td>2022-07-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1044">AVID-2026-R1044</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-31616</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1045">AVID-2026-R1045</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Puppetlabs-mysql Command Injection (CVE-2022-3276)</td><td>Advisory</td><td>2022-10-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1046">AVID-2026-R1046</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-32997</td><td>Advisory</td><td>2022-06-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1047">AVID-2026-R1047</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-33002</td><td>Advisory</td><td>2022-06-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1048">AVID-2026-R1048</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper authentication in Qualcomm IPC (CVE-2022-33242)</td><td>Advisory</td><td>2023-03-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1049">AVID-2026-R1049</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar C++/Python OAuth Clients prior to 3.0.0 were vulnerable to an MITM attack due to Disabled Certificate Validation (CVE-2022-33684)</td><td>Advisory</td><td>2022-11-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1050">AVID-2026-R1050</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Spark shell command injection vulnerability via Spark UI (CVE-2022-33891)</td><td>Advisory</td><td>2022-07-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1051">AVID-2026-R1051</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-34061</td><td>Advisory</td><td>2022-06-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1052">AVID-2026-R1052</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar: Improper Authentication for Pulsar Proxy Statistics Endpoint (CVE-2022-34321)</td><td>Advisory</td><td>2024-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1053">AVID-2026-R1053</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-34665</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1054">AVID-2026-R1054</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-34667</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1055">AVID-2026-R1055</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-34668</td><td>Advisory</td><td>2022-08-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1056">AVID-2026-R1056</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-34676</td><td>Advisory</td><td>2022-12-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1057">AVID-2026-R1057</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-34982</td><td>Advisory</td><td>2022-07-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1058">AVID-2026-R1058</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Streamlit directory traversal vulnerability (CVE-2022-35918)</td><td>Advisory</td><td>2022-08-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1059">AVID-2026-R1059</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">False positive signature verification in cosign (CVE-2022-35929)</td><td>Advisory</td><td>2022-08-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1060">AVID-2026-R1060</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` failure in tf.reshape in Tensorflow (CVE-2022-35934)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1061">AVID-2026-R1061</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` failure in `SobolSample` via missing validation in TensorFlow (CVE-2022-35935)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1062">AVID-2026-R1062</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OOB read in `Gather_nd` op in TensorFlow Lite (CVE-2022-35937)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1063">AVID-2026-R1063</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OOB read in `Gather_nd` op in TensorFlow Lite Micro (CVE-2022-35938)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1064">AVID-2026-R1064</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds write in `scatter_nd` op in TensorFlow Lite (CVE-2022-35939)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1065">AVID-2026-R1065</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Int overflow in `RaggedRangeOp` in Tensoflow (CVE-2022-35940)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1066">AVID-2026-R1066</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` failure in `AvgPoolOp` in Tensorflow (CVE-2022-35941)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1067">AVID-2026-R1067</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` failures in `UnbatchGradOp` in TensorFlow (CVE-2022-35952)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1068">AVID-2026-R1068</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` failures in `AvgPool3DGrad` in TensorFlow (CVE-2022-35959)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1069">AVID-2026-R1069</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` failure in `TensorListReserve` in TensorFlow (CVE-2022-35960)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1070">AVID-2026-R1070</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` failures in `FractionalAvgPoolGrad` in TensorFlow (CVE-2022-35963)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1071">AVID-2026-R1071</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `BlockLSTMGradV2` in TensorFlow (CVE-2022-35964)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1072">AVID-2026-R1072</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `LowerBound` and `UpperBound` in TensorFlow (CVE-2022-35965)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1073">AVID-2026-R1073</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `QuantizedAvgPool` in TensorFlow (CVE-2022-35966)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1074">AVID-2026-R1074</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `QuantizedAdd` in TensorFlow (CVE-2022-35967)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1075">AVID-2026-R1075</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `AvgPoolGrad` in TensorFlow (CVE-2022-35968)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1076">AVID-2026-R1076</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `Conv2DBackpropInput` in TensorFlow (CVE-2022-35969)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1077">AVID-2026-R1077</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `QuantizedInstanceNorm` in TensorFlow (CVE-2022-35970)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1078">AVID-2026-R1078</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `FakeQuantWithMinMaxVars` in TensorFlow (CVE-2022-35971)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1079">AVID-2026-R1079</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `QuantizedBiasAdd` in TensorFlow (CVE-2022-35972)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1080">AVID-2026-R1080</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `QuantizedMatMul` in TensorFlow (CVE-2022-35973)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1081">AVID-2026-R1081</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `QuantizedRelu` and `QuantizedRelu6` (CVE-2022-35979)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1082">AVID-2026-R1082</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `FractionalMaxPoolGrad` in TensorFlow (CVE-2022-35981)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1083">AVID-2026-R1083</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `SparseBincount` in TensorFlow (CVE-2022-35982)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1084">AVID-2026-R1084</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `Save` and `SaveSlices` in TensorFlow (CVE-2022-35983)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1085">AVID-2026-R1085</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `ParameterizedTruncatedNormal` in TensorFlow (CVE-2022-35984)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1086">AVID-2026-R1086</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `LRNGrad` in TensorFlow (CVE-2022-35985)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1087">AVID-2026-R1087</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `RaggedBincount` in TensorFlow (CVE-2022-35986)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1088">AVID-2026-R1088</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `DenseBincount` in TensorFlow (CVE-2022-35987)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1089">AVID-2026-R1089</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `MaxPool` in TensorFlow (CVE-2022-35989)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1090">AVID-2026-R1090</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `FakeQuantWithMinMaxVarsPerChannelGradient` in TensorFlow (CVE-2022-35990)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1091">AVID-2026-R1091</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `TensorListScatter` and `TensorListScatterV2` in TensorFlow (CVE-2022-35991)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1092">AVID-2026-R1092</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `TensorListFromTensor` in TensorFlow (CVE-2022-35992)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1093">AVID-2026-R1093</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `CollectiveGather` in TensorFlow (CVE-2022-35994)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1094">AVID-2026-R1094</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `AudioSummaryV2` in TensorFlow (CVE-2022-35995)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1095">AVID-2026-R1095</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Floating point exception in `Conv2D` in TensorFlow (CVE-2022-35996)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1096">AVID-2026-R1096</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `tf.sparse.cross` in TensorFlow (CVE-2022-35997)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1097">AVID-2026-R1097</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `EmptyTensorList` in TensorFlow (CVE-2022-35998)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1098">AVID-2026-R1098</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `Conv2DBackpropInput` in TensorFlow (CVE-2022-35999)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1099">AVID-2026-R1099</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null dereference on MLIR on empty function attributes in TensorFlow (CVE-2022-36000)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1100">AVID-2026-R1100</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `DrawBoundingBoxes` in TensorFlow (CVE-2022-36001)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1101">AVID-2026-R1101</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `Unbatch` in TensorFlow (CVE-2022-36002)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1102">AVID-2026-R1102</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `RandomPoissonV2` in TensorFlow (CVE-2022-36003)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1103">AVID-2026-R1103</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `tf.random.gamma` in TensorFlow (CVE-2022-36004)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1104">AVID-2026-R1104</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `FakeQuantWithMinMaxVarsGradient` in TensorFlow (CVE-2022-36005)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1105">AVID-2026-R1105</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null dereference on MLIR on empty function attributes in TensorFlow (CVE-2022-36011)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1106">AVID-2026-R1106</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Assertion fail on MLIR empty edge names in TensorFlow (CVE-2022-36012)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1107">AVID-2026-R1107</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null-dereference in `mlir::tfg::GraphDefImporter::ConvertNodeDef` in TensorFlow (CVE-2022-36013)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1108">AVID-2026-R1108</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null-dereference in `mlir::tfg::TFOp::nameAttr` in TensorFlow (CVE-2022-36014)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1109">AVID-2026-R1109</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Integer overflow in math ops in TensorFlow (CVE-2022-36015)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1110">AVID-2026-R1110</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK`-fail in `tensorflow::full_type::SubstituteFromAttrs` in TensorFlow (CVE-2022-36016)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1111">AVID-2026-R1111</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `Requantize` in TensorFlow (CVE-2022-36017)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1112">AVID-2026-R1112</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `FakeQuantWithMinMaxVarsPerChannel` in TensorFlow (CVE-2022-36019)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1113">AVID-2026-R1113</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Some Deeplearning4J packages use unclaimed s3 bucket in tests and examples (CVE-2022-36022)</td><td>Advisory</td><td>2022-11-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1114">AVID-2026-R1114</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault TFLite converter on per-channel quantized transposed convolutions in TensorFlow (CVE-2022-36027)</td><td>Advisory</td><td>2022-09-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1115">AVID-2026-R1115</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerabilities with blob verification in sigstore cosign (CVE-2022-36056)</td><td>Advisory</td><td>2022-09-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1116">AVID-2026-R1116</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Extracting malicious crates can fill the file system (CVE-2022-36114)</td><td>Advisory</td><td>2022-09-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1117">AVID-2026-R1117</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Calcite Avatica JDBC driver `httpclient_impl` connection property can be used as an RCE vector (CVE-2022-36364)</td><td>Advisory</td><td>2022-07-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1118">AVID-2026-R1118</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Cloud Pak for Data file upload (CVE-2022-36769)</td><td>Advisory</td><td>2023-04-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1119">AVID-2026-R1119</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Docker Provider <3.0 RCE vulnerability in example dag (CVE-2022-38362)</td><td>Advisory</td><td>2022-08-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1120">AVID-2026-R1120</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Pinot provider allowed Command Injection (CVE-2022-38649)</td><td>Advisory</td><td>2022-11-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1121">AVID-2026-R1121</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-38881</td><td>Advisory</td><td>2022-09-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1122">AVID-2026-R1122</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Python-jwt subject to Authentication Bypass by Spoofing (CVE-2022-39227)</td><td>Advisory</td><td>2022-09-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1123">AVID-2026-R1123</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Execution with Unnecessary Privileges in JupyterApp (CVE-2022-39286)</td><td>Advisory</td><td>2022-10-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1124">AVID-2026-R1124</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Dependency-Track vulnerable to logging of API keys in clear text when handling API requests using keys with insufficient permissions (CVE-2022-39351)</td><td>Advisory</td><td>2022-10-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1125">AVID-2026-R1125</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Fluentd vulnerable to remote code execution due to insecure deserialization (in non-default configuration) (CVE-2022-39379)</td><td>Advisory</td><td>2022-11-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1126">AVID-2026-R1126</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airlfow Pig Provider RCE (CVE-2022-40189)</td><td>Advisory</td><td>2022-11-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1127">AVID-2026-R1127</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-40432</td><td>Advisory</td><td>2022-09-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1128">AVID-2026-R1128</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-40808</td><td>Advisory</td><td>2022-09-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1129">AVID-2026-R1129</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-40811</td><td>Advisory</td><td>2022-09-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1130">AVID-2026-R1130</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Spark Provider RCE that bypass restrictions to read arbitrary files (CVE-2022-40954)</td><td>Advisory</td><td>2022-11-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1131">AVID-2026-R1131</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-41237</td><td>Advisory</td><td>2022-09-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1132">AVID-2026-R1132</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson Knowledge Catalog on Cloud Pak SQL injection (CVE-2022-41731)</td><td>Advisory</td><td>2023-02-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1133">AVID-2026-R1133</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ThreadUnsafeUnigramCandidateSampler Heap out of bounds in Tensorflow (CVE-2022-41880)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1134">AVID-2026-R1134</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds segmentation fault due to unequal op inputs in Tensorflow (CVE-2022-41883)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1135">AVID-2026-R1135</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Seg fault in `ndarray_tensor_bridge` due to zero and large inputs in Tensorflow (CVE-2022-41884)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1136">AVID-2026-R1136</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow in `FusedResizeAndPadConv2D` in Tensorflow (CVE-2022-41885)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1137">AVID-2026-R1137</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow in `ImageProjectiveTransformV2` in Tensorflow (CVE-2022-41886)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1138">AVID-2026-R1138</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow in `tf.keras.losses.poisson` in Tensorflow (CVE-2022-41887)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1139">AVID-2026-R1139</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unckecked rank size in `tf.image.generate_bounding_box_proposals` in Tensorflow (CVE-2022-41888)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1140">AVID-2026-R1140</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault via invalid attributes in `pywrap_tfe_src.cc` in Tensorflow (CVE-2022-41889)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1141">AVID-2026-R1141</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail in `BCast` overflow in Tensorflow (CVE-2022-41890)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1142">AVID-2026-R1142</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `tf.raw_ops.TensorListConcat` in Tensorflow (CVE-2022-41891)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1143">AVID-2026-R1143</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK_EQ` fail in `tf.raw_ops.TensorListResize` in Tensorflow (CVE-2022-41893)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1144">AVID-2026-R1144</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Buffer overflow in `CONV_3D_TRANSPOSE` on TFLite (CVE-2022-41894)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1145">AVID-2026-R1145</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`MirrorPadGrad` heap out of bounds read in Tensorflow (CVE-2022-41895)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1146">AVID-2026-R1146</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`tf.raw_ops.Mfcc` crashes in Tensorflow (CVE-2022-41896)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1147">AVID-2026-R1147</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`FractionalMaxPoolGrad` Heap out of bounds read in Tensorflow (CVE-2022-41897)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1148">AVID-2026-R1148</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail via inputs in `SparseFillEmptyRowsGrad` in Tensorflow (CVE-2022-41898)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1149">AVID-2026-R1149</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail via inputs in `SdcaOptimizer` in Tensorflow (CVE-2022-41899)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1150">AVID-2026-R1150</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FractionalMaxPool and FractionalAVGPool heap out-of-bounds acess in Tensorflow (CVE-2022-41900)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1151">AVID-2026-R1151</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK_EQ` fail via input in `SparseMatrixNNZ` in Tensorflow (CVE-2022-41901)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1152">AVID-2026-R1152</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Out of bounds write in grappler in Tensorflow (CVE-2022-41902)</td><td>Advisory</td><td>2022-12-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1153">AVID-2026-R1153</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Overflow in `ResizeNearestNeighborGrad` in Tensorflow (CVE-2022-41907)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1154">AVID-2026-R1154</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">`CHECK` fail via inputs in `PyFunc` in Tensorflow (CVE-2022-41908)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1155">AVID-2026-R1155</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in `CompositeTensorVariantToComponents` in Tensorflow (CVE-2022-41909)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1156">AVID-2026-R1156</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap out of bounds read in `QuantizeAndDequantizeV2` in Tensorflow (CVE-2022-41910)</td><td>Advisory</td><td>2022-12-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1157">AVID-2026-R1157</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Invalid char to bool conversion when printing a tensor in Tensorflow (CVE-2022-41911)</td><td>Advisory</td><td>2022-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1158">AVID-2026-R1158</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-42036</td><td>Advisory</td><td>2022-10-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1159">AVID-2026-R1159</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-42037</td><td>Advisory</td><td>2022-10-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1160">AVID-2026-R1160</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-42039</td><td>Advisory</td><td>2022-10-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1161">AVID-2026-R1161</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-42041</td><td>Advisory</td><td>2022-10-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1162">AVID-2026-R1162</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-42042</td><td>Advisory</td><td>2022-10-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1163">AVID-2026-R1163</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-42044</td><td>Advisory</td><td>2022-10-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1164">AVID-2026-R1164</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-42261</td><td>Advisory</td><td>2022-12-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1165">AVID-2026-R1165</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-44054</td><td>Advisory</td><td>2022-11-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1166">AVID-2026-R1166</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-45907</td><td>Advisory</td><td>2022-11-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1167">AVID-2026-R1167</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-45908</td><td>Advisory</td><td>2022-11-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1168">AVID-2026-R1168</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Hive Provider: Hive Provider RCE vulnerability with hive_cli_params (CVE-2022-46421)</td><td>Advisory</td><td>2022-12-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1169">AVID-2026-R1169</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: Security vulnerability on AirFlow Connections (CVE-2022-46651)</td><td>Advisory</td><td>2023-07-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1170">AVID-2026-R1170</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-46741</td><td>Advisory</td><td>2022-12-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1171">AVID-2026-R1171</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2022-46742</td><td>Advisory</td><td>2022-12-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1172">AVID-2026-R1172</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deserializing compromised object with MongoDB .NET/C# Driver may cause remote code execution (CVE-2022-48282)</td><td>Advisory</td><td>2023-02-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1173">AVID-2026-R1173</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-0189</td><td>Advisory</td><td>2023-04-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1174">AVID-2026-R1174</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-0193</td><td>Advisory</td><td>2023-03-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1175">AVID-2026-R1175</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-0196</td><td>Advisory</td><td>2023-03-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1176">AVID-2026-R1176</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Absolute Path Traversal in mlflow/mlflow (CVE-2023-1176)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1177">AVID-2026-R1177</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ChatBot < 4.4.9 - Subscriber+ OpenAI Settings Update to Stored XSS (CVE-2023-1651)</td><td>Advisory</td><td>2023-05-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1178">AVID-2026-R1178</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-22355</td><td>Advisory</td><td>2023-05-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1179">AVID-2026-R1179</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Jena: Exposure of arbitrary execution in script engine expressions. (CVE-2023-22665)</td><td>Advisory</td><td>2023-04-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1180">AVID-2026-R1180</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow JDBC Provider: RCE Vulnerability (CVE-2023-22886)</td><td>Advisory</td><td>2023-06-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1181">AVID-2026-R1181</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure Machine Learning Compute Instance Information Disclosure Vulnerability (CVE-2023-23382)</td><td>Advisory</td><td>2023-02-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1182">AVID-2026-R1182</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Relative Path Traversal in mlflow/mlflow (CVE-2023-2356)</td><td>Advisory</td><td>2023-04-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1183">AVID-2026-R1183</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">vantage6's Pickle serialization is insecure (CVE-2023-23930)</td><td>Advisory</td><td>2023-10-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1184">AVID-2026-R1184</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-25510</td><td>Advisory</td><td>2023-04-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1185">AVID-2026-R1185</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-25511</td><td>Advisory</td><td>2023-04-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1186">AVID-2026-R1186</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-25512</td><td>Advisory</td><td>2023-04-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1187">AVID-2026-R1187</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-25513</td><td>Advisory</td><td>2023-04-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1188">AVID-2026-R1188</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-25514</td><td>Advisory</td><td>2023-04-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1189">AVID-2026-R1189</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-25517</td><td>Advisory</td><td>2023-07-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1190">AVID-2026-R1190</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-25523</td><td>Advisory</td><td>2023-07-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1191">AVID-2026-R1191</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">JupyterHub's LTI13Authenticator: JWT signature not validated (CVE-2023-25574)</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1192">AVID-2026-R1192</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow vulnerable to Out-of-Bounds Read in GRUBlockCellGrad (CVE-2023-25658)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1193">AVID-2026-R1193</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow vulnerable to Out-of-Bounds Read in DynamicStitch (CVE-2023-25659)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1194">AVID-2026-R1194</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow vulnerable to seg fault in `tf.raw_ops.Print` (CVE-2023-25660)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1195">AVID-2026-R1195</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow vulnerable to integer overflow in EditDistance (CVE-2023-25662)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1196">AVID-2026-R1196</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Null Pointer Error in TensorArrayConcatV2 (CVE-2023-25663)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1197">AVID-2026-R1197</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow vulnerable to Heap Buffer Overflow in AvgPoolGrad (CVE-2023-25664)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1198">AVID-2026-R1198</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Floating Point Exception in AudioSpectrogram (CVE-2023-25666)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1199">AVID-2026-R1199</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow vulnerable to segfault when opening multiframe gif (CVE-2023-25667)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1200">AVID-2026-R1200</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow vulnerable to heap out-of-buffer read in the QuantizeAndDequantize operation (CVE-2023-25668)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1201">AVID-2026-R1201</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Floating Point Exception in AvgPoolGrad with XLA (CVE-2023-25669)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1202">AVID-2026-R1202</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Null Pointer Error in QuantizedMatMulWithBiasAndDequantize (CVE-2023-25670)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1203">AVID-2026-R1203</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has segmentation fault in tfg-translate (CVE-2023-25671)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1204">AVID-2026-R1204</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Null Pointer Error in LookupTableImportV2 (CVE-2023-25672)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1205">AVID-2026-R1205</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Floating Point Exception in TensorListSplit with XLA (CVE-2023-25673)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1206">AVID-2026-R1206</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Null Pointer Error in RandomShuffle with XLA enable (CVE-2023-25674)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1207">AVID-2026-R1207</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Segfault in Bincount with XLA (CVE-2023-25675)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1208">AVID-2026-R1208</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has null dereference on ParallelConcat with XLA (CVE-2023-25676)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1209">AVID-2026-R1209</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Google Provider: Google Cloud Sql Provider Remote Command Execution (CVE-2023-25691)</td><td>Advisory</td><td>2023-02-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1210">AVID-2026-R1210</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Sqoop Apache Airflow Provider Remote Code Execution Vulnerability (CVE-2023-25693)</td><td>Advisory</td><td>2023-02-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1211">AVID-2026-R1211</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Information disclosure in Apache Airflow (CVE-2023-25695)</td><td>Advisory</td><td>2023-03-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1212">AVID-2026-R1212</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AI-Engine < 1.6.83 - Admin+ Stored XSS (CVE-2023-2580)</td><td>Advisory</td><td>2023-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1213">AVID-2026-R1213</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has double free in Fractional(Max/Avg)Pool (CVE-2023-25801)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1214">AVID-2026-R1214</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ReportPortal DoS vulnerability on creating a Launch with too many recursively nested elements (CVE-2023-25822)</td><td>Advisory</td><td>2023-10-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1215">AVID-2026-R1215</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Gradio contains Use of Hard-coded Credentials (CVE-2023-25823)</td><td>Advisory</td><td>2023-02-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1216">AVID-2026-R1216</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow AWS Provider: Arbitrary file read via AWS provider (CVE-2023-25956)</td><td>Advisory</td><td>2023-02-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1217">AVID-2026-R1217</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenCV wechat_qrcode Module decoded_bit_stream_parser.cpp decodeHanziSegment memory leak (CVE-2023-2618)</td><td>Advisory</td><td>2023-05-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1218">AVID-2026-R1218</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-26263</td><td>Advisory</td><td>2023-04-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1219">AVID-2026-R1219</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson CP4D Data Stores file modificiation (CVE-2023-26282)</td><td>Advisory</td><td>2024-03-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1220">AVID-2026-R1220</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache EventMesh RabbitMQ-Connector plugin allows RCE through deserialization of untrusted data (CVE-2023-26512)</td><td>Advisory</td><td>2023-07-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1221">AVID-2026-R1221</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson CP4D Data Stores information disclosure (CVE-2023-27291)</td><td>Advisory</td><td>2024-03-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1222">AVID-2026-R1222</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-27506</td><td>Advisory</td><td>2023-08-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1223">AVID-2026-R1223</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson CP4D Data Stores denial of service (CVE-2023-27540)</td><td>Advisory</td><td>2023-07-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1224">AVID-2026-R1224</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson CloudPak for Data Data Stores information disclosure (CVE-2023-27545)</td><td>Advisory</td><td>2024-02-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1225">AVID-2026-R1225</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow has Floating Point Exception in TFLite in conv kernel (CVE-2023-27579)</td><td>Advisory</td><td>2023-03-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1226">AVID-2026-R1226</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Sqoop Provider: Airflow Sqoop Provider RCE Vulnerability (CVE-2023-27604)</td><td>Advisory</td><td>2023-08-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1227">AVID-2026-R1227</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insecure Temporary File in huggingface/transformers (CVE-2023-2800)</td><td>Advisory</td><td>2023-05-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1228">AVID-2026-R1228</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-28380</td><td>Advisory</td><td>2023-08-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1229">AVID-2026-R1229</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-28405</td><td>Advisory</td><td>2023-08-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1230">AVID-2026-R1230</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson CP4D Data Stores improper input validation (CVE-2023-28512)</td><td>Advisory</td><td>2024-03-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1231">AVID-2026-R1231</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Hive Provider Beeline Remote Command Execution (CVE-2023-28706)</td><td>Advisory</td><td>2023-04-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1232">AVID-2026-R1232</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Spark Provider Arbitrary File Read via JDBC (CVE-2023-28710)</td><td>Advisory</td><td>2023-04-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1233">AVID-2026-R1233</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Linkis DatasourceManager module has a deserialization command execution (CVE-2023-29216)</td><td>Advisory</td><td>2023-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1234">AVID-2026-R1234</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindSpore json_helper.cc UpdateArray memory corruption (CVE-2023-2970)</td><td>Advisory</td><td>2023-05-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1235">AVID-2026-R1235</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-30172</td><td>Advisory</td><td>2023-05-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1236">AVID-2026-R1236</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson Machine Learning on Cloud Pak for Data server-side request forgery (CVE-2023-30444)</td><td>Advisory</td><td>2023-04-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1237">AVID-2026-R1237</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write when Extracting a Remotely retrieved Tarball in mindsdb/mindsdb (CVE-2023-30620)</td><td>Advisory</td><td>2023-04-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1238">AVID-2026-R1238</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-30767</td><td>Advisory</td><td>2024-02-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1239">AVID-2026-R1239</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CVE (CVE-2023-31036)</td><td>Advisory</td><td>2024-01-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1240">AVID-2026-R1240</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">in-toto vulnerable to Configuration Read From Local Directory (CVE-2023-32076)</td><td>Advisory</td><td>2023-05-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1241">AVID-2026-R1241</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Planet's secret file is created with excessive permissions (CVE-2023-32303)</td><td>Advisory</td><td>2023-05-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1242">AVID-2026-R1242</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Sqlite-jdbc vulnerable to remote code execution when JDBC url is attacker controlled (CVE-2023-32697)</td><td>Advisory</td><td>2023-05-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1243">AVID-2026-R1243</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">malformed proposed intoto v0.0.2 entries can cause a panic in Rekor (CVE-2023-33199)</td><td>Advisory</td><td>2023-05-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1244">AVID-2026-R1244</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">S3 credentials included when exporting elyra notebook (CVE-2023-3361)</td><td>Advisory</td><td>2023-10-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1245">AVID-2026-R1245</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TensorFlow segfault in array_ops.upper_bound (CVE-2023-33976)</td><td>Advisory</td><td>2024-07-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1246">AVID-2026-R1246</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Java Deserialization vulnerability in Spring-Kafka When Improperly Configured (CVE-2023-34040)</td><td>Advisory</td><td>2023-08-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1247">AVID-2026-R1247</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Snowflake Python Connector vulnerable to Command Injection (CVE-2023-34233)</td><td>Advisory</td><td>2023-06-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1248">AVID-2026-R1248</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow ODBC Provider: Remote code execution vulnerability (CVE-2023-34395)</td><td>Advisory</td><td>2023-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1249">AVID-2026-R1249</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Hive Provider Beeline RCE with Principal (CVE-2023-35797)</td><td>Advisory</td><td>2023-07-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1250">AVID-2026-R1250</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Dependency cache path traversal in Gradle (CVE-2023-35946)</td><td>Advisory</td><td>2023-06-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1251">AVID-2026-R1251</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Visual Studio Code Jupyter Extension Spoofing Vulnerability (CVE-2023-36018)</td><td>Advisory</td><td>2023-11-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1252">AVID-2026-R1252</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-36189</td><td>Advisory</td><td>2023-07-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1253">AVID-2026-R1253</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-36281</td><td>Advisory</td><td>2023-08-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1254">AVID-2026-R1254</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure Identity SDK Remote Code Execution Vulnerability (CVE-2023-36414)</td><td>Advisory</td><td>2023-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1255">AVID-2026-R1255</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AWS data.all vulnerable to RCE through user injection of Python Commands (CVE-2023-36467)</td><td>Advisory</td><td>2023-06-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1256">AVID-2026-R1256</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: Exposure of sensitive connection information, DOS and SSRF on "test connection" feature (CVE-2023-37379)</td><td>Advisory</td><td>2023-08-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1257">AVID-2026-R1257</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar Function Worker: Incorrect Authorization for Function Worker Can Leak Sink/Source Credentials (CVE-2023-37579)</td><td>Advisory</td><td>2023-07-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1258">AVID-2026-R1258</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Absolute Path Traversal in mlflow/mlflow (CVE-2023-3765)</td><td>Advisory</td><td>2023-07-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1259">AVID-2026-R1259</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-38669</td><td>Advisory</td><td>2023-07-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1260">AVID-2026-R1260</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in paddle.flip (CVE-2023-38670)</td><td>Advisory</td><td>2023-07-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1261">AVID-2026-R1261</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in paddle.trace (CVE-2023-38671)</td><td>Advisory</td><td>2023-07-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1262">AVID-2026-R1262</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in paddle.nanmedian (CVE-2023-38674)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1263">AVID-2026-R1263</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in paddle.linalg.matrix_rank (CVE-2023-38675)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1264">AVID-2026-R1264</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in paddle.dot (CVE-2023-38676)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1265">AVID-2026-R1265</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in paddle.linalg.eig (CVE-2023-38677)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1266">AVID-2026-R1266</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindsDB 'Call to requests with verify=False disabling SSL certificate checks, security issue.' issue (CVE-2023-38699)</td><td>Advisory</td><td>2023-08-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1267">AVID-2026-R1267</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-38976</td><td>Advisory</td><td>2023-08-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1268">AVID-2026-R1268</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Avro Java SDK: Memory when deserializing untrusted data in Avro Java SDK (CVE-2023-39410)</td><td>Advisory</td><td>2023-09-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1269">AVID-2026-R1269</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-39659</td><td>Advisory</td><td>2023-08-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1270">AVID-2026-R1270</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-39660</td><td>Advisory</td><td>2023-08-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1271">AVID-2026-R1271</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-39662</td><td>Advisory</td><td>2023-08-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1272">AVID-2026-R1272</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Open Redirect Vulnerability in jupyter-server (CVE-2023-39968)</td><td>Advisory</td><td>2023-08-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1273">AVID-2026-R1273</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Spark Provider Deserialization Vulnerability RCE (CVE-2023-40195)</td><td>Advisory</td><td>2023-08-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1274">AVID-2026-R1274</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow Spark Provider Arbitrary File Read via JDBC (CVE-2023-40272)</td><td>Advisory</td><td>2023-08-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1275">AVID-2026-R1275</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OS Command Injection in mlflow/mlflow (CVE-2023-4033)</td><td>Advisory</td><td>2023-08-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1276">AVID-2026-R1276</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson CP4D Data Stores information disclosure (CVE-2023-40694)</td><td>Advisory</td><td>2024-05-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1277">AVID-2026-R1277</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in Custom Integration Upload in Fides (CVE-2023-41319)</td><td>Advisory</td><td>2023-09-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1278">AVID-2026-R1278</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-41626</td><td>Advisory</td><td>2023-09-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1279">AVID-2026-R1279</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: Improper access control to DAG resources (CVE-2023-42792)</td><td>Advisory</td><td>2023-10-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1280">AVID-2026-R1280</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TorchServe Server-Side Request Forgery (CVE-2023-43654)</td><td>Advisory</td><td>2023-09-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1281">AVID-2026-R1281</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Trojan Lockfilein pdm (CVE-2023-45805)</td><td>Advisory</td><td>2023-10-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1282">AVID-2026-R1282</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">D-Tale vulnerable to Remote Code Execution through the Custom Filter Input (CVE-2023-46134)</td><td>Advisory</td><td>2023-10-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1283">AVID-2026-R1283</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-46229</td><td>Advisory</td><td>2023-10-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1284">AVID-2026-R1284</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Submarine: Fix CVE-2022-1471 SnakeYaml unsafe deserialization (CVE-2023-46302)</td><td>Advisory</td><td>2023-11-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1285">AVID-2026-R1285</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-46492</td><td>Advisory</td><td>2023-11-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1286">AVID-2026-R1286</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Elasticsearch-hadoop Unsafe Deserialization (CVE-2023-46674)</td><td>Advisory</td><td>2023-12-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1287">AVID-2026-R1287</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow missing fix for CVE-2023-40611 in 2.7.1 (DAG run broken access) (CVE-2023-47037)</td><td>Advisory</td><td>2023-11-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1288">AVID-2026-R1288</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Object Relational Mapper Leak Vulnerability in Filtering Task in Label Studio (CVE-2023-47117)</td><td>Advisory</td><td>2023-11-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1289">AVID-2026-R1289</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyArrow, PyArrow: Arbitrary code execution when loading a malicious data file (CVE-2023-47248)</td><td>Advisory</td><td>2023-11-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1290">AVID-2026-R1290</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Inconsistent interpretation of `Content-Length` vs. `Transfer-Encoding` in aiohttp (CVE-2023-47641)</td><td>Advisory</td><td>2023-11-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1291">AVID-2026-R1291</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-48022</td><td>Advisory</td><td>2023-11-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1292">AVID-2026-R1292</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-48023</td><td>Advisory</td><td>2023-11-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1293">AVID-2026-R1293</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: Improper access control to DAG resources (CVE-2023-48291)</td><td>Advisory</td><td>2023-12-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1294">AVID-2026-R1294</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TorchServe ZipSlip (CVE-2023-48299)</td><td>Advisory</td><td>2023-11-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1295">AVID-2026-R1295</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Authentication Bypass by Primary Weakness in mintplex-labs/anything-llm (CVE-2023-4898)</td><td>Advisory</td><td>2023-09-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1296">AVID-2026-R1296</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SQL Injection in mintplex-labs/anything-llm (CVE-2023-4899)</td><td>Advisory</td><td>2023-09-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1297">AVID-2026-R1297</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unsafe YAML deserialization in PyDrive2 (CVE-2023-49297)</td><td>Advisory</td><td>2023-12-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1298">AVID-2026-R1298</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindsDB Server-Side Request Forgery vulnerability (CVE-2023-49795)</td><td>Advisory</td><td>2023-12-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1299">AVID-2026-R1299</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindsDB Arbitrary File Write vulnerability (CVE-2023-49796)</td><td>Advisory</td><td>2023-12-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1300">AVID-2026-R1300</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-50447</td><td>Advisory</td><td>2024-01-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1301">AVID-2026-R1301</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindsDB has arbitrary file write in file.py (CVE-2023-50731)</td><td>Advisory</td><td>2023-12-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1302">AVID-2026-R1302</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress AI Engine plugin <= 1.9.98 - Unauthenticated Arbitrary File Upload vulnerability (CVE-2023-51409)</td><td>Advisory</td><td>2024-04-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1303">AVID-2026-R1303</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar: Timing attack in SASL token signature verification (CVE-2023-51437)</td><td>Advisory</td><td>2024-02-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1304">AVID-2026-R1304</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Make the `/file` secure against file traversal attacks (CVE-2023-51449)</td><td>Advisory</td><td>2023-12-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1305">AVID-2026-R1305</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in paddle.nextafter (CVE-2023-52302)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1306">AVID-2026-R1306</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Segfault in paddle.put_along_axis (CVE-2023-52303)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1307">AVID-2026-R1307</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stack overflow in paddle.searchsorted (CVE-2023-52304)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1308">AVID-2026-R1308</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in paddle.topk (CVE-2023-52305)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1309">AVID-2026-R1309</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in paddle.lerp (CVE-2023-52306)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1310">AVID-2026-R1310</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stack overflow in paddle.linalg.lu_unpack (CVE-2023-52307)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1311">AVID-2026-R1311</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in paddle.amin (CVE-2023-52308)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1312">AVID-2026-R1312</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Heap buffer overflow in paddle.repeat_interleave (CVE-2023-52309)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1313">AVID-2026-R1313</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command injection in get_online_pass_interval (CVE-2023-52310)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1314">AVID-2026-R1314</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command injection in _wget_download (CVE-2023-52311)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1315">AVID-2026-R1315</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Null pointer dereference in paddle.crop (CVE-2023-52312)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1316">AVID-2026-R1316</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">FPE in paddle.argmin and paddle.argmax (CVE-2023-52313)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1317">AVID-2026-R1317</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command injection in convert_shape_compare (CVE-2023-52314)</td><td>Advisory</td><td>2024-01-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1318">AVID-2026-R1318</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-5241</td><td>Advisory</td><td>2023-10-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1319">AVID-2026-R1319</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Using MLeap for loading a saved model (zip archive) can lead to path traversal/arbitrary file creation and possibly remote code execution. (CVE-2023-5245)</td><td>Advisory</td><td>2023-11-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1320">AVID-2026-R1320</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2023-5534</td><td>Advisory</td><td>2023-10-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1321">AVID-2026-R1321</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">H2O Local File Include (CVE-2023-6013)</td><td>Advisory</td><td>2023-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1322">AVID-2026-R1322</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">H2O Remote Code Execution via POJO Model Import (CVE-2023-6016)</td><td>Advisory</td><td>2023-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1323">AVID-2026-R1323</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MLflow Arbitrary File Write (CVE-2023-6018)</td><td>Advisory</td><td>2023-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1324">AVID-2026-R1324</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Ray Command Injection in cpu_profile Parameter (CVE-2023-6019)</td><td>Advisory</td><td>2023-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1325">AVID-2026-R1325</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Ray Log File Local File Include (CVE-2023-6021)</td><td>Advisory</td><td>2023-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1326">AVID-2026-R1326</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cross-Site Request Forgery (CSRF) in prefecthq/prefect (CVE-2023-6022)</td><td>Advisory</td><td>2023-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1327">AVID-2026-R1327</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Reflected XSS via Content-Type Header in mlflow/mlflow (CVE-2023-6568)</td><td>Advisory</td><td>2023-12-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1328">AVID-2026-R1328</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">External Control of File Name or Path in h2oai/h2o-3 (CVE-2023-6569)</td><td>Advisory</td><td>2023-12-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1329">AVID-2026-R1329</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Server-Side Request Forgery (SSRF) in kubeflow/kubeflow (CVE-2023-6570)</td><td>Advisory</td><td>2023-12-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1330">AVID-2026-R1330</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cross-site Scripting (XSS) - Reflected in kubeflow/kubeflow (CVE-2023-6571)</td><td>Advisory</td><td>2023-12-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1331">AVID-2026-R1331</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in mlflow/mlflow (CVE-2023-6753)</td><td>Advisory</td><td>2023-12-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1332">AVID-2026-R1332</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cross-site Scripting (XSS) - Stored in allegroai/clearml-server (CVE-2023-6778)</td><td>Advisory</td><td>2023-12-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1333">AVID-2026-R1333</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal: '\..ilename' in mlflow/mlflow (CVE-2023-6831)</td><td>Advisory</td><td>2023-12-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1334">AVID-2026-R1334</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal: '\..ilename' in mlflow/mlflow (CVE-2023-6909)</td><td>Advisory</td><td>2023-12-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1335">AVID-2026-R1335</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command Injection (CVE-2023-6940)</td><td>Advisory</td><td>2023-12-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1336">AVID-2026-R1336</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Server-Side Request Forgery (SSRF) (CVE-2023-6974)</td><td>Advisory</td><td>2023-12-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1337">AVID-2026-R1337</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unrestricted Upload of File with Dangerous Type (CVE-2023-6976)</td><td>Advisory</td><td>2023-12-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1338">AVID-2026-R1338</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deserialization of Untrusted Data in huggingface/transformers (CVE-2023-7018)</td><td>Advisory</td><td>2023-12-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1339">AVID-2026-R1339</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0072</td><td>Advisory</td><td>2024-04-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1340">AVID-2026-R1340</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0076</td><td>Advisory</td><td>2024-04-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1341">AVID-2026-R1341</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CVE (CVE-2024-0087)</td><td>Advisory</td><td>2024-05-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1342">AVID-2026-R1342</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CVE (CVE-2024-0095)</td><td>Advisory</td><td>2024-06-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1343">AVID-2026-R1343</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CVE (CVE-2024-0100)</td><td>Advisory</td><td>2024-05-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1344">AVID-2026-R1344</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0102</td><td>Advisory</td><td>2024-08-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1345">AVID-2026-R1345</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CVE (CVE-2024-0103)</td><td>Advisory</td><td>2024-06-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1346">AVID-2026-R1346</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0109</td><td>Advisory</td><td>2024-08-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R1347">AVID-2026-R1347</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0110</td><td>Advisory</td><td>2024-08-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R1348">AVID-2026-R1348</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0115</td><td>Advisory</td><td>2024-08-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1349">AVID-2026-R1349</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0116</td><td>Advisory</td><td>2024-10-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1350">AVID-2026-R1350</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0125</td><td>Advisory</td><td>2024-10-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1351">AVID-2026-R1351</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0140</td><td>Advisory</td><td>2025-01-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1352">AVID-2026-R1352</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0378</td><td>Advisory</td><td>2024-03-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1353">AVID-2026-R1353</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AI ChatBot <= 5.3.4 - Missing Authorization via openai_file_list_callback (CVE-2024-0451)</td><td>Advisory</td><td>2024-05-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1354">AVID-2026-R1354</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AI ChatBot <= 5.3.4 - Missing Authorization via openai_file_delete_callback (CVE-2024-0453)</td><td>Advisory</td><td>2024-05-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1355">AVID-2026-R1355</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution due to Full Controlled File Write in mlflow/mlflow (CVE-2024-0520)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1356">AVID-2026-R1356</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Download and export of file via default user role (CVE-2024-0551)</td><td>Advisory</td><td>2024-02-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1357">AVID-2026-R1357</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">DeepFaceLab Util.py deserialization (CVE-2024-0654)</td><td>Advisory</td><td>2024-01-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1358">AVID-2026-R1358</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper validation of document removal parameter (CVE-2024-0763)</td><td>Advisory</td><td>2024-02-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1359">AVID-2026-R1359</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0815</td><td>Advisory</td><td>2024-03-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1360">AVID-2026-R1360</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0818</td><td>Advisory</td><td>2024-03-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1361">AVID-2026-R1361</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-0917</td><td>Advisory</td><td>2024-03-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1362">AVID-2026-R1362</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal and OS Command Injection in parisneo/lollms-webui (CVE-2024-10019)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1363">AVID-2026-R1363</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">flairNLP flair Mode File Loader clustering.py ClusteringModel code injection (CVE-2024-10073)</td><td>Advisory</td><td>2024-10-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1364">AVID-2026-R1364</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stored XSS in comfyanonymous/comfyui (CVE-2024-10099)</td><td>Advisory</td><td>2024-10-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1365">AVID-2026-R1365</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in infiniflow/ragflow (CVE-2024-10131)</td><td>Advisory</td><td>2024-10-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1366">AVID-2026-R1366</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unauthenticated Remote Code Execution in ElasticRendezvousHandler in horovod/horovod (CVE-2024-10190)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1367">AVID-2026-R1367</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">chidiwilliams buzz model_loader.py download_model temp file (CVE-2024-10372)</td><td>Advisory</td><td>2024-10-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1368">AVID-2026-R1368</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service by ReDOS in h2oai/h2o-3 (CVE-2024-10549)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1369">AVID-2026-R1369</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service by ReDOS in h2oai/h2o-3 (CVE-2024-10550)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1370">AVID-2026-R1370</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Jdbc Deserialization in h2oai/h2o-3 (CVE-2024-10553)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1371">AVID-2026-R1371</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service and Arbitrary File Write in h2oai/h2o-3 (CVE-2024-10572)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1372">AVID-2026-R1372</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Regular Expression Denial of Service (ReDoS) in gradio-app/gradio (CVE-2024-10624)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1373">AVID-2026-R1373</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in gradio-app/gradio (CVE-2024-10648)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1374">AVID-2026-R1374</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Open Redirect in binary-husky/gpt_academic (CVE-2024-10812)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1375">AVID-2026-R1375</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deserialization of Untrusted Data in binary-husky/gpt_academic (CVE-2024-11039)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1376">AVID-2026-R1376</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Hugging Face Transformers MobileViTV2 Deserialization of Untrusted Data Remote Code Execution Vulnerability (CVE-2024-11392)</td><td>Advisory</td><td>2024-11-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1377">AVID-2026-R1377</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Hugging Face Transformers MaskFormer Model Deserialization of Untrusted Data Remote Code Execution Vulnerability (CVE-2024-11393)</td><td>Advisory</td><td>2024-11-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1378">AVID-2026-R1378</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Hugging Face Transformers Trax Model Deserialization of Untrusted Data Remote Code Execution Vulnerability (CVE-2024-11394)</td><td>Advisory</td><td>2024-11-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1379">AVID-2026-R1379</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CORS Vulnerability in feast-dev/feast (CVE-2024-11602)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1380">AVID-2026-R1380</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Privilege Escalation in langgenius/dify (CVE-2024-11821)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1381">AVID-2026-R1381</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution by Pickle Deserialization in open-mmlab/mmdetection (CVE-2024-12044)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1382">AVID-2026-R1382</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Server-Side Request Forgery in haotian-liu/llava (CVE-2024-12068)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1383">AVID-2026-R1383</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in kedro-org/kedro (CVE-2024-12215)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1384">AVID-2026-R1384</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write via TarSlip in dmlc/gluon-cv (CVE-2024-12216)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1385">AVID-2026-R1385</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Post Saint: ChatGPT, GPT4, DALL-E, Stable Diffusion, Pexels, Dezgo AI Text & Image Generator <= 1.3.1 - Missing Authorization to Authenticated (Subscriber+) Arbitrary File Upload (CVE-2024-12471)</td><td>Advisory</td><td>2025-01-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1386">AVID-2026-R1386</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Regular Expression Denial of Service (ReDoS) in huggingface/transformers (CVE-2024-12720)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1387">AVID-2026-R1387</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Dependency on Vulnerable Third-Party Component exposes Vulnerabilities in NI Vision Software (CVE-2024-12740)</td><td>Advisory</td><td>2025-01-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1388">AVID-2026-R1388</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SQL Injection in the Amazon Redshift Python Connector affecting v2.1.4 (CVE-2024-12745)</td><td>Advisory</td><td>2024-12-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1389">AVID-2026-R1389</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF in langgenius/dify (CVE-2024-12775)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1390">AVID-2026-R1390</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service in aimhubio/aim (CVE-2024-12777)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1391">AVID-2026-R1391</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in mintplex-labs/anything-llm (CVE-2024-13059)</td><td>Advisory</td><td>2025-02-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1392">AVID-2026-R1392</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">DeepFaceLab main.py apply_xseg deserialization (CVE-2024-1432)</td><td>Advisory</td><td>2024-02-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1393">AVID-2026-R1393</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">S3 Bucket Takeover in h2oai/h2o-3 (CVE-2024-1456)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1394">AVID-2026-R1394</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal Vulnerability in mlflow/mlflow (CVE-2024-1483)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1395">AVID-2026-R1395</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal Vulnerability in parisneo/lollms-webui (CVE-2024-1511)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1396">AVID-2026-R1396</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cross-Site Request Forgery (CSRF) Leading to Remote Code Execution in parisneo/lollms-webui (CVE-2024-1522)</td><td>Advisory</td><td>2024-03-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1397">AVID-2026-R1397</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command Injection in gradio-app/gradio via deploy+test-visual.yml workflow (CVE-2024-1540)</td><td>Advisory</td><td>2024-03-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1398">AVID-2026-R1398</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stored XSS leading to RCE in parisneo/lollms-webui (CVE-2024-1602)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1399">AVID-2026-R1399</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">confirmed (CVE-2024-1603)</td><td>Advisory</td><td>2024-03-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1400">AVID-2026-R1400</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Local File Inclusion in gradio-app/gradio (CVE-2024-1728)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1401">AVID-2026-R1401</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CSRF to RCE in significant-gravitas/autogpt (CVE-2024-1879)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1402">AVID-2026-R1402</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Session Reuse Vulnerability in lunary-ai/lunary (CVE-2024-1902)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1403">AVID-2026-R1403</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal leading to Arbitrary File Write and RCE in vertaai/modeldb (CVE-2024-1961)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1404">AVID-2026-R1404</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command Injection in mudler/localai (CVE-2024-2029)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1405">AVID-2026-R1405</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Directory Traversal in zenml-io/zenml (CVE-2024-2083)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1406">AVID-2026-R1406</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure SDK Spoofing Vulnerability (CVE-2024-21421)</td><td>Advisory</td><td>2024-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1407">AVID-2026-R1407</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21485</td><td>Advisory</td><td>2024-02-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1408">AVID-2026-R1408</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21552</td><td>Advisory</td><td>2024-07-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1409">AVID-2026-R1409</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21574</td><td>Advisory</td><td>2024-12-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1410">AVID-2026-R1410</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21577</td><td>Advisory</td><td>2024-12-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1411">AVID-2026-R1411</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote code execution (CVE-2024-21649)</td><td>Advisory</td><td>2024-01-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1412">AVID-2026-R1412</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">vantage6 insecure SSH configuration for node and server containers (CVE-2024-21653)</td><td>Advisory</td><td>2024-01-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1413">AVID-2026-R1413</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21766</td><td>Advisory</td><td>2024-08-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1414">AVID-2026-R1414</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal Vulnerability in parisneo/lollms-webui (CVE-2024-2178)</td><td>Advisory</td><td>2024-06-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1415">AVID-2026-R1415</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21792</td><td>Advisory</td><td>2024-05-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1416">AVID-2026-R1416</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21799</td><td>Advisory</td><td>2024-11-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1417">AVID-2026-R1417</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21802</td><td>Advisory</td><td>2024-02-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1418">AVID-2026-R1418</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21949</td><td>Advisory</td><td>2024-11-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1419">AVID-2026-R1419</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in aimhubio/aim (CVE-2024-2195)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1420">AVID-2026-R1420</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21974</td><td>Advisory</td><td>2024-11-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1421">AVID-2026-R1421</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-21975</td><td>Advisory</td><td>2024-11-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1422">AVID-2026-R1422</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF Vulnerability in gradio-app/gradio (CVE-2024-2206)</td><td>Advisory</td><td>2024-03-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1423">AVID-2026-R1423</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal and Arbitrary File Upload Vulnerability in qdrant/qdrant (CVE-2024-2221)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1424">AVID-2026-R1424</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Spring Cloud Function Web DOS Vulnerability (CVE-2024-22271)</td><td>Advisory</td><td>2024-07-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1425">AVID-2026-R1425</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unsecured endpoints in the jupyter-lsp server extension (CVE-2024-22415)</td><td>Advisory</td><td>2024-01-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1426">AVID-2026-R1426</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-22476</td><td>Advisory</td><td>2024-05-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1427">AVID-2026-R1427</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Client configured with permissive trust policies susceptible to rollback attack in Notary Project (CVE-2024-23332)</td><td>Advisory</td><td>2024-01-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1428">AVID-2026-R1428</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">python-ecdsa vulnerable to Minerva attack on P-256 (CVE-2024-23342)</td><td>Advisory</td><td>2024-01-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1429">AVID-2026-R1429</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-23496</td><td>Advisory</td><td>2024-02-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1430">AVID-2026-R1430</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal leading to Remote Code Execution in parisneo/lollms-webui (CVE-2024-2358)</td><td>Advisory</td><td>2024-05-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1431">AVID-2026-R1431</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Neutralization of Special Elements used in an OS Command in parisneo/lollms-webui (CVE-2024-2359)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1432">AVID-2026-R1432</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-23750</td><td>Advisory</td><td>2024-01-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1433">AVID-2026-R1433</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-23751</td><td>Advisory</td><td>2024-01-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1434">AVID-2026-R1434</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CORS settings overly permissive in vantage6 (CVE-2024-23823)</td><td>Advisory</td><td>2024-03-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1435">AVID-2026-R1435</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Use after free in C++ protobuf (CVE-2024-2410)</td><td>Advisory</td><td>2024-05-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1436">AVID-2026-R1436</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-24590</td><td>Advisory</td><td>2024-02-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1437">AVID-2026-R1437</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-24591</td><td>Advisory</td><td>2024-02-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1438">AVID-2026-R1438</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-24593</td><td>Advisory</td><td>2024-02-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1439">AVID-2026-R1439</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindsDB Vulnerable to Bypass of SSRF Protection with DNS Rebinding (CVE-2024-24759)</td><td>Advisory</td><td>2024-09-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1440">AVID-2026-R1440</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">RedisBloom heap buffer overflow in CF.LOADCHUNK command (CVE-2024-25115)</td><td>Advisory</td><td>2024-04-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1441">AVID-2026-R1441</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-25723</td><td>Advisory</td><td>2024-02-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1442">AVID-2026-R1442</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insufficient sanitization in MLflow leads to XSS when running a recipe that uses an untrusted dataset. (CVE-2024-27133)</td><td>Advisory</td><td>2024-02-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1443">AVID-2026-R1443</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Excessive directory permissions in MLflow leads to local privilege escalation when using spark_udf (CVE-2024-27134)</td><td>Advisory</td><td>2024-11-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1444">AVID-2026-R1444</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar: Improper Input Validation in Pulsar Function Worker allows Remote Code Execution (CVE-2024-27135)</td><td>Advisory</td><td>2024-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1445">AVID-2026-R1445</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar: Pulsar Functions Worker's Archive Extraction Vulnerability Allows Unauthorized File Modification (CVE-2024-27317)</td><td>Advisory</td><td>2024-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1446">AVID-2026-R1446</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-27318</td><td>Advisory</td><td>2024-02-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1447">AVID-2026-R1447</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-27319</td><td>Advisory</td><td>2024-02-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1448">AVID-2026-R1448</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Pulsar: Pulsar Functions Worker Allows Unauthorized File Access and Unauthorized HTTP/HTTPS Proxying (CVE-2024-27894)</td><td>Advisory</td><td>2024-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1449">AVID-2026-R1449</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Jupyter Server Proxy's Websocket Proxying does not require authentication (CVE-2024-28179)</td><td>Advisory</td><td>2024-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1450">AVID-2026-R1450</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">jupyter-scheduler's endpoint is missing authentication (CVE-2024-28188)</td><td>Advisory</td><td>2024-05-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1451">AVID-2026-R1451</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-28950</td><td>Advisory</td><td>2024-11-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1452">AVID-2026-R1452</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-29083</td><td>Advisory</td><td>2024-11-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1453">AVID-2026-R1453</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress AI Engine plugin <= 2.1.4 - Arbitrary File Upload vulnerability (CVE-2024-29100)</td><td>Advisory</td><td>2024-03-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1454">AVID-2026-R1454</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insecure Deserialization Leading to RCE in bentoml/bentoml (CVE-2024-2912)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1455">AVID-2026-R1455</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TarSlip Vulnerability in deepjavalibrary/djl (CVE-2024-2914)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1456">AVID-2026-R1456</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Local File Inclusion (LFI) via URI Fragment Parsing in mlflow/mlflow (CVE-2024-2928)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1457">AVID-2026-R1457</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cosign vulnerable to machine-wide denial of service via malicious artifacts (CVE-2024-29903)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1458">AVID-2026-R1458</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Qdrant Full Snapshot REST API snapshots.rs path traversal (CVE-2024-3078)</td><td>Advisory</td><td>2024-03-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1459">AVID-2026-R1459</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Privilege Escalation via Improper Input Validation in mintplex-labs/anything-llm (CVE-2024-3101)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1460">AVID-2026-R1460</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in mintplex-labs/anything-llm (CVE-2024-3104)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1461">AVID-2026-R1461</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in create_conda_env function in parisneo/lollms (CVE-2024-3121)</td><td>Advisory</td><td>2024-06-24</td></tr>
    <tr><td><a href="/database/AVID-2026-R1462">AVID-2026-R1462</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GPT Academic: Pickle deserializing cookies may pose RCE risk (CVE-2024-31224)</td><td>Advisory</td><td>2024-04-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1463">AVID-2026-R1463</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command Injection in parisneo/lollms-webui (CVE-2024-3126)</td><td>Advisory</td><td>2024-05-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1464">AVID-2026-R1464</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress Copymatic plugin <= 1.6 - Unauthenticated Arbitrary File Upload vulnerability (CVE-2024-31351)</td><td>Advisory</td><td>2024-05-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1465">AVID-2026-R1465</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Privilege Escalation and Local File Inclusion in mintplex-labs/anything-llm (CVE-2024-3152)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1466">AVID-2026-R1466</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-31580</td><td>Advisory</td><td>2024-04-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1467">AVID-2026-R1467</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-31583</td><td>Advisory</td><td>2024-04-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1468">AVID-2026-R1468</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Zeppelin: Remote code execution by adding malicious JDBC connection string (CVE-2024-31864)</td><td>Advisory</td><td>2024-04-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1469">AVID-2026-R1469</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Kohya_ss is vulnerable to a command injection in basic_caption_gui.py (GHSL-2024-019) (CVE-2024-32022)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1470">AVID-2026-R1470</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Kohya_ss vulnerable to path injection in `common_gui.py` `find_and_replace` function (`GHSL-2024-024`) (CVE-2024-32023)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1471">AVID-2026-R1471</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Kohya_ss is vulnerable to a command injection in `group_images_gui.py` (`GHSL-2024-021`) (CVE-2024-32025)</td><td>Advisory</td><td>2024-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1472">AVID-2026-R1472</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in gaizhenbiao/chuanhuchatgpt (CVE-2024-3234)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1473">AVID-2026-R1473</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Use of Uninitialized Variable Vulnerability in llama.cpp (CVE-2024-32878)</td><td>Advisory</td><td>2024-04-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1474">AVID-2026-R1474</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">lobe-chat `/api/proxy` endpoint Server-Side Request Forgery vulnerability (CVE-2024-32964)</td><td>Advisory</td><td>2024-05-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1475">AVID-2026-R1475</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Buffer Over-read in Neural Processing Unit (CVE-2024-33037)</td><td>Advisory</td><td>2024-12-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1476">AVID-2026-R1476</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in parisneo/lollms-webui (CVE-2024-3322)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1477">AVID-2026-R1477</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-33664</td><td>Advisory</td><td>2024-04-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1478">AVID-2026-R1478</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deserialization of Untrusted Data in sagemaker-python-sdk (CVE-2024-34072)</td><td>Advisory</td><td>2024-05-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1479">AVID-2026-R1479</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Command Injection in sagemaker-python-sdk (CVE-2024-34073)</td><td>Advisory</td><td>2024-05-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1480">AVID-2026-R1480</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-34165</td><td>Advisory</td><td>2024-11-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1481">AVID-2026-R1481</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">@cyclonedx/cyclonedx-library Improper Restriction of XML External Entity Reference vulnerability (CVE-2024-34345)</td><td>Advisory</td><td>2024-05-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1482">AVID-2026-R1482</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress AI Engine plugin <= 2.2.63 - Auth. Arbitrary File Upload vulnerability (CVE-2024-34440)</td><td>Advisory</td><td>2024-05-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1483">AVID-2026-R1483</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-34997</td><td>Advisory</td><td>2024-05-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1484">AVID-2026-R1484</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Jupyter server on Windows discloses Windows user password hash (CVE-2024-35178)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1485">AVID-2026-R1485</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TorchServe bypass allowed_urls configuration (CVE-2024-35198)</td><td>Advisory</td><td>2024-07-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1486">AVID-2026-R1486</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TorchServe gRPC Port Exposure (CVE-2024-35199)</td><td>Advisory</td><td>2024-07-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1487">AVID-2026-R1487</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary Code Execution via Deserialization in huggingface/transformers (CVE-2024-3568)</td><td>Advisory</td><td>2024-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1488">AVID-2026-R1488</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in qdrant/qdrant (CVE-2024-3584)</td><td>Advisory</td><td>2024-05-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1489">AVID-2026-R1489</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Submarine Server Core: authorization bypass (CVE-2024-36265)</td><td>Advisory</td><td>2024-06-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1490">AVID-2026-R1490</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-36328</td><td>Advisory</td><td>2025-04-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1491">AVID-2026-R1491</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-36336</td><td>Advisory</td><td>2025-04-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1492">AVID-2026-R1492</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-36732</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1493">AVID-2026-R1493</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-36736</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1494">AVID-2026-R1494</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-36740</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1495">AVID-2026-R1495</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-37014</td><td>Advisory</td><td>2024-06-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1496">AVID-2026-R1496</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-37061</td><td>Advisory</td><td>2024-06-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1497">AVID-2026-R1497</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-37062</td><td>Advisory</td><td>2024-06-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1498">AVID-2026-R1498</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-37288</td><td>Advisory</td><td>2024-09-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1499">AVID-2026-R1499</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress AI Power: Complete AI Pack – Powered by GPT-4 plugin <= 1.8.66 - Cross Site Scripting (XSS) vulnerability (CVE-2024-37465)</td><td>Advisory</td><td>2024-07-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1500">AVID-2026-R1500</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path thraversal in DeepJavaLibrary (CVE-2024-37902)</td><td>Advisory</td><td>2024-06-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1501">AVID-2026-R1501</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-38302</td><td>Advisory</td><td>2024-07-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1502">AVID-2026-R1502</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Restriction of XML External Entity Reference in org.cyclonedx:cyclonedx-core-java (CVE-2024-38374)</td><td>Advisory</td><td>2024-06-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1503">AVID-2026-R1503</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">QNAP AI Core (CVE-2024-38647)</td><td>Advisory</td><td>2024-11-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1504">AVID-2026-R1504</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress AI ENGINE plugin <= 2.4.7 - Server Side Request Forgery (SSRF) vulnerability (CVE-2024-38791)</td><td>Advisory</td><td>2024-08-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1505">AVID-2026-R1505</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">fishaudio/Bert-VITS2 Command Injection in webui_preprocess.py bert_gen function (CVE-2024-39686)</td><td>Advisory</td><td>2024-07-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1506">AVID-2026-R1506</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">fishaudio/Bert-VITS2 Limited File Write in webui_preprocess.py generate_config function (CVE-2024-39688)</td><td>Advisory</td><td>2024-07-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1507">AVID-2026-R1507</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution (RCE) vulnerability in jupyterlab extension template  `update-integration-tests` GitHub Action (CVE-2024-39700)</td><td>Advisory</td><td>2024-07-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1508">AVID-2026-R1508</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-39705</td><td>Advisory</td><td>2024-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1509">AVID-2026-R1509</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: DAG Author Code Execution possibility in airflow-scheduler (CVE-2024-39877)</td><td>Advisory</td><td>2024-07-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1510">AVID-2026-R1510</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-40441</td><td>Advisory</td><td>2024-09-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1511">AVID-2026-R1511</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-40442</td><td>Advisory</td><td>2024-09-23</td></tr>
    <tr><td><a href="/database/AVID-2026-R1512">AVID-2026-R1512</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote code execution in streamlit geospatial in pages/1_📷_Timelapse.py MODIS Ocean Color SMI option palette (CVE-2024-41115)</td><td>Advisory</td><td>2024-07-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1513">AVID-2026-R1513</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote code execution in streamlit geospatial in pages/10_🌍_Earth_Engine_Datasets.py (CVE-2024-41117)</td><td>Advisory</td><td>2024-07-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1514">AVID-2026-R1514</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">streamlit-geospatial remote code execution in pages/8_🏜️_Raster_Data_Visualization.py (CVE-2024-41119)</td><td>Advisory</td><td>2024-07-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1515">AVID-2026-R1515</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">llama.cpp null pointer dereference in gguf_init_from_file (CVE-2024-41130)</td><td>Advisory</td><td>2024-07-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1516">AVID-2026-R1516</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insecure Jinja2 templates rendered in Haystack Components can lead to RCE (CVE-2024-41950)</td><td>Advisory</td><td>2024-07-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R1517">AVID-2026-R1517</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">open-telemetry has an Observable Timing Discrepancy (CVE-2024-42368)</td><td>Advisory</td><td>2024-08-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1518">AVID-2026-R1518</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Streamlit Path Traversal Security Vulnerability on Windows (CVE-2024-42474)</td><td>Advisory</td><td>2024-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1519">AVID-2026-R1519</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">llama.cpp global-buffer-overflow in ggml_type_size (CVE-2024-42477)</td><td>Advisory</td><td>2024-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1520">AVID-2026-R1520</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">llama.cpp allows Arbitrary Address Read in rpc_server::get_tensor (CVE-2024-42478)</td><td>Advisory</td><td>2024-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1521">AVID-2026-R1521</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">llama.cpp allows write-what-where in rpc_server::set_tensor (CVE-2024-42479)</td><td>Advisory</td><td>2024-08-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1522">AVID-2026-R1522</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Secrets Exfiltration in gradio-app/gradio (CVE-2024-4254)</td><td>Advisory</td><td>2024-06-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1523">AVID-2026-R1523</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in berriai/litellm (CVE-2024-4264)</td><td>Advisory</td><td>2024-05-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1524">AVID-2026-R1524</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-42835</td><td>Advisory</td><td>2024-10-31</td></tr>
    <tr><td><a href="/database/AVID-2026-R1525">AVID-2026-R1525</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Lack of login attempt rate-limiting in zenml-io/zenml (CVE-2024-4311)</td><td>Advisory</td><td>2024-11-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1526">AVID-2026-R1526</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution due to LFI in '/install_extension' in parisneo/lollms-webui (CVE-2024-4320)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1527">AVID-2026-R1527</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Server-Side Request Forgery (SSRF) in gradio-app/gradio (CVE-2024-4325)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1528">AVID-2026-R1528</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution via `/apply_settings` and `/execute_code` in parisneo/lollms-webui (CVE-2024-4326)</td><td>Advisory</td><td>2024-05-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1529">AVID-2026-R1529</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">DeepSpeed Remote Code Execution Vulnerability (CVE-2024-43497)</td><td>Advisory</td><td>2024-10-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1530">AVID-2026-R1530</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CSRF in restart_program in parisneo/lollms-webui (CVE-2024-4403)</td><td>Advisory</td><td>2024-06-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1531">AVID-2026-R1531</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Airflow: Authenticated DAG authors could execute code on scheduler nodes (CVE-2024-45034)</td><td>Advisory</td><td>2024-09-07</td></tr>
    <tr><td><a href="/database/AVID-2026-R1532">AVID-2026-R1532</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-45201</td><td>Advisory</td><td>2024-08-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1533">AVID-2026-R1533</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-45758</td><td>Advisory</td><td>2024-09-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1534">AVID-2026-R1534</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-45846</td><td>Advisory</td><td>2024-09-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1535">AVID-2026-R1535</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-45851</td><td>Advisory</td><td>2024-09-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1536">AVID-2026-R1536</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-45857</td><td>Advisory</td><td>2024-09-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1537">AVID-2026-R1537</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Computer Vision Annotation Tool (CVAT) contains a stored XSS via the quality report data endpoint (CVE-2024-47063)</td><td>Advisory</td><td>2024-09-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1538">AVID-2026-R1538</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CORS origin validation is not performed when the request has a cookie in Gradio (CVE-2024-47084)</td><td>Advisory</td><td>2024-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1539">AVID-2026-R1539</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The `is_in_or_equal` function may be bypassed in Gradio (CVE-2024-47164)</td><td>Advisory</td><td>2024-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1540">AVID-2026-R1540</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">One-level read path traversal in `/custom_component` in Gradio (CVE-2024-47166)</td><td>Advisory</td><td>2024-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1541">AVID-2026-R1541</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF in the path parameter of /queue/join in Gradio (CVE-2024-47167)</td><td>Advisory</td><td>2024-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1542">AVID-2026-R1542</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The `enable_monitoring` flag set to `False` does not disable monitoring in Gradio (CVE-2024-47168)</td><td>Advisory</td><td>2024-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1543">AVID-2026-R1543</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Agnai vulnerable to Remote Code Execution via JS Upload using Directory Traversal (CVE-2024-47169)</td><td>Advisory</td><td>2024-09-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1544">AVID-2026-R1544</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Computer Vision Annotation Tool (CVAT) access control is broken in several PATCH endpoints (CVE-2024-47172)</td><td>Advisory</td><td>2024-09-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1545">AVID-2026-R1545</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-47481</td><td>Advisory</td><td>2024-10-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1546">AVID-2026-R1546</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-47483</td><td>Advisory</td><td>2024-10-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1547">AVID-2026-R1547</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Lack of integrity check on the downloaded FRP client in Gradio (CVE-2024-47867)</td><td>Advisory</td><td>2024-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1548">AVID-2026-R1548</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Insecure communication between the FRP client and server in Gradio (CVE-2024-47871)</td><td>Advisory</td><td>2024-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1549">AVID-2026-R1549</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-48052</td><td>Advisory</td><td>2024-11-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1550">AVID-2026-R1550</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-48057</td><td>Advisory</td><td>2024-11-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1551">AVID-2026-R1551</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-48063</td><td>Advisory</td><td>2024-10-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1552">AVID-2026-R1552</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TorchGeo Remote Code Execution Vulnerability (CVE-2024-49048)</td><td>Advisory</td><td>2024-11-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1553">AVID-2026-R1553</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-49194</td><td>Advisory</td><td>2024-12-17</td></tr>
    <tr><td><a href="/database/AVID-2026-R1554">AVID-2026-R1554</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson Studio Local cross-site request forgery (CVE-2024-49340)</td><td>Advisory</td><td>2024-10-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1555">AVID-2026-R1555</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">IBM Watson Speech Services Cartridge for IBM Cloud Pak for Data denial of service (CVE-2024-49353)</td><td>Advisory</td><td>2024-11-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1556">AVID-2026-R1556</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">XSS and Open Redirect via SVG File Upload in parisneo/lollms-webui (CVE-2024-5125)</td><td>Advisory</td><td>2024-11-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1557">AVID-2026-R1557</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in mudler/localai (CVE-2024-5182)</td><td>Advisory</td><td>2024-06-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1558">AVID-2026-R1558</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Overwrite in download_model_with_test_data in onnx/onnx (CVE-2024-5187)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1559">AVID-2026-R1559</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ReDoS in Giskard Scan text perturbation (CVE-2024-52524)</td><td>Advisory</td><td>2024-11-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1560">AVID-2026-R1560</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">LLama Factory Remote OS Command Injection Vulnerability (CVE-2024-52803)</td><td>Advisory</td><td>2024-11-21</td></tr>
    <tr><td><a href="/database/AVID-2026-R1561">AVID-2026-R1561</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Issuer field partial matches allowed in pyjwt (CVE-2024-53861)</td><td>Advisory</td><td>2024-11-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1562">AVID-2026-R1562</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53870</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1563">AVID-2026-R1563</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53872</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1564">AVID-2026-R1564</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53873</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1565">AVID-2026-R1565</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53874</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1566">AVID-2026-R1566</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53875</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1567">AVID-2026-R1567</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53876</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1568">AVID-2026-R1568</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53877</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1569">AVID-2026-R1569</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53878</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1570">AVID-2026-R1570</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53879</td><td>Advisory</td><td>2025-02-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1571">AVID-2026-R1571</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-53880</td><td>Advisory</td><td>2025-02-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1572">AVID-2026-R1572</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress AIKCT Engine Chatbot, ChatGPT, Gemini, GPT-4o Best AI Chatbot plugin <= 1.6.2 - Cross Site Request Forgery (CSRF) vulnerability (CVE-2024-54306)</td><td>Advisory</td><td>2024-12-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1573">AVID-2026-R1573</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">RCE via Property/Class Pollution in lightning-ai/pytorch-lightning (CVE-2024-5452)</td><td>Advisory</td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1574">AVID-2026-R1574</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2024-55459</td><td>Advisory</td><td>2025-01-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1575">AVID-2026-R1575</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">RedisBloom Integer Overflow Remote Code Execution Vulnerability (CVE-2024-55656)</td><td>Advisory</td><td>2025-01-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R1576">AVID-2026-R1576</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">D-Tale allows Remote Code Execution through the Custom Filter Input (CVE-2024-55890)</td><td>Advisory</td><td>2024-12-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1577">AVID-2026-R1577</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MaxKB RCE vulnerability in function library (CVE-2024-56137)</td><td>Advisory</td><td>2025-01-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R1578">AVID-2026-R1578</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Firecrawl has SSRF Vulnerability via malicious scrape target (CVE-2024-56800)</td><td>Advisory</td><td>2024-12-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1579">AVID-2026-R1579</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in BerriAI/litellm (CVE-2024-5751)</td><td>Advisory</td><td>2024-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1580">AVID-2026-R1580</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unprotected WebSocket in stitionai/devika (CVE-2024-5820)</td><td>Advisory</td><td>2024-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1581">AVID-2026-R1581</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service via Invalid Argument in h2oai/h2o-3 (CVE-2024-5979)</td><td>Advisory</td><td>2024-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1582">AVID-2026-R1582</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write via /v1/runs API endpoint in lightning-ai/pytorch-lightning (CVE-2024-5980)</td><td>Advisory</td><td>2024-06-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1583">AVID-2026-R1583</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing client_id in parisneo/lollms-webui (CVE-2024-6040)</td><td>Advisory</td><td>2024-08-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1584">AVID-2026-R1584</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF and Partial LFI in /models/apply Endpoint in mudler/localai (CVE-2024-6095)</td><td>Advisory</td><td>2024-07-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1585">AVID-2026-R1585</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in pypa/setuptools (CVE-2024-6345)</td><td>Advisory</td><td>2024-07-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1586">AVID-2026-R1586</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Overwrite and Data Exfiltration in aimhubio/aim (CVE-2024-6396)</td><td>Advisory</td><td>2024-07-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1587">AVID-2026-R1587</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File/Directory Deletion in aimhubio/aim (CVE-2024-6483)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1588">AVID-2026-R1588</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unclaimed S3 Bucket Usage in pytorch/serve (CVE-2024-6577)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1589">AVID-2026-R1589</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in stangirard/quivr (CVE-2024-6583)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1590">AVID-2026-R1590</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in BerriAI/litellm (CVE-2024-6825)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1591">AVID-2026-R1591</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Overwrite through tarfile-extraction in aimhubio/aim (CVE-2024-6829)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1592">AVID-2026-R1592</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SmartSearchWP < 2.4.6 - Unauthenticated OpenAI Key Disclosure (CVE-2024-6845)</td><td>Advisory</td><td>2024-09-25</td></tr>
    <tr><td><a href="/database/AVID-2026-R1593">AVID-2026-R1593</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Overwrite in h2oai/h2o-3 (CVE-2024-6854)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1594">AVID-2026-R1594</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write in mudler/LocalAI (CVE-2024-6868)</td><td>Advisory</td><td>2024-10-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1595">AVID-2026-R1595</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">JFrog Artifactory Cache Poisoning (CVE-2024-6915)</td><td>Advisory</td><td>2024-08-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1596">AVID-2026-R1596</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in Calculate Function in parisneo/lollms (CVE-2024-6982)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1597">AVID-2026-R1597</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in mudler/localai (CVE-2024-6983)</td><td>Advisory</td><td>2024-09-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1598">AVID-2026-R1598</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution due to Arbitrary File Write in open-webui/open-webui (CVE-2024-7034)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1599">AVID-2026-R1599</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Neutralization of Special Elements used in a Command ('Command Injection') in GitLab (CVE-2024-7110)</td><td>Advisory</td><td>2024-08-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1600">AVID-2026-R1600</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AI Chatbot with ChatGPT by AYS <= 2.0.9 - Unauthenticated OpenAI Key Disclosure (CVE-2024-7713)</td><td>Advisory</td><td>2024-09-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1601">AVID-2026-R1601</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AI Assistant with ChatGPT by AYS <= 2.0.9 - Unauthenticated AJAX Calls (CVE-2024-7714)</td><td>Advisory</td><td>2024-09-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1602">AVID-2026-R1602</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CSRF in aimhubio/aim (CVE-2024-7760)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1603">AVID-2026-R1603</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service in h2oai/h2o-3 (CVE-2024-7765)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1604">AVID-2026-R1604</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service in h2oai/h2o-3 (CVE-2024-7768)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1605">AVID-2026-R1605</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Overwrite in onnx/onnx (CVE-2024-7776)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1606">AVID-2026-R1606</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Overwrite in danswer-ai/danswer (CVE-2024-7957)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1607">AVID-2026-R1607</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Write/Overwrite in lightning-ai/pytorch-lightning (CVE-2024-8019)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1608">AVID-2026-R1608</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Open Redirect in gradio-app/gradio (CVE-2024-8021)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1609">AVID-2026-R1609</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service in aimhubio/aim (CVE-2024-8061)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1610">AVID-2026-R1610</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service in h2oai/h2o-3 (CVE-2024-8062)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1611">AVID-2026-R1611</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Divide by Zero in ollama/ollama (CVE-2024-8063)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1612">AVID-2026-R1612</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CSRF in danswer-ai/danswer (CVE-2024-8065)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1613">AVID-2026-R1613</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CORS Misconfiguration in prefecthq/prefect (CVE-2024-8183)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1614">AVID-2026-R1614</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unrestricted Code Execution in aimhubio/aim (CVE-2024-8238)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1615">AVID-2026-R1615</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in mintplex-labs/anything-llm (CVE-2024-8248)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1616">AVID-2026-R1616</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Protection of Alternate Path in GitLab (CVE-2024-8311)</td><td>Advisory</td><td>2024-09-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1617">AVID-2026-R1617</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Object deserialization in Reverb leading to RCE (CVE-2024-8375)</td><td>Advisory</td><td>2024-09-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1618">AVID-2026-R1618</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in modelscope/agentscope (CVE-2024-8438)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1619">AVID-2026-R1619</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CORS Vulnerability in modelscope/agentscope (CVE-2024-8487)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1620">AVID-2026-R1620</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution via Deserialization in modelscope/agentscope (CVE-2024-8502)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1621">AVID-2026-R1621</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Local File Inclusion (LFI) in modelscope/agentscope (CVE-2024-8550)</td><td>Advisory</td><td>2025-02-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1622">AVID-2026-R1622</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in modelscope/agentscope (CVE-2024-8551)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1623">AVID-2026-R1623</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Overwrite in h2oai/h2o-3 (CVE-2024-8616)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1624">AVID-2026-R1624</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Arbitrary File Deletion via Relative Path Traversal in aimhubio/aim (CVE-2024-8769)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1625">AVID-2026-R1625</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Ansible-core: exposure of sensitive information in ansible vault files due to improper logging (CVE-2024-8775)</td><td>Advisory</td><td>2024-09-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1626">AVID-2026-R1626</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in mlflow/mlflow (CVE-2024-8859)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1627">AVID-2026-R1627</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">h2oai h2o-3 JDBC Connection 1 getConnectionSafe deserialization (CVE-2024-8862)</td><td>Advisory</td><td>2024-09-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1628">AVID-2026-R1628</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path Traversal in parisneo/lollms-webui (CVE-2024-8898)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1629">AVID-2026-R1629</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Local File Inclusion in bentoml/openllm (CVE-2024-8982)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1630">AVID-2026-R1630</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service in bentoml/bentoml (CVE-2024-9056)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1631">AVID-2026-R1631</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Privilege Escalation in lunary-ai/lunary (CVE-2024-9098)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1632">AVID-2026-R1632</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service (DoS) via Multipart Boundary in zenml-io/zenml (CVE-2024-9340)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1633">AVID-2026-R1633</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Directory Traversal in polyaxon/polyaxon (CVE-2024-9362)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1634">AVID-2026-R1634</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cross-Site Request Forgery (CSRF) in polyaxon/polyaxon (CVE-2024-9365)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1635">AVID-2026-R1635</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Privilege Management in transformeroptimus/superagi (CVE-2024-9431)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1636">AVID-2026-R1636</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in transformeroptimus/superagi (CVE-2024-9439)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1637">AVID-2026-R1637</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stored XSS in Kubeflow Pipeline View (CVE-2024-9526)</td><td>Advisory</td><td>2024-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1638">AVID-2026-R1638</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution in kedro-org/kedro (CVE-2024-9701)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1639">AVID-2026-R1639</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Missing Authentication Check in parisneo/lollms-webui (CVE-2024-9919)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1640">AVID-2026-R1640</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Unrestricted File Upload and Execution in parisneo/lollms-webui (CVE-2024-9920)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1641">AVID-2026-R1641</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service (DoS) by Sending Large Filename at File Upload Endpoint in gradio-app/gradio (CVE-2025-0187)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1642">AVID-2026-R1642</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF in gaizhenbiao/chuanhuchatgpt (CVE-2025-0188)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1643">AVID-2026-R1643</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stored Cross-site Scripting (XSS) in wandb/openui (CVE-2025-0192)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1644">AVID-2026-R1644</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Exposure of Sensitive Information in berriai/litellm (CVE-2025-0330)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1645">AVID-2026-R1645</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">SSRF Check Bypass in Requests Utility in significant-gravitas/autogpt (CVE-2025-0454)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1646">AVID-2026-R1646</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MD5 Hash Collision in SageMaker Workflow in aws/sagemaker-python-sdk (CVE-2025-0508)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1647">AVID-2026-R1647</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Stack Exhaustion In Tensorflow Serving (CVE-2025-0649)</td><td>Advisory</td><td>2025-05-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1648">AVID-2026-R1648</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Improper Access Control vulnerability in EmbedAI (CVE-2025-0744)</td><td>Advisory</td><td>2025-01-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1649">AVID-2026-R1649</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Path traversal issue in Deep Java Library (CVE-2025-0851)</td><td>Advisory</td><td>2025-01-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1650">AVID-2026-R1650</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Orthanc Server Missing Authentication for Critical Function (CVE-2025-0896)</td><td>Advisory</td><td>2025-02-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1651">AVID-2026-R1651</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Regular Expression Denial of Service (ReDoS) in huggingface/transformers (CVE-2025-1194)</td><td>Advisory</td><td>2025-04-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1652">AVID-2026-R1652</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Weak Password Requirements in mlflow/mlflow (CVE-2025-1474)</td><td>Advisory</td><td>2025-03-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1653">AVID-2026-R1653</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">vLLM AIBrix Prefix Caching hash.go random values (CVE-2025-1953)</td><td>Advisory</td><td>2025-03-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R1654">AVID-2026-R1654</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-1979</td><td>Advisory</td><td>2025-03-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1655">AVID-2026-R1655</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Regular Expression Denial of Service (ReDoS) in huggingface/transformers (CVE-2025-2099)</td><td>Advisory</td><td>2025-05-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1656">AVID-2026-R1656</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch Tuple torch.ops.profiler._call_end_callbacks_on_jit_fut memory corruption (CVE-2025-2148)</td><td>Advisory</td><td>2025-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1657">AVID-2026-R1657</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AutoGPT SSRF vulnerability (CVE-2025-22603)</td><td>Advisory</td><td>2025-03-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1658">AVID-2026-R1658</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-22892</td><td>Advisory</td><td>2025-05-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1659">AVID-2026-R1659</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Gradio Blocked Path ACL Bypass Vulnerability (CVE-2025-23042)</td><td>Advisory</td><td>2025-01-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1660">AVID-2026-R1660</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">CVAT allows remote code execution via tracker Nuclio functions (CVE-2025-23045)</td><td>Advisory</td><td>2025-01-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R1661">AVID-2026-R1661</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-23243</td><td>Advisory</td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1662">AVID-2026-R1662</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-23247</td><td>Advisory</td><td>2025-05-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R1663">AVID-2026-R1663</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-23249</td><td>Advisory</td><td>2025-04-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1664">AVID-2026-R1664</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-23250</td><td>Advisory</td><td>2025-04-22</td></tr>
    <tr><td><a href="/database/AVID-2026-R1665">AVID-2026-R1665</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-23360</td><td>Advisory</td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R1666">AVID-2026-R1666</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">WordPress Salvador – AI Image Generator plugin <= 1.0.11 - Broken Access Control vulnerability (CVE-2025-23954)</td><td>Advisory</td><td>2025-01-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1667">AVID-2026-R1667</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The Snowflake Connector for Python uses insecure cache files permissions (CVE-2025-24795)</td><td>Advisory</td><td>2025-01-29</td></tr>
    <tr><td><a href="/database/AVID-2026-R1668">AVID-2026-R1668</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Label Studio has a Path Traversal Vulnerability via image Field (CVE-2025-25295)</td><td>Advisory</td><td>2025-02-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1669">AVID-2026-R1669</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Rembg CORS misconfiguration (CVE-2025-25302)</td><td>Advisory</td><td>2025-03-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1670">AVID-2026-R1670</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote code execution when loading a crafted GraphQL schema (CVE-2025-27407)</td><td>Advisory</td><td>2025-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1671">AVID-2026-R1671</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Snowflake JDBC Driver client-side encryption key in DEBUG logs (CVE-2025-27496)</td><td>Advisory</td><td>2025-03-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1672">AVID-2026-R1672</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Applio allows SSRF and file write in model_download.py (CVE-2025-27775)</td><td>Advisory</td><td>2025-03-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1673">AVID-2026-R1673</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Applio allows unsafe deserialization in model_information.py (CVE-2025-27780)</td><td>Advisory</td><td>2025-03-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1674">AVID-2026-R1674</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Applio allows unsafe deserialization in inference.py (CVE-2025-27781)</td><td>Advisory</td><td>2025-03-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1675">AVID-2026-R1675</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Applio allows arbitrary file write in inference.py (CVE-2025-27782)</td><td>Advisory</td><td>2025-03-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1676">AVID-2026-R1676</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Applio allows a DoS in restart.py (CVE-2025-27787)</td><td>Advisory</td><td>2025-03-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1677">AVID-2026-R1677</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vulnerability CVE-2025-29189</td><td>Advisory</td><td>2025-04-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1678">AVID-2026-R1678</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">vLLM  Allows Remote Code Execution via Mooncake Integration (CVE-2025-29783)</td><td>Advisory</td><td>2025-03-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R1679">AVID-2026-R1679</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Apache Parquet Java: Arbitrary code execution in the parquet-avro module when reading an Avro schema from a Parquet file metadata (CVE-2025-30065)</td><td>Advisory</td><td>2025-04-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1680">AVID-2026-R1680</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Remote Code Execution Vulnerability in vLLM Multi-Node Cluster Configuration (CVE-2025-30165)</td><td>Advisory</td><td>2025-05-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R1681">AVID-2026-R1681</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Document Intelligence Studio On-Prem Elevation of Privilege Vulnerability (CVE-2025-30387)</td><td>Advisory</td><td>2025-05-13</td></tr>
    <tr><td><a href="/database/AVID-2026-R1682">AVID-2026-R1682</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure Bot Framework SDK Elevation of Privilege Vulnerability (CVE-2025-30389)</td><td>Advisory</td><td>2025-04-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1683">AVID-2026-R1683</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure ML Compute Elevation of Privilege Vulnerability (CVE-2025-30390)</td><td>Advisory</td><td>2025-04-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1684">AVID-2026-R1684</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Azure AI Bot Elevation of Privilege Vulnerability (CVE-2025-30392)</td><td>Advisory</td><td>2025-04-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1685">AVID-2026-R1685</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindSpore mindspore.numpy.fft.hfftn memory corruption (CVE-2025-3144)</td><td>Advisory</td><td>2025-04-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1686">AVID-2026-R1686</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MindSpore mindspore.numpy.fft.rfft2 memory corruption (CVE-2025-3145)</td><td>Advisory</td><td>2025-04-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1687">AVID-2026-R1687</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">AutoGPT allows SSRF due to DNS Rebinding in requests wrapper (CVE-2025-31490)</td><td>Advisory</td><td>2025-04-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1688">AVID-2026-R1688</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">InternLM LMDeploy conf.py open code injection (CVE-2025-3163)</td><td>Advisory</td><td>2025-04-03</td></tr>
    <tr><td><a href="/database/AVID-2026-R1689">AVID-2026-R1689</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Denial of Service by abusing xgrammar unbounded cache in memory (CVE-2025-32381)</td><td>Advisory</td><td>2025-04-09</td></tr>
    <tr><td><a href="/database/AVID-2026-R1690">AVID-2026-R1690</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">MaxKB has a reverse shell vulnerability in function library (CVE-2025-32383)</td><td>Advisory</td><td>2025-04-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R1691">AVID-2026-R1691</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch: `torch.load` with `weights_only=True` leads to remote code execution (CVE-2025-32434)</td><td>Advisory</td><td>2025-04-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R1692">AVID-2026-R1692</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">vLLM Vulnerable to Remote Code Execution via Mooncake Integration (CVE-2025-32444)</td><td>Advisory</td><td>2025-04-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1693">AVID-2026-R1693</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">labsai/eddi Vulnerable to Path Traversal (Zip Slip) in ZIP Import Function (CVE-2025-32779)</td><td>Advisory</td><td>2025-04-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1694">AVID-2026-R1694</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">conda-forge-webservices has an Unauthorized Artifact Modification Race Condition (CVE-2025-32784)</td><td>Advisory</td><td>2025-04-15</td></tr>
    <tr><td><a href="/database/AVID-2026-R1695">AVID-2026-R1695</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch LossCTC.cpp torch.nn.functional.ctc_loss denial of service (CVE-2025-3730)</td><td>Advisory</td><td>2025-04-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R1696">AVID-2026-R1696</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">PyTorch nccl.py torch.cuda.nccl.reduce denial of service (CVE-2025-4287)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1697">AVID-2026-R1697</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GHSL-2025-012_Retrieval-based-Voice-Conversion-WebUI (CVE-2025-43842)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1698">AVID-2026-R1698</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GHSL-2025-013_Retrieval-based-Voice-Conversion-WebUI (CVE-2025-43843)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1699">AVID-2026-R1699</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GHSL-2025-016_Retrieval-based-Voice-Conversion-WebUI (CVE-2025-43846)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1700">AVID-2026-R1700</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GHSL-2025-017_Retrieval-based-Voice-Conversion-WebUI (CVE-2025-43847)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1701">AVID-2026-R1701</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GHSL-2025-019_Retrieval-based-Voice-Conversion-WebUI (CVE-2025-43849)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1702">AVID-2026-R1702</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GHSL-2025-020_Retrieval-based-Voice-Conversion-WebUI (CVE-2025-43850)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1703">AVID-2026-R1703</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GHSL-2025-021_Retrieval-based-Voice-Conversion-WebUI (CVE-2025-43851)</td><td>Advisory</td><td>2025-05-05</td></tr>
    <tr><td><a href="/database/AVID-2026-R1704">AVID-2026-R1704</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Divide By Zero in dlib (CVE-2025-4637)</td><td>Advisory</td><td>2025-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1705">AVID-2026-R1705</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">LLaMA-Factory Allows Arbitrary Code Execution via Unsafe Deserialization in Ilamafy_baichuan2.py (CVE-2025-46567)</td><td>Advisory</td><td>2025-05-01</td></tr>
    <tr><td><a href="/database/AVID-2026-R1706">AVID-2026-R1706</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OZI-Project/ozi-publish Code Injection vulnerability (CVE-2025-47271)</td><td>Advisory</td><td>2025-05-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1707">AVID-2026-R1707</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ToolHive stores secrets in the state store with no encryption (CVE-2025-47274)</td><td>Advisory</td><td>2025-05-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R1708">AVID-2026-R1708</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">vLLM Allows Remote Code Execution via PyNcclPipe Communication Service (CVE-2025-47277)</td><td>Advisory</td><td>2025-05-20</td></tr>
    <tr><td><a href="/database/AVID-2026-R1709">AVID-2026-R1709</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">5ire Client Vulnerable to Cross-Site Scripting (XSS) and Remote Code Execution (RCE) (CVE-2025-47777)</td><td>Advisory</td><td>2025-05-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R1710">AVID-2026-R1710</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">vLLM has a Regular Expression Denial of Service (ReDoS, Exponential Complexity) Vulnerability in `pythonic_tool_parser.py` (CVE-2025-48887)</td><td>Advisory</td><td>2025-05-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1711">AVID-2026-R1711</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Gradio Allows Unauthorized File Copy via Path Manipulation (CVE-2025-48889)</td><td>Advisory</td><td>2025-05-30</td></tr>
    <tr><td><a href="/database/AVID-2026-R1712">AVID-2026-R1712</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">erdogant pypickle pypickle.py load deserialization (CVE-2025-5174)</td><td>Advisory</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1713">AVID-2026-R1713</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">erdogant pypickle pypickle.py save improper authorization (CVE-2025-5175)</td><td>Advisory</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R1714">AVID-2026-R1714</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Trivy ecosystem supply chain briefly compromised (CVE-2026-33634)</td><td>Advisory</td><td>2026-03-23</td></tr>
  </tbody>
</table>
<div class="avid-report-pager" id="reports-2026-pager" style="display: flex; justify-content: flex-start; align-items: center; gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;"></div>

<script>
if (!window.__avidReportTableInit) {
  window.__avidReportTableInit = function (tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    if (!tbody) return;
    var pageSizeSelect = document.getElementById(tableId + '-page-size');
    var pager = document.getElementById(tableId + '-pager');
    if (!pageSizeSelect || !pager) return;

    var state = {
      page: 1,
      pageSize: Number(pageSizeSelect.value) || 20,
    };

    function getRows() {
      return Array.from(tbody.querySelectorAll('tr'));
    }

    function renderPager(totalPages) {
      pager.innerHTML = '';

      function appendButton(label, pageNo, disabled) {
        var button = document.createElement('button');
        button.type = 'button';
        button.textContent = label;
        button.style.width = 'auto';
        button.style.minWidth = '2.25rem';
        button.style.display = 'inline-block';
        button.disabled = !!disabled;
        if (!button.disabled) {
          button.addEventListener('click', function () {
            state.page = pageNo;
            render();
          });
        }
        pager.appendChild(button);
      }

      function appendEllipsis() {
        var span = document.createElement('span');
        span.textContent = '...';
        span.className = 'avid-pager-ellipsis';
        pager.appendChild(span);
      }

      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);

      if (totalPages <= 3) {
        for (var i = 1; i <= totalPages; i += 1) {
          appendButton(String(i), i, i === state.page);
        }
      } else {
        appendButton('1', 1, state.page === 1);
        appendButton('2', 2, state.page === 2);
        appendEllipsis();
        appendButton(String(totalPages), totalPages, state.page === totalPages);
      }

      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);
    }

    function syncSortIndicators() {
      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {
        var arrow = th.querySelector('.avid-sort-arrow');
        if (!arrow) {
          arrow = document.createElement('span');
          arrow.className = 'avid-sort-arrow';
          arrow.style.marginLeft = '0.35rem';
          th.appendChild(arrow);
        }
        var dir = th.getAttribute('data-sort-dir');
        if (dir === 'asc') {
          arrow.textContent = '↑';
        } else if (dir === 'desc') {
          arrow.textContent = '↓';
        } else {
          arrow.textContent = '↕';
        }
      });
    }

    function render() {
      var rows = getRows();
      var totalRows = rows.length;
      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));
      if (state.page > totalPages) state.page = totalPages;
      if (state.page < 1) state.page = 1;

      var start = (state.page - 1) * state.pageSize;
      var end = start + state.pageSize;
      rows.forEach(function (row, idx) {
        row.style.display = idx >= start && idx < end ? '' : 'none';
      });

      renderPager(totalPages);
    }

    function sortRows(col, dir) {
      var rows = getRows();
      rows.sort(function (a, b) {
        var av = (a.children[col] && a.children[col].innerText || '').trim();
        var bv = (b.children[col] && b.children[col].innerText || '').trim();
        var ad = Date.parse(av);
        var bd = Date.parse(bv);
        var cmp;
        if (!Number.isNaN(ad) && !Number.isNaN(bd)) {
          cmp = ad - bd;
        } else {
          cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });
        }
        return dir === 'asc' ? cmp : -cmp;
      });
      rows.forEach(function (row) { tbody.appendChild(row); });
    }

    if (!table.dataset.avidSortBound) {
      table.dataset.avidSortBound = 'true';
      table.addEventListener('click', function (event) {
        var th = event.target.closest('th[data-sort-col]');
        if (!th || !table.contains(th)) return;

        var col = Number(th.getAttribute('data-sort-col'));
        var current = th.getAttribute('data-sort-dir') || '';
        var next = current === 'asc' ? 'desc' : 'asc';

        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {
          h.removeAttribute('data-sort-dir');
        });
        th.setAttribute('data-sort-dir', next);
        syncSortIndicators();

        sortRows(col, next);
        state.page = 1;
        render();
      });
    }

    if (!pageSizeSelect.dataset.avidPageSizeBound) {
      pageSizeSelect.dataset.avidPageSizeBound = 'true';
      pageSizeSelect.addEventListener('change', function () {
        state.pageSize = Number(pageSizeSelect.value) || 20;
        state.page = 1;
        render();
      });
    }

    sortRows(0, 'desc');
    syncSortIndicators();
    render();
  };
}
window.__avidReportTableInit('reports-2026');
</script>
<!-- reports-year:2026:end -->








<!-- reports-year:2025:start -->
#### 2025

<div class="avid-report-controls" style="display: flex; justify-content: flex-start; margin: 0.5rem 0;">
  <label style="display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;">
    Rows per page:
    <select id="reports-2025-page-size" style="display: inline-block; width: auto; min-width: 4.5rem;"><option value="10">10</option><option value="20" selected>20</option><option value="50">50</option></select>
  </label>
</div>
<table class="avid-report-table" id="reports-2025" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 18%;">
    <col style="width: 52%;">
    <col style="width: 15%;">
    <col style="width: 15%;">
  </colgroup>
  <thead>
    <tr>
      <th data-sort-col="0" data-sort-dir="desc" style="white-space: nowrap;">Report ID</th>
      <th data-sort-col="1" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Description</th>
      <th data-sort-col="2" style="white-space: nowrap;">Report Type</th>
      <th data-sort-col="3" style="white-space: nowrap;">Date Reported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><a href="/database/AVID-2025-R0001">AVID-2025-R0001</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">The application will provide the user with the answer to their math problem, violating existing controls.</td><td>Advisory</td><td>2025-01-17</td></tr>
    <tr><td><a href="/database/AVID-2025-R0002">AVID-2025-R0002</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Geopolitical bias in sentiment analysis for neutral phrases</td><td>Advisory</td><td>2025-01-17</td></tr>
    <tr><td><a href="/database/AVID-2025-R0003">AVID-2025-R0003</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the AI system gpt-4o-mini-2024-07-18 on the agentharm benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0004">AVID-2025-R0004</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the AI system gpt-4o-mini-2024-07-18 on the wmdp_bio benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0005">AVID-2025-R0005</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the AI system gpt-4o-mini-2024-07-18 on the wmdp_chem benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0006">AVID-2025-R0006</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the AI system gpt-4o-mini-2024-07-18 on the wmdp_cyber benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0007">AVID-2025-R0007</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the AI system gpt-4o-mini-2024-07-18 on the cyse2_interpreter_abuse benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0008">AVID-2025-R0008</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the AI system gpt-4o-mini-2024-07-18 on the cyse2_prompt_injection benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0012">AVID-2025-R0012</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Llama-3.3-70B-Instruct-Turbo on the agentharm benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0013">AVID-2025-R0013</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Llama-3.3-70B-Instruct-Turbo on the wmdp_bio benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0014">AVID-2025-R0014</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Llama-3.3-70B-Instruct-Turbo on the wmdp_chem benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0015">AVID-2025-R0015</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Llama-3.3-70B-Instruct-Turbo on the wmdp_cyber benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0016">AVID-2025-R0016</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Llama-3.3-70B-Instruct-Turbo on the cyse2_interpreter_abuse benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0017">AVID-2025-R0017</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Llama-3.3-70B-Instruct-Turbo on the cyse2_prompt_injection benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0021">AVID-2025-R0021</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM DeepSeek-R1 on the agentharm benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0022">AVID-2025-R0022</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM DeepSeek-R1 on the wmdp_bio benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0023">AVID-2025-R0023</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM DeepSeek-R1 on the wmdp_chem benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0024">AVID-2025-R0024</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM DeepSeek-R1 on the wmdp_cyber benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0025">AVID-2025-R0025</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM DeepSeek-R1 on the cyse2_interpreter_abuse benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0030">AVID-2025-R0030</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Mistral-Small-24B-Instruct-2501 on the agentharm benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0031">AVID-2025-R0031</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Mistral-Small-24B-Instruct-2501 on the wmdp_bio benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0032">AVID-2025-R0032</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Mistral-Small-24B-Instruct-2501 on the wmdp_chem benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0033">AVID-2025-R0033</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Mistral-Small-24B-Instruct-2501 on the wmdp_cyber benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0034">AVID-2025-R0034</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Mistral-Small-24B-Instruct-2501 on the cyse2_interpreter_abuse benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
    <tr><td><a href="/database/AVID-2025-R0035">AVID-2025-R0035</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evaluation of the LLM Mistral-Small-24B-Instruct-2501 on the cyse2_prompt_injection benchmark using Inspect Evals</td><td>Measurement</td><td>2025-05-26</td></tr>
  </tbody>
</table>
<div class="avid-report-pager" id="reports-2025-pager" style="display: flex; justify-content: flex-start; align-items: center; gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;"></div>

<script>
if (!window.__avidReportTableInit) {
  window.__avidReportTableInit = function (tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    if (!tbody) return;
    var pageSizeSelect = document.getElementById(tableId + '-page-size');
    var pager = document.getElementById(tableId + '-pager');
    if (!pageSizeSelect || !pager) return;

    var state = {
      page: 1,
      pageSize: Number(pageSizeSelect.value) || 20,
    };

    function getRows() {
      return Array.from(tbody.querySelectorAll('tr'));
    }

    function renderPager(totalPages) {
      pager.innerHTML = '';

      function appendButton(label, pageNo, disabled) {
        var button = document.createElement('button');
        button.type = 'button';
        button.textContent = label;
        button.style.width = 'auto';
        button.style.minWidth = '2.25rem';
        button.style.display = 'inline-block';
        button.disabled = !!disabled;
        if (!button.disabled) {
          button.addEventListener('click', function () {
            state.page = pageNo;
            render();
          });
        }
        pager.appendChild(button);
      }

      function appendEllipsis() {
        var span = document.createElement('span');
        span.textContent = '...';
        span.className = 'avid-pager-ellipsis';
        pager.appendChild(span);
      }

      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);

      if (totalPages <= 3) {
        for (var i = 1; i <= totalPages; i += 1) {
          appendButton(String(i), i, i === state.page);
        }
      } else {
        appendButton('1', 1, state.page === 1);
        appendButton('2', 2, state.page === 2);
        appendEllipsis();
        appendButton(String(totalPages), totalPages, state.page === totalPages);
      }

      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);
    }

    function syncSortIndicators() {
      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {
        var arrow = th.querySelector('.avid-sort-arrow');
        if (!arrow) {
          arrow = document.createElement('span');
          arrow.className = 'avid-sort-arrow';
          arrow.style.marginLeft = '0.35rem';
          th.appendChild(arrow);
        }
        var dir = th.getAttribute('data-sort-dir');
        if (dir === 'asc') {
          arrow.textContent = '↑';
        } else if (dir === 'desc') {
          arrow.textContent = '↓';
        } else {
          arrow.textContent = '↕';
        }
      });
    }

    function render() {
      var rows = getRows();
      var totalRows = rows.length;
      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));
      if (state.page > totalPages) state.page = totalPages;
      if (state.page < 1) state.page = 1;

      var start = (state.page - 1) * state.pageSize;
      var end = start + state.pageSize;
      rows.forEach(function (row, idx) {
        row.style.display = idx >= start && idx < end ? '' : 'none';
      });

      renderPager(totalPages);
    }

    function sortRows(col, dir) {
      var rows = getRows();
      rows.sort(function (a, b) {
        var av = (a.children[col] && a.children[col].innerText || '').trim();
        var bv = (b.children[col] && b.children[col].innerText || '').trim();
        var ad = Date.parse(av);
        var bd = Date.parse(bv);
        var cmp;
        if (!Number.isNaN(ad) && !Number.isNaN(bd)) {
          cmp = ad - bd;
        } else {
          cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });
        }
        return dir === 'asc' ? cmp : -cmp;
      });
      rows.forEach(function (row) { tbody.appendChild(row); });
    }

    if (!table.dataset.avidSortBound) {
      table.dataset.avidSortBound = 'true';
      table.addEventListener('click', function (event) {
        var th = event.target.closest('th[data-sort-col]');
        if (!th || !table.contains(th)) return;

        var col = Number(th.getAttribute('data-sort-col'));
        var current = th.getAttribute('data-sort-dir') || '';
        var next = current === 'asc' ? 'desc' : 'asc';

        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {
          h.removeAttribute('data-sort-dir');
        });
        th.setAttribute('data-sort-dir', next);
        syncSortIndicators();

        sortRows(col, next);
        state.page = 1;
        render();
      });
    }

    if (!pageSizeSelect.dataset.avidPageSizeBound) {
      pageSizeSelect.dataset.avidPageSizeBound = 'true';
      pageSizeSelect.addEventListener('change', function () {
        state.pageSize = Number(pageSizeSelect.value) || 20;
        state.page = 1;
        render();
      });
    }

    sortRows(0, 'desc');
    syncSortIndicators();
    render();
  };
}
window.__avidReportTableInit('reports-2025');
</script>
<!-- reports-year:2025:end -->

























<!-- reports-year:2023:start -->
#### 2023

<div class="avid-report-controls" style="display: flex; justify-content: flex-start; margin: 0.5rem 0;">
  <label style="display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;">
    Rows per page:
    <select id="reports-2023-page-size" style="display: inline-block; width: auto; min-width: 4.5rem;"><option value="10">10</option><option value="20" selected>20</option><option value="50">50</option></select>
  </label>
</div>
<table class="avid-report-table" id="reports-2023" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 18%;">
    <col style="width: 52%;">
    <col style="width: 15%;">
    <col style="width: 15%;">
  </colgroup>
  <thead>
    <tr>
      <th data-sort-col="0" data-sort-dir="desc" style="white-space: nowrap;">Report ID</th>
      <th data-sort-col="1" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Description</th>
      <th data-sort-col="2" style="white-space: nowrap;">Report Type</th>
      <th data-sort-col="3" style="white-space: nowrap;">Date Reported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><a href="/database/AVID-2023-R0001">AVID-2023-R0001</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ChatGPT fails to follow lexical constraints</td><td>Advisory</td><td>2023-01-13</td></tr>
    <tr><td><a href="/database/AVID-2023-R0002">AVID-2023-R0002</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ChatGPT links wrong authors to papers</td><td>Issue</td><td>2023-01-05</td></tr>
    <tr><td><a href="/database/AVID-2023-R0003">AVID-2023-R0003</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">It is possible to make ChatGPT perform remote code execution just by asking politely</td><td>Advisory</td><td>2023-03-26</td></tr>
  </tbody>
</table>
<div class="avid-report-pager" id="reports-2023-pager" style="display: flex; justify-content: flex-start; align-items: center; gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;"></div>

<script>
if (!window.__avidReportTableInit) {
  window.__avidReportTableInit = function (tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    if (!tbody) return;
    var pageSizeSelect = document.getElementById(tableId + '-page-size');
    var pager = document.getElementById(tableId + '-pager');
    if (!pageSizeSelect || !pager) return;

    var state = {
      page: 1,
      pageSize: Number(pageSizeSelect.value) || 20,
    };

    function getRows() {
      return Array.from(tbody.querySelectorAll('tr'));
    }

    function renderPager(totalPages) {
      pager.innerHTML = '';

      function appendButton(label, pageNo, disabled) {
        var button = document.createElement('button');
        button.type = 'button';
        button.textContent = label;
        button.style.width = 'auto';
        button.style.minWidth = '2.25rem';
        button.style.display = 'inline-block';
        button.disabled = !!disabled;
        if (!button.disabled) {
          button.addEventListener('click', function () {
            state.page = pageNo;
            render();
          });
        }
        pager.appendChild(button);
      }

      function appendEllipsis() {
        var span = document.createElement('span');
        span.textContent = '...';
        span.className = 'avid-pager-ellipsis';
        pager.appendChild(span);
      }

      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);

      if (totalPages <= 3) {
        for (var i = 1; i <= totalPages; i += 1) {
          appendButton(String(i), i, i === state.page);
        }
      } else {
        appendButton('1', 1, state.page === 1);
        appendButton('2', 2, state.page === 2);
        appendEllipsis();
        appendButton(String(totalPages), totalPages, state.page === totalPages);
      }

      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);
    }

    function syncSortIndicators() {
      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {
        var arrow = th.querySelector('.avid-sort-arrow');
        if (!arrow) {
          arrow = document.createElement('span');
          arrow.className = 'avid-sort-arrow';
          arrow.style.marginLeft = '0.35rem';
          th.appendChild(arrow);
        }
        var dir = th.getAttribute('data-sort-dir');
        if (dir === 'asc') {
          arrow.textContent = '↑';
        } else if (dir === 'desc') {
          arrow.textContent = '↓';
        } else {
          arrow.textContent = '↕';
        }
      });
    }

    function render() {
      var rows = getRows();
      var totalRows = rows.length;
      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));
      if (state.page > totalPages) state.page = totalPages;
      if (state.page < 1) state.page = 1;

      var start = (state.page - 1) * state.pageSize;
      var end = start + state.pageSize;
      rows.forEach(function (row, idx) {
        row.style.display = idx >= start && idx < end ? '' : 'none';
      });

      renderPager(totalPages);
    }

    function sortRows(col, dir) {
      var rows = getRows();
      rows.sort(function (a, b) {
        var av = (a.children[col] && a.children[col].innerText || '').trim();
        var bv = (b.children[col] && b.children[col].innerText || '').trim();
        var ad = Date.parse(av);
        var bd = Date.parse(bv);
        var cmp;
        if (!Number.isNaN(ad) && !Number.isNaN(bd)) {
          cmp = ad - bd;
        } else {
          cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });
        }
        return dir === 'asc' ? cmp : -cmp;
      });
      rows.forEach(function (row) { tbody.appendChild(row); });
    }

    if (!table.dataset.avidSortBound) {
      table.dataset.avidSortBound = 'true';
      table.addEventListener('click', function (event) {
        var th = event.target.closest('th[data-sort-col]');
        if (!th || !table.contains(th)) return;

        var col = Number(th.getAttribute('data-sort-col'));
        var current = th.getAttribute('data-sort-dir') || '';
        var next = current === 'asc' ? 'desc' : 'asc';

        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {
          h.removeAttribute('data-sort-dir');
        });
        th.setAttribute('data-sort-dir', next);
        syncSortIndicators();

        sortRows(col, next);
        state.page = 1;
        render();
      });
    }

    if (!pageSizeSelect.dataset.avidPageSizeBound) {
      pageSizeSelect.dataset.avidPageSizeBound = 'true';
      pageSizeSelect.addEventListener('change', function () {
        state.pageSize = Number(pageSizeSelect.value) || 20;
        state.page = 1;
        render();
      });
    }

    sortRows(0, 'desc');
    syncSortIndicators();
    render();
  };
}
window.__avidReportTableInit('reports-2023');
</script>
<!-- reports-year:2023:end -->























<!-- reports-year:2022:start -->
#### 2022

<div class="avid-report-controls" style="display: flex; justify-content: flex-start; margin: 0.5rem 0;">
  <label style="display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;">
    Rows per page:
    <select id="reports-2022-page-size" style="display: inline-block; width: auto; min-width: 4.5rem;"><option value="10">10</option><option value="20" selected>20</option><option value="50">50</option></select>
  </label>
</div>
<table class="avid-report-table" id="reports-2022" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 18%;">
    <col style="width: 52%;">
    <col style="width: 15%;">
    <col style="width: 15%;">
  </colgroup>
  <thead>
    <tr>
      <th data-sort-col="0" data-sort-dir="desc" style="white-space: nowrap;">Report ID</th>
      <th data-sort-col="1" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Description</th>
      <th data-sort-col="2" style="white-space: nowrap;">Report Type</th>
      <th data-sort-col="3" style="white-space: nowrap;">Date Reported</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><a href="/database/AVID-2022-R0001">AVID-2022-R0001</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Gender Bias in Sentence Completion Tasks performed by bert-base-uncased using the HONEST metric</td><td>Detection</td><td>2022-11-09</td></tr>
    <tr><td><a href="/database/AVID-2022-R0002">AVID-2022-R0002</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Gender Bias in Sentence Completion Tasks performed by xlm-roberta-base using the HONEST score</td><td>Detection</td><td>2022-11-09</td></tr>
    <tr><td><a href="/database/AVID-2022-R0003">AVID-2022-R0003</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Profession bias reinforcing gender stereotypes found in bert-base-uncased, as measured on the Winobias dataset</td><td>Detection</td><td>2022-11-09</td></tr>
    <tr><td><a href="/database/AVID-2022-R0004">AVID-2022-R0004</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Profession bias reinforcing gender stereotypes found in xlm-roberta-base, as measured on the Winobias dataset</td><td>Detection</td><td>2022-11-09</td></tr>
    <tr><td><a href="/database/AVID-2022-R0005">AVID-2022-R0005</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Demographic bias found in EleutherAI/gpt-neo-125M for multiple sensitive categories, as measured on prompts supplied in the BOLD dataset</td><td>Detection</td><td>2022-11-09</td></tr>
  </tbody>
</table>
<div class="avid-report-pager" id="reports-2022-pager" style="display: flex; justify-content: flex-start; align-items: center; gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;"></div>

<script>
if (!window.__avidReportTableInit) {
  window.__avidReportTableInit = function (tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    if (!tbody) return;
    var pageSizeSelect = document.getElementById(tableId + '-page-size');
    var pager = document.getElementById(tableId + '-pager');
    if (!pageSizeSelect || !pager) return;

    var state = {
      page: 1,
      pageSize: Number(pageSizeSelect.value) || 20,
    };

    function getRows() {
      return Array.from(tbody.querySelectorAll('tr'));
    }

    function renderPager(totalPages) {
      pager.innerHTML = '';

      function appendButton(label, pageNo, disabled) {
        var button = document.createElement('button');
        button.type = 'button';
        button.textContent = label;
        button.style.width = 'auto';
        button.style.minWidth = '2.25rem';
        button.style.display = 'inline-block';
        button.disabled = !!disabled;
        if (!button.disabled) {
          button.addEventListener('click', function () {
            state.page = pageNo;
            render();
          });
        }
        pager.appendChild(button);
      }

      function appendEllipsis() {
        var span = document.createElement('span');
        span.textContent = '...';
        span.className = 'avid-pager-ellipsis';
        pager.appendChild(span);
      }

      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);

      if (totalPages <= 3) {
        for (var i = 1; i <= totalPages; i += 1) {
          appendButton(String(i), i, i === state.page);
        }
      } else {
        appendButton('1', 1, state.page === 1);
        appendButton('2', 2, state.page === 2);
        appendEllipsis();
        appendButton(String(totalPages), totalPages, state.page === totalPages);
      }

      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);
    }

    function syncSortIndicators() {
      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {
        var arrow = th.querySelector('.avid-sort-arrow');
        if (!arrow) {
          arrow = document.createElement('span');
          arrow.className = 'avid-sort-arrow';
          arrow.style.marginLeft = '0.35rem';
          th.appendChild(arrow);
        }
        var dir = th.getAttribute('data-sort-dir');
        if (dir === 'asc') {
          arrow.textContent = '↑';
        } else if (dir === 'desc') {
          arrow.textContent = '↓';
        } else {
          arrow.textContent = '↕';
        }
      });
    }

    function render() {
      var rows = getRows();
      var totalRows = rows.length;
      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));
      if (state.page > totalPages) state.page = totalPages;
      if (state.page < 1) state.page = 1;

      var start = (state.page - 1) * state.pageSize;
      var end = start + state.pageSize;
      rows.forEach(function (row, idx) {
        row.style.display = idx >= start && idx < end ? '' : 'none';
      });

      renderPager(totalPages);
    }

    function sortRows(col, dir) {
      var rows = getRows();
      rows.sort(function (a, b) {
        var av = (a.children[col] && a.children[col].innerText || '').trim();
        var bv = (b.children[col] && b.children[col].innerText || '').trim();
        var ad = Date.parse(av);
        var bd = Date.parse(bv);
        var cmp;
        if (!Number.isNaN(ad) && !Number.isNaN(bd)) {
          cmp = ad - bd;
        } else {
          cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });
        }
        return dir === 'asc' ? cmp : -cmp;
      });
      rows.forEach(function (row) { tbody.appendChild(row); });
    }

    if (!table.dataset.avidSortBound) {
      table.dataset.avidSortBound = 'true';
      table.addEventListener('click', function (event) {
        var th = event.target.closest('th[data-sort-col]');
        if (!th || !table.contains(th)) return;

        var col = Number(th.getAttribute('data-sort-col'));
        var current = th.getAttribute('data-sort-dir') || '';
        var next = current === 'asc' ? 'desc' : 'asc';

        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {
          h.removeAttribute('data-sort-dir');
        });
        th.setAttribute('data-sort-dir', next);
        syncSortIndicators();

        sortRows(col, next);
        state.page = 1;
        render();
      });
    }

    if (!pageSizeSelect.dataset.avidPageSizeBound) {
      pageSizeSelect.dataset.avidPageSizeBound = 'true';
      pageSizeSelect.addEventListener('change', function () {
        state.pageSize = Number(pageSizeSelect.value) || 20;
        state.page = 1;
        render();
      });
    }

    sortRows(0, 'desc');
    syncSortIndicators();
    render();
  };
}
window.__avidReportTableInit('reports-2022');
</script>
<!-- reports-year:2022:end -->
















## Vulnerability
Vulnerabilities can be linked to one or more taxonomies through tags. In AVID taxonomy, these tags denote the risk domains (Security, Ethics, Performance), related (sub)categories, and lifecycle stages. A vulnerability in AVID can pertain to one or more of the three levels: *dataset*, *model*, or *system*.

### List of Vulnerabilities

<!-- vulnerabilities-year:2023:start -->
##### 2023

<div class="avid-report-controls" style="display: flex; justify-content: flex-start; margin: 0.5rem 0;">
  <label style="display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;">
    Rows per page:
    <select id="vulnerabilities-2023-page-size" style="display: inline-block; width: auto; min-width: 4.5rem;"><option value="10">10</option><option value="20" selected>20</option><option value="50">50</option></select>
  </label>
</div>
<table class="avid-report-table" id="vulnerabilities-2023" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 28%;">
    <col style="width: 72%;">
  </colgroup>
  <thead>
    <tr>
      <th data-sort-col="0" style="white-space: nowrap;">Vulnerability ID</th>
      <th data-sort-col="1" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><a href="/database/AVID-2023-V001">AVID-2023-V001</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Evasion of Deep Learning Detector for Malware C&C Traffic</td></tr>
    <tr><td><a href="/database/AVID-2023-V002">AVID-2023-V002</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Botnet Domain Generation Algorithm (DGA) Detection Evasion</td></tr>
    <tr><td><a href="/database/AVID-2023-V003">AVID-2023-V003</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">VirusTotal Poisoning</td></tr>
    <tr><td><a href="/database/AVID-2023-V004">AVID-2023-V004</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Bypassing Cylance's AI Malware Detection</td></tr>
    <tr><td><a href="/database/AVID-2023-V005">AVID-2023-V005</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Camera Hijack Attack on Facial Recognition System</td></tr>
    <tr><td><a href="/database/AVID-2023-V006">AVID-2023-V006</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Attack on Machine Translation Service - Google Translate, Bing Translator, and Systran Translate</td></tr>
    <tr><td><a href="/database/AVID-2023-V007">AVID-2023-V007</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ClearviewAI Misconfiguration</td></tr>
    <tr><td><a href="/database/AVID-2023-V008">AVID-2023-V008</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">GPT-2 Model Replication</td></tr>
    <tr><td><a href="/database/AVID-2023-V009">AVID-2023-V009</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ProofPoint Evasion</td></tr>
    <tr><td><a href="/database/AVID-2023-V010">AVID-2023-V010</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Microsoft Azure Service Disruption</td></tr>
    <tr><td><a href="/database/AVID-2023-V011">AVID-2023-V011</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Microsoft Edge AI Evasion</td></tr>
    <tr><td><a href="/database/AVID-2023-V012">AVID-2023-V012</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Face Identification System Evasion via Physical Countermeasures</td></tr>
    <tr><td><a href="/database/AVID-2023-V013">AVID-2023-V013</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Backdoor Attack on Deep Learning Models in Mobile Apps</td></tr>
    <tr><td><a href="/database/AVID-2023-V014">AVID-2023-V014</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Confusing Antimalware Neural Networks</td></tr>
    <tr><td><a href="/database/AVID-2023-V015">AVID-2023-V015</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Compromised PyTorch Dependency Chain</td></tr>
    <tr><td><a href="/database/AVID-2023-V016">AVID-2023-V016</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Achieving Code Execution in MathGPT via Prompt Injection</td></tr>
    <tr><td><a href="/database/AVID-2023-V017">AVID-2023-V017</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google’s YouTube Kids App Presents Inappropriate Content</td></tr>
    <tr><td><a href="/database/AVID-2023-V018">AVID-2023-V018</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Warehouse robot ruptures can of bear spray and injures workers</td></tr>
    <tr><td><a href="/database/AVID-2023-V019">AVID-2023-V019</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Crashes with Maneuvering Characteristics Augmentation System (MCAS)</td></tr>
    <tr><td><a href="/database/AVID-2023-V020">AVID-2023-V020</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Collection of Robotic Surgery Malfunctions</td></tr>
    <tr><td><a href="/database/AVID-2023-V021">AVID-2023-V021</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Uber Autonomous Cars Running Red Lights</td></tr>
    <tr><td><a href="/database/AVID-2023-V022">AVID-2023-V022</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">NY City School Teacher Evaluation Algorithm Contested</td></tr>
    <tr><td><a href="/database/AVID-2023-V023">AVID-2023-V023</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Kronos Scheduling Algorithm Allegedly Caused Financial Issues for Starbucks Employees</td></tr>
    <tr><td><a href="/database/AVID-2023-V024">AVID-2023-V024</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Northpointe Risk Models</td></tr>
    <tr><td><a href="/database/AVID-2023-V025">AVID-2023-V025</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ChatGPT fails to follow lexical constraints</td></tr>
    <tr><td><a href="/database/AVID-2023-V026">AVID-2023-V026</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">ChatGPT generates false or incomplete references to scientific literature</td></tr>
    <tr><td><a href="/database/AVID-2023-V027">AVID-2023-V027</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">It is possible to make ChatGPT perform remote code execution just by asking politely</td></tr>
  </tbody>
</table>
<div class="avid-report-pager" id="vulnerabilities-2023-pager" style="display: flex; justify-content: flex-start; align-items: center; gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;"></div>

<script>
if (!window.__avidReportTableInit) {
  window.__avidReportTableInit = function (tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    if (!tbody) return;
    var pageSizeSelect = document.getElementById(tableId + '-page-size');
    var pager = document.getElementById(tableId + '-pager');
    if (!pageSizeSelect || !pager) return;

    var state = {
      page: 1,
      pageSize: Number(pageSizeSelect.value) || 20,
    };

    function getRows() {
      return Array.from(tbody.querySelectorAll('tr'));
    }

    function renderPager(totalPages) {
      pager.innerHTML = '';

      function appendButton(label, pageNo, disabled) {
        var button = document.createElement('button');
        button.type = 'button';
        button.textContent = label;
        button.style.width = 'auto';
        button.style.minWidth = '2.25rem';
        button.style.display = 'inline-block';
        button.disabled = !!disabled;
        if (!button.disabled) {
          button.addEventListener('click', function () {
            state.page = pageNo;
            render();
          });
        }
        pager.appendChild(button);
      }

      function appendEllipsis() {
        var span = document.createElement('span');
        span.textContent = '...';
        span.className = 'avid-pager-ellipsis';
        pager.appendChild(span);
      }

      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);

      if (totalPages <= 3) {
        for (var i = 1; i <= totalPages; i += 1) {
          appendButton(String(i), i, i === state.page);
        }
      } else {
        appendButton('1', 1, state.page === 1);
        appendButton('2', 2, state.page === 2);
        appendEllipsis();
        appendButton(String(totalPages), totalPages, state.page === totalPages);
      }

      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);
    }

    function syncSortIndicators() {
      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {
        var arrow = th.querySelector('.avid-sort-arrow');
        if (!arrow) {
          arrow = document.createElement('span');
          arrow.className = 'avid-sort-arrow';
          arrow.style.marginLeft = '0.35rem';
          th.appendChild(arrow);
        }
        var dir = th.getAttribute('data-sort-dir');
        if (dir === 'asc') {
          arrow.textContent = '↑';
        } else if (dir === 'desc') {
          arrow.textContent = '↓';
        } else {
          arrow.textContent = '↕';
        }
      });
    }

    function render() {
      var rows = getRows();
      var totalRows = rows.length;
      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));
      if (state.page > totalPages) state.page = totalPages;
      if (state.page < 1) state.page = 1;

      var start = (state.page - 1) * state.pageSize;
      var end = start + state.pageSize;
      rows.forEach(function (row, idx) {
        row.style.display = idx >= start && idx < end ? '' : 'none';
      });

      renderPager(totalPages);
    }

    if (!table.dataset.avidSortBound) {
      table.dataset.avidSortBound = 'true';
      table.addEventListener('click', function (event) {
        var th = event.target.closest('th[data-sort-col]');
        if (!th || !table.contains(th)) return;

        var col = Number(th.getAttribute('data-sort-col'));
        var current = th.getAttribute('data-sort-dir') || '';
        var next = current === 'asc' ? 'desc' : 'asc';

        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {
          h.removeAttribute('data-sort-dir');
        });
        th.setAttribute('data-sort-dir', next);
        syncSortIndicators();

        var rows = getRows();
        rows.sort(function (a, b) {
          var av = (a.children[col] && a.children[col].innerText || '').trim();
          var bv = (b.children[col] && b.children[col].innerText || '').trim();
          var ad = Date.parse(av);
          var bd = Date.parse(bv);
          var cmp;
          if (!Number.isNaN(ad) && !Number.isNaN(bd)) {
            cmp = ad - bd;
          } else {
            cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });
          }
          return next === 'asc' ? cmp : -cmp;
        });
        rows.forEach(function (row) { tbody.appendChild(row); });
        state.page = 1;
        render();
      });
    }

    if (!pageSizeSelect.dataset.avidPageSizeBound) {
      pageSizeSelect.dataset.avidPageSizeBound = 'true';
      pageSizeSelect.addEventListener('change', function () {
        state.pageSize = Number(pageSizeSelect.value) || 20;
        state.page = 1;
        render();
      });
    }

    syncSortIndicators();
    render();
  };
}
window.__avidReportTableInit('vulnerabilities-2023');
</script>
<!-- vulnerabilities-year:2023:end -->




















<!-- vulnerabilities-year:2022:start -->
##### 2022

<div class="avid-report-controls" style="display: flex; justify-content: flex-start; margin: 0.5rem 0;">
  <label style="display: inline-flex; align-items: center; gap: 0.5rem; width: auto; margin: 0;">
    Rows per page:
    <select id="vulnerabilities-2022-page-size" style="display: inline-block; width: auto; min-width: 4.5rem;"><option value="10">10</option><option value="20" selected>20</option><option value="50">50</option></select>
  </label>
</div>
<table class="avid-report-table" id="vulnerabilities-2022" style="table-layout: fixed; width: 100%;">
  <colgroup>
    <col style="width: 28%;">
    <col style="width: 72%;">
  </colgroup>
  <thead>
    <tr>
      <th data-sort-col="0" style="white-space: nowrap;">Vulnerability ID</th>
      <th data-sort-col="1" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><a href="/database/AVID-2022-V001">AVID-2022-V001</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Gender Bias in Sentence Completion Tasks performed by bert-base-uncased</td></tr>
    <tr><td><a href="/database/AVID-2022-V002">AVID-2022-V002</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Gender Bias in Sentence Completion Tasks performed by xlm-roberta-base</td></tr>
    <tr><td><a href="/database/AVID-2022-V003">AVID-2022-V003</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Multiple fairness harms found in generated text from EleutherAI/gpt-neo-125M</td></tr>
    <tr><td><a href="/database/AVID-2022-V004">AVID-2022-V004</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Facebook translates 'good morning' into 'attack them', leading to arrest</td></tr>
    <tr><td><a href="/database/AVID-2022-V005">AVID-2022-V005</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Uber AV Killed Pedestrian in Arizona</td></tr>
    <tr><td><a href="/database/AVID-2022-V006">AVID-2022-V006</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">YouTube's Algorithms Failed to Remove Violating Content Related to Suicide and Self-Harm</td></tr>
    <tr><td><a href="/database/AVID-2022-V007">AVID-2022-V007</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Israeli Tax Authority Employed Opaque Algorithm to Impose Fines, Reportedly Refusing to Provide an Explanation for Amount Calculation to a Farmer</td></tr>
    <tr><td><a href="/database/AVID-2022-V008">AVID-2022-V008</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Security Robot Drowns Itself in a Fountain</td></tr>
    <tr><td><a href="/database/AVID-2022-V009">AVID-2022-V009</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Deepfake Video of Ukrainian President Yielding to Russia Posted on Ukrainian Websites and Social Media</td></tr>
    <tr><td><a href="/database/AVID-2022-V010">AVID-2022-V010</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Meta’s BlenderBot 3 Chatbot Demo Made Offensive Antisemitic Comments</td></tr>
    <tr><td><a href="/database/AVID-2022-V011">AVID-2022-V011</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Predictive Policing Biases of PredPol</td></tr>
    <tr><td><a href="/database/AVID-2022-V012">AVID-2022-V012</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Hive Box Facial-Recognition Locks Hacked by Fourth Graders Using Intended Recipient's Facial Photo</td></tr>
    <tr><td><a href="/database/AVID-2022-V013">AVID-2022-V013</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TayBot</td></tr>
  </tbody>
</table>
<div class="avid-report-pager" id="vulnerabilities-2022-pager" style="display: flex; justify-content: flex-start; align-items: center; gap: 0.35rem; flex-wrap: wrap; margin-top: 0.5rem;"></div>

<script>
if (!window.__avidReportTableInit) {
  window.__avidReportTableInit = function (tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;
    var tbody = table.querySelector('tbody');
    if (!tbody) return;
    var pageSizeSelect = document.getElementById(tableId + '-page-size');
    var pager = document.getElementById(tableId + '-pager');
    if (!pageSizeSelect || !pager) return;

    var state = {
      page: 1,
      pageSize: Number(pageSizeSelect.value) || 20,
    };

    function getRows() {
      return Array.from(tbody.querySelectorAll('tr'));
    }

    function renderPager(totalPages) {
      pager.innerHTML = '';

      function appendButton(label, pageNo, disabled) {
        var button = document.createElement('button');
        button.type = 'button';
        button.textContent = label;
        button.style.width = 'auto';
        button.style.minWidth = '2.25rem';
        button.style.display = 'inline-block';
        button.disabled = !!disabled;
        if (!button.disabled) {
          button.addEventListener('click', function () {
            state.page = pageNo;
            render();
          });
        }
        pager.appendChild(button);
      }

      function appendEllipsis() {
        var span = document.createElement('span');
        span.textContent = '...';
        span.className = 'avid-pager-ellipsis';
        pager.appendChild(span);
      }

      appendButton('‹', Math.max(1, state.page - 1), state.page <= 1);

      if (totalPages <= 3) {
        for (var i = 1; i <= totalPages; i += 1) {
          appendButton(String(i), i, i === state.page);
        }
      } else {
        appendButton('1', 1, state.page === 1);
        appendButton('2', 2, state.page === 2);
        appendEllipsis();
        appendButton(String(totalPages), totalPages, state.page === totalPages);
      }

      appendButton('›', Math.min(totalPages, state.page + 1), state.page >= totalPages);
    }

    function syncSortIndicators() {
      table.querySelectorAll('th[data-sort-col]').forEach(function (th) {
        var arrow = th.querySelector('.avid-sort-arrow');
        if (!arrow) {
          arrow = document.createElement('span');
          arrow.className = 'avid-sort-arrow';
          arrow.style.marginLeft = '0.35rem';
          th.appendChild(arrow);
        }
        var dir = th.getAttribute('data-sort-dir');
        if (dir === 'asc') {
          arrow.textContent = '↑';
        } else if (dir === 'desc') {
          arrow.textContent = '↓';
        } else {
          arrow.textContent = '↕';
        }
      });
    }

    function render() {
      var rows = getRows();
      var totalRows = rows.length;
      var totalPages = Math.max(1, Math.ceil(totalRows / state.pageSize));
      if (state.page > totalPages) state.page = totalPages;
      if (state.page < 1) state.page = 1;

      var start = (state.page - 1) * state.pageSize;
      var end = start + state.pageSize;
      rows.forEach(function (row, idx) {
        row.style.display = idx >= start && idx < end ? '' : 'none';
      });

      renderPager(totalPages);
    }

    if (!table.dataset.avidSortBound) {
      table.dataset.avidSortBound = 'true';
      table.addEventListener('click', function (event) {
        var th = event.target.closest('th[data-sort-col]');
        if (!th || !table.contains(th)) return;

        var col = Number(th.getAttribute('data-sort-col'));
        var current = th.getAttribute('data-sort-dir') || '';
        var next = current === 'asc' ? 'desc' : 'asc';

        table.querySelectorAll('th[data-sort-col]').forEach(function (h) {
          h.removeAttribute('data-sort-dir');
        });
        th.setAttribute('data-sort-dir', next);
        syncSortIndicators();

        var rows = getRows();
        rows.sort(function (a, b) {
          var av = (a.children[col] && a.children[col].innerText || '').trim();
          var bv = (b.children[col] && b.children[col].innerText || '').trim();
          var ad = Date.parse(av);
          var bd = Date.parse(bv);
          var cmp;
          if (!Number.isNaN(ad) && !Number.isNaN(bd)) {
            cmp = ad - bd;
          } else {
            cmp = av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' });
          }
          return next === 'asc' ? cmp : -cmp;
        });
        rows.forEach(function (row) { tbody.appendChild(row); });
        state.page = 1;
        render();
      });
    }

    if (!pageSizeSelect.dataset.avidPageSizeBound) {
      pageSizeSelect.dataset.avidPageSizeBound = 'true';
      pageSizeSelect.addEventListener('change', function () {
        state.pageSize = Number(pageSizeSelect.value) || 20;
        state.page = 1;
        render();
      });
    }

    syncSortIndicators();
    render();
  };
}
window.__avidReportTableInit('vulnerabilities-2022');
</script>
<!-- vulnerabilities-year:2022:end -->



















