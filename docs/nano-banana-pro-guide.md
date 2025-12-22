# Nano Banana Pro PPT 生成完整指南

本指南详细介绍如何使用 Gemini Nano Banana Pro 自动生成高质量 PowerPoint 演示文稿。

## 🌟 什么是 Nano Banana Pro？

Nano Banana Pro 是 Google Gemini 的图像生成功能，特点：

- 🎨 **高质量图像**: 专业级视觉效果
- 📝 **精准文字渲染**: 图像中的文字清晰可读
- 🔄 **多轮迭代**: 支持对话式优化
- 📐 **多种分辨率**: 支持 1K/2K/4K
- 🎯 **风格一致性**: 保持统一的视觉风格

## 🚀 三种使用模式

### 模式对比

| 特性 | 完全自动 | 半自动 | 纯手动 |
|------|---------|--------|--------|
| API 调用 | ✅ | ✅ 大纲 | ❌ |
| 图像生成 | ✅ API | 🖱️ 网页 | 🖱️ 网页 |
| 耗时 | 5 分钟 | 15 分钟 | 30 分钟 |
| 灵活性 | 中 | 高 | 最高 |
| 推荐场景 | 批量处理 | 首次使用 | 精品制作 |

### 模式 1: 完全自动化 ⭐️ 推荐批量使用

**特点**: 一键完成，无需人工干预

```bash
python3 auto-generate.py \
  --input paper.pdf \
  --output presentation.pptx \
  --auto-images
```

**流程**:
```
PDF → 大纲生成 → 图像批量生成 → PPTX组装 → 完成
      (API)      (Nano Banana API)    (本地)
```

**适合**:
- 需要快速生成多个演示
- 对图像要求不太严格

### 模式 2: 半自动化 ⭐️ 推荐首次使用

**特点**: 可以在 Gemini 网页界面交互式调整图像

```bash
python3 auto-generate.py \
  --input paper.pdf \
  --output presentation.pptx
```

**流程**:
```
PDF → 大纲生成 → 提示词生成 → [手动]生成图像 → PPTX组装
      (API)        (本地)          (网页界面)       (本地)
```

**适合**:
- 首次使用，想看效果
- 需要精细调整图像

### 模式 3: 纯手动

**特点**: 完全控制每个细节

使用 Gemini 网页界面，参考我们的提示词模板手动生成。

## 📖 完整工作流程

### 第一步：准备素材

支持的输入格式：

- PDF 文件（论文、报告）
- Markdown 文件（文档、笔记）
- 纯文本文件

```bash
# 示例素材
my-research/
├── paper.pdf           # 主要内容
├── notes.md            # 补充笔记
└── abstract.txt        # 摘要
```

### 第二步：生成大纲

```bash
cd skills/image-based-pptx/scripts/

python3 outline-generator.py \
  --input ../../../my-research/paper.pdf \
  --style academic \
  --slides 15 \
  --topic "深度学习研究进展" \
  --output outline.json
```

**输出**: `outline.json`
- 包含每张幻灯片的详细描述
- 包含风格指令
- 包含元数据

**可以手动编辑** `outline.json` 调整内容！

### 第三步：生成图像

#### 选项 A: 自动生成（API）

```bash
python3 image-generator.py \
  --outline outline.json \
  --output-dir ./my-slides/ \
  --auto \
  --model gemini-3-pro-image-preview \
  --image-size 2K \
  --aspect-ratio 16:9
```

**预计时间**: 3-5 分钟（15 张图像）

#### 选项 B: 手动生成（网页）

```bash
# 生成提示词文件
python3 image-generator.py \
  --outline outline.json \
  --output-dir ./my-slides/
```

然后：
1. 打开 https://gemini.google.com/
2. 选择 "🍌 Create Images" 工具
3. 复制 `my-slides/风格指令.txt` 发送给 Gemini
4. 依次复制 `my-slides/prompts/slide01_prompt.txt` 等
5. 下载图像，命名为 `slide01.png`, `slide02.png` 等
6. 保存到 `my-slides/images/` 目录

