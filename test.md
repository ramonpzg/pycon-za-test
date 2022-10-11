usage: dvc metrics [-h] [-q | -v] {show,diff} ...

Commands to display and compare metrics.
Documentation: <https://man.dvc.org/metrics>

positional arguments:
  {show,diff}    Use `dvc metrics CMD --help` to display command-specific help.
    show         Print metrics, with optional formatting.
    diff         Show changes in metrics between commits in the DVC repository, or between a commit and the workspace.

options:
  -h, --help     show this help message and exit
  -q, --quiet    Be quiet.
  -v, --verbose  Be verbose.
