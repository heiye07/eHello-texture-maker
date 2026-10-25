$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    python -m PyInstaller --noconfirm --clean --onefile --windowed --name '云海螺纹理工坊' --icon app.ico --add-data 'dist;dist' --collect-all webview --distpath release desktop.py
    if ($LASTEXITCODE -ne 0) { throw 'Build failed.' }
    Write-Host 'EXE saved to release/'
} finally {
    Pop-Location
}
