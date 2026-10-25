# eHello Texture Maker

English · [简体中文](README.md)

Turn a logo into a repeating brand pattern with live previews and high-resolution PNG export. Includes a standalone Windows application and a buildless web version, with the red eHello logo bundled.

## Download and run

Get the EXE or complete ZIP from **[GitHub Releases](https://github.com/heiye07/eHello-texture-maker/releases/latest)**. Extract the ZIP, then double-click `云海螺纹理工坊.exe`. Python is not required.

- Windows 10 / 11, 64-bit.
- Requires Microsoft Edge WebView2 Runtime. If missing, install it from [Microsoft](https://developer.microsoft.com/microsoft-edge/webview2/).
- Works offline. Image uploads, rendering, and PNG saving happen locally.
- The single-file executable briefly extracts its bundled files on startup.
- The application interface is currently in Simplified Chinese.

## Features

- Live preview with synchronized sliders and numeric inputs.
- Adjust rotation, logos per row, horizontal/vertical spacing, row offset, and opacity.
- Soft pattern and brand red presets; replace the logo and choose logo/background colors.
- Transparent backgrounds with PNG alpha-channel export.
- A4 portrait/landscape, 4000 × 4000 square, 4K landscape, and custom pixel dimensions.
- Up to 40 megapixels, with each side between 100 and 10,000 pixels.
- Native Windows Save As dialog for exporting files.

## Usage

1. Launch the app and use the bundled logo, or choose “更换 Logo 图片” to load another image.
2. Drag sliders or enter numbers directly, watching the live preview.
3. Set the canvas size and optionally enable “透明背景” (transparent background).
4. Click “导出高清 PNG” (export high-resolution PNG), then choose a save location.

Horizontal and vertical gaps are percentages of the logo width. Row offset is a percentage of the horizontal repeat spacing. Logos per row controls horizontal density; partial logos may appear at the edges to suggest a continuous pattern.

Uploaded images have white backgrounds reduced/removed and are recolored as **single-color artwork**. Transparent PNG logos are recommended; multicolor images will be flattened to the selected color. The preview checkerboard indicates transparency and is not included in the export.

> Exports are full-canvas repeated patterns, not guaranteed seamless tiles that can be repeated along all four edges. Resolution is specified in pixels. A4 presets use dimensions commonly associated with 300 DPI, but do not embed 300 DPI print metadata.

## Example

<img src="docs/example.png" alt="Soft red repeating eHello logo pattern" width="420">

## Run from source

On Windows, Python 3.12 is recommended:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python desktop.py
```

### Build the Windows EXE

After installing the dependencies, run in Windows PowerShell:

```powershell
.\build.ps1
```

Output: `release/云海螺纹理工坊.exe`. Build on Windows.

### Run the web version

```powershell
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Open <http://127.0.0.1:8000>. The web version downloads PNGs through the browser; the desktop version uses a native save dialog.

## Project structure

```text
dist/index.html    Live preview UI, Canvas rendering, and PNG export
dist/logo.png      Bundled eHello logo
desktop.py         Desktop window, PNG validation, and native file saving
app.ico            Application icon
build.ps1          Windows single-file build script
requirements.txt   Python build/runtime dependencies
docs/example.png   Example export
```

## Validation

Verified numeric-input/slider synchronization, 2480 × 3508 PNG export, and transparency. The packaged executable passed bundled-asset, PNG validation, and alpha-channel self-checks, plus a Windows launch check. The native save dialog has not been tested with end-to-end automation.

Run the built-in self-check and write its result to a file:

```powershell
python desktop.py --self-test self-test.txt
```

## Brand assets

The bundled eHello logo and branded examples are brand assets. Publication of this repository does not grant trademark or brand-asset rights. Use these assets only with appropriate authorization.
