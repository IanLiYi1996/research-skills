#!/usr/bin/env python3
"""
幻灯片图像批量生成器

从大纲 JSON 生成每张幻灯片的图像提示词，并提供手动/自动生成选项。
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

try:
    from prompt_templates import PromptTemplates
except ImportError:
    print("错误: 无法导入 prompt_templates")
    print("请确保 prompt_templates.py 在同一目录下")
    sys.exit(1)


def load_outline(outline_file: str) -> Dict:
    """
    加载大纲 JSON 文件

    Args:
        outline_file: 大纲文件路径

    Returns:
        大纲字典
    """
    path = Path(outline_file)

    if not path.exists():
        raise FileNotFoundError(f"大纲文件不存在: {outline_file}")

    with open(path, 'r', encoding='utf-8') as f:
        outline = json.load(f)

    return outline


def generate_image_prompts(outline: Dict) -> List[Dict]:
    """
    为每张幻灯片生成图像提示词

    Args:
        outline: 大纲字典

    Returns:
        图像提示词列表
    """
    style_instruction = outline.get('style_instruction', '')
    slides = outline.get('slides', [])

    image_prompts = []

    for i, slide in enumerate(slides, 1):
        # 生成图像提示词
        prompt = PromptTemplates.generate_image_prompt(
            slide_description=slide,
            style_instruction=style_instruction
        )

        image_prompts.append({
            'slide_num': i,
            'prompt': prompt,
            'slide_info': {
                'narrative_goal': slide.get('narrative_goal', '')[:100],
                'key_content': slide.get('key_content', '')[:100]
            }
        })

    return image_prompts


def save_prompts_for_manual_use(
    prompts: List[Dict],
    output_dir: str
) -> None:
    """
    保存提示词文件，供手动在 Gemini 界面使用

    Args:
        prompts: 图像提示词列表
        output_dir: 输出目录
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. 保存单独的提示词文件
    prompts_dir = output_path / 'prompts'
    prompts_dir.mkdir(exist_ok=True)

    for prompt_data in prompts:
        slide_num = prompt_data['slide_num']
        filename = f"slide{slide_num:02d}_prompt.txt"

        with open(prompts_dir / filename, 'w', encoding='utf-8') as f:
            f.write(prompt_data['prompt'])

    print(f"✓ 已保存 {len(prompts)} 个提示词文件到: {prompts_dir}")

    # 2. 保存合并的提示词文件（便于复制）
    combined_file = output_path / 'all_prompts.txt'

    with open(combined_file, 'w', encoding='utf-8') as f:
        for prompt_data in prompts:
            f.write(f"\n{'='*60}\n")
            f.write(f"幻灯片 {prompt_data['slide_num']}\n")
            f.write(f"{'='*60}\n\n")
            f.write(prompt_data['prompt'])
            f.write(f"\n\n")

    print(f"✓ 已保存合并提示词到: {combined_file}")

    # 3. 创建使用说明
    instructions_file = output_path / 'INSTRUCTIONS.md'

    instructions = f"""# 图像生成使用说明

## 自动生成（推荐）

已为您生成 {len(prompts)} 张幻灯片的提示词。

## 手动生成步骤

### 方法 1: 在 Gemini 网页界面生成

1. **打开 Gemini**
   访问: https://gemini.google.com/

2. **选择图像生成工具**
   - 点击 "🍌 Create Images" 或类似的图像生成工具

3. **复制风格指令**
   打开 `风格指令.txt` 文件，将内容复制到 Gemini
   - 这会设定所有幻灯片的统一视觉风格

4. **逐个生成幻灯片图像**
   对于每张幻灯片：
   a. 打开 `prompts/slide01_prompt.txt`（从 01 到 {len(prompts):02d}）
   b. 复制内容并发送给 Gemini
   c. 等待图像生成
   d. 下载图像，命名为 `slide01.png`（与序号对应）
   e. 保存到 `images/` 目录

5. **重复步骤 4** 直到所有幻灯片图像都生成完毕

### 方法 2: 使用批量提示词

如果你想一次性看到所有提示词：

1. 打开 `all_prompts.txt`
2. 按顺序复制每个提示词到 Gemini
3. 生成并下载图像

## 文件结构

```
{output_path.name}/
├── INSTRUCTIONS.md          # 本文件
├── 风格指令.txt             # 统一的风格设定
├── all_prompts.txt          # 所有提示词（合并）
├── prompts/                 # 单独的提示词文件
│   ├── slide01_prompt.txt
│   ├── slide02_prompt.txt
│   └── ...
└── images/                  # 存放生成的图像
    ├── slide01.png
    ├── slide02.png
    └── ...
```

## 图像命名规范

**重要**: 请严格按照以下格式命名图像：

- `slide01.png` - 第 1 张幻灯片
- `slide02.png` - 第 2 张幻灯片
- `slide03.png` - 第 3 张幻灯片
- ...
- `slide{len(prompts):02d}.png` - 第 {len(prompts)} 张幻灯片

## 生成完毕后

当所有图像都生成并下载到 `images/` 目录后，运行：

```bash
python pptx-assembler.py --images {output_path}/images/ --output presentation.pptx
```

这将把所有图像组装成一个完整的 PowerPoint 演示文稿。

## 提示

- ✅ 保持统一的风格指令很重要
- ✅ 按顺序生成可以更好地保持叙事连贯性
- ✅ 如果某张图像不满意，可以多次生成并选择最好的
- ✅ 可以在提示词基础上微调，以获得更好的效果

## 故障排除

**Q: Gemini 说无法生成图像?**
A: 确保你选择了图像生成工具（Create Images / Imagen）

**Q: 图像质量不够好?**
A: 尝试在提示词中添加更多细节，或调整风格指令

**Q: 想要修改某张幻灯片的内容?**
A: 直接编辑对应的 `slideXX_prompt.txt` 文件，然后重新生成该图像
"""

    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write(instructions)

    print(f"✓ 已保存使用说明到: {instructions_file}")

    # 4. 保存风格指令
    style_instruction_file = output_path / '风格指令.txt'

    # 从大纲中获取风格指令
    outline_file = output_path.parent / 'outline.json'
    if outline_file.exists():
        with open(outline_file, 'r', encoding='utf-8') as f:
            outline = json.load(f)
            style_instruction = outline.get('style_instruction', '')

        with open(style_instruction_file, 'w', encoding='utf-8') as f:
            f.write(style_instruction)

        print(f"✓ 已保存风格指令到: {style_instruction_file}")

    # 5. 创建图像目录
    images_dir = output_path / 'images'
    images_dir.mkdir(exist_ok=True)
    print(f"✓ 已创建图像目录: {images_dir}")


