# 自定义风格完全指南

本指南教你如何创建和使用自己的演示文稿视觉风格。

## 🎨 什么是自定义风格？

自定义风格允许你完全控制演示文稿的视觉外观，包括：

- 配色方案
- 字体选择
- 视觉元素类型
- 整体美学风格

## 📝 风格配置文件格式

### 必需字段

创建一个 JSON 文件，包含以下字段：

```json
{
  "aesthetic": "整体设计美学描述",
  "background_color": "#HEXCODE",
  "background_desc": "背景颜色描述",
  "primary_font": "标题字体名称",
  "secondary_font": "正文字体名称",
  "primary_text_color": "#HEXCODE",
  "primary_accent_color": "#HEXCODE",
  "visual_elements": "视觉元素和设计风格描述"
}
```

### 字段详解

#### 1. aesthetic (美学风格)

描述整体的设计感觉和氛围。

**示例**:
```json
"aesthetic": "干净、精致、极简主义，受建筑蓝图启发"
"aesthetic": "大胆、色彩丰富、充满创意和视觉冲击力"
"aesthetic": "现代科技感，赛博朋克风格，霓虹色彩"
"aesthetic": "温暖、友好、手绘插画风格"
```

#### 2. background_color (背景颜色)

16进制颜色代码。

**建议**:
- 浅色背景: `#F8F7F5`, `#FFFFFF`, `#FFF9E6`
- 深色背景: `#181B24`, `#1E1E1E`, `#0A0E27`
- 特殊背景: `#FAFAFA`, `#F0F4EC`

#### 3. background_desc (背景描述)

用文字描述背景颜色的感觉。

**示例**:
```json
"background_desc": "微妙的、有纹理的灰白色"
"background_desc": "深色科技感背景"
"background_desc": "温暖米色，如牛皮纸"
```

#### 4. primary_font (主字体)

用于标题和重要文字。

**中文字体推荐**:
- 学术: `思源黑体 Bold`, `苹方 Bold`
- 创意: `站酷快乐体`, `方正胖头鱼`
- 商务: `Microsoft YaHei Bold`
- 技术: `等距更纱黑体`, `Sarasa Mono SC`

**英文字体推荐**:
- 学术: `Helvetica Neue Bold`, `Roboto Bold`
- 创意: `Montserrat Bold`, `Poppins Bold`
- 商务: `Arial Bold`, `Open Sans Bold`
- 技术: `Roboto Mono Bold`, `Fira Code Bold`

#### 5. secondary_font (次字体)

用于正文和辅助文字。

通常选择与主字体配套的常规体或细体。

#### 6. primary_text_color (主文字颜色)

正文的主要颜色。

**建议**:
- 深色文字配浅色背景: `#2F3542`, `#333333`
- 浅色文字配深色背景: `#E0E0E0`, `#FFFFFF`

#### 7. primary_accent_color (强调色)

用于高亮、重点标注。

**建议**:
- 蓝色系: `#007AFF`, `#2196F3`, `#00D9FF`
- 红色系: `#FF6B6B`, `#FF6B35`
- 绿色系: `#7CB342`, `#00C853`
- 紫色系: `#B165FB`, `#9C27B0`
- 彩色: `#FF6B9D`, `#FFB84D`

#### 8. visual_elements (视觉元素)

描述要使用的图形、图标、装饰元素风格。

**示例**:
```json
"visual_elements": "精细的线条图、示意图、干净的矢量图形"
"visual_elements": "插画、卡通图标、柔和色彩、波浪线条"
"visual_elements": "数据图表、进度条、指标卡片、渐变和阴影"
"visual_elements": "霓虹灯效果、网格线、几何图形、渐变色"
```

## 💡 完整示例

### 示例 1: 赛博朋克风格

```json
{
  "aesthetic": "赛博朋克、未来主义、霓虹灯光、高科技低生活",
  "background_color": "#0A0E27",
  "background_desc": "深蓝黑背景，如夜空般深邃",
  "primary_font": "Orbitron Bold",
  "secondary_font": "Rajdhani Regular",
  "primary_text_color": "#00FFFF",
  "primary_accent_color": "#FF00FF",
  "visual_elements": "霓虹灯管效果、网格地板、全息投影感。使用青色和品红色强调，添加发光效果和扫描线"
}
```

