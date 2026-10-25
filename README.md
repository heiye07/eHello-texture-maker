# 云海螺 Logo 纹理工坊

[English](README.en.md) · 简体中文

把一个 Logo 排列成连续重复的品牌纹理，边调边看，并导出高清 PNG。提供 Windows 本地 EXE 和无需构建的网页版，内置红色 eHello Logo。

## 下载与运行

前往 **[Releases 下载 Windows 版](https://github.com/heiye07/eHello-texture-maker/releases/latest)**，下载 EXE 或完整 ZIP。ZIP 解压后双击 `云海螺纹理工坊.exe` 即可，无需安装 Python。

- 系统：Windows 10 / 11，64 位。
- 依赖系统的 Microsoft Edge WebView2 运行时；若缺失，请从 [Microsoft 官方页面](https://developer.microsoft.com/microsoft-edge/webview2/)安装。
- 可离线使用，上传图片、生成图案和保存 PNG 都在本机处理。
- 单文件版首次启动会短暂解压，请稍候。

## 功能

- 实时预览，滑块与数值输入框双向同步。
- 调整倾斜角度、每行数量、横纵间隙、逐行错位与 Logo 不透明度。
- 内置淡色纹理、品牌红预设；支持更换 Logo、自选 Logo 颜色和背景颜色。
- 支持透明背景，导出的 PNG 保留透明通道。
- 支持 A4 竖版/横版、4000 × 4000 正方形、4K 横版和自定义像素尺寸。
- 最大 4000 万像素，单边尺寸 100–10000 像素。
- Windows 版通过“另存为”对话框保存文件。

## 使用方法

1. 打开程序，使用内置 Logo，或点击“更换 Logo 图片”。
2. 拖动滑块或直接输入数字，观察右侧预览。
3. 选择画布尺寸，根据需要勾选“透明背景”。
4. 点击“导出高清 PNG”，选择保存位置。

横纵间隙以单个 Logo 的宽度为基准；逐行错位以横向排列间距为基准。每行数量用于控制横向排列密度，边缘可能显示部分 Logo，以呈现连续延伸的效果。

更换图片后，程序会淡化/去除白色背景，并按选定颜色生成**单色图案**。建议上传透明 PNG；多色图片会被统一着色。预览棋盘格表示透明区域，不会导出到图片中。

> 此工具生成铺满画布的重复纹理 PNG；不保证导出的整张图片可作为四边无缝拼接的贴图单元。高清以像素尺寸为准，A4 预设采用常见的 300 DPI 对应像素尺寸，不写入 300 DPI 打印元数据。

## 效果示例

<img src="docs/example.png" alt="淡红色 eHello 重复纹理示例" width="420">

## 从源码运行

Windows，推荐 Python 3.12：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python desktop.py
```

### 构建 Windows EXE

安装上述依赖后，在 Windows PowerShell 中运行：

```powershell
.\build.ps1
```

输出：`release/云海螺纹理工坊.exe`。构建需在 Windows 上完成。

### 运行网页版

```powershell
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

在浏览器打开 <http://127.0.0.1:8000>。网页版通过浏览器下载 PNG，Windows EXE 通过系统保存窗口保存。

## 项目结构

```text
dist/index.html    实时预览界面与 Canvas 渲染、PNG 导出
dist/logo.png      内置 eHello Logo
desktop.py         Windows 桌面窗口、PNG 校验与本地保存
app.ico            程序图标
build.ps1          Windows 单文件打包脚本
requirements.txt   Python 构建和运行依赖
docs/example.png   导出示例
```

## 验证

已验证数值输入与滑块同步、2480 × 3508 PNG 导出及透明通道。打包后的 EXE 已通过内置资源、PNG 数据校验、透明通道自检，并完成 Windows 启动检查；系统保存对话框未做自动化端到端验证。

运行内置自检（结果写入指定文件）：

```powershell
python desktop.py --self-test self-test.txt
```

## 品牌素材

仓库内置 eHello / 云海螺 Logo 和相关示例为品牌素材；公开仓库不代表授予商标或品牌素材使用权。请在拥有相应授权的范围内使用。
