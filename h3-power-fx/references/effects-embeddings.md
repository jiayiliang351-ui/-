# 可选效果 embedding

只有用户要求使用效果文件时才查本页。纯文字异能提示词不依赖它们，默认不往提示词里加触发词。

## 来源和适用范围

[ComfyUI 文档](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide)说明，ComfyUI 支持 H3 的 `embedding:` 语法；[Comfy-Org 托管目录](https://huggingface.co/Comfy-Org/MiniMax-H3/tree/main/embeddings)的 10 个效果文件来自社区贡献者 silveroxides，并非 MiniMax 官方自带效果。[实现变更](https://github.com/Comfy-Org/ComfyUI/pull/15697)可用于核对支持范围。

托管目录的文件名包括 `minimaxh3_art_is_explosion.safetensors`、`minimaxh3_bullet_time.safetensors` 等。名字只表示预期效果，不能证明适合当前剧情，也不能将 bullet time 自动等同于用户要求的全场时间静止。

## 使用前核对

1. 查实际运行环境的 H3 文本编码节点和 tokenizer 是否走支持 embedding 的解析路径；本地与云端分别检查，模型下拉框的名字不能代替检查。
2. 查该环境的 embedding 搜索目录和实际文件名。下载、安装或改工作流需要在用户授权范围内进行，不凭目录网页认定本机已安装。
3. 确认支持且文件已存在后，按实际文件名原样写触发词。例如实际文件是 `minimaxh3_bullet_time.safetensors`，才写 `embedding:minimaxh3_bullet_time`。放在描述正文中，与自然语言以空白分隔，不紧贴句号或其他标点，也不放在 `non_diegetic_music` 后面。
4. 检查编码日志有没有缺文件或忽略提示；没有报错仍不等于视觉有效。不承诺强度是否可调，参数取决于实际解析实现。
5. 与不加 embedding 的版本保持其余提示词、模型、模式和采样配置一致，至少两个相同种子分别对照。记录实际出片效果后，才将它加入项目已验证用法。

本页提供来源与启用条件，没有该用户项目的 embedding 出片结论。法力颜色、作用对象、范围和结果仍由简报及项目卡决定，不由效果名称替代。
