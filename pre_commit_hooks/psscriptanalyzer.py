from __future__ import annotations

import argparse
import subprocess
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    pwsh_is_pssa_installed = (
        'Get-InstalledModule -Name PSScriptAnalyzer'
        ' -ErrorAction SilentlyContinue'
    )
    pwsh_install_pssa = (
        'Install-Module -Name PSScriptAnalyzer'
        ' -Scope CurrentUser -AllowClobber -Force'
    )

    m = subprocess.run(
        [
            'pwsh.exe', '-Command',
            'if (!(' + pwsh_is_pssa_installed + ')) {' + pwsh_install_pssa + '}',
        ],
        stdout=subprocess.PIPE, text=True, )

    if (len(m.stdout) > 0):
        print('Install-Module result:', m.stdout)

    pssa_output_count = 0

    for filename in args.filenames:
        print(f'{filename}: checking...')
        p = subprocess.run(
            ['pwsh.exe', '-Command', 'Invoke-ScriptAnalyzer', filename],
            stdout=subprocess.PIPE, text=True, )

        if (len(p.stdout) > 0):
            print('Invoke-ScriptAnalyzer result:', p.stdout)
            pssa_output_count += 1

    retval = 1 if pssa_output_count > 0 else 0
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
