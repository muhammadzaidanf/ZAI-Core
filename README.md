<div align="center">

# 🧠 ZAI Core  
### *v0.2.4 — Adaptive Intelligence Update*

![PyPI](https://img.shields.io/pypi/v/zaicore?label=PyPI%20Version&style=for-the-badge&color=blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green?style=for-the-badge)
![Downloads](https://static.pepy.tech/badge/zaicore?style=for-the-badge)
![License](https://img.shields.io/github/license/muhammadzaidanf/ZAI-Core?style=for-the-badge)
![Made in Indonesia](https://img.shields.io/badge/Made%20in-Indonesia-red?style=for-the-badge)

</div>

---

## 🧩 Overview
**ZAI Core v0.2.4** introduces the **Adaptive Intelligence Update**, evolving beyond static learning.  
This version enables **auto-learning**, **reinforcement tracking**, and **insight analytics**, allowing ZAI Core to analyze itself and grow smarter over time.

> “Now it learns by itself — not just when you tell it to.”

---

## ⚙️ New in v0.2.4
- 🧠 **Auto-Learn Engine** — automatically saves unknown queries as pending knowledge.  
- 🔁 **Reinforcement Tracker** — increases confidence score each time a fact is recalled.  
- 📊 **Insight Analyzer** — tracks learning statistics, recall frequency, and confidence.  
- ⚙️ **Config File Support (`zai_config.json`)** — customize default modes (remote, auto-learn).  
- 🌐 **Persistent + Networked Sync** — hybrid AI that works both offline and online.  

---

## 🧱 Folder Structure
```text
./ZAI-Core/
│
├── ./zai_config.json          # config file for remote/auto-learn options
├── ./zaicore/
│   ├── ./__init__.py
│   ├── ./__main__.py
│   ├── ./core.py              # Adaptive learning core
│   ├── ./analytics.py         # Insight and reinforcement system
│   ├── ./reasoning.py         # Contextual recall engine
│   ├── ./network.py           # Remote API sync system
│   ├── ./plugins/
│   │   ├── ./__init__.py
│   │   └── ./websearch_connector.py
│   └── ./utils/
│       ├── ./__init__.py
│       └── ./data_handler.py
│
├── ./setup.py
├── ./README.md
└── ./LICENSE
```

---

## 💻 Installation
```bash
pip install zaicore
```

---

## ⚡ Quick Start

### 🧠 Local Mode
```python
from zaicore import ZAICore

ai = ZAICore()
ai.learn("creator", "Muhammad Zaidan")
ai.recall("who created you?")
```

### 🌐 Remote Mode (optional)
```python
ai = ZAICore(remote_mode=True, remote_url="https://example.com/zai_core_api")
ai.learn("framework", "ZAI Core")
```

### ⚙️ Auto-Learn
If the AI doesn’t recognize something, it will store it as pending knowledge automatically:
```
🧠 > who is zaidan
🤖 I don't know that yet. Saved as pending knowledge.
```

---

## 💬 CLI Commands
```
learn key=value     → store knowledge
recall <query>      → ask the AI
list | ls           → show all memory entries
insights            → show memory insights & confidence stats
stats               → show engine statistics
config              → show current configuration
set key=value       → change config (auto_learn, remote_mode, remote_url)
wipe                → delete all memory
exit                → quit
```

---

## 📊 Insight Example
```
🧠 > insights
📊 Insight Summary:
- Total entries: 18
- Most recalled: creator (4x)
- Average confidence: 0.83
```

---

## ⚙️ Config File Example (`zai_config.json`)
```json
{
  "remote_mode": false,
  "remote_url": "https://example.com/zai_core_api",
  "auto_learn": true
}
```

---

## 🧩 Development Roadmap
| Version | Feature | Status |
|----------|----------|--------|
| **v0.1.0** | Basic Learn & Recall | ✅ Released |
| **v0.2.1** | Persistent Brain | ✅ Released |
| **v0.2.2** | Cognitive Layer | ✅ Released |
| **v0.2.3** | Networked Intelligence | ✅ Released |
| **v0.2.4** | Adaptive Intelligence | 🧠 Active |
| **v0.3.0** | Neural Bridge (Web Dashboard + Plugin API) | 🔜 Planned |

---

## 🧑‍💻 Author
**Muhammad Zaidan Faiz**  
💼 [LinkedIn](https://www.linkedin.com/in/mzaidanfaiz/)  
🌍 [GitHub](https://github.com/muhammadzaidanf)  
📧 [muhammadzaidanfaiz8@gmail.com](mailto:muhammadzaidanfaiz8@gmail.com)

---

## 📄 License
Released under the **MIT License** — free to learn, modify, and build upon.

---

<div align="center">

⭐ *ZAI Core — Adaptive Intelligence Framework.*  
<br>
💬 *“Don’t just build AI. Build something that adapts and evolves with you.”*

</div>