### 第四步：组装 PPTX

```bash
python3 pptx-assembler.py \
  --images ./my-slides/images/ \
  --output presentation.pptx \
  --add-textbox \
  --textbox-position bottom
```

**输出**: `presentation.pptx`
- 可以用 PowerPoint 或 LibreOffice 打开
- 图像铺满每页
- 可选的文本框可以编辑

## 🎨 风格选择指南

### 风格对比

| 风格 | 背景色 | 字体风格 | 强调色 | 适用场景 |
|------|--------|---------|--------|---------|
| `academic` | 灰白 #F8F7F5 | 思源黑体/宋体 | 蓝 #007AFF | 学术演讲、论文答辩 |
| `technical` | 深色 #181B24 | Roboto Mono | 科技蓝 #00D9FF | 技术演示、架构设计 |
| `business` | 纯白 #FFFFFF | 微软雅黑 | 商务红 #FF6B6B | 商业提案、报告 |
| `creative` | 米色 #FFF9E6 | 站酷快乐体 | 橙红 #FF6B35 | 创意展示、作品集 |
| `minimal` | 浅灰 #FAFAFA | 苹方 | 纯黑 #000000 | 快速演示、简报 |
| `playful` | 米白 #FFF9F0 | 方正胖头鱼 | 活力粉 #FF6B9D | 教学、入门教程 |

### 如何选择？

**学术研究场合**:
```bash
--style academic     # 简洁专业
--style minimal      # 极简聚焦
```

**技术分享**:
```bash
--style technical    # 蓝图感、流程图
--style minimal      # 代码演示
```

**商业场合**:
```bash
--style business     # 现代商务
--style creative     # 创意提案
```

**教学培训**:
```bash
--style playful      # 友好俏皮
--style creative     # 生动有趣
```

## 🎛️ 参数调优

### 图像质量参数

#### 模型选择

```bash
# Nano Banana Pro (高质量)
--image-model gemini-3-pro-image-preview

# Nano Banana (快速)
--image-model gemini-2.5-flash-image
```

**建议**:
- 专业演示 → Nano Banana Pro
- 快速原型 → Nano Banana
- 批量处理 → Nano Banana（成本低）

#### 分辨率选择

```bash
--image-size 1K    # 1024px（最快）
--image-size 2K    # 2048px（推荐）
--image-size 4K    # 4096px（打印/大屏）
```

**建议**:
- 普通演示 → 2K
- 网页分享 → 1K
- 打印/投影 → 4K

#### 宽高比选择

```bash
--aspect-ratio 16:9    # 标准宽屏（推荐）
--aspect-ratio 4:3     # 传统比例
--aspect-ratio 1:1     # 方形（社交媒体）
```

### 幻灯片数量建议

| 场景 | 推荐页数 | 说明 |
|------|---------|------|
| 快速汇报 | 5-8 页 | 核心要点 |
| 标准演示 | 12-15 页 | 完整叙事 |
| 详细演讲 | 20-25 页 | 深入讲解 |
| 论文答辩 | 25-30 页 | 全面覆盖 |

**注意**: 不要超过 20 页（提示词限制），如需更多可分批生成

## 💡 高级技巧

### 技巧 1: 自定义指令

在生成大纲时添加特殊要求：

```bash
python3 outline-generator.py \
  --input paper.pdf \
  --custom-instructions "每页必须包含数据可视化；使用蓝绿色调；避免纯文字页面"
```

### 技巧 2: 批量处理多个文档

```bash
#!/bin/bash
# batch-generate.sh

for pdf in papers/*.pdf; do
  name=$(basename "$pdf" .pdf)
  echo "处理: $name"

  python3 auto-generate.py \
    --input "$pdf" \
    --style academic \
    --auto-images \
    --output "presentations/${name}.pptx"

  echo "完成: $name"
done
```

### 技巧 3: 从中断处恢复

```bash
# 如果中途失败或中断
python3 auto-generate.py \
  --resume ./ppt-generation \
  --output presentation.pptx
```

