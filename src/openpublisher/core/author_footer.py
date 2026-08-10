DEFAULT_AUTHOR_FOOTER = """## 关于作者

大家好，我是 **王仕宇（JavaPub）**。

一名持续探索 **AI、软件开发和数字化创业** 的实践者。

过去几年一直深耕软件开发领域，关注 **后端架构、云原生、大模型应用、AI Agent 以及自动化工具**。在技术之外，也持续探索如何利用 AI 和互联网产品实现更高效的工作方式，以及技术人的商业化路径。

这里分享的不只是代码和技术，也包括：

🤖 AI 工具与大模型应用实践
🚀 软件产品开发与创业探索
💡 程序员成长与个人品牌建设
💰 AI 时代的效率提升与商业机会
🌍 对未来科技趋势的观察与思考

我相信，AI 不只是一次技术升级，更是一场关于个人能力、生产方式和商业模式的变革。

希望通过持续实践和分享，帮助更多人理解 AI、使用 AI，并找到属于自己的机会。

如果你关注 AI、技术、创业和未来趋势，欢迎一起交流。

个人主页：
[https://javapub.net.cn](https://javapub.net.cn)

一起成为勇猛精进的人类。"""


def append_author_footer(body_markdown: str) -> str:
    """Append the author profile once, preserving an already-present footer."""
    normalized_footer = DEFAULT_AUTHOR_FOOTER.strip()
    if normalized_footer in body_markdown:
        return body_markdown

    return f"{body_markdown.rstrip()}\n\n---\n\n{normalized_footer}\n"

