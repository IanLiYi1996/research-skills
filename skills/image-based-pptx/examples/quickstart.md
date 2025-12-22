# 快速开始示例

本文档提供完整的使用示例，帮助你快速上手 Nano Banana Pro 图像式 PPT 生成。

## 前置准备

### 1. 安装依赖

```bash
cd /home/ubuntu/research/research-skills/skills/image-based-pptx/
bash setup.sh
```

### 2. 设置 API 密钥

```bash
# 获取 API 密钥: https://aistudio.google.com/app/apikey

# 临时设置（本次会话）
export GEMINI_API_KEY="your-api-key-here"

# 永久设置（推荐）
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 3. 验证安装

```bash
cd scripts/
python3 gemini_client.py --test-text
```

## 示例 1: 完全自动化生成（最简单）

适合：快速生成、批量处理

```bash
cd /home/ubuntu/research/research-skills/skills/image-based-pptx/scripts/

# 一键生成完整 PPT
python3 auto-generate.py \
  --input /path/to/your/paper.pdf \
  --output my-presentation.pptx \
  --auto-images

# 查看结果
ls -lh my-presentation.pptx
```

**预计时间**: 3-5 分钟（15 页）

## 示例 2: 半自动化生成（推荐首次使用）

适合：交互式调整、精细控制

```bash
cd /home/ubuntu/research/research-skills/skills/image-based-pptx/scripts/

# 步骤 1: 生成大纲和提示词
python3 auto-generate.py \
  --input /path/to/your/paper.pdf \
  --output my-presentation.pptx

# 脚本会暂停，提示你:
# 1. 在 Gemini 网页界面生成图像
# 2. 下载图像到 ./ppt-generation/images/
# 3. 按 Enter 继续

# 步骤 2: 按照提示操作后，按 Enter
# 脚本会自动组装 PPTX
```

**预计时间**: 10-15 分钟（包括手动生成图像）

## 示例 3: 指定风格和参数

```bash
# 学术风格，20 页，4K 高清
python3 auto-generate.py \
  --input paper.pdf \
  --style academic \
  --slides 20 \
  --image-size 4K \
  --auto-images \
  --output academic-presentation.pptx

# 技术风格，蓝图感
python3 auto-generate.py \
  --input architecture-doc.md \
  --style technical \
  --slides 15 \
  --auto-images \
  --output tech-presentation.pptx

# 商业风格，方形比例
python3 auto-generate.py \
  --input business-plan.pdf \
  --style business \
  --aspect-ratio 4:3 \
  --auto-images \
  --output business-presentation.pptx

# 创意风格，使用更快的模型
python3 auto-generate.py \
  --input creative-brief.md \
  --style creative \
  --image-model gemini-2.5-flash-image \
  --auto-images \
  --output creative-presentation.pptx
```

## 示例 4: 分步骤精细控制

如果你想对每个步骤有更多控制：

```bash
cd /home/ubuntu/research/research-skills/skills/image-based-pptx/scripts/

# 步骤 1: 生成大纲
python3 outline-generator.py \
  --input paper.pdf \
  --style academic \
  --slides 15 \
  --topic "深度学习在医疗影像中的应用" \
  --output outline.json

# 查看大纲
cat outline.json | jq '.slides[0]'

# 如果不满意，可以修改 outline.json 后继续

# 步骤 2: 自动生成图像
python3 image-generator.py \
  --outline outline.json \
  --output-dir ./my-slides/ \
  --auto \
  --model gemini-3-pro-image-preview \
  --image-size 2K

# 或者：生成提示词手动生成
python3 image-generator.py \
  --outline outline.json \
  --output-dir ./my-slides/

# 步骤 3: 组装 PPTX
python3 pptx-assembler.py \
  --images ./my-slides/images/ \
  --output presentation.pptx \
  --add-textbox \
  --textbox-position bottom
```

## 示例 5: 只用图像组装器

如果你已经有图像（从其他来源）：

```bash
# 假设你有一个目录包含图像：
# my-images/
# ├── slide01.png
# ├── slide02.png
# └── slide03.png

python3 pptx-assembler.py \
  --images ./my-images/ \
  --output from-existing-images.pptx \
  --layout full
```

## 示例 6: 测试单个组件

### 测试文本生成

```bash
python3 gemini_client.py --test-text
```

### 测试大纲生成

```bash
python3 gemini_client.py --test-outline
```

### 测试图像生成

```bash
python3 gemini_client.py --test-image --output test-slide.png
```

## 示例 7: 从多个文件生成

```bash
# 合并多个文档
python3 auto-generate.py \
  --input paper.pdf notes.md abstract.txt \
  --style academic \
  --auto-images \
  --output comprehensive-presentation.pptx
```

## 常见使用场景

### 场景 1: 论文答辩演示

```bash
python3 auto-generate.py \
  --input thesis.pdf \
  --style academic \
  --slides 25 \
  --topic "我的博士研究" \
  --auto-images \
  --image-size 4K \
  --output defense-presentation.pptx
```

### 场景 2: 技术分享

```bash
python3 auto-generate.py \
  --input architecture.md \
  --style technical \
  --slides 12 \
  --auto-images \
  --output tech-talk.pptx
```

### 场景 3: 项目提案

```bash
python3 auto-generate.py \
  --input proposal.pdf \
  --style business \
  --slides 10 \
  --auto-images \
  --output project-proposal.pptx
```

### 场景 4: 教学课件

```bash
python3 auto-generate.py \
  --input lecture-notes.md \
  --style playful \
  --slides 18 \
  --auto-images \
  --output lecture-slides.pptx
```

## 故障排除

### 问题 1: API 密钥错误

```bash
# 检查密钥是否设置
echo $GEMINI_API_KEY

# 如果为空，重新设置
export GEMINI_API_KEY="your-key"
```

### 问题 2: 依赖缺失

```bash
# 重新安装依赖
pip3 install -r ../requirements.txt
```

### 问题 3: 图像生成失败

```bash
# 使用手动模式作为备选
python3 auto-generate.py --input paper.pdf --output ppt.pptx
# 不加 --auto-images 参数

# 然后在 Gemini 网页界面手动生成
```

### 问题 4: 生成速度慢

```bash
# 使用更快的 Nano Banana 模型
python3 auto-generate.py \
  --input paper.pdf \
  --auto-images \
  --image-model gemini-2.5-flash-image \
  --output ppt.pptx
```

## 下一步

- 阅读 [SKILL.md](../SKILL.md) 了解所有功能
- 查看 [prompt-template-zh.md](../assets/prompt-template-zh.md) 学习自定义提示词
- 探索不同风格预设
- 尝试调整图像分辨率和宽高比

## 提示技巧

1. **选择合适的模型**:
   - 快速原型 → `gemini-2.5-flash-image`
   - 专业演示 → `gemini-3-pro-image-preview`

2. **选择合适的分辨率**:
   - 普通演示 → `1K` 或 `2K`
   - 打印、大屏幕 → `4K`

3. **选择合适的风格**:
   - 学术场合 → `academic` 或 `minimal`
   - 技术演示 → `technical`
   - 商业提案 → `business`
   - 创意展示 → `creative` 或 `playful`

4. **优化效率**:
   - 首次生成使用半自动模式测试效果
   - 确认满意后再使用自动模式批量处理
   - 使用 `gemini-2.5-flash-image` 加快速度

---

**祝你生成出色的演示文稿！** 🎉
