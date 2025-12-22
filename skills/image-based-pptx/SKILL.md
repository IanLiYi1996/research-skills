---
name: image-based-pptx
description: AI 驱动的图像式 PPT 生成技能，使用 Gemini Nano Banana Pro 生成高质量演示文稿图像。通过 AI 生成幻灯片大纲和风格指令，然后批量生成精美的图像并组装成 PPTX 文件。关键词：Nano Banana Pro, AI 演示文稿, 图像生成, Gemini, 自动化 PPT, 视觉演示。
---

# 图像式 PPT 生成 Skill

使用 Gemini Nano Banana Pro 生成视觉效果出色的演示文稿，结合 AI 图像生成的强大能力和 PPT 的可编辑性。

## 核心能力

### 1. AI 驱动的内容规划

- 根据素材自动生成幻灯片大纲
- 智能提取关键信息和叙事结构
- 支持多种演示类型（学术、技术、商务）
- 自定义风格和视觉主题

### 2. 批量图像生成

- 使用 Gemini API 批量生成幻灯片图像
- 保持统一的视觉风格
- 支持复杂图形和概念可视化
- 16:9 宽屏比例优化

### 3. PPTX 组装

- 将生成的图像组装成可编辑的 PPTX
- 可选添加文本框供后期编辑
- 保持高清晰度和专业外观
- 支持批量处理

## 安装依赖

```bash
# Python 依赖
pip install google-generativeai python-pptx pillow

# 设置 API 密钥
export GEMINI_API_KEY="your-api-key-here"
```

## 快速开始

### 方法 1：完全自动化

一键生成整个演示文稿：

```bash
# 从 PDF 或文档生成 PPT
python skills/image-based-pptx/scripts/auto-generate.py \
  --input my-research.pdf \
  --output presentation.pptx \
  --style academic \
  --slides 15
```

### 方法 2：分步骤控制

更精细的控制，适合需要中途调整的场景：

```bash
# 1. 生成大纲和风格指令
python skills/image-based-pptx/scripts/outline-generator.py \
  --input my-research.pdf \
  --style academic \
  --slides 15 \
  --output outline.json

# 2. 批量生成图像
python skills/image-based-pptx/scripts/image-generator.py \
  --outline outline.json \
  --output-dir ./slide-images/

# 3. 组装成 PPTX
python skills/image-based-pptx/scripts/pptx-assembler.py \
  --images ./slide-images/ \
  --output presentation.pptx \
  --add-textbox
```

### 方法 3：使用现有图像

如果你已经在 Gemini 网页界面生成了图像：

```bash
# 直接从图像创建 PPTX
python skills/image-based-pptx/scripts/pptx-assembler.py \
  --images ./my-slide-images/ \
  --output presentation.pptx
```

## 风格预设

内置多种专业风格：

| 风格名称 | 适用场景 | 特点 |
|---------|---------|-----|
| `academic` | 学术演讲、论文答辩 | 简洁、专业、重视数据 |
| `technical` | 技术演示、架构设计 | 蓝图风格、概念图、流程图 |
| `business` | 商业提案、报告 | 现代、商务、数据可视化 |
| `creative` | 创意展示、设计作品 | 大胆、色彩丰富、视觉冲击 |
| `minimal` | 快速演示、简报 | 极简、聚焦内容 |
| `playful` | 教学、入门教程 | 友好、插画风格、轻松 |

## 提示词模板

### 使用内置模板

```python
from skills.image_based_pptx.scripts.prompt_templates import PromptTemplates

# 加载学术风格模板
template = PromptTemplates.load('academic')

# 自定义参数
custom_config = {
    'slide_count': 15,
    'topic': '深度学习在医疗影像中的应用',
    'audience': '计算机视觉研究者',
    'language': 'zh'
}

# 生成提示词
prompt = template.generate(custom_config)
```

### 自定义风格

创建自己的风格配置：

```python
custom_style = {
    'aesthetic': '现代科技感，渐变色背景',
    'background_color': '#1A1A2E',
    'primary_font': 'Microsoft YaHei',
    'secondary_font': 'Microsoft YaHei Light',
    'primary_text_color': '#E0E0E0',
    'primary_accent_color': '#FF6B6B',
    'visual_elements': '使用扁平化图标，几何形状，渐变配色'
}

template = PromptTemplates.create_custom(custom_style)
```

## 命令行工具

### 生成大纲

```bash
# 基础用法
python scripts/outline-generator.py --input document.pdf

# 指定风格和幻灯片数量
python scripts/outline-generator.py \
  --input document.pdf \
  --style technical \
  --slides 20 \
  --language en

# 从多个文件生成
python scripts/outline-generator.py \
  --input paper1.pdf paper2.pdf notes.md \
  --output outline.json
```

### 生成图像

```bash
# 从大纲生成
python scripts/image-generator.py \
  --outline outline.json \
  --output-dir ./images/

# 自定义图像质量
python scripts/image-generator.py \
  --outline outline.json \
  --output-dir ./images/ \
  --quality high \
  --retry-failed

# 并行生成（加快速度）
python scripts/image-generator.py \
  --outline outline.json \
  --output-dir ./images/ \
  --parallel 3
```

### 组装 PPTX

```bash
# 基础组装
python scripts/pptx-assembler.py \
  --images ./images/ \
  --output presentation.pptx

# 添加可编辑文本框
python scripts/pptx-assembler.py \
  --images ./images/ \
  --output presentation.pptx \
  --add-textbox \
  --textbox-position bottom

# 自定义排序和布局
python scripts/pptx-assembler.py \
  --images ./images/ \
  --output presentation.pptx \
  --sort name \
  --layout fit
```

