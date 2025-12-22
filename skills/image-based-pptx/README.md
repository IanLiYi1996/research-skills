# 图像式 PPT 生成 Skill

使用 AI 生成高质量演示文稿图像，然后组装成可编辑的 PowerPoint 文件。基于 Gemini Nano Banana Pro 方法论。

## 🎯 特点

- ✅ **AI 驱动**: 使用 Gemini Nano Banana Pro 生成幻灯片大纲和图像
- ✅ **真正自动化**: 一键从文档到完整 PPT，支持 API 自动生成图像
- ✅ **视觉出众**: 生成专业、精美的演示文稿图像
- ✅ **灵活编辑**: 生成的 PPTX 可以正常编辑（可添加文本框）
- ✅ **多种风格**: 6种内置风格（学术、技术、商务等）
- ✅ **双模式**: 支持完全自动化和半自动化（手动调整）

## 📋 快速开始

### 1. 安装依赖

```bash
# Python 依赖
pip install google-generativeai python-pptx pillow PyPDF2

# 设置 API 密钥
export GEMINI_API_KEY="your-api-key-here"
```

### 2. 基本用法

```bash
# 方法 1: 完全自动化（推荐）⭐️
cd skills/image-based-pptx/scripts/
python3 auto-generate.py \
  --input your-paper.pdf \
  --output presentation.pptx \
  --auto-images

# 方法 2: 半自动化（可交互调整）
python3 auto-generate.py \
  --input your-paper.pdf \
  --output presentation.pptx
# 脚本会暂停，让你在 Gemini 网页界面手动生成图像

# 方法 3: 分步骤精细控制
# 步骤 1: 生成大纲
python3 outline-generator.py --input paper.pdf --output outline.json

# 步骤 2a: 自动生成图像
python3 image-generator.py --outline outline.json --output-dir ./slides/ --auto

# 或步骤 2b: 生成提示词（手动模式）
python3 image-generator.py --outline outline.json --output-dir ./prompts/

# 步骤 3: 组装 PPTX
python3 pptx-assembler.py --images ./slides/images/ --output presentation.pptx
```

## 🎨 可用风格

| 风格 | 适用场景 | 特点 |
|-----|---------|------|
| `academic` | 学术演讲、论文答辩 | 简洁、专业、数据导向 |
| `technical` | 技术演示、架构设计 | 蓝图风格、流程图 |
| `business` | 商业提案、报告 | 现代、商务、图表 |
| `creative` | 创意展示、作品集 | 大胆、色彩丰富 |
| `minimal` | 快速演示 | 极简、聚焦内容 |
| `playful` | 教学、入门教程 | 友好、插画风格 |

## 📁 项目结构

```
skills/image-based-pptx/
├── SKILL.md                 # Skill 说明文档
├── README.md               # 本文件
├── assets/
│   └── prompt-template-zh.md  # 提示词模板文档
└── scripts/
    ├── prompt_templates.py     # 提示词模板系统
    ├── gemini_client.py        # Gemini API 客户端
    ├── outline-generator.py    # 大纲生成器
    ├── image-generator.py      # 图像生成器
    ├── pptx-assembler.py       # PPTX 组装器
    └── auto-generate.py        # 自动化主脚本
```

## 📖 详细文档

- [完整功能说明](SKILL.md)
- [提示词模板详解](assets/prompt-template-zh.md)
- [集成方案文档](../../docs/image-based-ppt-integration-plan.md)

## 💡 使用示例

### 示例 1: 学术论文答辩（完全自动）

```bash
python3 auto-generate.py \
  --input thesis.pdf \
  --style academic \
  --slides 20 \
  --topic "深度学习研究" \
  --auto-images \
  --image-size 4K \
  --output defense-presentation.pptx
```

### 示例 2: 技术架构演示（快速生成）

