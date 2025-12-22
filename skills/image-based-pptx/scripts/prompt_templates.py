#!/usr/bin/env python3
"""
提示词模板系统

用于管理和生成演示文稿的 AI 提示词，支持多种风格预设和自定义配置。
基于 Nano Banana Pro 方法论。
"""

import json
import os
from typing import Dict, List, Optional
from pathlib import Path


class PromptTemplates:
    """幻灯片生成提示词模板管理器"""

    # 内置风格预设
    STYLES = {
        "academic": {
            "aesthetic": "干净、精致、极简主义的编辑风格，受建筑蓝图和高端技术期刊启发",
            "background_color": "#F8F7F5",
            "background_desc": "微妙的、有纹理的灰白色",
            "primary_font": "思源黑体 Bold",
            "secondary_font": "思源宋体",
            "primary_text_color": "#2F3542",
            "primary_accent_color": "#007AFF",
            "visual_elements": "精细的线条图、示意图、干净的矢量图形。布局空间感强，优先考虑信息层级"
        },
        "technical": {
            "aesthetic": "现代科技感，蓝图风格，突出系统架构和技术细节",
            "background_color": "#181B24",
            "background_desc": "深色科技感背景",
            "primary_font": "Roboto Mono Bold",
            "secondary_font": "Roboto",
            "primary_text_color": "#E0E0E0",
            "primary_accent_color": "#00D9FF",
            "visual_elements": "流程图、架构图、技术示意图。使用等线条和几何形状，强调逻辑关系"
        },
        "business": {
            "aesthetic": "专业、现代、商务化，突出数据和成果",
            "background_color": "#FFFFFF",
            "background_desc": "纯白背景",
            "primary_font": "Microsoft YaHei Bold",
            "secondary_font": "Microsoft YaHei Light",
            "primary_text_color": "#333333",
            "primary_accent_color": "#FF6B6B",
            "visual_elements": "数据图表、进度条、指标卡片。使用渐变和阴影增加层次感"
        },
        "creative": {
            "aesthetic": "大胆、色彩丰富、充满创意和视觉冲击力",
            "background_color": "#FFF9E6",
            "background_desc": "温暖米色",
            "primary_font": "站酷快乐体",
            "secondary_font": "思源黑体",
            "primary_text_color": "#1A1A1A",
            "primary_accent_color": "#FF6B35",
            "visual_elements": "插画风格、手绘元素、不规则图形。使用明亮配色和动态构图"
        },
        "minimal": {
            "aesthetic": "极简主义，少即是多，聚焦核心信息",
            "background_color": "#FAFAFA",
            "background_desc": "极浅灰",
            "primary_font": "苹方 Bold",
            "secondary_font": "苹方 Regular",
            "primary_text_color": "#000000",
            "primary_accent_color": "#000000",
            "visual_elements": "大量留白、简单几何图形、单色配色。强调排版和空间"
        },
        "playful": {
            "aesthetic": "友好、俏皮、插画风格，适合教学和入门内容",
            "background_color": "#FFF9F0",
            "background_desc": "柔和米白",
            "primary_font": "方正胖头鱼 Regular",
            "secondary_font": "思源黑体 Regular",
            "primary_text_color": "#2C3E50",
            "primary_accent_color": "#FF6B9D",
            "visual_elements": "插画、卡通图标、柔和色彩。使用波浪线条和圆角矩形"
        }
    }

    # 核心提示词模板
    CORE_PROMPT_TEMPLATE = """你是架构师（The Architect），一个旨在将指令可视化为高端数据展示的精密 AI。你的输出是精确、分析性且美学上精美的。

**核心指令 (CORE DIRECTIVES):**

1. 分析用户提示词的结构、意图和关键要素。
2. 将指令转化为干净、结构化的视觉隐喻（蓝图、展示图、原理图）。
3. 使用特定的、克制的调色板和字体系列，以获得最大的清晰度和专业影响力。
4. 所有视觉输出必须严格保持 16:9 的长宽比。
5. 以三联画或基于网格的布局呈现信息，保持文本和视觉的平衡。

**风格指令 (STYLE INSTRUCTIONS):**

Design Aesthetic: {aesthetic}

Background Color: {background_color}（{background_desc}）

Primary Font: {primary_font}

Secondary Font: {secondary_font}

Color Palette:
    Primary Text Color: {primary_text_color}
    Primary Accent Color: {primary_accent_color}

Visual Elements: {visual_elements}

**绘制内容 (CONTENT TO DRAW):**
"""

    # 大纲生成提示词模板
    OUTLINE_PROMPT_TEMPLATE = """你是一位世界级的演示文稿设计师和故事讲述者。你创作的幻灯片在视觉上令人震撼、极其精美，并能有效地传达复杂的信息。

你现在正在为下述幻灯片演示编写一份**大纲**。我们将把这份大纲提供给一位专家级设计师，由其制作最终的实际演示文稿。

幻灯片内容应使用{language}。占位符应保留{language}。

**演示信息:**
- 主题: {topic}
- 目标受众: {audience}
- 幻灯片数量: {slide_count} 页
- 演示类型: {presentation_type}

**源素材概要:**
{content_summary}

**自定义要求:**
{custom_instructions}

**大纲规则:**

1. **专注于演示文稿的大纲以及每张幻灯片应涵盖的内容**
2. **每张幻灯片的描述必须全面且结构严谨**
3. **第 1 页必须是封面页，最后一页必须是封底页**
4. **封面和封底的风格应与内部页面截然不同**
5. **生成的幻灯片数量恰好是 {slide_count} 页**
6. **避免"标题：副标题"格式**，使用叙事性的主题句
7. **避免 AI 陈词滥调**，如"不仅仅是 [X]，而是 [Y]"
8. **使用直接、自信、主动的人类语言**
9. **切勿包含任何占位符幻灯片**（如"插入姓名"等）
10. **切勿要求包含知名人物的逼真照片**
11. **切勿以通用的"有问题吗？"或"谢谢"结尾**

**幻灯片描述格式:**

对于每一张幻灯片，必须包含以下 4 个部分：

// SLIDE {slide_num}: {slide_title}

// NARRATIVE GOAL
(解释这张幻灯片在整个故事中的具体叙事目的)

// KEY CONTENT
(列出标题、副标题和正文/要点。每一个具体数据点都必须能追溯到源材料)

// VISUAL
(描述支持该观点所需的图像、图表、图形或抽象视觉元素)

// LAYOUT
(描述构图、层级、空间安排或焦点)

现在请生成完整的幻灯片大纲，从第 1 页（封面）到第 {slide_count} 页（封底）。
"""

    @classmethod
    def load(cls, style_name: str) -> Dict:
        """
        加载内置风格预设

        Args:
            style_name: 风格名称 (academic, technical, business, creative, minimal, playful)

        Returns:
            风格配置字典

        Raises:
            ValueError: 如果风格名称不存在
        """
        if style_name not in cls.STYLES:
            raise ValueError(
                f"Unknown style: {style_name}. "
                f"Available styles: {', '.join(cls.STYLES.keys())}"
            )
        return cls.STYLES[style_name].copy()

    @classmethod
    def list_styles(cls) -> List[str]:
        """返回所有可用的风格名称"""
        return list(cls.STYLES.keys())

    @classmethod
    def get_style_info(cls, style_name: str) -> Dict:
        """获取风格的详细信息"""
        return cls.load(style_name)

    @classmethod
    def create_custom(cls, style_config: Dict) -> Dict:
        """
        创建自定义风格配置

        Args:
            style_config: 包含风格参数的字典

        Returns:
            完整的风格配置

        Required keys:
            - aesthetic
            - background_color
            - primary_font
            - secondary_font
            - primary_text_color
            - primary_accent_color
            - visual_elements
        """
        required_keys = [
            "aesthetic", "background_color", "primary_font",
            "secondary_font", "primary_text_color",
            "primary_accent_color", "visual_elements"
        ]

        for key in required_keys:
            if key not in style_config:
                raise ValueError(f"Missing required key: {key}")

        # 添加默认的背景描述（如果没有提供）
        if "background_desc" not in style_config:
            style_config["background_desc"] = style_config["background_color"]

        return style_config

    @classmethod
    def generate_style_instruction(cls, style_name: str) -> str:
        """
        生成风格指令提示词

        Args:
            style_name: 风格名称或自定义风格字典

        Returns:
            完整的风格指令提示词
        """
        if isinstance(style_name, str):
            style = cls.load(style_name)
        elif isinstance(style_name, dict):
            style = cls.create_custom(style_name)
        else:
            raise TypeError("style_name must be str or dict")

        return cls.CORE_PROMPT_TEMPLATE.format(**style)

    @classmethod
    def generate_outline_prompt(
        cls,
        topic: str,
        slide_count: int = 15,
        style: str = "academic",
        audience: str = "专业人士",
        presentation_type: str = "学术演示",
        content_summary: str = "",
        custom_instructions: str = "",
        language: str = "中文"
    ) -> str:
        """
        生成完整的大纲生成提示词

        Args:
            topic: 演示主题
            slide_count: 幻灯片数量
            style: 风格名称
            audience: 目标受众
            presentation_type: 演示类型
            content_summary: 源素材概要
            custom_instructions: 自定义指令
            language: 语言（中文/英文）

        Returns:
            完整的大纲生成提示词（包含风格指令）
        """
        # 生成风格指令
        style_instruction = cls.generate_style_instruction(style)

        # 生成大纲提示词
        outline_prompt = cls.OUTLINE_PROMPT_TEMPLATE.format(
            language=language,
            topic=topic,
            audience=audience,
            slide_count=slide_count,
            presentation_type=presentation_type,
            content_summary=content_summary or "（将根据提供的素材自动分析）",
            custom_instructions=custom_instructions or"（无特殊要求）",
            slide_num="{slide_num}",  # 这个留给后续填充
            slide_title="{slide_title}"
        )

        # 组合完整提示词
        full_prompt = f"{style_instruction}\n\n{outline_prompt}"

        return full_prompt

    @classmethod
    def generate_image_prompt(
        cls,
        slide_description: Dict,
        style_instruction: str
    ) -> str:
        """
        为单张幻灯片生成图像生成提示词

        Args:
            slide_description: 幻灯片描述字典，包含：
                - narrative_goal
                - key_content
                - visual
                - layout
            style_instruction: 风格指令

        Returns:
            图像生成提示词
        """
        image_prompt = f"""{style_instruction}

**幻灯片描述:**

叙事目标: {slide_description.get('narrative_goal', '')}

关键内容:
{slide_description.get('key_content', '')}

视觉要求:
{slide_description.get('visual', '')}

布局要求:
{slide_description.get('layout', '')}

请严格按照以上风格指令和要求，生成一张 16:9 比例的幻灯片图像。
"""
        return image_prompt

    @classmethod
    def save_prompt(cls, prompt: str, output_path: str):
        """
        保存提示词到文件

        Args:
            prompt: 提示词内容
            output_path: 输出文件路径
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(prompt)

        print(f"✓ Prompt saved to: {output_path}")

    @classmethod
    def load_prompt(cls, file_path: str) -> str:
        """
        从文件加载提示词

        Args:
            file_path: 文件路径

        Returns:
            提示词内容
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()


def main():
    """示例用法"""
    import argparse

    parser = argparse.ArgumentParser(description='提示词模板生成工具')
    parser.add_argument('--list-styles', action='store_true',
                       help='列出所有可用风格')
    parser.add_argument('--style', default='academic',
                       help='选择风格预设')
    parser.add_argument('--topic', help='演示主题')
    parser.add_argument('--slides', type=int, default=15,
                       help='幻灯片数量')
    parser.add_argument('--output', help='输出文件路径')

    args = parser.parse_args()

    if args.list_styles:
        print("可用风格:")
        for style_name in PromptTemplates.list_styles():
            style = PromptTemplates.load(style_name)
            print(f"\n{style_name}:")
            print(f"  {style['aesthetic']}")
        return

    if not args.topic:
        print("错误: 需要指定 --topic")
        return

    # 生成提示词
    prompt = PromptTemplates.generate_outline_prompt(
        topic=args.topic,
        slide_count=args.slides,
        style=args.style
    )

    if args.output:
        PromptTemplates.save_prompt(prompt, args.output)
    else:
        print("\n" + "="*60)
        print("生成的提示词:")
        print("="*60)
        print(prompt)


if __name__ == "__main__":
    main()
