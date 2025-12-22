# 使用速查表

## 🚀 快速命令

### 完全自动化（一键生成）

```bash
python3 auto-generate.py --input paper.pdf --output ppt.pptx --auto-images
```

### 半自动化（手动调整图像）

```bash
python3 auto-generate.py --input paper.pdf --output ppt.pptx
```

### 使用自定义风格

```bash
python3 outline-generator.py --input paper.pdf --custom-style my-style.json --output outline.json
python3 image-generator.py --outline outline.json --auto --output-dir ./slides/
python3 pptx-assembler.py --images ./slides/images/ --output ppt.pptx
```

### 只组装现有图像

```bash
python3 pptx-assembler.py --images ./my-images/ --output ppt.pptx
```

## 📋 参数速查

### auto-generate.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input` | 输入文件（PDF/MD/TXT） | 必需 |
| `--output` | 输出 PPTX 文件 | presentation.pptx |
| `--style` | 风格（6选1） | academic |
| `--slides` | 幻灯片数量 | 15 |
| `--auto-images` | 自动生成图像 | false |
| `--image-model` | 模型选择 | gemini-3-pro-image-preview |
| `--image-size` | 分辨率（1K/2K/4K） | 2K |
| `--aspect-ratio` | 宽高比 | 16:9 |

### outline-generator.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input` | 输入文件 | 必需 |
| `--output` | 输出 JSON 文件 | outline.json |
| `--style` | 内置风格 | academic |
| `--custom-style` | 自定义风格 JSON | None |
| `--slides` | 幻灯片数量 | 15 |
| `--topic` | 演示主题 | 自动提取 |

### image-generator.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--outline` | 大纲 JSON 文件 | 必需 |
| `--output-dir` | 输出目录 | ./slide-generation/ |
| `--auto` | 自动生成图像 | false（手动模式） |
| `--model` | 模型选择 | gemini-3-pro-image-preview |
| `--image-size` | 分辨率 | 2K |
| `--aspect-ratio` | 宽高比 | 16:9 |

### pptx-assembler.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--images` | 图像目录 | 必需 |
| `--output` | 输出 PPTX | presentation.pptx |
| `--layout` | 布局（full/fit） | full |
| `--add-textbox` | 添加文本框 | false |
| `--textbox-position` | 文本框位置 | bottom |
| `--sort` | 排序方式 | name |

## 🎨 风格选择

| 风格 | 关键词 | 适用 |
|------|--------|------|
| `academic` | 简洁、专业 | 学术演讲 |
| `technical` | 蓝图、流程 | 技术演示 |
| `business` | 现代、商务 | 商业提案 |
| `creative` | 大胆、多彩 | 创意展示 |
| `minimal` | 极简、留白 | 快速演示 |
| `playful` | 友好、插画 | 教学培训 |

## 📐 常用宽高比

| 比例 | 说明 | 用途 |
|------|------|------|
| `16:9` | 标准宽屏 | 现代演示（推荐） |
| `4:3` | 传统比例 | 经典投影仪 |
| `1:1` | 正方形 | 社交媒体 |
| `9:16` | 竖屏 | 手机、竖屏显示 |

## 🎯 常见任务

### 任务 1: 从 PDF 快速生成

```bash
python3 auto-generate.py --input paper.pdf --output ppt.pptx --auto-images
```

### 任务 2: 指定特定风格

```bash
python3 auto-generate.py --input doc.pdf --style technical --auto-images --output ppt.pptx
```

### 任务 3: 生成高分辨率演示

```bash
python3 auto-generate.py --input doc.pdf --auto-images --image-size 4K --output ppt.pptx
```

### 任务 4: 使用自定义风格

```bash
# 1. 创建风格文件
cat > cyberpunk.json << 'EOF'
{
  "aesthetic": "赛博朋克，霓虹色彩",
  "background_color": "#0A0E27",
  "background_desc": "深蓝黑背景",
  "primary_font": "Orbitron Bold",
  "secondary_font": "Rajdhani",
  "primary_text_color": "#00FFFF",
  "primary_accent_color": "#FF00FF",
  "visual_elements": "霓虹灯效果、网格线"
}
EOF

# 2. 使用
python3 outline-generator.py --input doc.pdf --custom-style cyberpunk.json --output outline.json
python3 image-generator.py --outline outline.json --auto --output-dir ./slides/
python3 pptx-assembler.py --images ./slides/images/ --output cyberpunk.pptx
```

### 任务 5: 批量处理多个文档

```bash
for pdf in papers/*.pdf; do
  name=$(basename "$pdf" .pdf)
  python3 auto-generate.py --input "$pdf" --auto-images --output "ppts/${name}.pptx"
done
```

### 任务 6: 只组装现有图像

```bash
python3 pptx-assembler.py --images ./downloaded-images/ --output ppt.pptx --add-textbox
```

## 🔧 故障处理

### 问题：API 密钥错误

```bash
echo $GEMINI_API_KEY
export GEMINI_API_KEY="your-key"
python3 gemini_client.py --test-text
```

### 问题：依赖缺失

```bash
pip3 install -r ../requirements.txt
```

### 问题：图像生成失败

```bash
# 切换到手动模式
python3 auto-generate.py --input paper.pdf --output ppt.pptx
# 不加 --auto-images
```

### 问题：想修改某张图像

```bash
# 1. 查看提示词
cat ./ppt-generation/prompts/slide05_prompt.txt

# 2. 手动在 Gemini 重新生成

# 3. 替换图像
cp new-slide.png ./ppt-generation/images/slide05.png

# 4. 重新组装
python3 pptx-assembler.py --images ./ppt-generation/images/ --output ppt.pptx
```

## 📞 获取帮助

### 查看帮助

```bash
python3 auto-generate.py --help
python3 outline-generator.py --help
python3 image-generator.py --help
python3 pptx-assembler.py --help
```

### 测试功能

```bash
python3 gemini_client.py --test-text
python3 gemini_client.py --test-outline
python3 gemini_client.py --test-image
bash test-setup.sh
```

### 查看文档

```bash
cat ../README.md              # 快速开始
cat ../SKILL.md               # 完整功能
cat ../examples/quickstart.md          # 详细示例
cat ../examples/custom-style-guide.md  # 自定义风格
```

## 🎓 学习路径

### 新手（第 1 天）

1. 安装依赖：`bash ../setup.sh`
2. 测试 API：`python3 gemini_client.py --test-text`
3. 半自动生成：`python3 auto-generate.py --input doc.pdf --output ppt.pptx`

### 进阶（第 2 天）

1. 尝试不同风格
2. 使用自动模式：`--auto-images`
3. 调整参数（分辨率、宽高比）

### 高级（第 3+ 天）

1. 创建自定义风格
2. 批量处理文档
3. 集成到工作流程

---

**保存本文件供快速查阅！** 📑
