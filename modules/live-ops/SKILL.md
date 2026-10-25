---
name: lingjiang-live-ops
description: |
  当用户提到「直播skill」，或要求审计/改写直播话术、短视频脚本、详情页/贴片文案；判断一句话是需求/痛点/属性/功能/卖点/价值/买点；按 PFABES 逐句标注；诊断转化/停留/点击问题；评估主播 60 分；搭建人货场/直播间；分析八大人群、购买动机、话术表与读稿迭代时调用。
  
  覆盖：七词判定与翻译、PFABES 六元素与 12 个 canonical 闭环、话术审计五层流程（词层→结构层→动机层→人层→合规层）、六催化剂与逼单心态、60 分主播/七大三观/对话感、八大人群、人货场、短视频结构/28 理论、直播搭建与对标、传播失败诊断、话术表与读稿迭代、四力诊断、产品差异化命名。
  
  不适用于：平台后台操作与投流报表、法律/医疗/金融/化妆品功效等强监管合规意见、代写虚假宣传或伪造数据/资质/评价。
  
  Triggers: 直播skill/直播话术/话术审计/话术拆解/卖点还是需求/PFABES/七词/八大人群/人货场/主播60分/短视频脚本/直播搭建/对标
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.live-commerce-skill
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
> 本文件是凌酱 Skill（lingjiang-content）的「直播运营」子模块入口。由主 SKILL 在用户说「开启凌酱直播运营skill」等触发语时加载。相对路径均相对于本目录 `modules/live-ops/`。