```bash
python3 auto-generate.py \
  --input architecture-doc.md \
  --style technical \
  --slides 15 \
  --auto-images \
  --image-model gemini-2.5-flash-image \
  --output tech-presentation.pptx
```

### 示例 3: 商业提案（半自动调整）

```bash
# 半自动模式：可在 Gemini 网页界面交互式调整图像
python3 auto-generate.py \
  --input proposal.pdf business-plan.md \
  --style business \
  --slides 12 \
  --output business-proposal.pptx
```

## ⚙️ 高级用法

### 使用自定义风格 ⭐️

除了 6 种内置风格，你可以创建自己的风格：

```bash
# 1. 创建风格配置文件（JSON）
cat > my-style.json << 'EOF'
{
  "aesthetic": "现代科技感，赛博朋克风格",
  "background_color": "#0A0E27",
  "background_desc": "深蓝黑背景",
  "primary_font": "Rajdhani Bold",
  "secondary_font": "Rajdhani Regular",
  "primary_text_color": "#00FFFF",
  "primary_accent_color": "#FF00FF",
  "visual_elements": "霓虹灯效果、网格线、渐变色"
}
EOF

# 2. 使用自定义风格生成
python3 outline-generator.py \
  --input paper.pdf \
  --custom-style my-style.json \
  --output outline.json

python3 image-generator.py \
  --outline outline.json \
  --auto \
  --output-dir ./slides/
```

**更多示例**:
- 查看 `examples/custom-style-guide.md` 了解详细说明
- 查看 `examples/style-templates/` 获取更多风格模板

### 批量处理

```bash
# 为多个文档生成演示
for file in papers/*.pdf; do
  python3 auto-generate.py \
    --input "$file" \
    --output "presentations/$(basename $file .pdf).pptx"
done
```

## 🔧 故障排除

### API 密钥问题

**问题**: `未找到 GEMINI_API_KEY`

**解决**:
```bash
# 临时设置
export GEMINI_API_KEY="your-key"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export GEMINI_API_KEY="your-key"' >> ~/.bashrc
source ~/.bashrc
```

### 图像生成问题

**问题**: 无法自动生成图像

**原因**: Gemini API 不直接支持图像生成

**解决**: 使用手动模式（见"基本用法"中的方法 2）

### 依赖安装问题

```bash
# 如果 pip install 失败，尝试：
pip install --upgrade pip
pip install google-generativeai python-pptx pillow PyPDF2 --no-cache-dir
```

## 📊 性能指标

### 完全自动模式（--auto-images）

| 任务 | 平均耗时 |
|------|---------|
| 生成 15 页大纲 | 30-60 秒 |
| 生成 15 张图像 | 3-5 分钟 |
| 组装 PPTX | 5-10 秒 |
| **完整流程** | **4-6 分钟** |

### 半自动模式（默认）

| 任务 | 平均耗时 |
|------|---------|
| 生成 15 页大纲 | 30-60 秒 |
| 生成提示词 | 5-10 秒 |
| 手动生成图像 | 10-15 分钟 |
| 组装 PPTX | 5-10 秒 |
| **完整流程** | **15-20 分钟** |

## 🤝 贡献

欢迎贡献！可以：

- 添加新的风格预设
- 改进提示词模板
- 集成 Vertex AI Imagen 3
- 添加更多示例

## 📜 许可证

MIT License

## 🙏 致谢

- 基于宝玉老师的 [Nano Banana Pro 方法论](https://mp.weixin.qq.com/s/MgM__WTDRNNSXividqpx5A)
- 使用 [python-pptx](https://python-pptx.readthedocs.io/) 库
- 使用 [Gemini API](https://ai.google.dev/)

## 📞 支持

遇到问题？

1. 查看 [SKILL.md](SKILL.md) 的故障排除部分
2. 查看 [集成方案文档](../../docs/image-based-ppt-integration-plan.md)
3. 提交 Issue 到项目仓库

---

**Happy Presenting! 🎉**
