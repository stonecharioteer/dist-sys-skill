default:
  @just --list

install-hooks:
  uvx pre-commit install --hook-type pre-commit --hook-type commit-msg

test-status:
  python3 systems-design/scripts/dist_sys_status.py ls

next:
  python3 systems-design/scripts/dist_sys_status.py next

lint:
  uvx pre-commit run --all-files
