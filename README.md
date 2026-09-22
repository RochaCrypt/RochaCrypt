<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:3a0008,100:ff2e4c&height=210&section=header&text=Alexandre%20Rocha&fontSize=44&fontColor=ffffff&desc=Offensive%20Security%20%7C%20Lead%20Cybersecurity%20Engineer&descSize=16&descAlignY=66&animation=fadeIn" width="100%" alt="Alexandre Rocha — Offensive Security"/>

<a href="https://github.com/DenverCoder1/readme-typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=17&duration=2600&pause=900&color=FF2E4C&center=true&vCenter=true&width=640&height=40&lines=root%40rochacrypt%3A~%23+whoami;%3E+pentester+%7C+threat+hunter+%7C+red+%26+purple+team;root%40rochacrypt%3A~%23+nmap+-sC+-sV+-p-+target;%3E+22%2Ftcp+open+ssh+%7C+443%2Ftcp+open+https;root%40rochacrypt%3A~%23+.%2Fexploit+--authorised-only;%3E+%5B%2B%5D+access+granted.+writing+report..." alt="Terminal animation"/>
</a>

<br/>

<a href="https://linkedin.com/in/alexandrevrocha"><img src="https://img.shields.io/badge/LinkedIn-0d1117?style=flat-square&logo=linkedin&logoColor=ff2e4c" alt="LinkedIn"/></a>
<a href="mailto:alexandrev.rocha@hotmail.com"><img src="https://img.shields.io/badge/Email-0d1117?style=flat-square&logo=maildotru&logoColor=ff2e4c" alt="Email"/></a>
<img src="https://img.shields.io/badge/Location-Dublin%2C_IE-0d1117?style=flat-square&labelColor=0d1117&color=ff2e4c" alt="Dublin, Ireland"/>
<img src="https://komarev.com/ghpvc/?username=RochaCrypt&style=flat-square&color=ff2e4c&label=hits" alt="Profile hits"/>

<sub>
<a href="#-whoami">whoami</a> ·
<a href="#-kill-chain">kill chain</a> ·
<a href="#-arsenal">arsenal</a> ·
<a href="#-projects">projects</a> ·
<a href="#-operations">operations</a> ·
<a href="#-career-log">career</a> ·
<a href="#-certs">certs</a> ·
<a href="#-studies">studies</a> ·
<a href="#-activity">activity</a>
</sub>

</div>

---

## 💀 whoami

```console
root@rochacrypt:~# cat profile.txt
name       : Alexandre Rocha
role       : Lead Cybersecurity Engineer — Offensive Security
experience : 14+ yrs IT · 7+ yrs offensive security, vuln management & SOC
base       : Dublin, Ireland  [PT-BR native | EN professional | ES basic]
mindset    : think like an attacker, report like a consultant
frameworks : MITRE ATT&CK · OWASP Top 10 · NIST CSF · ISO 27001
researching: LLM application security & offensive AI testing
rules      : authorised targets only. always.
```

---

## 🎯 Kill Chain

How I work an engagement — from first packet to executive report.

```mermaid
flowchart LR
    A[🔍 Recon<br/>OSINT · footprinting] --> B[🚪 Initial Access<br/>web · network · auth]
    B --> C[💥 Exploitation<br/>manual · Metasploit]
    C --> D[🧗 Post-Exploitation<br/>privesc · lateral movement]
    D --> E[🛡️ Detection Review<br/>what did the EDR/SIEM see?]
    E --> F[📄 Report<br/>technical + executive]
    style A fill:#0d1117,stroke:#ff2e4c,color:#ffffff
    style B fill:#0d1117,stroke:#ff2e4c,color:#ffffff
    style C fill:#3a0008,stroke:#ff2e4c,color:#ffffff
    style D fill:#3a0008,stroke:#ff2e4c,color:#ffffff
    style E fill:#0d1117,stroke:#8b949e,color:#ffffff
    style F fill:#0d1117,stroke:#8b949e,color:#ffffff
```

