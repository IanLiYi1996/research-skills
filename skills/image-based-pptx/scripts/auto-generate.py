#!/usr/bin/env python3
"""
自动化 PPT 生成主脚本

一键串联所有步骤，从源文件到完整 PPTX。
"""

import argparse
import sys
import subprocess
from pathlib import Path
from typing import List


def run_command(cmd: List[str], description: str) -> bool:
    """
    运行命令

    Args:
        cmd: 命令参数列表
        description: 命令描述

    Returns:
        是否成功
    """
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}\n")

    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=False,
            text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ 命令执行失败: {e}")
        return False
    except FileNotFoundError:
        print(f"\n❌ 找不到命令: {cmd[0]}")
        return False


def auto_generate(
    input_files: List[str],
    output_file: str,
    style: str = "academic",
    slides: int = 15,
    topic: str = None,
    work_dir: str = "./ppt-generation",
    auto_images: bool = False,
    image_model: str = "gemini-3-pro-image-preview",
    image_size: str = "2K",
    aspect_ratio: str = "16:9"
) -> None:
    """
    自动化生成流程

    Args:
        input_files: 输入文件列表
        output_file: 输出 PPTX 文件路径
        style: 风格
        slides: 幻灯片数量
        topic: 主题
        work_dir: 工作目录
        auto_images: 是否自动生成图像
        image_model: 图像生成模型
        image_size: 图像分辨率
        aspect_ratio: 图像宽高比
    """
    print("="*60)
    print("自动化 PPT 生成")
    print("="*60)
    print(f"\n📁 工作目录: {work_dir}")
    print(f"📝 输入文件: {', '.join([Path(f).name for f in input_files])}")
    print(f"🎨 风格: {style}")
    print(f"📊 幻灯片数: {slides}")
    if topic:
        print(f"📌 主题: {topic}")

    # 创建工作目录
    work_path = Path(work_dir)
    work_path.mkdir(parents=True, exist_ok=True)

    # 定义文件路径
    outline_file = work_path / "outline.json"
    prompts_dir = work_path / "prompts"
    images_dir = work_path / "images"

    # 步骤 1: 生成大纲
    print("\n" + "🔹"*30)
    print("步骤 1/3: 生成幻灯片大纲")
    print("🔹"*30)

    outline_cmd = [
        "python3",
        str(Path(__file__).parent / "outline-generator.py"),
        "--input", *input_files,
        "--output", str(outline_file),
        "--style", style,
        "--slides", str(slides)
    ]

    if topic:
        outline_cmd.extend(["--topic", topic])

    if not run_command(outline_cmd, "生成大纲"):
        sys.exit(1)

    # 步骤 2: 生成图像提示词
    print("\n" + "🔹"*30)
    print("步骤 2/3: 生成图像提示词")
    print("🔹"*30)

    prompts_cmd = [
        "python3",
        str(Path(__file__).parent / "image-generator.py"),
        "--outline", str(outline_file),
        "--output-dir", str(work_path)
    ]

    # 根据模式选择
    if auto_images:
        # 自动模式：使用 API 生成图像
        prompts_cmd.extend([
            "--auto",
            "--model", image_model,
            "--image-size", image_size,
            "--aspect-ratio", aspect_ratio
        ])

        if not run_command(prompts_cmd, "自动生成图像"):
            sys.exit(1)

    else:
        # 手动模式：生成提示词
        if not run_command(prompts_cmd, "生成提示词"):
            sys.exit(1)

        # 步骤 2.5: 等待用户生成图像
        print("\n" + "⏸️ "*30)
        print("需要手动操作")
        print("⏸️ "*30)

        print(f"\n📋 下一步:")
        print(f"  1. 打开 Gemini: https://gemini.google.com/")
        print(f"  2. 阅读说明: {work_path}/INSTRUCTIONS.md")
        print(f"  3. 使用提示词生成图像")
        print(f"  4. 将图像保存到: {images_dir}/")
        print(f"  5. 图像命名: slide01.png, slide02.png, ...")

        print(f"\n提示词位置:")
        print(f"  - 单独文件: {prompts_dir}/")
        print(f"  - 合并文件: {work_path}/all_prompts.txt")

        # 询问是否继续
        print("\n" + "-"*60)
        response = input("完成图像生成后，按 Enter 继续组装 PPTX，或输入 'q' 退出: ")

        if response.lower() == 'q':
            print("\n✓ 已保存中间文件，可以稍后继续")
            print(f"  继续命令: python3 {__file__} --resume {work_dir}")
            sys.exit(0)

        # 检查图像目录
        if not images_dir.exists() or not list(images_dir.glob('*.png')):
            print(f"\n⚠️  警告: 在 {images_dir} 中未找到图像文件")
            response = input("是否继续? (y/N): ")
            if response.lower() != 'y':
                sys.exit(0)

    # 步骤 3: 组装 PPTX
    print("\n" + "🔹"*30)
    print("步骤 3/3: 组装 PPTX")
    print("🔹"*30)

    pptx_cmd = [
        "python3",
        str(Path(__file__).parent / "pptx-assembler.py"),
        "--images", str(images_dir),
        "--output", output_file
    ]

    if not run_command(pptx_cmd, "组装 PPTX"):
        sys.exit(1)

    # 完成
    print("\n" + "✅"*30)
    print("全部完成！")
    print("✅"*30)

    print(f"\n📊 生成的文件:")
    print(f"  - 大纲: {outline_file}")
    print(f"  - 提示词: {prompts_dir}/")
    print(f"  - 图像: {images_dir}/")
    print(f"  - 演示文稿: {output_file}")

    print(f"\n🎉 可以用 PowerPoint 打开:")
    print(f"  {output_file}")


