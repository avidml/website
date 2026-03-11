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
      <th data-sort-col="0" style="white-space: nowrap;">Report ID</th>
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
    <tr><td><a href="/database/AVID-2026-R0252">AVID-2026-R0252</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Bypassing ChatGPT image safeguards</td><td>Advisory</td><td>2026-03-04</td></tr>
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
    <tr><td><a href="/database/AVID-2026-R0413">AVID-2026-R0413</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI ChatGPT Content Safety Explicit Image Bypass</td><td></td><td>2026-01-28</td></tr>
    <tr><td><a href="/database/AVID-2026-R0414">AVID-2026-R0414</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Eclipse Theia IDE MCP Configuration Code Execution</td><td></td><td>2025-11-18</td></tr>
    <tr><td><a href="/database/AVID-2026-R0415">AVID-2026-R0415</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI Codex CLI Notify Field Configuration Remote Code Execution</td><td></td><td>2026-01-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0416">AVID-2026-R0416</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI Codex CLI Model Provider Configuration Remote Code Execution</td><td></td><td>2026-01-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0417">AVID-2026-R0417</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">OpenAI Codex CLI MCP Configuration Remote Code Execution</td><td></td><td>2026-01-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0418">AVID-2026-R0418</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Amazon Kiro IDE Data Exfiltration via Filename Prompt Injection and Kiro Powers Registry Fetching</td><td></td><td>2025-12-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0419">AVID-2026-R0419</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Amazon Kiro IDE Data Exfiltration via Steering File</td><td></td><td>2025-12-08</td></tr>
    <tr><td><a href="/database/AVID-2026-R0420">AVID-2026-R0420</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Gemini CLI Tool Discovery Code Execution</td><td></td><td>2025-12-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0421">AVID-2026-R0421</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Gemini CLI MCP Configuration Code Execution</td><td></td><td>2025-12-26</td></tr>
    <tr><td><a href="/database/AVID-2026-R0422">AVID-2026-R0422</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">JetBrains Junie AI Coding Agent guidelines.md Code Execution</td><td></td><td>2025-11-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0423">AVID-2026-R0423</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">TheLibrarian.io Internal Cloud Environment Access via web_fetch Tool</td><td></td><td>2025-10-10</td></tr>
    <tr><td><a href="/database/AVID-2026-R0424">AVID-2026-R0424</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Zed IDE LSP Configuration Code Execution</td><td></td><td>2025-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0425">AVID-2026-R0425</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Zed IDE MCP Configuration Code Execution</td><td></td><td>2025-11-16</td></tr>
    <tr><td><a href="/database/AVID-2026-R0426">AVID-2026-R0426</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Google Antigravity IDE Persistent Code Execution</td><td></td><td>2025-11-19</td></tr>
    <tr><td><a href="/database/AVID-2026-R0427">AVID-2026-R0427</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cline Bot AI Coding Agent Code Execution via Prompt Injection and TOCTOU Script Invocation</td><td></td><td>2025-08-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0428">AVID-2026-R0428</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cline Bot AI Coding Agent Code Execution via Prompt Injection and .clinerules Directives</td><td></td><td>2025-08-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0429">AVID-2026-R0429</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Cline Bot AI Coding Agent Data Exfiltration via Prompt Injection and DNS</td><td></td><td>2025-08-27</td></tr>
    <tr><td><a href="/database/AVID-2026-R0430">AVID-2026-R0430</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Nvidia NemoGuard Jailbreak Detect Guardrail Evasion</td><td></td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0431">AVID-2026-R0431</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Protect AI Jailbreak and Prompt Injection Guardrail Evasion</td><td></td><td>2025-03-12</td></tr>
    <tr><td><a href="/database/AVID-2026-R0432">AVID-2026-R0432</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Vijil Prompt Injection Guardrail Evasion</td><td></td><td>2025-03-14</td></tr>
    <tr><td><a href="/database/AVID-2026-R0433">AVID-2026-R0433</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Meta Prompt Guard Guardrail Evasion</td><td></td><td>2025-03-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0434">AVID-2026-R0434</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Microsoft Azure Prompt Shield Guardrail Evasion</td><td></td><td>2024-06-06</td></tr>
    <tr><td><a href="/database/AVID-2026-R0435">AVID-2026-R0435</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Microsoft Azure AI Content Safety Guardrail Evasion</td><td></td><td>2024-03-04</td></tr>
    <tr><td><a href="/database/AVID-2026-R0436">AVID-2026-R0436</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mistral Vibe CLI MCP Configuration Code Execution</td><td></td><td>2025-12-11</td></tr>
    <tr><td><a href="/database/AVID-2026-R0437">AVID-2026-R0437</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mistral Vibe CLI Shell Expansion Command Execution</td><td></td><td>2026-01-02</td></tr>
    <tr><td><a href="/database/AVID-2026-R0438">AVID-2026-R0438</a></td><td style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Mistral Vibe CLI Python Tools Code Execution</td><td></td><td>2025-12-12</td></tr>
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
      <th data-sort-col="0" style="white-space: nowrap;">Report ID</th>
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
      <th data-sort-col="0" style="white-space: nowrap;">Report ID</th>
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
      <th data-sort-col="0" style="white-space: nowrap;">Report ID</th>
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