## 工作流程

### 典型工作流

```text
素材准备 → 大纲生成 → 图像生成 → PPTX 组装 → 微调
   ↓           ↓           ↓           ↓         ↓
  PDF       outline    images/     .pptx    编辑文本
  MD        .json      *.png                 调整布局
  图片
```

### 推荐实践

1. **第一次尝试**：使用完全自动化模式快速生成原型
2. **需要调整**：使用分步骤模式，在大纲阶段就进行优化
3. **精益求精**：手动在 Gemini 界面生成图像，获得最佳效果
4. **批量处理**：为多个类似主题的演示文稿使用自动化脚本

## 高级功能

### 1. 多语言支持

```python
# 中文演示
outline_generator.py --input doc.pdf --language zh

# 英文演示
outline_generator.py --input doc.pdf --language en

# 双语演示（每页都有中英文）
outline_generator.py --input doc.pdf --language zh --bilingual
```

### 2. 批量处理

```bash
# 为多个文档生成演示
for file in papers/*.pdf; do
  python scripts/auto-generate.py \
    --input "$file" \
    --output "presentations/$(basename $file .pdf).pptx" \
    --style academic
done
```

### 3. 自定义提示词注入

```python
# 在大纲生成时注入特殊指令
custom_instructions = """
- 每页幻灯片必须包含数据可视化
- 使用蓝绿色调的配色方案
- 避免使用纯文字幻灯片
"""

outline_generator.py \
  --input doc.pdf \
  --custom-instructions "$custom_instructions"
```

### 4. 图像后处理

```python
from skills.image_based_pptx.scripts.image_processor import ImageProcessor

processor = ImageProcessor()

# 批量处理图像
processor.batch_process(
    input_dir='./raw-images/',
    output_dir='./processed-images/',
    operations=[
        ('resize', {'width': 1920, 'height': 1080}),
        ('enhance', {'contrast': 1.2, 'brightness': 1.1}),
        ('add_border', {'color': '#000000', 'width': 2})
    ]
)
```

## 与其他 Skills 集成

### 与 latex-writing 集成

生成包含数学公式的演示：

```bash
# LaTeX 文档 → 演示文稿
python scripts/auto-generate.py \
  --input thesis.tex \
  --style academic \
  --preserve-equations
```

### 与 data-visualization 集成

数据驱动的演示：

```bash
# 先生成可视化图表
python skills/data-visualization/scripts/generate-charts.py \
  --data results.csv \
  --output-dir ./charts/

# 然后生成演示（包含图表）
python scripts/auto-generate.py \
  --input paper.pdf \
  --images ./charts/ \
  --output presentation.pptx
```

### 与 academic-research 集成

从文献综述生成演示：

```bash
# 从参考文献生成综述演示
python scripts/auto-generate.py \
  --input papers/ \
  --style academic \
  --type literature-review \
  --output review-presentation.pptx
```

## 故障排除

### API 错误

**问题**：`google.api_core.exceptions.PermissionDenied`

**解决**：
```bash
# 确认 API 密钥已设置
echo $GEMINI_API_KEY

# 检查 API 配额
python scripts/check-quota.py

# 使用备用密钥
export GEMINI_API_KEY="backup-key"
```

### 图像质量问题

**问题**：生成的图像模糊或比例不对

**解决**：
```bash
# 使用更高质量设置
python scripts/image-generator.py \
  --quality high \
  --resolution 1920x1080

# 后处理增强
python scripts/image-processor.py \
  --input-dir ./images/ \
  --enhance
```

### 生成速度慢

**问题**：批量生成耗时过长

**解决**：
```bash
# 启用并行处理
python scripts/image-generator.py \
  --parallel 5 \
  --cache-prompts

# 使用更快的模型
python scripts/image-generator.py \
  --model gemini-pro-vision-fast
```

## 最佳实践

### 1. 内容准备

- ✅ 提供结构清晰的源文件（有标题、段落分明）
- ✅ 包含关键数据和图表
- ✅ 明确演示的目标受众
- ❌ 避免过长的纯文字文档

### 2. 风格选择

- ✅ 根据场合选择合适的风格预设
- ✅ 保持整个演示的风格一致性
- ✅ 考虑受众的审美偏好
- ❌ 不要混合多种冲突的风格

### 3. 图像生成

- ✅ 先生成少量样本测试效果
- ✅ 为重要幻灯片多生成几个版本备选
- ✅ 保存原始提示词以便后续调整
- ❌ 不要一次性生成所有图像再检查

### 4. 后期编辑

- ✅ 使用 `--add-textbox` 添加可编辑文本
- ✅ 在 PowerPoint 中调整布局和动画
- ✅ 添加备注和演讲提示
- ❌ 不要过度依赖图像中的文字

## 示例项目

查看 `examples/` 目录获取完整示例：

- `examples/academic-defense/` - 博士论文答辩演示
- `examples/tech-presentation/` - 技术架构展示
- `examples/business-proposal/` - 商业提案
- `examples/tutorial/` - 入门教程

## 参考资源

- [提示词模板详解](assets/prompt-template-zh.md)
- [风格配置指南](assets/style-guide.md)
- [API 使用最佳实践](assets/api-best-practices.md)
- [常见问题解答](assets/faq.md)

## 版本历史

- v1.0.0 (2024-12) - 初始版本，支持全自动化生成
- 计划中：支持 PPT 模板、动画效果、更多风格
