# Static scanner fixtures

These functions are deliberately never called. They are non-deployable,
synthetic code used only to confirm that static scanners produce findings for
known patterns. Do not import this module into an application or run it with
untrusted input.

Expected ReviewOps Semgrep rules include dynamic evaluation, dynamic execution,
shell-enabled subprocess calls, and unsafe YAML loading.
