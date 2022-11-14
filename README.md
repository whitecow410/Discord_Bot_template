[![Python 3.10.6](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3106/)

# Discord Python Bot 骨架

Discord.py 基礎骨架

---

## ⚡ 簡介

這裡提供一個新的機器人基本骨架，方便快速開發一隻新的 Bot

- Cog 架構
- For (初學者/開發者)
- Bot 指令/類別/功能 分離
- I18n 多語言支持

## 📥 安裝

> 運行環境 :
>
> - [Python](https://www.python.org/) 版本 `>= 3.10` 或以上
> - [Discord.py](https://discordpy.readthedocs.io/en/stable/) 版本 `2.0.1` 或以上

- 安裝 Discord.py

  > 請於 PowerShell 中使用

  ```
  pip install -U discord.py
  ```

### 🔧 設置

1. 下載專案
2. 打開 `setting.jsin` 把機器人的 Token 貼上
3. 運行 `bot.py`

<br>

## 🔩 資料夾結構

```
/ # 根目錄

- bot.py # Bot 啟動文件
- setting.json # 設定檔

/cogs # Cog 指令

- main.py  # 主要指令區
- event.py # 事件觸發區
- admin.py # 需權限指令區
- owner.py # 擁有者指令區

/core  # 核心功能
- classes.py #
```