# 《直播电商基础课》— 直播skill — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 平台后台具体操作、投流计划搭建、千川/云图账户操作（需按当前平台版本核实）
- 法律、医疗、金融、化妆品功效等强监管合规意见（需专业审核）
- 代写虚假宣传、伪造数据/资质/评价、冒充权威机构
- 具体选品、供应链、财务测算（只做四力归因，不替代专业分析）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 先判词，再改句：需求/痛点/属性/功能/卖点/价值/买点分清，才动手改话术。
2. 价值 = 卖点 + 消费者能感知的好处；卖点 + 功能 ≠ 价值。
3. 买点 = 价值 + 购买动机；先有理由型（痛点/价值），再上催化剂型（价格/保障/紧迫/信任/从众/急需）。
4. 话术最小闭环是 FB；E 必须在 B 后；S 必须在 E 后，S 提前会清零好感。
5. 短视频先做到一秒看懂、一个视频一个定位；呈现价值，不呈现卖点。
6. 主播 60 分 = 分享感 + 素品力 + 正能量；三观是职业人设，不是欺骗许可证。
7. 任何话术都要过合规边界：不虚构原价/稀缺/资质/功效，不冒充权威，不无依据贬低竞品。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 审计一整段直播话术或短视频脚本；判断一句话是卖点/需求/价值/买点；按 PFABES 逐句标注并找缺口；改写话术但保留说话风格；复盘话术为什么没转化 | references/capabilities/script-audit.md | references/capabilities/seven-word-translation.md、references/capabilities/pfabes-scripting.md、references/capabilities/purchase-motivation.md、references/capabilities/host-60-score.md、references/capabilities/traffic-diagnosis.md |
| 判断一句话属于需求/痛点/属性/功能/卖点/价值/买点；把产品参数翻译成消费者听得懂的价值；区分卖点和价值、功能和价值、买点和价值；统一团队对七词的口径；为直播/短视频/详情页/贴片提炼价值句 | references/capabilities/seven-word-translation.md | references/capabilities/purchase-motivation.md、references/capabilities/pfabes-scripting.md、references/capabilities/script-audit.md、references/capabilities/eight-audience-segments.md |
| 写直播话术/逐字稿，不知道怎么排顺序；逐句标 P/F/A/B/E/S，找缺口；判断一句话是 F/A/B/E 哪个；判断什么时候可以逼单；拆解竞品话术的逻辑 | references/capabilities/pfabes-scripting.md | references/capabilities/seven-word-translation.md、references/capabilities/purchase-motivation.md、references/capabilities/script-audit.md、references/capabilities/host-60-score.md、references/capabilities/script-table-iteration.md |
| 设计“现在买”的理由；逼单/促单/临门一脚；用户说再看看/考虑一下；设计限时、限量、保障、信任；主播不敢逼单、觉得羞耻 | references/capabilities/purchase-motivation.md | references/capabilities/seven-word-translation.md、references/capabilities/pfabes-scripting.md、references/capabilities/script-audit.md、references/capabilities/host-60-score.md、references/capabilities/four-force-diagnosis.md |
| 评估主播能打几分/行不行；主播像机器人/没状态/不敢播；主播不会素品/长时间不讲产品；主播被公屏带跑/说错话就慌；给主播做训练计划 | references/capabilities/host-60-score.md | references/capabilities/pfabes-scripting.md、references/capabilities/purchase-motivation.md、references/capabilities/ren-huo-chang.md、references/capabilities/four-force-diagnosis.md、references/capabilities/script-table-iteration.md |
| 搭直播间/拍短视频，场景怎么选；主播/演员与产品不搭；画面说不出来哪里怪；选短视频演员/主播；补信任场景（工厂/门店/科学性/权威性） | references/capabilities/ren-huo-chang.md | references/capabilities/eight-audience-segments.md、references/capabilities/live-setup-benchmarking.md、references/capabilities/short-video-structure.md、references/capabilities/seven-word-translation.md |
| 判断账号/产品的前三人群；投流/云图人群包怎么选；这个品适合卖给谁；对标账号的人群是否一致；团队对八大人群口径不一致 | references/capabilities/eight-audience-segments.md | references/capabilities/ren-huo-chang.md、references/capabilities/short-video-structure.md、references/capabilities/live-setup-benchmarking.md、references/capabilities/four-force-diagnosis.md |
| 短视频怎么拍/脚本怎么写；开头怎么抓人/前3秒；一个视频讲几个卖点；产品拍不出来/观众看不懂；视频有播放没转化 | references/capabilities/short-video-structure.md | references/capabilities/seven-word-translation.md、references/capabilities/eight-audience-segments.md、references/capabilities/ren-huo-chang.md、references/capabilities/host-60-score.md、references/capabilities/pfabes-scripting.md |
| 新开直播间，设备/道具怎么配；直播间画面 low/进入率低；怎么找对标/对标账号怎么选；贴片写什么；复制别人直播间但很别扭 | references/capabilities/live-setup-benchmarking.md | references/capabilities/eight-audience-segments.md、references/capabilities/ren-huo-chang.md、references/capabilities/short-video-structure.md、references/capabilities/host-60-score.md |
| 视频/直播没效果，问题在哪；观众留不住/停留短/点击低；主播讲话没逻辑/绕来绕去；视频什么都讲了但没人记住；复盘不知道问题在哪 | references/capabilities/traffic-diagnosis.md | references/capabilities/script-audit.md、references/capabilities/seven-word-translation.md、references/capabilities/host-60-score.md、references/capabilities/four-force-diagnosis.md、references/capabilities/short-video-structure.md |
| 建直播话术表/六列表；写逐字稿/怎么背稿；读稿要读多少遍/怎么改；主播现场不会调度；拆竞品逐字稿建素材库 | references/capabilities/script-table-iteration.md | references/capabilities/seven-word-translation.md、references/capabilities/pfabes-scripting.md、references/capabilities/script-audit.md、references/capabilities/host-60-score.md |
| 账号一直起不来，问题在哪；要不要加大投流/找运营；团队知道方法但做不到；先补产品、短视频、直播还是供应链；一直计划/害怕失败/坚持不下去 | references/capabilities/four-force-diagnosis.md | references/capabilities/host-60-score.md、references/capabilities/live-setup-benchmarking.md、references/capabilities/short-video-structure.md、references/capabilities/purchase-motivation.md |
| 产品很普通/没差异化怎么讲；给面料/工艺/系列起名字；怎么包装卖点/概念；差异化是不是编的；概念营销会不会违规 | references/capabilities/product-differentiation.md | references/capabilities/seven-word-translation.md、references/capabilities/script-audit.md、references/capabilities/short-video-structure.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 用户要求虚构原价/库存/资质/功效 → 拒绝，改为真实卖点表达。
- 关键事实缺失（产品、人群、渠道）→ 先列缺口，不硬编；可做结构诊断并标注假设。
- 涉及强监管类目 → 只做话术结构建议，提示专业合规审核。
- 问题明显是流量/选品/供应链 → 说明不在话术审计范围，转 four-force-diagnosis。