### 技巧 4: 只重新生成部分图像

```bash
# 假设 slide05.png 效果不好，想重新生成

# 1. 查看原始提示词
cat ./ppt-generation/prompts/slide05_prompt.txt

# 2. 修改提示词（可选）
# 编辑文件，调整描述

# 3. 手动在 Gemini 生成新图像
# 或使用 gemini_client.py

# 4. 替换图像文件
cp new-slide05.png ./ppt-generation/images/slide05.png

# 5. 重新组装
python3 pptx-assembler.py \
  --images ./ppt-generation/images/ \
  --output presentation.pptx
```

### 技巧 5: 添加可编辑文本

```bash
# 生成时添加文本框
python3 pptx-assembler.py \
  --images ./images/ \
  --output presentation.pptx \
  --add-textbox \
  --textbox-position bottom

# 然后在 PowerPoint 中编辑文本框
```

## 🐛 故障排除详解

### 问题 1: "未找到 GEMINI_API_KEY"

**原因**: 环境变量未设置

**解决**:
```bash
# 检查
echo $GEMINI_API_KEY

# 设置（临时）
export GEMINI_API_KEY="AIza..."

# 设置（永久）
echo 'export GEMINI_API_KEY="AIza..."' >> ~/.bashrc
source ~/.bashrc

# 验证
python3 gemini_client.py --test-text
```

### 问题 2: "API 调用失败"

**可能原因**:
- API 密钥无效
- 网络问题
- 配额已用尽

**解决**:
```bash
# 1. 验证密钥
python3 gemini_client.py --check-quota

# 2. 检查网络
curl https://generativelanguage.googleapis.com/

# 3. 查看详细错误
python3 outline-generator.py --input paper.pdf --output outline.json
```

### 问题 3: "图像生成失败"

**原因**: 提示词可能违反内容政策

**解决**:
```bash
# 1. 查看失败的提示词
cat ./ppt-generation/prompts/slideXX_prompt.txt

# 2. 修改提示词，移除敏感内容

# 3. 手动在网页生成该图像
```

### 问题 4: "Python 模块导入错误"

**解决**:
```bash
# 重新安装依赖
pip3 uninstall google-generativeai python-pptx pillow PyPDF2
pip3 install google-generativeai python-pptx pillow PyPDF2

# 或使用虚拟环境
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### 问题 5: "生成的图像质量不好"

**解决方案**:

```bash
# 1. 使用更高分辨率
--image-size 4K

# 2. 使用 Nano Banana Pro 模型
--image-model gemini-3-pro-image-preview

# 3. 调整提示词
# 在 outline.json 中添加更详细的视觉描述

# 4. 使用半自动模式，在网页界面调整
```

## 📈 最佳实践

### 1. 内容准备

✅ **好的输入**:
- 结构清晰的文档（有标题、段落）
- 包含数据和图表
- 明确的主题和受众

❌ **避免**:
- 纯文字墙（无结构）
- 过长的文档（超过 50 页）
- 格式混乱的 PDF

### 2. 风格选择

✅ **好的做法**:
- 根据场合选择合适风格
- 保持整个演示风格一致
- 考虑受众审美偏好

❌ **避免**:
- 在一个演示中混合多种风格
- 选择与内容不匹配的风格
- 过于花哨（学术场合）

### 3. 提示词优化

✅ **好的提示词**:
```
创建一张学术风格的封面幻灯片：
- 标题："深度学习在医疗影像中的应用"
- 副标题："研究进展与展望"
- 居中布局，包含抽象的神经网络图案作为装饰
- 使用蓝色系配色，简洁专业
- 16:9 比例
```

❌ **不好的提示词**:
```
创建一张幻灯片
```

### 4. 迭代优化

**推荐流程**:
1. 先生成 5 页测试效果
2. 查看风格是否符合预期
3. 调整参数后生成完整版
4. 对不满意的单独重新生成

### 5. 选择合适的模式

**选择建议**:
- 首次使用 → 半自动模式（更直观）
- 批量处理 → 完全自动模式（更高效）
- 精品制作 → 纯手动模式（最灵活）

## 🔬 实战案例

### 案例 1: 博士论文答辩（30 页）

```bash
# 需求：高质量、专业、数据详实