### 示例 2: 优雅古典风格

```json
{
  "aesthetic": "优雅、古典、奢华，受欧洲宫廷艺术启发",
  "background_color": "#F5F3EE",
  "background_desc": "温暖的象牙白，如古老羊皮纸",
  "primary_font": "Playfair Display Bold",
  "secondary_font": "Lora Regular",
  "primary_text_color": "#2C2416",
  "primary_accent_color": "#B8860B",
  "visual_elements": "装饰性花纹边框、优雅的曲线、金色装饰。使用对称布局和古典比例，营造高雅气质"
}
```

### 示例 3: 清新自然风格

```json
{
  "aesthetic": "清新、自然、有机，与大自然和谐共处",
  "background_color": "#F0F4EC",
  "background_desc": "浅绿米色，如清晨的薄雾",
  "primary_font": "Quicksand Bold",
  "secondary_font": "Quicksand Regular",
  "primary_text_color": "#2D5016",
  "primary_accent_color": "#7CB342",
  "visual_elements": "水彩笔触、叶子图案、有机曲线。使用大地色系和绿色，加入自然纹理和柔和阴影"
}
```

### 示例 4: 极简黑白风格

```json
{
  "aesthetic": "极简主义、黑白对比、瑞士国际主义风格",
  "background_color": "#FFFFFF",
  "background_desc": "纯白背景，如画布般纯净",
  "primary_font": "Helvetica Neue Bold",
  "secondary_font": "Helvetica Neue Light",
  "primary_text_color": "#000000",
  "primary_accent_color": "#000000",
  "visual_elements": "纯几何图形、粗黑线条、大量留白。只使用黑白两色，通过排版和空间创造视觉层次"
}
```

## 🚀 使用自定义风格

### 方法 1: 使用示例风格

```bash
# 使用赛博朋克风格
python3 outline-generator.py \
  --input paper.pdf \
  --custom-style ../examples/custom-style-example.json \
  --output outline.json

# 使用优雅风格
python3 outline-generator.py \
  --input paper.pdf \
  --custom-style ../examples/style-templates/elegant.json \
  --output outline.json
```

### 方法 2: 创建你自己的风格

```bash
# 1. 创建风格文件
cat > my-style.json << 'EOF'
{
  "aesthetic": "你的美学描述",
  "background_color": "#yourcolor",
  "background_desc": "颜色描述",
  "primary_font": "你的字体",
  "secondary_font": "你的字体",
  "primary_text_color": "#yourcolor",
  "primary_accent_color": "#yourcolor",
  "visual_elements": "你的视觉元素描述"
}
EOF

# 2. 验证 JSON 格式
python3 -m json.tool my-style.json

# 3. 使用自定义风格
python3 outline-generator.py \
  --input paper.pdf \
  --custom-style my-style.json \
  --output outline.json
```

### 方法 3: 在代码中创建

```python
from prompt_templates import PromptTemplates
import json

# 定义风格
my_style = {
    "aesthetic": "极简主义、日式美学、侘寂风格",
    "background_color": "#E8E6E3",
    "background_desc": "温润的米灰色，如和纸般温暖",
    "primary_font": "Noto Serif JP Bold",
    "secondary_font": "Noto Sans JP Light",
    "primary_text_color": "#3A3A3A",
    "primary_accent_color": "#8B4513",
    "visual_elements": "极简线条、留白艺术、墨点装饰。使用自然材质纹理，营造平静禅意"
}

# 保存为文件
with open('japanese-zen.json', 'w', encoding='utf-8') as f:
    json.dump(my_style, f, ensure_ascii=False, indent=2)

# 验证风格
try:
    style = PromptTemplates.create_custom(my_style)
    print("✓ 风格配置有效")
except ValueError as e:
    print(f"❌ 风格配置错误: {e}")
```

## 🎨 配色方案建议

### 学术/专业

```json
{
  "background_color": "#F8F7F5",
  "primary_text_color": "#2F3542",
  "primary_accent_color": "#007AFF"
}
```

### 商务/现代

