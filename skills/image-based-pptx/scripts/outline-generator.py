#!/usr/bin/env python3
"""
幻灯片大纲生成器

从源文件（PDF, MD, TXT）生成结构化的幻灯片大纲。
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

try:
    from gemini_client import GeminiClient
except ImportError:
    print("错误: 无法导入 gemini_client")
    print("请确保 gemini_client.py 在同一目录下")
    sys.exit(1)


def read_text_file(file_path: str) -> str:
    """
    读取文本文件

    Args:
        file_path: 文件路径

    Returns:
        文件内容
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {file_path}")

    # 读取文本
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # 尝试其他编码
        with open(path, 'r', encoding='gbk') as f:
            content = f.read()

    return content


def read_pdf_file(file_path: str) -> str:
    """
    读取 PDF 文件

    Args:
        file_path: PDF 文件路径

    Returns:
        提取的文本内容
    """
    try:
        import PyPDF2
    except ImportError:
        print("警告: PyPDF2 未安装，无法读取 PDF")
        print("安装方法: pip install PyPDF2")
        return ""

    path = Path(file_path)
    text_parts = []

    with open(path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        total_pages = len(pdf_reader.pages)

        print(f"📄 读取 PDF: {path.name} ({total_pages} 页)")

        for i, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            text_parts.append(text)

            if (i + 1) % 10 == 0:
                print(f"  已处理 {i + 1}/{total_pages} 页")

    full_text = '\n\n'.join(text_parts)
    print(f"✓ 提取了 {len(full_text)} 字符\n")

    return full_text


def read_source_files(file_paths: List[str]) -> str:
    """
    读取多个源文件并合并内容

    Args:
        file_paths: 文件路径列表

    Returns:
        合并后的文本内容
    """
    all_content = []

    for file_path in file_paths:
        path = Path(file_path)
        suffix = path.suffix.lower()

        print(f"📖 读取: {path.name}")

        if suffix == '.pdf':
            content = read_pdf_file(file_path)
        elif suffix in ['.md', '.txt', '.text']:
            content = read_text_file(file_path)
        else:
            print(f"⚠️  不支持的文件格式: {suffix}")
            continue

        all_content.append(f"# 文件: {path.name}\n\n{content}")

    return '\n\n---\n\n'.join(all_content)


def extract_topic_from_content(content: str) -> str:
    """
    从内容中提取可能的主题

    Args:
        content: 文本内容

    Returns:
        提取的主题
    """
    # 简单提取前几行作为主题
    lines = [line.strip() for line in content.split('\n') if line.strip()]

    if not lines:
        return "演示文稿"

    # 查找第一个实质性标题
    for line in lines[:10]:
        if len(line) > 5 and len(line) < 100:
            # 移除markdown标记
            line = line.lstrip('#').strip()
            if line:
                return line

    return lines[0][:100]


def generate_outline(
    input_files: List[str],
    output_file: str,
    style: str = "academic",
    custom_style_file: Optional[str] = None,
    slides: int = 15,
    topic: Optional[str] = None,
    audience: str = "专业人士",
    presentation_type: str = "学术演示",
    custom_instructions: str = "",
    language: str = "zh"
) -> None:
    """
    生成幻灯片大纲

    Args:
        input_files: 输入文件路径列表
        output_file: 输出 JSON 文件路径
        style: 风格名称（当 custom_style_file 为 None 时使用）
        custom_style_file: 自定义风格 JSON 文件路径
        slides: 幻灯片数量
        topic: 主题（如果为 None 则自动提取）
        audience: 目标受众
        presentation_type: 演示类型
        custom_instructions: 自定义指令
        language: 语言
    """
    print("="*60)
    print("幻灯片大纲生成器")
    print("="*60 + "\n")

    # 1. 读取源文件
    print("步骤 1: 读取源文件")
    print("-" * 40)
    content = read_source_files(input_files)

    if not content.strip():
        print("❌ 错误: 无法读取任何内容")
        sys.exit(1)

    print(f"✓ 总共读取 {len(content)} 字符\n")

    # 2. 提取主题（如果未指定）
    if not topic:
        print("步骤 2: 提取主题")
        print("-" * 40)
        topic = extract_topic_from_content(content)
        print(f"✓ 自动识别主题: {topic}\n")
    else:
        print(f"✓ 使用指定主题: {topic}\n")

    # 3. 初始化 Gemini 客户端
    print("步骤 3: 连接 Gemini API")
    print("-" * 40)
    try:
        client = GeminiClient()
        print("✓ API 连接成功\n")
    except Exception as e:
        print(f"❌ API 连接失败: {e}")
        sys.exit(1)

    # 3.5. 加载自定义风格（如果指定）
    actual_style = style
    if custom_style_file:
        print("步骤 3.5: 加载自定义风格")
        print("-" * 40)
        try:
            with open(custom_style_file, 'r', encoding='utf-8') as f:
                custom_style_data = json.load(f)
            actual_style = custom_style_data
            print(f"✓ 已加载自定义风格: {custom_style_file}")
            print(f"  美学: {custom_style_data.get('aesthetic', 'N/A')[:60]}...\n")
        except Exception as e:
            print(f"❌ 加载自定义风格失败: {e}")
            print("将使用默认风格...\n")
            actual_style = style

    # 4. 生成大纲
    print("步骤 4: 生成大纲")
    print("-" * 40)
    try:
        outline = client.generate_outline(
            content=content,
            style=actual_style,
            slide_count=slides,
            topic=topic,
            audience=audience,
            presentation_type=presentation_type,
            custom_instructions=custom_instructions
        )
    except Exception as e:
        print(f"❌ 大纲生成失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # 5. 保存大纲
    print("\n步骤 5: 保存大纲")
    print("-" * 40)
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 添加元数据
    outline['metadata'] = {
        'topic': topic,
        'style': style,
        'slide_count': slides,
        'audience': audience,
        'presentation_type': presentation_type,
        'source_files': [str(Path(f).name) for f in input_files],
        'language': language
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(outline, f, ensure_ascii=False, indent=2)

    print(f"✓ 大纲已保存到: {output_file}")
    print(f"  - 幻灯片数量: {len(outline['slides'])}")
    print(f"  - 风格: {style}")
    print(f"  - 主题: {topic}")

    # 6. 显示预览
    print("\n" + "="*60)
    print("大纲预览")
    print("="*60)

    for i, slide in enumerate(outline['slides'][:3], 1):
        print(f"\n幻灯片 {i}:")
        print(f"  叙事目标: {slide.get('narrative_goal', 'N/A')[:80]}...")
        print(f"  关键内容: {slide.get('key_content', 'N/A')[:80]}...")

    if len(outline['slides']) > 3:
        print(f"\n... 还有 {len(outline['slides']) - 3} 张幻灯片")

    print("\n✓ 大纲生成完成！")
    print(f"\n下一步:")
    print(f"  python image-generator.py --outline {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='生成幻灯片大纲',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 从单个 PDF 生成
  %(prog)s --input paper.pdf --output outline.json

  # 从多个文件生成
  %(prog)s --input paper.pdf notes.md --output outline.json

  # 指定风格和幻灯片数量
  %(prog)s --input paper.pdf --style technical --slides 20

  # 自定义主题和受众
  %(prog)s --input paper.pdf --topic "AI 研究" --audience "研究人员"

可用风格:
  academic   - 学术风格（默认）
  technical  - 技术风格
  business   - 商务风格
  creative   - 创意风格
  minimal    - 极简风格
  playful    - 俏皮风格
        """
    )

    parser.add_argument(
        '--input', '-i',
        nargs='+',
        required=True,
        help='输入文件路径（支持 PDF, MD, TXT）'
    )

    parser.add_argument(
        '--output', '-o',
        default='outline.json',
        help='输出 JSON 文件路径（默认: outline.json）'
    )

    parser.add_argument(
        '--style', '-s',
        default='academic',
        choices=['academic', 'technical', 'business', 'creative', 'minimal', 'playful'],
        help='演示风格（默认: academic）- 如果指定了 --custom-style，此参数将被忽略'
    )

    parser.add_argument(
        '--custom-style',
        help='自定义风格 JSON 文件路径（优先级高于 --style）'
    )

    parser.add_argument(
        '--slides', '-n',
        type=int,
        default=15,
        help='幻灯片数量（默认: 15）'
    )

    parser.add_argument(
        '--topic', '-t',
        help='演示主题（如果不指定则自动提取）'
    )

    parser.add_argument(
        '--audience', '-a',
        default='专业人士',
        help='目标受众（默认: 专业人士）'
    )

    parser.add_argument(
        '--type',
        dest='presentation_type',
        default='学术演示',
        help='演示类型（默认: 学术演示）'
    )

    parser.add_argument(
        '--custom-instructions',
        default='',
        help='自定义指令'
    )

    parser.add_argument(
        '--language', '-l',
        default='zh',
        choices=['zh', 'en'],
        help='语言（默认: zh）'
    )

    args = parser.parse_args()

    try:
        generate_outline(
            input_files=args.input,
            output_file=args.output,
            style=args.style,
            custom_style_file=args.custom_style,
            slides=args.slides,
            topic=args.topic,
            audience=args.audience,
            presentation_type=args.presentation_type,
            custom_instructions=args.custom_instructions,
            language=args.language
        )
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