| Phase | MITRE ATT&CK | What I do |
| :--- | :--- | :--- |
| **Recon** | TA0043 | Network footprinting, service enumeration, attack-surface mapping |
| **Initial Access** | TA0001 | Web application testing against OWASP Top 10, exposed services, weak auth |
| **Exploitation** | TA0002 | Manual exploitation and controlled threat simulation |
| **Post-Exploitation** | TA0004 · TA0008 | Privilege escalation and lateral movement paths |
| **Detection Review** | — | Purple-team view: validating what CrowdStrike Falcon and FortiSIEM actually caught |
| **Report** | — | Evidence-driven findings, risk ratings and remediation for tech and exec audiences |

---

## ⚔️ Arsenal

<div align="center">

### 🧰 [**Browse my full arsenal — 112 tools, searchable →**](https://rochacrypt.github.io/arsenal/)

<sub>An interactive catalog of security tooling, segmented by function · <a href="https://github.com/RochaCrypt/arsenal">repo</a></sub>

</div>

<table>
<tr>
<td valign="top" width="50%">

**🔴 Offensive**

| Use | Tools |
| :--- | :--- |
| Recon & enumeration | Nmap, Kali Linux |
| Web app testing | Burp Suite, OWASP methodology |
| Exploitation | Metasploit |
| Vuln discovery | Qualys VMDR / WAS, custom QQL |
| Reporting | SysReptor |

</td>
<td valign="top" width="50%">

**🔵 Defenses I operate & test against**

| Use | Platforms |
| :--- | :--- |
| EDR / XDR / MDR | CrowdStrike Falcon (RTR), FortiEDR |
| SIEM | FortiSIEM |
| Firewall / VPN | Fortinet FortiGate, FortiManager |
| Network defence | IDS/IPS, Web Filtering, Application Control |
| Edge / WAF / DDoS | Cloudflare, WAF & DDoS protection |
| Identity / SSO | Keycloak |
| Cloud | Private, Public & Hybrid Cloud security |

</td>
</tr>
</table>

<div align="center">

<img src="https://img.shields.io/badge/Kali_Linux-0d1117?style=flat-square&logo=kalilinux&logoColor=ff2e4c"/>
<img src="https://img.shields.io/badge/Burp_Suite-0d1117?style=flat-square&logo=burpsuite&logoColor=ff2e4c"/>
<img src="https://img.shields.io/badge/Metasploit-0d1117?style=flat-square&logo=metasploit&logoColor=ff2e4c"/>
<img src="https://img.shields.io/badge/Nmap-0d1117?style=flat-square&labelColor=0d1117"/>
<img src="https://img.shields.io/badge/OWASP-0d1117?style=flat-square&logo=owasp&logoColor=ff2e4c"/>
<img src="https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=ff2e4c"/>
<img src="https://img.shields.io/badge/PowerShell-0d1117?style=flat-square"/>
<img src="https://img.shields.io/badge/Bash-0d1117?style=flat-square&logo=gnubash&logoColor=ff2e4c"/>
<img src="https://img.shields.io/badge/Docker-0d1117?style=flat-square&logo=docker&logoColor=ff2e4c"/>
<img src="https://img.shields.io/badge/AWS-0d1117?style=flat-square"/>

</div>

---

## 🗂️ Projects

```console
root@rochacrypt:~# ls ~/projects
```

<div align="center">

<a href="https://github.com/RochaCrypt/arsenal"><img src="https://img.shields.io/badge/🧰_Arsenal-0d1117?style=for-the-badge&logo=gnubash&logoColor=ff2e4c" alt="Arsenal"/></a>
<a href="https://github.com/RochaCrypt/security-knowledge-base"><img src="https://img.shields.io/badge/🧠_Knowledge_Base-0d1117?style=for-the-badge&logo=bookstack&logoColor=ff2e4c" alt="Knowledge Base"/></a>

</div>