```json
{
  "background_color": "#FFFFFF",
  "primary_text_color": "#333333",
  "primary_accent_color": "#FF6B6B"
}
```

### 创意/活力

```json
{
  "background_color": "#FFF9E6",
  "primary_text_color": "#1A1A1A",
  "primary_accent_color": "#FF6B35"
}
```

### 科技/深色

```json
{
  "background_color": "#181B24",
  "primary_text_color": "#E0E0E0",
  "primary_accent_color": "#00D9FF"
}
```

## 🧪 测试你的风格

### 快速测试

```bash
# 1. 创建测试风格
cat > test-style.json << 'EOF'
{
  "aesthetic": "测试风格",
  "background_color": "#FFFFFF",
  "background_desc": "纯白",
  "primary_font": "Arial Bold",
  "secondary_font": "Arial",
  "primary_text_color": "#000000",
  "primary_accent_color": "#FF0000",
  "visual_elements": "简单图形"
}
EOF

# 2. 生成 3 页测试
python3 outline-generator.py \
  --input short-doc.md \
  --custom-style test-style.json \
  --slides 3 \
  --output test-outline.json

# 3. 生成图像
python3 image-generator.py \
  --outline test-outline.json \
  --auto \
  --output-dir ./test-output/

# 4. 查看效果
python3 pptx-assembler.py \
  --images ./test-output/images/ \
  --output test.pptx

# 5. 在 PowerPoint 中打开查看
```

## 💡 设计技巧

### 1. 选择配色