# 方案：分两批生成（避免超过20页限制）

# 第一批：1-20 页
python3 outline-generator.py \
  --input thesis.pdf \
  --style academic \
  --slides 20 \
  --topic "我的博士研究（上）" \
  --custom-instructions "重点展示研究方法和实验设计" \
  --output outline-part1.json

python3 image-generator.py \
  --outline outline-part1.json \
  --auto \
  --model gemini-3-pro-image-preview \
  --image-size 4K \
  --output-dir ./defense-part1/

# 第二批：21-30 页
python3 outline-generator.py \
  --input thesis.pdf \
  --style academic \
  --slides 10 \
  --topic "我的博士研究（下）" \
  --custom-instructions "重点展示实验结果和创新点" \
  --output outline-part2.json

python3 image-generator.py \
  --outline outline-part2.json \
  --auto \
  --model gemini-3-pro-image-preview \
  --image-size 4K \
  --output-dir ./defense-part2/

# 合并图像
mkdir -p ./defense-all/images/
cp ./defense-part1/images/*.png ./defense-all/images/
cp ./defense-part2/images/*.png ./defense-all/images/
cd ./defense-all/images/ && for i in {21..30}; do mv slide$(printf "%02d" $((i-20))).png slide$(printf "%02d" $i).png; done

# 组装完整 PPT
python3 pptx-assembler.py \
  --images ./defense-all/images/ \
  --output defense-presentation.pptx \
  --add-textbox
```

### 案例 2: 快速技术分享（12 页）

```bash
# 需求：快速生成、成本低

# 方案：使用 Nano Banana（快速模型）

python3 auto-generate.py \
  --input architecture-overview.md \
  --style technical \
  --slides 12 \
  --auto-images \
  --image-model gemini-2.5-flash-image \
  --output tech-share.pptx

# 耗时：2-3 分钟
```

### 案例 3: 商业提案（15 页）

```bash
# 需求：视觉冲击、交互调整

# 方案：使用半自动模式

python3 auto-generate.py \
  --input business-proposal.pdf \
  --style business \
  --slides 15 \
  --output proposal.pptx

# 脚本暂停后：
# 1. 在 Gemini 网页界面逐张生成
# 2. 对每张图像精细调整
# 3. 确保符合品牌要求
# 4. 下载并继续
```

## 📊 性能基准

### 性能数据（15 页演示）

| 步骤 | 完全自动 | 半自动 |
|------|---------|--------|
| 读取文件 | 2-5 秒 | 2-5 秒 |
| 生成大纲 | 30-60 秒 | 30-60 秒 |
| 生成图像 | 3-5 分钟 | 10-15 分钟 |
| 组装 PPTX | 5-10 秒 | 5-10 秒 |
| **总计** | **4-6 分钟** | **15-20 分钟** |

## 🎓 进阶教程

### 教程 1: 创建自定义风格

```python
# custom-style.py

from prompt_templates import PromptTemplates

# 定义你的风格
my_style = {
    'aesthetic': '未来科技感，赛博朋克风格',
    'background_color': '#0A0E27',
    'background_desc': '深蓝黑背景',
    'primary_font': 'Rajdhani Bold',
    'secondary_font': 'Rajdhani',
    'primary_text_color': '#00FFFF',
    'primary_accent_color': '#FF00FF',
    'visual_elements': '霓虹灯效果、网格线、未来主义图标'
}

# 生成风格指令
style_instruction = PromptTemplates.generate_style_instruction(my_style)

# 保存供后续使用
with open('cyberpunk-style.txt', 'w') as f:
    f.write(style_instruction)
```

### 教程 2: 多语言演示

```bash
# 生成英文演示
python3 auto-generate.py \
  --input paper-en.pdf \
  --output presentation-en.pptx \
  --language en \
  --auto-images

# 生成中文演示
python3 auto-generate.py \
  --input paper-zh.pdf \
  --output presentation-zh.pptx \
  --language zh \
  --auto-images

# 生成双语演示
python3 outline-generator.py \
  --input paper.pdf \
  --custom-instructions "每页幻灯片使用中英双语，中文为主，关键术语标注英文" \
  --output outline-bilingual.json
```

### 教程 3: 集成数据可视化

```bash
# 1. 先生成数据图表
python3 ../../data-visualization/scripts/generate-charts.py \
  --data results.csv \
  --output-dir ./charts/

# 2. 生成演示（提示词中引用图表）
python3 outline-generator.py \
  --input paper.pdf \
  --custom-instructions "在相关幻灯片中使用 ./charts/ 中的数据图表" \
  --output outline.json

# 3. 手动组合或使用提示词描述图表
```

## 📚 参考资源

### 官方文档
- [Gemini 图像生成文档](https://ai.google.dev/gemini-api/docs/image-generation)
- [Nano Banana Pro 指南](https://ai.google.dev/)
- [python-pptx 文档](https://python-pptx.readthedocs.io/)

### 项目文档
- [SKILL.md](../skills/image-based-pptx/SKILL.md) - 完整功能说明
- [prompt-template-zh.md](../skills/image-based-pptx/assets/prompt-template-zh.md) - 提示词模板
- [quickstart.md](../skills/image-based-pptx/examples/quickstart.md) - 快速开始
- [integration-plan.md](./image-based-ppt-integration-plan.md) - 技术方案

### 社区资源
- [原始教程（宝玉）](https://mp.weixin.qq.com/s/MgM__WTDRNNSXividqpx5A)
- [Gemini Gem 中文版](https://gemini.google.com/gem/1KNxu_WTCLKb7PSuqlTsdZUeMWQbroWdR)

## 🤔 常见问题

### Q1: 完全自动化 vs 半自动化，如何选择？

**A**:
- **首次使用** → 半自动（了解流程）
- **批量处理** → 完全自动（节省时间）
- **精品制作** → 半自动（精细调整）
- **成本敏感** → 半自动（成本低）

### Q2: 生成的图像可以编辑吗？

**A**: 图像本身不可编辑（是图片），但可以：
- 使用 `--add-textbox` 添加可编辑文本框
- 在 PowerPoint 中添加新的文本、形状
- 使用 Gemini 网页界面重新生成图像

### Q3: 支持哪些输入格式？

**A**:
- ✅ PDF（最常用）
- ✅ Markdown (.md)
- ✅ 纯文本 (.txt)
- ⚠️ Word (.docx) - 需要先转换
- ⚠️ PPT (.pptx) - 需要先转换

### Q4: 可以生成多少页幻灯片？

**A**:
- 单次最多 20 页（提示词限制）
- 可以分批生成然后合并
- 推荐 12-15 页（最佳效果）

### Q5: 成本大概多少？

**A**:
- 完全自动（15 页，2K）: ~$0.30-0.60
- 半自动（15 页）: ~$0.01
- 使用 Nano Banana（快速）: ~$0.15-0.30

### Q6: 可以商用吗？

**A**:
- 图像带有 SynthID 水印
- 需要遵守 Gemini API 使用条款
- 建议查看 Google 的商用政策

## 🎯 下一步

1. **快速测试**:
   ```bash
   cd scripts/
   bash test-setup.sh
   ```

2. **生成第一个 PPT**:
   ```bash
   python3 auto-generate.py \
     --input /path/to/paper.pdf \
     --auto-images \
     --output my-first-ppt.pptx
   ```

3. **探索高级功能**:
   - 尝试不同风格
   - 调整分辨率和比例
   - 自定义提示词

4. **加入讨论**:
   - 分享你的使用经验
   - 提出改进建议
   - 贡献新风格预设

---

**祝你制作出精彩的演示文稿！** 🎉🚀