| Project | What it is | Stack |
| :--- | :--- | :--- |
| [**🧰 Arsenal**](https://github.com/RochaCrypt/arsenal) | Interactive catalog of 112 security tools + my own scripts | `Bash` `Python` `PowerShell` `HTML` |
| [**🧠 Security Knowledge Base**](https://github.com/RochaCrypt/security-knowledge-base) | 50 certification & framework mind maps | `Docs` `Mermaid` |

<!--
ADD your own projects below — one row per project, or a detailed block:

<details>
<summary><b>Project name</b> · Year · <code>Tag</code> <code>Tag</code></summary>
<br/>

- **What it is:** one-line description
- **What I built:** your role and the key features
- **Result:** outcome or metric
- 🔗 [Repository](https://github.com/RochaCrypt/REPO)

</details>
-->

---

## 🗂️ Operations

<!--
ADD only real engagements/projects. Client names omitted for confidentiality.

<details>
<summary><b>[OP-01] Engagement name</b> · Year · <code>Web</code> <code>Internal</code></summary>
<br/>

- **Scope:** what was tested
- **Approach:** techniques / ATT&CK tactics used
- **Impact:** key finding type and business risk (no sensitive details)
- **Outcome:** what got fixed / measurable result

</details>
-->

> 🔒 Engagement details are confidential. Sanitised write-ups coming soon.

---

## 🧠 Studies

```console
root@rochacrypt:~# cd ~/knowledge-base && ls
```

A catalog of **50 security certifications & frameworks** — each with what it is, what it validates, key concepts and a mind map. Marked ✔️ are ones I hold.

<div align="center">

| | Map | What's inside |
| :-: | :--- | :--- |
| ⚔️ | [**CEH**](https://github.com/RochaCrypt/security-knowledge-base/blob/main/catalog/ceh.md) ✔️ | 5 phases of hacking, 20 modules, Nmap cheat sheet |
| 🦅 | [**CCFA**](https://github.com/RochaCrypt/security-knowledge-base/blob/main/catalog/ccfa.md) ✔️ | Falcon policies, exclusions, RTR in practice |
| 🤖 | [**CLLMSP**](https://github.com/RochaCrypt/security-knowledge-base/blob/main/catalog/cllmsp.md) ✔️ | OWASP Top 10 for LLM applications |
| 🗡️ | [**OSCP**](https://github.com/RochaCrypt/security-knowledge-base/blob/main/catalog/oscp.md) | Hands-on pentest benchmark |
| 🏛️ | [**CISSP**](https://github.com/RochaCrypt/security-knowledge-base/blob/main/catalog/cissp.md) | Senior security management |

<a href="https://github.com/RochaCrypt/security-knowledge-base"><img src="https://img.shields.io/badge/Open_the_Knowledge_Base_(50_maps)-0d1117?style=for-the-badge&logo=github&logoColor=ff2e4c" alt="Open the Knowledge Base"/></a>

</div>

---

## 📜 Career Log

```console
root@rochacrypt:~# cat /var/log/career.log | grep privesc
[2015] tech support ─► [2017] network eng ─► [2019] jr sec analyst ─► [2020] sec analyst
       ─► [2021] cyber engineer ─► [2024] senior analyst ─► [2026] lead engineer   # uid=0(root)
```

### 🏢 Claranet
<sub>Mar 2019 – Present · 7+ years · Managed security & cloud services provider</sub>

**Lead Cybersecurity Engineer**
<br/><sub>Mar 2026 – Present · Dublin, Ireland (remote)</sub>
- Lead technical cybersecurity initiatives across Private, Public and Hybrid Cloud customer environments
- Lead penetration testing across infrastructure, network and web applications
- Design, implement and manage EDR/XDR solutions, including CrowdStrike Falcon
- Lead incident response investigations and threat analysis; Level 3 escalation for incidents and complex projects
- Perform vulnerability assessments, risk analysis and remediation planning; support SOC capability design
- Review and approve security architectures for customer projects
- Deliver executive and technical reports and mentor security teams
- Align delivery with NIST CSF, MITRE ATT&CK, OWASP and ISO 27001

**Senior Cybersecurity Analyst**
<br/><sub>Sep 2024 – Mar 2026 · São Paulo, Brazil (hybrid)</sub>
- Led security operations, threat detection and vulnerability management across managed customer environments
- Ran PoCs and technical evaluations of security solutions; managed EDR, MDR and XDR platforms
- Designed and deployed firewalls, IDS/IPS, WAF and DDoS protection
- Built SIEM use cases, correlation rules and monitoring dashboards
- Investigated incidents, coordinated response actions and supported ISO 27001 governance

<details>
<summary><b>Cybersecurity Engineer</b> · Jun 2021 – Sep 2024 · Brazil (hybrid)</summary>
<br/>

- Designed and implemented secure network and cybersecurity architectures, from project kick-off to production
- Deployed and managed firewalls, IDS/IPS, WAF, Web Filtering and Application Control
- Implemented centralised log management and SIEM integrations
- Developed and enforced security policies with FortiManager
- Supported pre-sales in customer workshops and technical demos

</details>

<details>
<summary><b>Information Security Analyst</b> · Jun 2020 – Jul 2021 · Brazil (on-site)</summary>
<br/>

- Supported cybersecurity operations, vulnerability management and customer security projects
- Monitored and investigated security alerts; assisted with vulnerability assessments and remediation

</details>

<details>
<summary><b>Junior Information Security Analyst</b> · Mar 2019 – Jun 2020 · Barueri, Brazil (on-site)</summary>
<br/>

- Monitored security events and alerts, supported vulnerability scanning and took part in incident response

</details>

### 🏢 Amistad Networks
<sub>Jul 2015 – Mar 2019 · 3 years 9 months</sub>

<details>
<summary><b>Network & Telecommunications Engineer</b> · Apr 2017 – Mar 2019 · Brazil</summary>
<br/>

- Designed, deployed and supported networking and telecom infrastructure for enterprise customers
- Configured and managed routers, switches and firewalls; supported VPN, VLAN, NAT and routing services
- Supported security controls and secure network architectures; investigated network incidents and restored service

</details>

<details>
<summary><b>Technical Support Specialist</b> · Jul 2015 – Apr 2017 · Brazil</summary>
<br/>

- First-line support for telecom and network services; supported VoIP deployments and infrastructure troubleshooting

</details>

---

## 🏴 Certs

```console
root@rochacrypt:~# ls ~/certs
```

| Certification | Issuer |
| :--- | :--- |
| **CEH** — Certified Ethical Hacker | EC-Council |
| **CCFA** — CrowdStrike Certified Falcon Administrator | CrowdStrike |
| **CLLMSP** — Certified LLM Security Professional | — |
| **Certified Associate in Cybersecurity** | Fortinet |
| **Ethical Hacking Essentials** · **Network Defense Essentials** | EC-Council |
| **Architecting on AWS** (training) | AWS |

🎓 **Postgraduate, Cybersecurity** — Instituto Daryus (2023–2024) · **BSc, Information Security Management** — UNINOVE (2018–2021)

---

## 📡 Activity

```console
root@rochacrypt:~# tail -f activity.log
```

<div align="center">

<img src="https://streak-stats.demolab.com?user=RochaCrypt&theme=dark&hide_border=true&background=0d1117&ring=ff2e4c&fire=ff2e4c&currStreakNum=ffffff&sideNums=ff2e4c&currStreakLabel=ff2e4c&sideLabels=c9d1d9&dates=8b949e&stroke=30363d" alt="Contribution streak"/>

<br/><br/>

<img src="./profile-3d-contrib/profile-night-view.svg" alt="3D contribution calendar" width="100%"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RochaCrypt/RochaCrypt/output/snake-dark.svg"/>
  <img src="https://raw.githubusercontent.com/RochaCrypt/RochaCrypt/output/snake.svg" alt="Contribution snake" width="100%"/>
</picture>

<!-- Uncomment and replace YOUR_USER / YOUR_ID -->
<!-- <img src="https://tryhackme-badges.s3.amazonaws.com/YOUR_USER.png" alt="TryHackMe"/> -->
<!-- <img src="https://www.hackthebox.com/badge/image/YOUR_ID" alt="Hack The Box"/> -->

</div>

---

<div align="center">

```console
[!] All techniques and tooling are used exclusively in authorised engagements.
```

<sub>🔐 Security is a process, not a product.</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff2e4c,50:3a0008,100:000000&height=100&section=footer" width="100%" alt=""/>

</div>