**在线工具**:
- [Adobe Color](https://color.adobe.com/)
- [Coolors](https://coolors.co/)
- [Paletton](https://paletton.com/)

**配色原则**:
- 背景与文字要有足够对比度
- 强调色要醒目但不刺眼
- 整体不超过 3-4 种颜色

### 2. 字体搭配

**经典搭配**:
- 无衬线标题 + 衬线正文
- 粗体标题 + 细体正文
- 等宽标题 + 常规正文（技术风格）

**字体资源**:
- [Google Fonts](https://fonts.google.com/)
- [思源字体](https://github.com/adobe-fonts/source-han-sans)
- [站酷字体](https://www.zcool.com.cn/special/zcoolfonts/)

### 3. 视觉元素描述

越详细越好！告诉 AI：

- 使用什么类型的图形（几何、有机、手绘）
- 线条粗细和样式
- 是否使用阴影、渐变
- 图标风格（扁平、立体、线性）

## 📚 常见风格模板

我们提供了一些预制的风格模板，可直接使用或修改：

### 可用模板

```bash
examples/style-templates/
├── elegant.json       # 优雅奢华风格
├── nature.json        # 清新自然风格
└── modern-dark.json   # 现代深色风格
```

### 使用模板

```bash
# 直接使用
python3 outline-generator.py \
  --input paper.pdf \
  --custom-style ../examples/style-templates/elegant.json \
  --output outline.json

# 修改后使用
cp ../examples/style-templates/elegant.json my-elegant.json
# 编辑 my-elegant.json
python3 outline-generator.py \
  --input paper.pdf \
  --custom-style my-elegant.json \
  --output outline.json
```

## 🎯 实战案例

### 案例 1: 为医疗主题创建风格

```json
{
  "aesthetic": "清洁、专业、医疗健康感，传递信任和关怀",
  "background_color": "#F7FBFF",
  "background_desc": "极浅的医疗蓝，如清晨的天空",
  "primary_font": "Source Sans Pro Bold",
  "secondary_font": "Source Sans Pro Regular",
  "primary_text_color": "#2C3E50",
  "primary_accent_color": "#3498DB",
  "visual_elements": "医疗图标（十字、心电图）、柔和的圆角矩形、渐变蓝色。使用干净的线条图和简化的人体图示，营造专业可信赖的感觉"
}
```

使用：
```bash
python3 auto-generate.py \
  --input medical-research.pdf \
  --custom-style medical-style.json \
  --auto-images \
  --output medical-presentation.pptx
```

### 案例 2: 为艺术作品集创建风格

```json
{
  "aesthetic": "艺术画廊风格、高端展览感、突出作品本身",
  "background_color": "#FAFAFA",
  "background_desc": "极浅灰，如画廊白墙",
  "primary_font": "Didot Bold",
  "secondary_font": "Futura Light",
  "primary_text_color": "#1A1A1A",
  "primary_accent_color": "#D4AF37",
  "visual_elements": "大量留白、精致的边框、金色细线。作品图像占据主要空间，文字简洁克制，营造艺术馆的展示氛围"
}
```

### 案例 3: 为教育课件创建风格

```json
{
  "aesthetic": "友好、生动、教育性，激发学习兴趣",
  "background_color": "#FFF8E7",
  "background_desc": "温暖奶黄色，如笔记本纸",
  "primary_font": "Comic Neue Bold",
  "secondary_font": "Comic Neue Regular",
  "primary_text_color": "#3D4852",
  "primary_accent_color": "#FF9500",
  "visual_elements": "卡通图标、对话气泡、手绘箭头。使用明亮但柔和的配色，添加趣味性元素（星星、笑脸），让学习变得轻松愉快"
}
```

## ⚠️ 常见错误

### 错误 1: 缺少必需字段

```json
{
  "aesthetic": "我的风格",
  "background_color": "#FFFFFF"
  // ❌ 缺少其他必需字段
}
```

**错误信息**: `Missing required key: primary_font`

**解决**: 确保包含所有 8 个必需字段

### 错误 2: 颜色格式错误

```json
{
  "background_color": "white"  // ❌ 应该用十六进制
}
```

**正确格式**: `"#FFFFFF"` 或 `"#FFF"`

### 错误 3: JSON 格式错误

```json
{
  "aesthetic": "我的风格",  // ✓ 最后一项后不应有逗号
}  // ❌ 多余的逗号
```

**验证方法**:
```bash
python3 -m json.tool your-style.json
```

## 🔍 调试技巧

### 查看生成的风格指令

```python
from prompt_templates import PromptTemplates
import json

# 加载你的风格
with open('my-style.json', 'r') as f:
    style = json.load(f)

# 生成风格指令
instruction = PromptTemplates.generate_style_instruction(style)

# 打印查看
print(instruction)

# 保存供检查
with open('style-instruction.txt', 'w', encoding='utf-8') as f:
    f.write(instruction)
```

### 对比效果

```bash
# 生成同一内容的不同风格版本
for style in elegant nature modern-dark; do
  python3 outline-generator.py \
    --input paper.pdf \
    --custom-style ../examples/style-templates/$style.json \
    --slides 5 \
    --output outline-$style.json
done

# 然后分别生成图像对比
```

## 🎨 风格灵感来源

### 设计网站
- [Behance](https://www.behance.net/) - 设计作品展示
- [Dribbble](https://dribbble.com/) - UI/UX 设计
- [Pinterest](https://pinterest.com/) - 视觉灵感板

### 演示文稿灵感
- [Slidesgo](https://slidesgo.com/) - 演示模板
- [Canva](https://www.canva.com/templates/presentations/) - 设计模板

### 配色工具
- [Coolors](https://coolors.co/) - 配色生成器
- [Adobe Color](https://color.adobe.com/) - 配色轮盘
- [ColorHunt](https://colorhunt.co/) - 流行配色

## 📋 最佳实践

### 1. 从预设开始

先使用内置风格，看哪个最接近你的需求，然后基于它修改。

```bash
# 复制预设风格
cp ../examples/style-templates/elegant.json my-style.json

# 编辑修改
nano my-style.json
```

### 2. 保持一致性

整个演示使用同一风格配置，不要中途改变。

### 3. 测试少量页面

先生成 3-5 页测试效果，满意后再生成完整版。

### 4. 记录你的风格

为每个项目保存风格文件，便于后续复用。

```bash
project/
├── my-style.json
├── outline.json
└── presentation.pptx
```

### 5. 迭代优化

不满意就调整配置重新生成，直到达到理想效果。

## 🤝 分享你的风格

如果你创建了优秀的风格配置，欢迎分享！

可以提交到：
```
skills/image-based-pptx/examples/style-templates/your-style.json
```

---

**创造属于你自己的独特风格！** 🎨✨
