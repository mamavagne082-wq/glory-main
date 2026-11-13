# -*- coding: utf-8 -*-
"""
ALAMIN A9X BD — Free Fire Squad Bot Launcher
100% Working Fix Integration (Homer RUDP + Updated Protobufs + Web Dashboard)
"""

import sys
import os
import subprocess
import asyncio

_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
if _CUR_DIR not in sys.path:
    sys.path.insert(0, _CUR_DIR)

# ----------------------------------------------------------------------
# 1. Automatic Python 3.14 Delegation (for local execution on 3.12 / older)
# ----------------------------------------------------------------------
if sys.version_info < (3, 14):
    _PY314_CANDIDATES = [
        os.path.join(_CUR_DIR, ".venv", "Scripts", "python.exe"),
        os.path.join(_CUR_DIR, ".venv", "bin", "python"),
        r"C:\Users\Al Amin\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\python.exe",
    ]
    _found_py = None
    for _p in _PY314_CANDIDATES:
        if os.path.isfile(_p):
            _found_py = _p
            break

    if _found_py:
        print(f"[ALAMIN LAUNCHER] Upgrading runtime to Python 3.14 via: {_found_py}")
        sys.stdout.flush()
        _cmd = [_found_py, os.path.abspath(__file__)] + sys.argv[1:]
        _proc = subprocess.run(_cmd)
        sys.exit(_proc.returncode)
    else:
        # Try uv run
        try:
            print("[ALAMIN LAUNCHER] Starting via uv run --python 3.14...")
            sys.stdout.flush()
            _cmd = ["uv", "run", "--python", "3.14", "python", os.path.abspath(__file__)] + sys.argv[1:]
            _proc = subprocess.run(_cmd)
            sys.exit(_proc.returncode)
        except Exception:
            pass

# ----------------------------------------------------------------------
# 2. Output Filter: Ensure 100% ALAMIN Branding Everywhere
# ----------------------------------------------------------------------
_orig_stdout_write = sys.stdout.write
def _clean_write(s):
    if isinstance(s, str):
        s = s.replace("ARIYAN", "ALAMIN").replace("Ariyan", "Alamin").replace("ariyan", "alamin")
        s = s.replace("RAFIN TxT", "ALAMIN A9X").replace("RAFIN  X  MEHEDI", "ALAMIN A9X BD")
    return _orig_stdout_write(s)
sys.stdout.write = _clean_write

# ----------------------------------------------------------------------
# 3. Environment & Port Binding Setup
# ----------------------------------------------------------------------
_PORT = int(os.environ.get("PORT", os.environ.get("WEB_PORT", 25567)))
_HOST = "0.0.0.0"

# Hook aiohttp TCPSite to enforce dynamic port, host and address reuse
try:
    from aiohttp import web
    _orig_tcpsite_init = web.TCPSite.__init__
    def _hooked_tcpsite_init(self, runner, host=None, port=None, *args, **kwargs):
        kwargs["reuse_address"] = True
        return _orig_tcpsite_init(self, runner, _HOST, _PORT, *args, **kwargs)
    web.TCPSite.__init__ = _hooked_tcpsite_init
except Exception:
    pass

# Ensure accounts.json exists
_acc_file = os.path.join(_CUR_DIR, "accounts.json")
if not os.path.exists(_acc_file):
    with open(_acc_file, "w", encoding="utf-8") as f:
        f.write("[]")

# Ensure index.html is available in all lookup directories
_idx_src = os.path.join(_CUR_DIR, "Ariyan", "index.html")
if os.path.exists(_idx_src):
    for _sub in ["", "MAX", "templates"]:
        _target_dir = os.path.join(_CUR_DIR, _sub) if _sub else _CUR_DIR
        os.makedirs(_target_dir, exist_ok=True)
        _target_file = os.path.join(_target_dir, "index.html")
        if not os.path.exists(_target_file) or os.path.getsize(_target_file) != os.path.getsize(_idx_src):
            try:
                with open(_idx_src, "r", encoding="utf-8") as rf:
                    _c = rf.read()
                with open(_target_file, "w", encoding="utf-8") as wf:
                    wf.write(_c)
            except Exception:
                pass

# ----------------------------------------------------------------------
# 4. Import Core Bot Engine & Apply Port/Path Configuration
# ----------------------------------------------------------------------
import main1

main1.WEB_HOST = _HOST
main1.WEB_PORT = _PORT
main1.INDEX_HTML_PATH = os.path.join(_CUR_DIR, "index.html")
main1.ACCOUNTS_FILE = _acc_file

def _custom_banner():
    print(r"""
    █████╗ ██╗      █████╗ ███╗   ███╗██╗███╗   ██╗
   ██╔══██╗██║     ██╔══██╗████╗ ████║██║████╗  ██║
   ███████║██║     ███████║██╔████╔██║██║██╔██╗ ██║
   ██╔══██║██║     ██╔══██║██║╚██╔╝██║██║██║╚██╗██║
   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║
   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝

    ╔══════════════════════════════════════════════════════════╗
    ║   ✦  A L A M I N   A 9 X   ✦   P R E M I U M   ║
    ╠══════════════════════════════════════════════════════════╣
    ║   ▸ FREE FIRE 4-BOT SQUAD ENGINE (100% FIXED)            ║
    ║   ▸ Auto Create · Anti-AFK · Multi-Region · Team Play    ║
    ║   ▸ Engine v2.0  ·  Homer RUDP  ·  All Systems Online    ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    sys.stdout.flush()

main1.print_banner = _custom_banner

# ----------------------------------------------------------------------
# 5. Main Execution
# ----------------------------------------------------------------------
if __name__ == "__main__":
    try:
        asyncio.run(main1.main())
    except (KeyboardInterrupt, SystemExit):
        pass
