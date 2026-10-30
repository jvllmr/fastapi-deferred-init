# AGENTS.md

## Benchmark regressions are functional regressions

This project exists for one reason: faster FastAPI start-up with many nested
routers. **Avoid benchmark regressions at all cost.** A change that makes the
benchmarks slower defeats the purpose of the project, no matter how small or
well-intentioned.

Rules of engagement:

- The benchmark is `pdm benchmark` (pytest-benchmark; the key number is
  `tests/test_lib.py::test_basic[True]`, the `benchmark(load_code)` timing of
  importing the generated 50-router app with the patch applied).
- Before committing anything that touches route registration, router include
  paths, or the monkey patches (`src/fastapi_deferred_init/routing.py`,
  `src/fastapi_deferred_init/patch.py`), run the benchmark on your branch and
  on the base commit and compare. Do not merge a slower result.
- This includes **dependency and submodule bumps** (e.g. the `fastapi`
  submodule): always benchmark after bumping them. A fastapi upgrade can
  silently neutralize the deferral (this happened with 0.162.0, whose new
  include machinery built handlers eagerly) — if so, adapt the patch before
  merging, or do not bump.
- If a regression is truly unavoidable, do not hide it: state it explicitly in
  the commit message with before/after numbers and the reason.
