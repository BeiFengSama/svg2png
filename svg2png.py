import cairosvg
import os

# 获取当前目录下的所有SVG文件
svg_files = [f for f in os.listdir('.') if f.lower().endswith('.svg')]

# 遍历每个SVG文件并转换为PNG
for svg_file in svg_files:
    png_file = os.path.splitext(svg_file)[0] + ".png"  # 输出PNG文件的文件名
    try:
        # 使用cairosvg将SVG转换为PNG
        cairosvg.svg2png(url=svg_file, write_to=png_file)
        print(f"成功转换: {svg_file} -> {png_file}")
    except Exception as e:
        print(f"转换失败: {svg_file} - 错误: {e}")