def generate_images_auto(
    outline_file: str,
    output_dir: str,
    model: str = "gemini-3-pro-image-preview",
    image_size: str = "2K",
    aspect_ratio: str = "16:9"
) -> None:
    """
    自动生成图像（使用 Nano Banana Pro）

    Args:
        outline_file: 大纲文件路径
        output_dir: 输出目录
        model: 模型名称
        image_size: 图像分辨率
        aspect_ratio: 宽高比
    """
    try:
        from gemini_client import GeminiClient
    except ImportError:
        print("错误: 无法导入 gemini_client")
        sys.exit(1)

    print("="*60)
    print("图像自动生成器（Nano Banana Pro）")
    print("="*60 + "\n")

    # 1. 加载大纲
    print("步骤 1: 加载大纲")
    print("-" * 40)
    outline = load_outline(outline_file)
    print(f"✓ 已加载 {len(outline['slides'])} 张幻灯片\n")

    # 2. 生成提示词
    print("步骤 2: 生成图像提示词")
    print("-" * 40)
    prompts = generate_image_prompts(outline)
    print(f"✓ 已生成 {len(prompts)} 个图像提示词\n")

    # 3. 初始化客户端
    print("步骤 3: 连接 Gemini API")
    print("-" * 40)
    try:
        client = GeminiClient()
        print(f"✓ API 连接成功")
        print(f"✓ 使用模型: {model}")
        print(f"✓ 图像分辨率: {image_size}")
        print(f"✓ 宽高比: {aspect_ratio}\n")
    except Exception as e:
        print(f"❌ API 连接失败: {e}")
        sys.exit(1)

    # 4. 批量生成图像
    print("步骤 4: 批量生成图像")
    print("-" * 40)

    output_path = Path(output_dir)
    images_dir = output_path / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0
    failed_slides = []

    for i, prompt_data in enumerate(prompts, 1):
        slide_num = prompt_data['slide_num']
        prompt = prompt_data['prompt']
        output_file = images_dir / f"slide{slide_num:02d}.png"

        print(f"\n[{i}/{len(prompts)}] 生成幻灯片 {slide_num}")
        print(f"  目标: {output_file.name}")

        try:
            success = client.generate_image(
                prompt=prompt,
                output_path=str(output_file),
                aspect_ratio=aspect_ratio,
                model=model,
                image_size=image_size
            )

            if success:
                success_count += 1
            else:
                failed_slides.append(slide_num)

        except Exception as e:
            print(f"  ❌ 生成失败: {e}")
            failed_slides.append(slide_num)

    # 5. 保存提示词备份
    print("\n步骤 5: 保存提示词备份")
    print("-" * 40)
    save_prompts_for_manual_use(prompts, output_dir)

    # 6. 显示结果
    print("\n" + "="*60)
    print("图像生成完成！")
    print("="*60)
    print(f"\n📊 统计:")
    print(f"  - 总数: {len(prompts)}")
    print(f"  - 成功: {success_count}")
    print(f"  - 失败: {len(failed_slides)}")

    if failed_slides:
        print(f"\n⚠️  失败的幻灯片: {', '.join(map(str, failed_slides))}")
        print(f"  提示词已保存到 {output_dir}/prompts/")
        print(f"  您可以手动在 Gemini 网页界面重新生成")

    print(f"\n📁 输出目录: {images_dir}")
    print(f"\n下一步:")
    print(f"  python pptx-assembler.py --images {images_dir} --output presentation.pptx")


