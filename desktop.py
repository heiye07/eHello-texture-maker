import base64
import io
import os
import sys
from pathlib import Path

import webview
from PIL import Image

ROOT = Path(getattr(sys, '_MEIPASS', Path(__file__).parent))

def decode_png(data, width, height):
    if not isinstance(data, str) or not data.startswith('data:image/png;base64,'):
        raise ValueError('无效的 PNG 数据')
    raw = base64.b64decode(data.split(',', 1)[1], validate=True)
    with Image.open(io.BytesIO(raw)) as image:
        if image.format != 'PNG' or image.size != (int(width), int(height)):
            raise ValueError('图片尺寸校验失败')
        image.verify()
    return raw

class Api:
    window = None

    def save_png(self, data, width, height):
        try:
            raw = decode_png(data, width, height)
            paths = self.window.create_file_dialog(
                webview.FileDialog.SAVE,
                directory=str(Path.home() / 'Pictures'),
                save_filename=f'eHello-纹理-{width}x{height}.png',
                file_types=('PNG 图片 (*.png)',),
            )
            if not paths:
                return {'ok': False, 'cancelled': True}
            target = Path(paths if isinstance(paths, str) else paths[0]).with_suffix('.png')
            target.write_bytes(raw)
            return {'ok': True, 'path': str(target)}
        except Exception as exc:
            return {'ok': False, 'error': str(exc)}

def self_test():
    html = (ROOT / 'dist/index.html').read_text(encoding='utf-8')
    assert 'Number' in html and '透明背景' in html and 'window.pywebview.api.save_png' in html
    Image.open(ROOT / 'dist/logo.png').verify()
    out = io.BytesIO()
    Image.new('RGBA', (100, 120), (251, 0, 35, 0)).save(out, 'PNG')
    raw = decode_png('data:image/png;base64,' + base64.b64encode(out.getvalue()).decode(), 100, 120)
    assert Image.open(io.BytesIO(raw)).getpixel((0, 0))[3] == 0
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text('PASS: bundled assets, UI, PNG validation, alpha channel', encoding='utf-8')

if __name__ == '__main__':
    if '--self-test' in sys.argv:
        self_test()
    else:
        api = Api()
        api.window = webview.create_window('云海螺 · Logo 纹理工坊', str(ROOT / 'dist/index.html'),
                                          js_api=api, width=1280, height=900, min_size=(800, 640))
        webview.start(gui='edgechromium', http_server=True)
