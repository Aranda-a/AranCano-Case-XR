# 展示素材说明

公开仓只保留故事板大图。单张界面原图在实现仓：`docs/portfolio-assets/ui/`。

## 已上架故事板

| 文件 | 内容 |
|------|------|
| `storyboard-main-path.png` | 主路径：打开 → 对准 → 选台面 → 出模贴住 → 长按蓄力 → 封印收束 |
| `storyboard-guide-loop.png` | 闭环分镜：想挠 → 快门 → 识别 → 长按 → 出餐 |
| `storyboard-press-multimodal.png` | 按压：开捏前 → 贴住可按 → 蓄力中 |
| `storyboard-decision-fallback.png` | 决策与退路：默认 C / 退路 A + 微调贴位 |
| `storyboard-seal-record.png` | 封印 → 月历 → 今日入册 |
| `storyboard-brand-entry.png` | 开屏 → 认识 Annno → 去开捏 |

重新生成：在公开仓根目录运行 `python tools/make_storyboard.py`（需本地仍有 `assets/ui/` 源帧，或从实现仓拷回后再跑）。

## 待补

| 文件 | 内容 |
|------|------|
| `hero.webp` 或外链 | 约 15 秒主流程 |
| 完整走查 | 约 45–60 秒，Release 或外链 |
| B/C 同镜对比 | 短循环 |
| 硬失败 → 改走轻量平面 | 真机片段；暂无时用决策故事板说明入口 |

## 规范

- 公开页不贴单张 UI 缩略图墙
- 故事板清晰度优先（当前单帧高度约 780px，整图宽上限 2400px）
- 裁掉人脸、通知栏、可识别环境与开发者指针后再纳入源帧
