# OpenPublisher 共识（初版）

## 目标

准备一份标准化文章（以 Markdown 为主），一次发布到自建博客、掘金、CSDN、知乎、微信公众号、Medium、Dev.to 以及本地 Git 仓库，并返回每个目标的状态和链接。

## 总体设计

系统分为两层：

- **Platform Skill**：描述平台规则、字段限制、内容转换、图片处理、登录和发布流程。
- **Platform Adapter**：用 Python 实现稳定的执行接口，负责校验、转换、上传资源、发布和结果归一化。

Skill 是规则层，Adapter 是执行层；新增平台应尽量只新增对应目录，不影响其他平台。

## 统一文章

统一输入包含：Markdown 正文、标题、摘要、标签、分类、封面图、SEO 信息和文章图片资源。平台适配器可以按规则转换字段，但不修改原始文章。

## 发布结果

每个平台独立执行，允许部分成功。结果至少包含平台名称、状态、公开 URL（如有）、外部 ID（如有）和错误信息。任务需要支持重试，避免重复发布。

## 强制内容边界

所有平台、草稿、图片描述、SEO 字段和 Git 输出都必须经过统一的读者可见内容校验。不得暴露内部系统名称、自动化实现、测试标签、本地路径、凭证或运行说明。平台 Skill 只能增加限制，不能绕过或削弱这一规则。完整规则见 [Mandatory Publishing Rules](../skills/PUBLISHING_RULES.md)。

## 强制作者尾注

所有发布目标必须在每篇文章末尾保留王仕宇（JavaPub）的统一作者介绍和个人主页链接。发布管线在平台转换前自动追加尾注，重复执行不得生成多份尾注；平台适配器不得移除或缩短该内容。

## 测试图片上传铁律

每个平台的测试发布必须包含一次真实图片上传。测试流程必须确认平台托管图片 URL、编辑器或预览中的渲染结果，以及保存后图片仍与文章关联。仅启用自动封面不视为完成图片上传测试。

## 登录和凭证

优先使用 API Token、OAuth 或本地浏览器会话。未登录或登录过期时，必须直接进入该平台的登录页并保留为接力页面，等待用户完成登录后从同一页面继续；不得停在平台首页或要求用户提供 Cookie。账号密码仅允许从本机 `.env` 读取，不进入日志、文章或 Git 仓库。遇到验证码、人机检测或二次认证时，必须立即停止受阻操作，保留当前浏览器页面、已填写字段和已上传素材，交由用户完成验证后从同一页面恢复；不得尝试绕过、猜测或重复提交验证。

## 本地 Git 发布

本地 Git 仓库是一级发布目标。流程为：生成文章和图片、检查工作区和 diff、写入文件、可选 commit、可选 push。默认不得覆盖无关未提交修改，不允许 force push，也不得提交敏感凭证。

## 默认实施顺序

先完成文章模型、Skill 规范、Adapter 接口、发布结果模型和本地 Git 适配器；再接入 API 稳定的平台，最后处理需要浏览器会话的平台。

## CSDN Discovery

CSDN 已完成第一轮浏览器流程验证：首次点击“保存草稿”才生成 `articleId`，并将其写入编辑器 URL。后续保存、发布和重试必须持久化并复用这个 ID，避免因重新打开编辑器而创建重复草稿。详细记录见 [CSDN Browser Discovery](platforms/csdn-discovery.md)，平台规则见 [CSDN Skill](../skills/platforms/csdn/SKILL.md)。

## 51CTO Discovery

51CTO 已完成浏览器流程验证。每次发布必须先访问签到页；本次账号已显示“今日已签到”。从签到页点击“写文章”后进入 Markdown 编辑器，编辑器自动保存草稿，但在已观察的 URL 和页面字段中没有暴露可复用文章 ID。已验证正文工具栏的“上传图片”可将本地图片转为 51CTO 托管 URL 并在编辑器中渲染；发布需要双级分类、最多五个标签、摘要、话题、封面、版权、可见性和置顶配置。详细记录见 [51CTO Browser Discovery](platforms/51cto-discovery.md)，平台规则见 [51CTO Skill](../skills/platforms/51cto/SKILL.md)。

## 博客园 Discovery

博客园已完成浏览器发布验证。已登录会话从首页“写随笔”进入 Markdown 编辑器；正文图片必须经过两步操作：先点击“自动备份”下方的“上传图片”打开“插入图片”面板，再点击面板中的“上传图片”选择本地文件。平台将图片回写为 `img2024.cnblogs.com` 托管 URL，最终公开页也已验证图片渲染。AI 生成内容必须勾选平台声明；发布成功后编辑 URL 暴露 `postId`，并使用“立即查看”链接验证公开文章。详细记录见 [博客园 Browser Discovery](platforms/cnblogs-discovery.md)，平台规则见 [博客园 Skill](../skills/platforms/cnblogs/SKILL.md)。

## SegmentFault Discovery

SegmentFault 已完成浏览器发布验证。已登录会话从首页“撰写”进入 CodeMirror Markdown 编辑器；正文图片通过 `.icon-image` 打开“添加图片”，本地上传后写入相对 Markdown 地址 `/img/<image-id>`，公开页解析为 `https://segmentfault.com/img/<image-id>` 并已确认渲染。平台最多五个标签，未观察到独立分类或摘要字段；成功发布直接跳转至 `https://segmentfault.com/a/<article-id>`。详细记录见 [SegmentFault Browser Discovery](platforms/segmentfault-discovery.md)，平台规则见 [SegmentFault Skill](../skills/platforms/segmentfault/SKILL.md)。

## 当前非目标

暂不实现真实平台 API、浏览器自动登录、复杂前端、定时任务和多用户权限。这些将在核心流程跑通后逐项增加。
