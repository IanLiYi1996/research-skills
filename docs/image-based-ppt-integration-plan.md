# Nano Banana Pro 图像式 PPT 生成功能集成方案

## 概述

本文档描述如何将基于 Gemini Nano Banana Pro 的图像式 PPT 生成功能集成到 research-skills 项目中。

## 工作原理

### 传统方法 vs 新方法

**传统方法** (现有实现):
- 手动创建 HTML 文件 → 使用 html2pptx 转换 → 生成 PPTX
- 优点：完全可控，文字可编辑
- 缺点：需要手动编写 HTML 和样式

**新方法** (Nano Banana Pro):
- AI 生成幻灯片描述 → 生成图像 → 将图像插入 PPTX
- 优点：快速、视觉效果好、可以生成复杂图形
- 缺点：图像中的文字不可编辑（但可以添加文本框）

### 工作流程

```text
┌─────────────────────┐
│  1. 内容准备        │
│  - 上传素材         │
│  - 定义主题风格     │
└──────┬──────────────┘
       │
       ↓
┌─────────────────────┐
│  2. 生成大纲        │
│  - 风格指令         │
│  - 每页详细描述     │
└──────┬──────────────┘
       │
       ↓
┌─────────────────────┐
│  3. 图像生成        │
│  - Gemini API       │
│  - 批量生成图像     │
└──────┬──────────────┘
       │
       ↓
┌─────────────────────┐
│  4. 组装 PPTX       │
│  - 插入图像         │
│  - 添加可编辑文本   │
└─────────────────────┘
```

## 技术实现方案

### 方案 A：半自动化（推荐快速实现）

**适用场景**: 快速上手，利用现有 Gemini 界面

**实现步骤**:

1. **创建新 Skill**: `image-based-pptx`
    - 提供中文版提示词模板
    - 提供工作流程指导
    - 包含示例会话链接

2. **创建转换脚本**: `scripts/images-to-pptx.py`
   ```python
   # 功能：
   # - 读取目录中的所有图像
   # - 按文件名排序
   # - 创建 PPTX，每页一张图像
   # - 可选：添加可编辑文本框
   ```

3. **用户工作流程**:
   ```bash
   # 1. 用户在 Gemini 中生成图像
   # 2. 下载图像到本地目录
   # 3. 运行转换命令
   /slides from-images ./my-slides/ --output presentation.pptx
   ```

**优点**:

- 实现简单快速
- 不需要 API 集成
- 充分利用 Gemini 的交互式调整能力

**缺点**:

- 需要手动操作 Gemini 界面
- 需要手动下载图像

### 方案 B：全自动化

**适用场景**: 完整自动化工作流

**实现步骤**:

1. **集成 Gemini API**

   ```python
   # 需要：
   # - google-generativeai Python SDK
   # - GEMINI_API_KEY 环境变量
   ```

2. **创建完整流程**:
   ```bash
   # 一键生成 PPT
   /slides generate-from-content \
     --input my-research.pdf \
     --style "academic" \
     --slides 15 \
     --output presentation.pptx
   ```

3. **实现组件**:
    - `scripts/outline-generator.py` - 生成大纲
    - `scripts/image-generator.py` - 批量生成图像
    - `scripts/pptx-assembler.py` - 组装 PPTX

**优点**:

- 完全自动化
- 可批量处理

**缺点**:

- 需要 API 密钥和配额
- 实现复杂度高
- 图像调整不如交互式方便

### 方案 C：混合方案（最佳实践）

结合两种方案的优点：

1. **第一次生成**: 使用方案 A（交互式）
   - 在 Gemini 中调整到满意
   - 下载最终图像

2. **批量处理**: 使用方案 B（自动化）
   - 处理类似主题的多个演示
   - 批量更新

## 项目结构

```text
research-skills/
├── skills/
│   └── image-based-pptx/          # 新 Skill
│       ├── SKILL.md               # Skill 说明
│       ├── assets/
│       │   ├── prompt-template-zh.md    # 中文提示词模板
│       │   └── prompt-template-en.md    # 英文提示词模板
│       ├── scripts/
│       │   ├── images-to-pptx.py        # 图像转 PPTX
│       │   └── outline-generator.py     # 大纲生成器（可选）
│       └── examples/
│           ├── example-style.md         # 风格指令示例
│           └── example-slide.md         # 幻灯片描述示例
│
├── commands/
│   └── slides.md                  # 更新现有命令文档
│
└── docs/
    └── image-based-ppt-guide.md   # 用户指南
```

## 实现细节

### 1. 提示词模板封装

文章中的提示词很长，建议：

- 创建 Python/Node.js 脚本读取模板
- 支持变量替换（如风格、页数等）
- 提供预设风格选项

```python
# 示例
STYLES = {
    "academic": {
        "aesthetic": "干净、精致、极简主义",
        "background": "#F8F7F5",
        "primary_font": "Neue Haas Grotesk Display Pro",
        ...
    },
    "playful": {
        "aesthetic": "俏皮、友好、插画风格",
        "background": "#FFF9F0",
        ...
    }
}
```

