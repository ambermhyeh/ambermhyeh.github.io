# 影片放這裡（選用）

版型預設用 **GIF 動畫**（放在 `assets/img/breakout.gif`、`assets/img/babynames.gif`），用 `<img>` 顯示、會自動循環播放，最簡單。

如果想改用 .mp4 影片（有播放鍵、畫質較好、可以有聲音）：

- 檔名：`breakout.mp4`、`babynames.mp4`（要跟 index.html 裡的 `src` 一致）
- 把 `index.html` 裡的 `<img ... .gif>` 換成註解中提供的 `<video>` 寫法
- 格式：請用 **.mp4（H.264）**。Mac 螢幕錄影產生的 `.mov` 可以用 QuickTime「檔案 → 輸出為 → 1080p」或 HandBrake 轉成 mp4
- 大小：建議每支 **< 25 MB**（GitHub 單檔上限 100 MB，太大網頁也會載很慢）
- 長度：30–60 秒，只錄最精彩的操作即可