def generate_images_manual(
    outline_file: str,
    output_dir: str
) -> None:
    """
    生成提示词文件，供手动使用

    Args:
        outline_file: 大纲文件路径
        output_dir: 输出目录
    """
    print("="*60)
    print("图像提示词生成器（手动模式）")
    print("="*60 + "\n")

    # 1. 加载大纲
    print("步骤 1: 加载大纲")
    print("-" * 40)
    outline = load_outline(outline_file)
    print(f"✓ 已加载 {len(outline['slides'])} 张幻灯片\n")

    # 2. 生成提示词
    print("步骤 2: 生成图像提示词")
    print("-" * 40)
    prompts = generate_image_prompts(outline)
    print(f"✓ 已生成 {len(prompts)} 个图像提示词\n")

    # 3. 保存提示词文件
    print("步骤 3: 保存提示词文件")
    print("-" * 40)
    save_prompts_for_manual_use(prompts, output_dir)

    # 4. 显示下一步
    print("\n" + "="*60)
    print("✓ 提示词生成完成！")
    print("="*60)
    print(f"\n📁 输出目录: {output_dir}")
    print(f"\n📋 下一步:")
    print(f"  1. 阅读 {output_dir}/INSTRUCTIONS.md")
    print(f"  2. 在 Gemini 网页界面生成图像")
    print(f"  3. 将图像保存到 {output_dir}/images/")
    print(f"  4. 运行: python pptx-assembler.py --images {output_dir}/images/")


def main():
    parser = argparse.ArgumentParser(
        description='生成幻灯片图像',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 自动生成图像（使用 Nano Banana Pro API）
  %(prog)s --outline outline.json --output-dir ./slides/ --auto

  # 使用 Nano Banana（更快）
  %(prog)s --outline outline.json --auto --model gemini-2.5-flash-image

  # 使用 Nano Banana Pro 生成 4K 图像
  %(prog)s --outline outline.json --auto --model gemini-3-pro-image-preview --image-size 4K

  # 手动模式：生成提示词文件
  %(prog)s --outline outline.json --output-dir ./slide-prompts/

  # 自定义宽高比
  %(prog)s --outline outline.json --auto --aspect-ratio 4:3

模型说明:
  gemini-3-pro-image-preview (Nano Banana Pro)
    - 高质量、专业资源制作
    - 支持 1K/2K/4K 分辨率
    - 更好的文字渲染和复杂场景
    - 适合：学术演示、商业提案

  gemini-2.5-flash-image (Nano Banana)
    - 快速、高效
    - 1024px 分辨率
    - 适合：快速原型、批量处理

工作流程:
  自动模式：
    1. 加载大纲 JSON
    2. 调用 Gemini API 批量生成图像
    3. 自动保存到 images/ 目录
    4. 提供提示词备份（供失败重试）

  手动模式：
    1. 生成所有幻灯片的图像提示词
    2. 您在 Gemini 网页界面使用提示词
    3. 下载图像到 images/ 目录
    4. 使用 pptx-assembler.py 组装
        """
    )

    parser.add_argument(
        '--outline', '-i',
        required=True,
        help='大纲 JSON 文件路径'
    )

    parser.add_argument(
        '--output-dir', '-o',
        default='./slide-generation/',
        help='输出目录（默认: ./slide-generation/）'
    )

    parser.add_argument(
        '--auto', '-a',
        action='store_true',
        help='自动模式：使用 API 自动生成图像（需要 API 密钥）'
    )

    parser.add_argument(
        '--model', '-m',
        default='gemini-3-pro-image-preview',
        choices=['gemini-3-pro-image-preview', 'gemini-2.5-flash-image'],
        help='模型选择（默认: gemini-3-pro-image-preview）'
    )

    parser.add_argument(
        '--image-size',
        default='2K',
        choices=['1K', '2K', '4K'],
        help='图像分辨率，仅 Nano Banana Pro 支持（默认: 2K）'
    )

    parser.add_argument(
        '--aspect-ratio',
        default='16:9',
        choices=['1:1', '2:3', '3:2', '3:4', '4:3', '4:5', '5:4', '9:16', '16:9', '21:9'],
        help='图像宽高比（默认: 16:9）'
    )

    args = parser.parse_args()

    try:
        if args.auto:
            # 自动模式
            generate_images_auto(
                outline_file=args.outline,
                output_dir=args.output_dir,
                model=args.model,
                image_size=args.image_size,
                aspect_ratio=args.aspect_ratio
            )
        else:
            # 手动模式
            generate_images_manual(
                outline_file=args.outline,
                output_dir=args.output_dir
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
