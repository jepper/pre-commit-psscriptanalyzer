psscriptanalyzer
================

Run PSScriptAnalyzer against PowerShell scripts via a python wrapper.

The script in this early version only works on Windows. I will add support for pwsh on Linux at some point.

This requires PowerShell core. The wrapper script will check is PSScriptAnalyzer is installed, and attempt to install if not found.

See also: https://github.com/pre-commit/pre-commit

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/jepper/pre-commit-psscriptanalyzer
    rev: v0.0.1  # Use the ref you want to point at
    hooks:
    -   id: psscriptanalyzer
```

