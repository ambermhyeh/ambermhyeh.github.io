// =============================================================
// 版型 B 的互動功能
//   1. 專案卡片的 Demo / Code / Details 分頁切換
//   2. 捲動時，左側選單自動標示目前所在的區塊
// 一般修改內容時不需要動這個檔案
// =============================================================

// ---------- 1. 分頁切換 ----------
document.querySelectorAll('.project').forEach(function (card) {
  const tabs = card.querySelectorAll('.tab');
  const panels = card.querySelectorAll('.panel');

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      const target = tab.dataset.tab;

      tabs.forEach(function (t) {
        t.classList.toggle('is-active', t === tab);
      });
      panels.forEach(function (panel) {
        const isTarget = panel.dataset.panel === target;
        panel.classList.toggle('is-active', isTarget);
        // 切到別的分頁時，把正在播放的影片暫停
        const video = panel.querySelector('video');
        if (video && !isTarget) video.pause();
      });
    });
  });
});

// ---------- 2. 左側選單標示目前區塊 ----------
const navLinks = document.querySelectorAll('.side-nav a');
const observer = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (!entry.isIntersecting) return;
    navLinks.forEach(function (link) {
      link.classList.toggle('is-current', link.getAttribute('href') === '#' + entry.target.id);
    });
  });
}, { rootMargin: '-40% 0px -55% 0px' });

document.querySelectorAll('main section[id]').forEach(function (section) {
  observer.observe(section);
});
