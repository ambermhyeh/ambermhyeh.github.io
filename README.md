# Amber Yeh · Personal Website

> 版型 B：Modern（現代側邊欄風） — 用 HTML / CSS 製作、部署在 GitHub Pages 的個人網頁，用於申請 MIS / MSIS 研究所。

網址：`https://YOUR-USERNAME.github.io`

## 資料夾結構

```
.
├── index.html            ← 網頁內容（文字、連結、專案都在這裡改）
├── style.css             ← 外觀（顏色、字體、排版）
├── script.js             ← 專案卡片分頁切換（通常不用改）
├── assets/
│   ├── img/              ← 大頭照、專案示範動畫（breakout.gif、babynames.gif）
│   ├── videos/           ← （選用）改用 .mp4 影片時放這裡
│   └── files/            ← 履歷 resume.pdf
├── projects/
│   ├── breakout/         ← 作業：Breakout 打磚塊（Python）
│   └── babynames/        ← 作業：Baby Names 資料視覺化（Python）
└── .nojekyll             ← 告訴 GitHub Pages 不要用 Jekyll 處理，原樣發布
```

## 我要改哪裡？

1. 在 Cursor 裡搜尋 `✏️`，每一個都是需要改的地方
2. `Cmd + Shift + H` 全部取代：`YOUR-USERNAME` → 你的 GitHub 帳號
3. 換照片：把照片放到 `assets/img/`，改 `index.html` 裡 `avatar.svg` 的檔名
4. 換示範動畫：把自己錄的 GIF 放到 `assets/img/`，檔名取代 `breakout.gif`、`babynames.gif`（每個 < 5 MB）；想用 .mp4 影片的話，`index.html` 註解裡有 `<video>` 寫法
5. 放履歷：`assets/files/resume.pdf`

## 本機預覽

直接用瀏覽器打開 `index.html`，或在終端機執行：

```bash
python3 -m http.server 8000
# 打開 http://localhost:8000
```

## 更新網站

```bash
git add .
git commit -m "Update projects section"
git push
```

推上去約 1–2 分鐘後，GitHub Pages 會自動更新。

## 執行作業程式（選用）

```bash
cd projects/breakout && python3 breakout_extension.py     # 需要安裝 campy
cd projects/babynames && python3 babygraphics.py
```
