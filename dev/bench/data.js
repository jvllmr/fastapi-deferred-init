window.BENCHMARK_DATA = {
  "lastUpdate": 1725575808904,
  "repoUrl": "https://github.com/jvllmr/fastapi-deferred-init",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "jan@vllmr.dev",
            "name": "Jan Vollmer",
            "username": "jvllmr"
          },
          "committer": {
            "email": "jan@vllmr.dev",
            "name": "Jan Vollmer",
            "username": "jvllmr"
          },
          "distinct": true,
          "id": "b20708b02d4920088d77acba2425b6bbe127da91",
          "message": "use cache in publish action",
          "timestamp": "2024-09-06T00:25:51+02:00",
          "tree_id": "1c97f4970f086f7aaa524eab6455912c8f2ee796",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/b20708b02d4920088d77acba2425b6bbe127da91"
        },
        "date": 1725575414101,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.5928785491043467,
            "unit": "iter/sec",
            "range": "stddev: 0.01066050745232246",
            "extra": "mean: 278.32836160000056 msec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jan@vllmr.dev",
            "name": "Jan Vollmer",
            "username": "jvllmr"
          },
          "committer": {
            "email": "jan@vllmr.dev",
            "name": "Jan Vollmer",
            "username": "jvllmr"
          },
          "distinct": true,
          "id": "db203633ce98765191e23387a5cf6f4bd45d3272",
          "message": "add missing env var on benchmark run",
          "timestamp": "2024-09-06T00:32:48+02:00",
          "tree_id": "2d064d5f8b641829e5c0224a1067a08d0d543777",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/db203633ce98765191e23387a5cf6f4bd45d3272"
        },
        "date": 1725575631416,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.6282003807700356,
            "unit": "iter/sec",
            "range": "stddev: 0.011024848100614318",
            "extra": "mean: 275.6187352000012 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.3589323746176862,
            "unit": "iter/sec",
            "range": "stddev: 0.165228249789474",
            "extra": "mean: 2.7860401310000014 sec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "84ac0ffc6914decebcaed03cc07a03a036b42616",
          "message": "Update all non-major dependencies (#10)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-09-06T00:35:53+02:00",
          "tree_id": "85db863cbaf1cfa1f4040c23b0a5474dc04e77a3",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/84ac0ffc6914decebcaed03cc07a03a036b42616"
        },
        "date": 1725575808660,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.6474187530432998,
            "unit": "iter/sec",
            "range": "stddev: 0.008811523185243201",
            "extra": "mean: 274.16649080000184 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.34568044822202865,
            "unit": "iter/sec",
            "range": "stddev: 0.1946502287670591",
            "extra": "mean: 2.8928451266000024 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}