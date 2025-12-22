#!/usr/bin/env python3
"""
Gemini API 客户端

封装 Google Generative AI API，提供文本生成和图像生成功能。
"""

import os
import time
import base64
from typing import Optional, Dict, List
from pathlib import Path
import json

try:
    import google.generativeai as genai
    from google.api_core import exceptions as google_exceptions
except ImportError:
    print("错误: 需要安装 google-generativeai")
    print("运行: pip install google-generativeai")
    exit(1)


class GeminiClient:
    """Gemini API 客户端封装"""

    def __init__(self, api_key: Optional[str] = None):
        """
        初始化 Gemini 客户端

        Args:
            api_key: Gemini API 密钥，如果为 None 则从环境变量读取
        """
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError(
                "未找到 GEMINI_API_KEY。请设置环境变量或传入 api_key 参数。\n"
                "设置方法: export GEMINI_API_KEY='your-api-key'"
            )

        genai.configure(api_key=self.api_key)

        # 默认模型配置
        self.text_model = 'gemini-1.5-pro'  # 用于文本生成
        self.image_model = 'gemini-1.5-pro'  # 用于图像生成（注意：实际使用 Imagen 3）

        # 重试配置
        self.max_retries = 3
        self.retry_delay = 2  # 秒

    def generate_text(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """
        生成文本内容

        Args:
            prompt: 输入提示词
            temperature: 温度参数 (0-1)
            max_tokens: 最大生成 token 数
            **kwargs: 其他生成参数

        Returns:
            生成的文本

        Raises:
            Exception: API 调用失败
        """
        model = genai.GenerativeModel(self.text_model)

        generation_config = {
            'temperature': temperature,
        }
        if max_tokens:
            generation_config['max_output_tokens'] = max_tokens

        generation_config.update(kwargs)

        for attempt in range(self.max_retries):
            try:
                response = model.generate_content(
                    prompt,
                    generation_config=generation_config
                )
                return response.text

            except google_exceptions.ResourceExhausted as e:
                print(f"⚠️  API 配额已用尽: {e}")
                if attempt < self.max_retries - 1:
                    wait_time = self.retry_delay * (2 ** attempt)
                    print(f"等待 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
                else:
                    raise

            except google_exceptions.InvalidArgument as e:
                print(f"❌ API 参数错误: {e}")
                raise

            except Exception as e:
                print(f"⚠️  API 调用失败 (尝试 {attempt + 1}/{self.max_retries}): {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise

    def generate_image(
        self,
        prompt: str,
        output_path: str,
        aspect_ratio: str = "16:9",
        model: str = "gemini-3-pro-image-preview",
        image_size: str = "2K",
        response_modalities: Optional[List[str]] = None,
        **kwargs
    ) -> bool:
        """
        生成图像（使用 Nano Banana Pro）

        Args:
            prompt: 图像描述提示词
            output_path: 输出图像路径
            aspect_ratio: 宽高比 (1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)
            model: 模型名称
                   - "gemini-3-pro-image-preview" (Nano Banana Pro, 高质量, 支持1K/2K/4K)
                   - "gemini-2.5-flash-image" (Nano Banana, 快速, 1024px)
            image_size: 图像分辨率 ("1K", "2K", "4K") - 仅 Nano Banana Pro 支持
            response_modalities: 响应模式，默认 ['Text', 'Image']
            **kwargs: 其他生成参数

        Returns:
            是否成功生成

        Raises:
            Exception: API 调用失败
        """
        from google.genai import types

        if response_modalities is None:
            response_modalities = ['Text', 'Image']

        # 构建配置
        config_params = {
            'response_modalities': response_modalities,
            'image_config': types.ImageConfig(
                aspect_ratio=aspect_ratio,
            )
        }

        # 只有 Nano Banana Pro 支持 image_size 参数
        if model == "gemini-3-pro-image-preview" and image_size:
            config_params['image_config'].image_size = image_size

        generation_config = types.GenerateContentConfig(**config_params)

        for attempt in range(self.max_retries):
            try:
                response = genai.Client(api_key=self.api_key).models.generate_content(
                    model=model,
                    contents=[prompt],
                    config=generation_config
                )

                # 保存生成的图像
                image_saved = False
                output_path_obj = Path(output_path)
                output_path_obj.parent.mkdir(parents=True, exist_ok=True)

                for part in response.parts:
                    if part.text is not None:
                        # 打印文本描述
                        print(f"  描述: {part.text[:100]}...")
                    elif part.inline_data is not None:
                        # 保存图像
                        image = part.as_image()
                        image.save(str(output_path_obj))
                        image_saved = True
                        print(f"  ✓ 图像已保存: {output_path}")
                        break

                if not image_saved:
                    print(f"  ⚠️ 警告: 响应中未找到图像数据")
                    return False

                return True

            except google_exceptions.ResourceExhausted as e:
                print(f"⚠️  API 配额已用尽: {e}")
                if attempt < self.max_retries - 1:
                    wait_time = self.retry_delay * (2 ** attempt)
                    print(f"等待 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
                else:
                    raise

            except google_exceptions.InvalidArgument as e:
                print(f"❌ API 参数错误: {e}")
                raise

            except Exception as e:
                print(f"⚠️  API 调用失败 (尝试 {attempt + 1}/{self.max_retries}): {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise

        return False

    def generate_outline(
        self,
        content: str,
        style: str = "academic",
        slide_count: int = 15,
        custom_instructions: str = "",
        **kwargs
    ) -> Dict:
        """
        生成幻灯片大纲

        Args:
            content: 源内容（文本、摘要等）
            style: 风格名称
            slide_count: 幻灯片数量
            custom_instructions: 自定义指令
            **kwargs: 其他参数（audience, topic等）

        Returns:
            大纲字典，包含 style_instruction 和 slides 列表
        """
        from .prompt_templates import PromptTemplates

        # 提取或生成主题
        topic = kwargs.get('topic', '演示文稿')
        audience = kwargs.get('audience', '专业人士')
        presentation_type = kwargs.get('presentation_type', '学术演示')

        # 生成提示词
        prompt = PromptTemplates.generate_outline_prompt(
            topic=topic,
            slide_count=slide_count,
            style=style,
            audience=audience,
            presentation_type=presentation_type,
            content_summary=content[:2000],  # 限制长度
            custom_instructions=custom_instructions
        )

        print(f"🎨 生成 {slide_count} 页 {style} 风格大纲...")
        print(f"📝 主题: {topic}")
        print(f"👥 受众: {audience}\n")

        # 调用 API 生成
        response_text = self.generate_text(
            prompt,
            temperature=0.7,
            max_tokens=8000
        )

        # 解析响应
        outline = self._parse_outline_response(response_text, style)

        print(f"✓ 成功生成 {len(outline['slides'])} 页大纲")

        return outline

    def _parse_outline_response(self, response: str, style: str) -> Dict:
        """
        解析大纲生成响应

        Args:
            response: API 响应文本
            style: 风格名称

        Returns:
            结构化的大纲字典
        """
        from .prompt_templates import PromptTemplates

        # 获取风格指令
        style_instruction = PromptTemplates.generate_style_instruction(style)

        # 简单解析（按 SLIDE 分割）
        slides = []
        lines = response.split('\n')

        current_slide = None
        current_section = None
        section_content = []

        for line in lines:
            line = line.strip()

            # 检测新幻灯片
            if line.startswith('// SLIDE') or line.startswith('//SLIDE'):
                # 保存上一张幻灯片
                if current_slide and current_section:
                    current_slide[current_section] = '\n'.join(section_content).strip()

                if current_slide:
                    slides.append(current_slide)

                # 开始新幻灯片
                current_slide = {'slide_num': len(slides) + 1}
                current_section = None
                section_content = []
                continue

            # 检测各个部分
            if line.startswith('// NARRATIVE GOAL'):
                if current_section and current_slide:
                    current_slide[current_section] = '\n'.join(section_content).strip()
                current_section = 'narrative_goal'
                section_content = []
                continue

            elif line.startswith('// KEY CONTENT'):
                if current_section and current_slide:
                    current_slide[current_section] = '\n'.join(section_content).strip()
                current_section = 'key_content'
                section_content = []
                continue

            elif line.startswith('// VISUAL'):
                if current_section and current_slide:
                    current_slide[current_section] = '\n'.join(section_content).strip()
                current_section = 'visual'
                section_content = []
                continue

            elif line.startswith('// LAYOUT'):
                if current_section and current_slide:
                    current_slide[current_section] = '\n'.join(section_content).strip()
                current_section = 'layout'
                section_content = []
                continue

            # 添加内容到当前部分
            if current_section and line and not line.startswith('//'):
                section_content.append(line)

        # 保存最后一张幻灯片
        if current_slide and current_section:
            current_slide[current_section] = '\n'.join(section_content).strip()
        if current_slide:
            slides.append(current_slide)

        return {
            'style': style,
            'style_instruction': style_instruction,
            'slides': slides
        }

    def check_quota(self) -> Dict:
        """
        检查 API 配额（模拟）

        Returns:
            配额信息字典
        """
        # 注意：Gemini API 目前没有直接的配额查询接口
        # 这里返回模拟信息
        return {
            'status': 'unknown',
            'message': 'Gemini API 没有提供配额查询接口。请在 API 调用时注意速率限制。'
        }


def main():
    """测试和示例"""
    import argparse

    parser = argparse.ArgumentParser(description='Gemini API 客户端测试')
    parser.add_argument('--test-text', action='store_true',
                       help='测试文本生成')
    parser.add_argument('--test-outline', action='store_true',
                       help='测试大纲生成')
    parser.add_argument('--test-image', action='store_true',
                       help='测试图像生成')
    parser.add_argument('--check-quota', action='store_true',
                       help='检查 API 配额')
    parser.add_argument('--output', default='test_image.png',
                       help='测试图像输出路径')

    args = parser.parse_args()

    try:
        client = GeminiClient()

        if args.test_text:
            print("测试文本生成...")
            response = client.generate_text(
                "请用一句话介绍 Gemini API",
                temperature=0.5
            )
            print(f"响应: {response}\n")

        if args.test_outline:
            print("测试大纲生成...")
            outline = client.generate_outline(
                content="这是一篇关于人工智能的研究论文，讨论了深度学习在计算机视觉中的应用。",
                style="academic",
                slide_count=5,
                topic="人工智能研究",
                audience="计算机科学研究者"
            )
            print(f"\n生成了 {len(outline['slides'])} 张幻灯片")
            print(f"第一张: {outline['slides'][0]}")

        if args.test_image:
            print("测试图像生成（Nano Banana Pro）...")
            print(f"输出路径: {args.output}\n")

            test_prompt = """你是架构师（The Architect），一个旨在将指令可视化为高端数据展示的精密 AI。

**风格指令:**
Design Aesthetic: 干净、精致、极简主义
Background Color: #F8F7F5（微妙的灰白色）
Primary Font: 思源黑体 Bold
Color Palette:
    Primary Text Color: #2F3542
    Primary Accent Color: #007AFF

**绘制内容:**
创建一张标题为"深度学习研究"的学术风格封面幻灯片。
居中布局，包含副标题"研究进展与展望"，底部标注作者信息。
使用简洁的几何图形作为装饰元素。
16:9 比例。
"""

            success = client.generate_image(
                prompt=test_prompt,
                output_path=args.output,
                model="gemini-3-pro-image-preview",
                image_size="2K",
                aspect_ratio="16:9"
            )

            if success:
                print(f"\n✓ 测试成功！图像已保存到: {args.output}")
            else:
                print(f"\n❌ 测试失败")

        if args.check_quota:
            quota = client.check_quota()
            print(f"配额状态: {quota}")

        if not any([args.test_text, args.test_outline, args.test_image, args.check_quota]):
            print("请指定测试选项:")
            print("  --test-text      测试文本生成")
            print("  --test-outline   测试大纲生成")
            print("  --test-image     测试图像生成（Nano Banana Pro）")
            print("  --check-quota    检查配额")

    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
