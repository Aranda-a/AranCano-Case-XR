# AranCano · Interactive Product Case Study

> 将短暂的皮肤烦躁，转译成一个可以完成、可以停止的摄像头按压仪式。

AranCano 是一个微信小程序交互原型。用户对准真实蚊子包后，屏幕生成可按压的视觉替身；持续按压会驱动模型形变、声音、振动和界面反馈，最终以塌陷和封印完成收束。

本案例重点展示游戏化产品思维、空间交互取舍与多模态反馈设计。它不提供诊断、治疗或止痒效果承诺。

> 为保护用户隐私与原创方案，本公开仓不包含产品源码、算法参数、坐标映射、完整 ADR、原始访谈、真实用户照片及未发布资产。

## Reading Guide

- **2 分钟**：继续阅读本页，了解产品、游戏化闭环和三轨决策；
- **5 分钟**：阅读完整的 [`Case Study`](docs/CASE-STUDY.md)；
- **设计 / 产品面试**：阅读 [`Validation Plan`](docs/VALIDATION.md)；
- **素材审核**：查看 [`Portfolio Asset Plan`](assets/README.md) 与 [`Public Disclosure Notice`](NOTICE.md)。

---

## 1. Product Question

短暂但反复出现的抓挠冲动，缺少一个有反馈、能完成、也能结束的替代动作。

项目没有用积分和排行榜延长使用，而是设计了一条短闭环：

```
对准真实目标 → 生成视觉替身 → 持续按压 → 满格塌陷 → 获得封印
```

判断体验是否成立，主要看三个结果：

- 替身是否像是贴在真实目标上；
- 按压是否具有连续、可信的反馈；
- 满格之后是否形成明确的结束感。

---

## 2. Gamified Core Loop

游戏化在这里承担三项职责：

### 目标化

把模糊的烦躁转译成一个可见、可操作的对象。

### 进度化

通过视觉形变、声音和振动建立持续增强的蓄力过程。

### 终点化

用塌陷和封印建立清楚的完成信号，而不是诱导无限游玩。

封印是完成凭证，不是金币或竞争排名；记录用于回看，不制造连续登录压力。

---

## 3. Multimodal Interaction

长按不是单一进度条，而是一条共同的反馈曲线：

- **视觉**：模型逐步变形、铺开，环境反馈随之收束；
- **听觉**：按压质感逐步增强，满格出现独立高潮；
- **触觉**：振动由稀疏变得更明确；
- **信息**：文案只解释状态和下一步动作。

四个通道表达同一个进度，避免用户看到、听到和摸到的节奏彼此冲突。

---

## 4. Three Spatial Strategies

三条轨道解决的是同一个产品任务，区别在于如何分配误差与工程成本。

### A · Lightweight Surface

优先兼容与稳定完成。代价是深度有限，更容易出现贴片感。

### B · Continuous Following

优先响应目标移动。代价是延迟和抖动会持续暴露，模型可能与相机背景产生割裂。

### C · Spatial Attachment

优先镜头运动下的空间一致性。风险集中在进入阶段，包括初始化与设备兼容。

当前暂定 C 为主路径。依据不是“技术越新越好”，而是：

> 一次可解释、可重试、可降级的进入风险，比互动全程持续发生的空间漂移更容易被接受。

A 保留为兼容退路，B 保留为产品对照。当前属于配对可用性验证，不是随机分流的 A/B 实验。

完整决策与产品过程见 [`docs/CASE-STUDY.md`](docs/CASE-STUDY.md)。

---

## 5. Productization Beyond the Happy Path

- 空间能力不可用时仍能完成核心仪式；
- 页面隐藏、重扫和返回时终止媒体与异步任务；
- 用户图像默认在本地流程内处理；
- 历史方案保留为决策证据，但不进入公开产品包；
- 决策记录包含证据、限制与回退条件。

当前仍是真机验证期原型，空间稳定性、设备差异和多模态反馈强度需要继续测试。

---

## 6. Portfolio Evidence

以下公开材料将在完成脱敏和授权检查后逐步补充：

1. **15 秒完整体验**：对准、出现、按压、塌陷、封印。
2. **Core Loop 分镜**：目标、蓄力、高潮、结果和结束。
3. **按压反馈时间线**：视觉、声音、振动与文案如何同步。
4. **三轨同动作对比**：相同环境和镜头运动下的体验差异。
5. **C 轨决策卡**：问题、证据、取舍、决定和可逆条件。
6. **失败与降级演示**：空间能力失败后如何解释与恢复。
7. **封印与记录结果**：奖励如何完成仪式，而不是延长使用。

素材规格与隐私检查见 [`assets/README.md`](assets/README.md)。

---

## 7. What This Case Demonstrates

- 游戏化产品与互动仪式设计
- 摄像头媒介与空间交互原型
- 多模态反馈编排
- 用户体验验证与技术取舍
- 原生微信小程序产品化
- Local-first 隐私边界

---

## Privacy and Disclosure

- 不公开人脸、位置、通知、设备标识和真实用户材料；
- 不提交 AppID、Webhook、密钥或本地配置；
- 不公开算法阈值、映射公式、调参表和完整测试素材；
- 用户反馈只使用匿名汇总或取得许可的改写；
- 第三方字体、音频、模型和品牌素材须先确认展示授权。

## Status

Independent interaction design and product prototyping case study.  
Current stage: on-device validation.

## Rights

All rights reserved.

Unless separately authorized in writing, the interaction concept, Annno IP, visual assets, documentation, and media in this repository may not be copied, redistributed, used for model training, or used commercially. Third-party assets remain the property of their respective owners.
