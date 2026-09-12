# 展示素材说明

公开仓保留：真机 GIF（README 内嵌预览）+ 可选 mp4 + 故事板大图。单张界面原图不入库。

## 真机短片（`assets/demo/`）

| 文件 | 内容 | 约时长 | 说明 |
|------|------|--------|------|
| `demo-onboarding.gif` | 开屏 → guide → 主页引导 | 15s | README 主预览 |
| `demo-track-c.gif` | 主路径 C（立体跟包） | 31s | README 主预览 |
| `demo-track-a.gif` | 次选轻量路径 A | 18s | README 主预览 |
| `demo-*.mp4` | 同上，有声清晰版 | 同上 | 可选下载；GitHub 文件页常无法内嵌播放 |

GIF 压码：宽约 280、8fps、128 色调色板。原片不入库。

入口角色：C 暂定主 CTA；A 兼容退路；B 不进默认入口。

## 皮肤与演示授权

故事板与短片中出现的局部皮肤 / 蚊子包画面：

- 来源：作者本人演示拍摄，或已获书面许可的演示对象
- 用途：仅说明对准、贴附与按压交互
- 不做：医疗诊断、疗效证明、未授权第三方肖像展示
- 处理：裁掉可识别人脸、家庭环境、通知栏与开发者指针后再纳入

用户试用原话若公开，只使用匿名改写；不上传原始聊天截图、头像与昵称。

## 已上架故事板

| 文件 | 内容 |
|------|------|
| `storyboard-main-path.png` | 主路径：打开 → 对准 → 选台面 → 出模贴住 → 长按蓄力 → 封印收束 |
| `storyboard-guide-loop.png` | 闭环分镜：想挠 → 快门 → 识别 → 长按 → 出餐 |
| `storyboard-press-multimodal.png` | 按压：开捏前 → 贴住可按 → 蓄力中 |
| `storyboard-decision-fallback.png` | 决策与退路：默认 C / 退路 A + 微调贴位 |
| `storyboard-seal-record.png` | 封印 → 月历 → 今日入册 |
| `storyboard-seal-stamps.png` | 封印章精选三枚（道具风，非皮肤实拍） |
| `storyboard-brand-entry.png` | 开屏 → 认识 Annno → 去开捏 |
| `storyboard-track-a.png` | 轻量平面（轨 A）：开捏前 → 贴图就绪 → 跟包 → 长按蓄力 |

重新生成：在公开仓根目录运行 `python tools/make_storyboard.py`（需本地备有源帧目录后再跑）。

## 待补

| 文件 | 内容 |
|------|------|
| B/C 同镜对比 | 短循环 |
| 硬失败 → 改走轻量平面 | 真机片段；暂无时用决策故事板 + `demo-track-a` 说明 |

## 规范

- 公开页不贴单张 UI 缩略图墙
- 故事板清晰度优先（当前单帧高度约 780px，整图宽上限 2400px）
- 真机预览优先 GIF；mp4 仅作可选清晰有声
- 裁掉人脸、通知栏、可识别环境与开发者指针后再纳入源帧
