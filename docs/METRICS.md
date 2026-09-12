# 作品集轻量数据卡 · 样本从哪来

## 在哪找

微信开发者工具打开本项目真机/模拟器调试：

1. 调试器 → **Storage**（或 AppData）  
2. 复制这两个键（只要匿名事件，不要皮肤图）：  
   - `aran_analytics_queue` → 主用（含 `session_summary`、`mood_submit`、`fallback_entered`）  
   - `aran_mood_history` → 备用（前后探针历史）

把 `aran_analytics_queue` 存成 JSON 文件，例如 `private/queue-export.json`（**不要提交到公开仓**）。

## 怎么汇总成三张卡

在公开仓根目录：

```bash
node tools/summarize-portfolio-metrics.js path/to/queue-export.json
```

终端会打出完成率、想挠平均变化、退到 A 次数，以及可粘进 README 的表格行。

## 口径（与实现一致）

| 卡 | 怎么算 |
|----|--------|
| 完成率 | `session_summary` 里 `completed=1`（按满并封印）÷ 有小结的局数 |
| 想挠前后变化 | 仅 `moodResponded=1`（前后都认真拖过、未跳过）；`urgeBefore - urgeAfter`，正数=平均更不想挠 |
| 退到 A | `fallbackEntered=1` 的局数（C 失败进轻量平面） |

小样本必须写 **n=**；不作疗效/显著性结论。