def resume_from_work_dir(work_dir: str, output_file: str) -> None:
    """
    从工作目录恢复并继续

    Args:
        work_dir: 工作目录
        output_file: 输出文件
    """
    work_path = Path(work_dir)
    images_dir = work_path / "images"

    if not images_dir.exists():
        print(f"❌ 错误: 图像目录不存在: {images_dir}")
        sys.exit(1)

    image_files = list(images_dir.glob('*.png'))
    if not image_files:
        print(f"❌ 错误: 在 {images_dir} 中未找到图像文件")
        sys.exit(1)

    print(f"✓ 找到 {len(image_files)} 个图像文件")

    # 组装 PPTX
    pptx_cmd = [
        "python3",
        str(Path(__file__).parent / "pptx-assembler.py"),
        "--images", str(images_dir),
        "--output", output_file
    ]

    if run_command(pptx_cmd, "组装 PPTX"):
        print(f"\n✓ 完成: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='自动化生成 PPT（半自动模式）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 完全自动化（使用 Nano Banana Pro API）⭐️ 推荐
  %(prog)s --input paper.pdf --output presentation.pptx --auto-images

  # 使用更快的 Nano Banana 模型
  %(prog)s --input paper.pdf --auto-images --image-model gemini-2.5-flash-image

  # 生成 4K 高分辨率图像
  %(prog)s --input paper.pdf --auto-images --image-size 4K

  # 半自动模式（手动在网页生成图像）
  %(prog)s --input paper.pdf --output presentation.pptx

  # 指定风格和幻灯片数
  %(prog)s --input paper.pdf --style academic --slides 20 --auto-images

  # 指定主题和宽高比
  %(prog)s --input paper.pdf --topic "深度学习研究" --aspect-ratio 4:3

  # 从中断处恢复
  %(prog)s --resume ./ppt-generation --output presentation.pptx

模式说明:
  完全自动模式 (--auto-images):
    1. 自动生成大纲（使用 Gemini API）
    2. 自动生成所有幻灯片图像（使用 Nano Banana Pro）
    3. 自动组装 PPTX
    ⚡ 优点：全自动，无需手动操作
    💰 成本：~$0.30-0.60 (15页)

  半自动模式 (默认):
    1. 自动生成大纲
    2. 生成图像提示词
    3. **手动**在 Gemini 网页界面生成图像
    4. 自动组装 PPTX
    ⚡ 优点：可以交互式调整图像
    💰 成本：~$0.01 (仅大纲)

推荐:
  - 首次使用：半自动模式（更直观）
  - 批量处理：完全自动模式（更高效）
        """
    )

    parser.add_argument(
        '--input', '-i',
        nargs='+',
        help='输入文件路径'
    )

    parser.add_argument(
        '--output', '-o',
        default='presentation.pptx',
        help='输出 PPTX 文件路径（默认: presentation.pptx）'
    )

    parser.add_argument(
        '--style', '-s',
        default='academic',
        choices=['academic', 'technical', 'business', 'creative', 'minimal', 'playful'],
        help='演示风格（默认: academic）'
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
        '--work-dir', '-w',
        default='./ppt-generation',
        help='工作目录（默认: ./ppt-generation）'
    )

    parser.add_argument(
        '--auto-images',
        action='store_true',
        help='自动生成图像（使用 Nano Banana Pro API，需要 API 密钥）'
    )

    parser.add_argument(
        '--image-model',
        default='gemini-3-pro-image-preview',
        choices=['gemini-3-pro-image-preview', 'gemini-2.5-flash-image'],
        help='图像生成模型（默认: gemini-3-pro-image-preview）'
    )

    parser.add_argument(
        '--image-size',
        default='2K',
        choices=['1K', '2K', '4K'],
        help='图像分辨率（默认: 2K，仅 Nano Banana Pro）'
    )

    parser.add_argument(
        '--aspect-ratio',
        default='16:9',
        help='图像宽高比（默认: 16:9）'
    )

    parser.add_argument(
        '--resume',
        metavar='WORK_DIR',
        help='从工作目录恢复并继续'
    )

    args = parser.parse_args()

    try:
        if args.resume:
            # 恢复模式
            resume_from_work_dir(args.resume, args.output)
        else:
            # 正常模式
            if not args.input:
                print("❌ 错误: 需要指定 --input 参数")
                sys.exit(1)

            auto_generate(
                input_files=args.input,
                output_file=args.output,
                style=args.style,
                slides=args.slides,
                topic=args.topic,
                work_dir=args.work_dir,
                auto_images=args.auto_images,
                image_model=args.image_model,
                image_size=args.image_size,
                aspect_ratio=args.aspect_ratio
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