### 2. 图像到 PPTX 转换

使用 `python-pptx` 库：

```python
from pptx import Presentation
from pptx.util import Inches
from PIL import Image
import os

def create_pptx_from_images(image_dir, output_file, add_text=False):
    """
    将目录中的图像转换为 PPTX

    Args:
        image_dir: 图像目录路径
        output_file: 输出 PPTX 文件路径
        add_text: 是否为每页添加空白文本框（供后期编辑）
    """
    prs = Presentation()
    prs.slide_width = Inches(10)  # 16:9
    prs.slide_height = Inches(5.625)

    # 获取所有图像文件
    images = sorted([f for f in os.listdir(image_dir)
                     if f.endswith(('.png', '.jpg', '.jpeg'))])

    for img_file in images:
        # 添加空白幻灯片
        blank_layout = prs.slide_layouts[6]  # 6 是空白布局
        slide = prs.slides.add_slide(blank_layout)

        # 插入图像（铺满整个幻灯片）
        img_path = os.path.join(image_dir, img_file)
        slide.shapes.add_picture(
            img_path,
            Inches(0), Inches(0),
            width=prs.slide_width,
            height=prs.slide_height
        )

        # 可选：添加文本框
        if add_text:
            left = Inches(1)
            top = Inches(4)
            width = Inches(8)
            height = Inches(1)
            txBox = slide.shapes.add_textbox(left, top, width, height)
            txBox.text_frame.text = ""  # 空文本框供编辑

    prs.save(output_file)
    print(f"✓ Created presentation with {len(images)} slides: {output_file}")
```

### 3. 命令接口设计

更新 `/slides` 命令，添加新选项：

```bash
# 从图像创建 PPTX
/slides from-images <image_dir> [options]

Options:
  --output <file>       输出文件路径（默认：presentation.pptx）
  --add-textbox         为每页添加可编辑文本框
  --layout <type>       布局方式：full（铺满），fit（适应）
  --sort <method>       排序方式：name（文件名），date（日期）

# 生成幻灯片大纲（使用模板）
/slides outline-nano <topic> [options]

Options:
  --style <name>        风格预设：academic, playful, business, minimal
  --slides <n>          目标幻灯片数量
  --output <file>       输出大纲文件
  --language <lang>     语言：zh（中文），en（英文）
```

## 与现有功能的对比

| 特性 | Slidev | python-pptx | Nano Banana Pro (新) |
|------|--------|-------------|----------------------|
| 实现方式 | Markdown → HTML | Python 代码 | AI 生成图像 |
| 文字可编辑 | ✅ | ✅ | ⚠️ 需要额外添加 |
| 视觉效果 | 好 | 中等 | 优秀 |
| 复杂图形 | 需要手动制作 | 需要代码 | AI 自动生成 |
| 制作速度 | 中等 | 慢 | 快 |
| 适用场景 | 技术演示 | 数据报告 | 创意演示 |

## 使用场景

### 适合使用 Nano Banana Pro 的场景

1. ✅ **视觉冲击力要求高**: 研究成果展示、答辩演示
2. ✅ **需要复杂图形**: 系统架构图、流程图、概念图
3. ✅ **快速原型**: 需要快速生成演示稿的初稿
4. ✅ **创意演示**: 需要独特视觉风格的场合

### 不适合的场景

1. ❌ **频繁修改文字**: 如果内容经常变动
2. ❌ **数据驱动**: 需要根据数据动态生成的图表
3. ❌ **代码演示**: 需要代码高亮的技术演示

## 实施建议

### Phase 1: 快速原型（1-2 天）

- [ ] 创建 `image-based-pptx` skill 目录
- [ ] 添加提示词模板（中英文）
- [ ] 实现 `images-to-pptx.py` 脚本
- [ ] 添加 `/slides from-images` 命令
- [ ] 创建用户指南文档

### Phase 2: 功能增强（3-5 天）

- [ ] 实现风格预设系统
- [ ] 添加 `/slides outline-nano` 命令
- [ ] 支持文本框自动添加
- [ ] 支持图像预处理（裁剪、调整）

### Phase 3: API 集成（可选，5-7 天）

- [ ] 集成 Gemini API
- [ ] 实现自动图像生成
- [ ] 批量处理支持
- [ ] 错误处理和重试机制

## 资源链接

- [Gemini Gem 中文版](https://gemini.google.com/gem/1KNxu_WTCLKb7PSuqlTsdZUeMWQbroWdR)
- [示例会话](https://gemini.google.com/share/bf834dc61a16)
- [python-pptx 文档](https://python-pptx.readthedocs.io/)

## 下一步

1. 确认实施方案（A、B 或 C）
2. 创建 skill 和脚本文件
3. 测试工作流程
4. 更新文档
