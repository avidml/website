---
title: Database
layout: page
image: "/uploads/avid.png"
url: /database
---

AVID stores instantiations of AI risks using two base data classes: **Vulnerability** and **Report**. A *vulnerability* (vuln) is a high-level evidence of an AI failure mode, in line with the NIST CVEs. A *report* is one example of a particular vulnerability occurring, supported by qualitative or quantitative evaluation.

Information about either is schematized and stored in AVID. To learn more about the motivations and technical details of vulns and reports, refer to our [documentation](https://avidml.gitbook.io/).

## Vulnerability
Vulnerabilities are linked to the taxonomy through multiple tags, denoting the AI risk domains (Security, Ethics, Performance) this vulnerability pertains to, (sub)categories under that domain, as well as AI lifecycle stages. A vulnerability in AVID can pertain to one or more of the three levels: *dataset*, *model*, or *system*.

### List of Vulnerabilities

##### 2023
| | | | |
|---|---|---|---|
| [AVID-2023-V001](/database/AVID-2023-V001) | [AVID-2023-V002](/database/AVID-2023-V002) | [AVID-2023-V003](/database/AVID-2023-V003) | [AVID-2023-V004](/database/AVID-2023-V004) |
| [AVID-2023-V005](/database/AVID-2023-V005) | [AVID-2023-V006](/database/AVID-2023-V006) | [AVID-2023-V007](/database/AVID-2023-V007) | [AVID-2023-V008](/database/AVID-2023-V008) |
| [AVID-2023-V009](/database/AVID-2023-V009) | [AVID-2023-V010](/database/AVID-2023-V010) | [AVID-2023-V011](/database/AVID-2023-V011) | [AVID-2023-V012](/database/AVID-2023-V012) |
| [AVID-2023-V013](/database/AVID-2023-V013) | [AVID-2023-V014](/database/AVID-2023-V014) | [AVID-2023-V015](/database/AVID-2023-V015) | [AVID-2023-V016](/database/AVID-2023-V016) |
| [AVID-2023-V017](/database/AVID-2023-V017) | [AVID-2023-V018](/database/AVID-2023-V018) | [AVID-2023-V019](/database/AVID-2023-V019) | [AVID-2023-V020](/database/AVID-2023-V020) |
| [AVID-2023-V021](/database/AVID-2023-V021) | [AVID-2023-V022](/database/AVID-2023-V022) | [AVID-2023-V023](/database/AVID-2023-V023) | [AVID-2023-V024](/database/AVID-2023-V024) |
| [AVID-2023-V025](/database/AVID-2023-V025) | [AVID-2023-V026](/database/AVID-2023-V026) | [AVID-2023-V027](/database/AVID-2023-V027) | |

##### 2022
| | | | |
|---|---|---|---|
| [AVID-2022-V001](/database/AVID-2022-V001) | [AVID-2022-V002](/database/AVID-2022-V002) | [AVID-2022-V003](/database/AVID-2022-V003) | [AVID-2022-V004](/database/AVID-2022-V004) |
| [AVID-2022-V005](/database/AVID-2022-V005) | [AVID-2022-V006](/database/AVID-2022-V006) | [AVID-2022-V007](/database/AVID-2022-V007) | [AVID-2022-V008](/database/AVID-2022-V008) |
| [AVID-2022-V009](/database/AVID-2022-V009) | [AVID-2022-V010](/database/AVID-2022-V010) | [AVID-2022-V011](/database/AVID-2022-V011) | [AVID-2022-V012](/database/AVID-2022-V012) |
| [AVID-2022-V013](/database/AVID-2022-V013) | | | |

## Reports
Reports are occurrences of a vulnerability. Based on the references provided in a specific report, reports can potentially more granular and reproducible than vulnerabilities.

### List of Reports

#### 2026
| | | | |
|---|---|---|---|
| [AVID-2026-R0001](/database/AVID-2026-R0001) | [AVID-2026-R0002](/database/AVID-2026-R0002) | [AVID-2026-R0003](/database/AVID-2026-R0003) | [AVID-2026-R0004](/database/AVID-2026-R0004) |
| [AVID-2026-R0005](/database/AVID-2026-R0005) | [AVID-2026-R0006](/database/AVID-2026-R0006) | [AVID-2026-R0007](/database/AVID-2026-R0007) | [AVID-2026-R0008](/database/AVID-2026-R0008) |
| [AVID-2026-R0009](/database/AVID-2026-R0009) | [AVID-2026-R0010](/database/AVID-2026-R0010) | [AVID-2026-R0011](/database/AVID-2026-R0011) | [AVID-2026-R0012](/database/AVID-2026-R0012) |
| [AVID-2026-R0013](/database/AVID-2026-R0013) | [AVID-2026-R0014](/database/AVID-2026-R0014) | [AVID-2026-R0015](/database/AVID-2026-R0015) | [AVID-2026-R0016](/database/AVID-2026-R0016) |
| [AVID-2026-R0017](/database/AVID-2026-R0017) | [AVID-2026-R0018](/database/AVID-2026-R0018) | [AVID-2026-R0019](/database/AVID-2026-R0019) | [AVID-2026-R0020](/database/AVID-2026-R0020) |
| [AVID-2026-R0021](/database/AVID-2026-R0021) | [AVID-2026-R0022](/database/AVID-2026-R0022) | [AVID-2026-R0023](/database/AVID-2026-R0023) | [AVID-2026-R0024](/database/AVID-2026-R0024) |
| [AVID-2026-R0025](/database/AVID-2026-R0025) | [AVID-2026-R0026](/database/AVID-2026-R0026) | [AVID-2026-R0027](/database/AVID-2026-R0027) | [AVID-2026-R0028](/database/AVID-2026-R0028) |
| [AVID-2026-R0029](/database/AVID-2026-R0029) | [AVID-2026-R0030](/database/AVID-2026-R0030) | [AVID-2026-R0031](/database/AVID-2026-R0031) | [AVID-2026-R0032](/database/AVID-2026-R0032) |
| [AVID-2026-R0033](/database/AVID-2026-R0033) | [AVID-2026-R0034](/database/AVID-2026-R0034) | [AVID-2026-R0035](/database/AVID-2026-R0035) | [AVID-2026-R0036](/database/AVID-2026-R0036) |
| [AVID-2026-R0037](/database/AVID-2026-R0037) | [AVID-2026-R0038](/database/AVID-2026-R0038) | [AVID-2026-R0039](/database/AVID-2026-R0039) | [AVID-2026-R0040](/database/AVID-2026-R0040) |
| [AVID-2026-R0041](/database/AVID-2026-R0041) | [AVID-2026-R0042](/database/AVID-2026-R0042) | [AVID-2026-R0043](/database/AVID-2026-R0043) | [AVID-2026-R0044](/database/AVID-2026-R0044) |
| [AVID-2026-R0045](/database/AVID-2026-R0045) | [AVID-2026-R0046](/database/AVID-2026-R0046) | [AVID-2026-R0047](/database/AVID-2026-R0047) | [AVID-2026-R0048](/database/AVID-2026-R0048) |
| [AVID-2026-R0049](/database/AVID-2026-R0049) | [AVID-2026-R0050](/database/AVID-2026-R0050) | [AVID-2026-R0051](/database/AVID-2026-R0051) | [AVID-2026-R0052](/database/AVID-2026-R0052) |
| [AVID-2026-R0053](/database/AVID-2026-R0053) | [AVID-2026-R0054](/database/AVID-2026-R0054) | [AVID-2026-R0055](/database/AVID-2026-R0055) | [AVID-2026-R0056](/database/AVID-2026-R0056) |
| [AVID-2026-R0057](/database/AVID-2026-R0057) | [AVID-2026-R0058](/database/AVID-2026-R0058) | [AVID-2026-R0059](/database/AVID-2026-R0059) | [AVID-2026-R0060](/database/AVID-2026-R0060) |
| [AVID-2026-R0061](/database/AVID-2026-R0061) | [AVID-2026-R0062](/database/AVID-2026-R0062) | [AVID-2026-R0063](/database/AVID-2026-R0063) | [AVID-2026-R0064](/database/AVID-2026-R0064) |
| [AVID-2026-R0065](/database/AVID-2026-R0065) | [AVID-2026-R0066](/database/AVID-2026-R0066) | [AVID-2026-R0067](/database/AVID-2026-R0067) | [AVID-2026-R0068](/database/AVID-2026-R0068) |
| [AVID-2026-R0069](/database/AVID-2026-R0069) | [AVID-2026-R0070](/database/AVID-2026-R0070) | [AVID-2026-R0071](/database/AVID-2026-R0071) | [AVID-2026-R0072](/database/AVID-2026-R0072) |
| [AVID-2026-R0073](/database/AVID-2026-R0073) | [AVID-2026-R0074](/database/AVID-2026-R0074) | [AVID-2026-R0075](/database/AVID-2026-R0075) | [AVID-2026-R0076](/database/AVID-2026-R0076) |
| [AVID-2026-R0077](/database/AVID-2026-R0077) | [AVID-2026-R0078](/database/AVID-2026-R0078) | [AVID-2026-R0079](/database/AVID-2026-R0079) | [AVID-2026-R0080](/database/AVID-2026-R0080) |
| [AVID-2026-R0081](/database/AVID-2026-R0081) | [AVID-2026-R0082](/database/AVID-2026-R0082) | [AVID-2026-R0083](/database/AVID-2026-R0083) | [AVID-2026-R0084](/database/AVID-2026-R0084) |
| [AVID-2026-R0085](/database/AVID-2026-R0085) | [AVID-2026-R0086](/database/AVID-2026-R0086) | [AVID-2026-R0087](/database/AVID-2026-R0087) | [AVID-2026-R0088](/database/AVID-2026-R0088) |
| [AVID-2026-R0089](/database/AVID-2026-R0089) | [AVID-2026-R0090](/database/AVID-2026-R0090) | [AVID-2026-R0091](/database/AVID-2026-R0091) | [AVID-2026-R0092](/database/AVID-2026-R0092) |
| [AVID-2026-R0093](/database/AVID-2026-R0093) | [AVID-2026-R0094](/database/AVID-2026-R0094) | [AVID-2026-R0095](/database/AVID-2026-R0095) | [AVID-2026-R0096](/database/AVID-2026-R0096) |
| [AVID-2026-R0097](/database/AVID-2026-R0097) | [AVID-2026-R0098](/database/AVID-2026-R0098) | [AVID-2026-R0099](/database/AVID-2026-R0099) | [AVID-2026-R0100](/database/AVID-2026-R0100) |
| [AVID-2026-R0101](/database/AVID-2026-R0101) | [AVID-2026-R0102](/database/AVID-2026-R0102) | [AVID-2026-R0103](/database/AVID-2026-R0103) | [AVID-2026-R0104](/database/AVID-2026-R0104) |
| [AVID-2026-R0105](/database/AVID-2026-R0105) | [AVID-2026-R0106](/database/AVID-2026-R0106) | [AVID-2026-R0107](/database/AVID-2026-R0107) | [AVID-2026-R0108](/database/AVID-2026-R0108) |
| [AVID-2026-R0109](/database/AVID-2026-R0109) | [AVID-2026-R0110](/database/AVID-2026-R0110) | [AVID-2026-R0111](/database/AVID-2026-R0111) | [AVID-2026-R0112](/database/AVID-2026-R0112) |
| [AVID-2026-R0113](/database/AVID-2026-R0113) | [AVID-2026-R0114](/database/AVID-2026-R0114) | [AVID-2026-R0115](/database/AVID-2026-R0115) | [AVID-2026-R0116](/database/AVID-2026-R0116) |
| [AVID-2026-R0117](/database/AVID-2026-R0117) | [AVID-2026-R0118](/database/AVID-2026-R0118) | [AVID-2026-R0119](/database/AVID-2026-R0119) | [AVID-2026-R0120](/database/AVID-2026-R0120) |
| [AVID-2026-R0121](/database/AVID-2026-R0121) | [AVID-2026-R0122](/database/AVID-2026-R0122) | [AVID-2026-R0123](/database/AVID-2026-R0123) | [AVID-2026-R0124](/database/AVID-2026-R0124) |
| [AVID-2026-R0125](/database/AVID-2026-R0125) | [AVID-2026-R0126](/database/AVID-2026-R0126) | [AVID-2026-R0127](/database/AVID-2026-R0127) | [AVID-2026-R0128](/database/AVID-2026-R0128) |
| [AVID-2026-R0129](/database/AVID-2026-R0129) | [AVID-2026-R0130](/database/AVID-2026-R0130) | [AVID-2026-R0131](/database/AVID-2026-R0131) | [AVID-2026-R0132](/database/AVID-2026-R0132) |
| [AVID-2026-R0133](/database/AVID-2026-R0133) | [AVID-2026-R0134](/database/AVID-2026-R0134) | [AVID-2026-R0135](/database/AVID-2026-R0135) | [AVID-2026-R0136](/database/AVID-2026-R0136) |
| [AVID-2026-R0137](/database/AVID-2026-R0137) | [AVID-2026-R0138](/database/AVID-2026-R0138) | [AVID-2026-R0139](/database/AVID-2026-R0139) | [AVID-2026-R0140](/database/AVID-2026-R0140) |
| [AVID-2026-R0141](/database/AVID-2026-R0141) | [AVID-2026-R0142](/database/AVID-2026-R0142) | [AVID-2026-R0143](/database/AVID-2026-R0143) | [AVID-2026-R0144](/database/AVID-2026-R0144) |
| [AVID-2026-R0145](/database/AVID-2026-R0145) | [AVID-2026-R0146](/database/AVID-2026-R0146) | [AVID-2026-R0147](/database/AVID-2026-R0147) | [AVID-2026-R0148](/database/AVID-2026-R0148) |
| [AVID-2026-R0149](/database/AVID-2026-R0149) | [AVID-2026-R0150](/database/AVID-2026-R0150) | [AVID-2026-R0151](/database/AVID-2026-R0151) | [AVID-2026-R0152](/database/AVID-2026-R0152) |
| [AVID-2026-R0153](/database/AVID-2026-R0153) | [AVID-2026-R0154](/database/AVID-2026-R0154) | [AVID-2026-R0155](/database/AVID-2026-R0155) | [AVID-2026-R0156](/database/AVID-2026-R0156) |
| [AVID-2026-R0157](/database/AVID-2026-R0157) | [AVID-2026-R0158](/database/AVID-2026-R0158) | [AVID-2026-R0159](/database/AVID-2026-R0159) | [AVID-2026-R0160](/database/AVID-2026-R0160) |
| [AVID-2026-R0161](/database/AVID-2026-R0161) | [AVID-2026-R0162](/database/AVID-2026-R0162) | [AVID-2026-R0163](/database/AVID-2026-R0163) | [AVID-2026-R0164](/database/AVID-2026-R0164) |
| [AVID-2026-R0165](/database/AVID-2026-R0165) | [AVID-2026-R0166](/database/AVID-2026-R0166) | [AVID-2026-R0167](/database/AVID-2026-R0167) | [AVID-2026-R0168](/database/AVID-2026-R0168) |
| [AVID-2026-R0169](/database/AVID-2026-R0169) | [AVID-2026-R0170](/database/AVID-2026-R0170) | [AVID-2026-R0171](/database/AVID-2026-R0171) | [AVID-2026-R0172](/database/AVID-2026-R0172) |
| [AVID-2026-R0173](/database/AVID-2026-R0173) | [AVID-2026-R0174](/database/AVID-2026-R0174) | [AVID-2026-R0175](/database/AVID-2026-R0175) | [AVID-2026-R0176](/database/AVID-2026-R0176) |
| [AVID-2026-R0177](/database/AVID-2026-R0177) | [AVID-2026-R0178](/database/AVID-2026-R0178) | [AVID-2026-R0179](/database/AVID-2026-R0179) | [AVID-2026-R0180](/database/AVID-2026-R0180) |
| [AVID-2026-R0181](/database/AVID-2026-R0181) | [AVID-2026-R0182](/database/AVID-2026-R0182) | [AVID-2026-R0183](/database/AVID-2026-R0183) | [AVID-2026-R0184](/database/AVID-2026-R0184) |
| [AVID-2026-R0185](/database/AVID-2026-R0185) | [AVID-2026-R0186](/database/AVID-2026-R0186) | [AVID-2026-R0187](/database/AVID-2026-R0187) | [AVID-2026-R0188](/database/AVID-2026-R0188) |
| [AVID-2026-R0189](/database/AVID-2026-R0189) | [AVID-2026-R0190](/database/AVID-2026-R0190) | [AVID-2026-R0191](/database/AVID-2026-R0191) | [AVID-2026-R0192](/database/AVID-2026-R0192) |
| [AVID-2026-R0193](/database/AVID-2026-R0193) | [AVID-2026-R0194](/database/AVID-2026-R0194) | [AVID-2026-R0195](/database/AVID-2026-R0195) | [AVID-2026-R0196](/database/AVID-2026-R0196) |
| [AVID-2026-R0197](/database/AVID-2026-R0197) | [AVID-2026-R0198](/database/AVID-2026-R0198) | [AVID-2026-R0199](/database/AVID-2026-R0199) | [AVID-2026-R0200](/database/AVID-2026-R0200) |
| [AVID-2026-R0201](/database/AVID-2026-R0201) | [AVID-2026-R0202](/database/AVID-2026-R0202) | [AVID-2026-R0203](/database/AVID-2026-R0203) | [AVID-2026-R0204](/database/AVID-2026-R0204) |
| [AVID-2026-R0205](/database/AVID-2026-R0205) | [AVID-2026-R0206](/database/AVID-2026-R0206) | [AVID-2026-R0207](/database/AVID-2026-R0207) | [AVID-2026-R0208](/database/AVID-2026-R0208) |
| [AVID-2026-R0209](/database/AVID-2026-R0209) | [AVID-2026-R0210](/database/AVID-2026-R0210) | [AVID-2026-R0211](/database/AVID-2026-R0211) | [AVID-2026-R0212](/database/AVID-2026-R0212) |
| [AVID-2026-R0213](/database/AVID-2026-R0213) |  |  |  |

#### 2025
| | | | |
|---|---|---|---|
| [AVID-2025-R0001](/database/AVID-2025-R0001) | [AVID-2025-R0002](/database/AVID-2025-R0002) | [AVID-2025-R0003](/database/AVID-2025-R0003) | [AVID-2025-R0004](/database/AVID-2025-R0004) |
| [AVID-2025-R0005](/database/AVID-2025-R0005) | [AVID-2025-R0006](/database/AVID-2025-R0006) | [AVID-2025-R0007](/database/AVID-2025-R0007) | [AVID-2025-R0008](/database/AVID-2025-R0008) |
| [AVID-2025-R0012](/database/AVID-2025-R0012) | [AVID-2025-R0013](/database/AVID-2025-R0013) | [AVID-2025-R0014](/database/AVID-2025-R0014) | [AVID-2025-R0015](/database/AVID-2025-R0015) |
| [AVID-2025-R0016](/database/AVID-2025-R0016) | [AVID-2025-R0017](/database/AVID-2025-R0017) | [AVID-2025-R0021](/database/AVID-2025-R0021) | [AVID-2025-R0022](/database/AVID-2025-R0022) |
| [AVID-2025-R0023](/database/AVID-2025-R0023) | [AVID-2025-R0024](/database/AVID-2025-R0024) | [AVID-2025-R0025](/database/AVID-2025-R0025) | [AVID-2025-R0030](/database/AVID-2025-R0030) |
| [AVID-2025-R0031](/database/AVID-2025-R0031) | [AVID-2025-R0032](/database/AVID-2025-R0032) | [AVID-2025-R0033](/database/AVID-2025-R0033) | [AVID-2025-R0034](/database/AVID-2025-R0034) |
| [AVID-2025-R0035](/database/AVID-2025-R0035) |  |  |  |

#### 2023
| | | | |
|---|---|---|---|
| [AVID-2023-R0001](/database/AVID-2023-R0001) | [AVID-2023-R0002](/database/AVID-2023-R0002) | [AVID-2023-R0003](/database/AVID-2023-R0003) | |

#### 2022
| | | | |
|---|---|---|---|
| [AVID-2022-R0001](/database/AVID-2022-R0001) | [AVID-2022-R0002](/database/AVID-2022-R0002) | [AVID-2022-R0003](/database/AVID-2022-R0003) | [AVID-2022-R0004](/database/AVID-2022-R0004) |
| [AVID-2022-R0005](/database/AVID-2022-R0005) | | | |