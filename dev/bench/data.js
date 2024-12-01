window.BENCHMARK_DATA = {
  "lastUpdate": 1733024449013,
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
          "id": "e2264e495fe1dc148b136dd6b58a06da570f1147",
          "message": "Lock file maintenance (#11)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-09-06T00:36:55+02:00",
          "tree_id": "85db863cbaf1cfa1f4040c23b0a5474dc04e77a3",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/e2264e495fe1dc148b136dd6b58a06da570f1147"
        },
        "date": 1725575871172,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.6770293642174923,
            "unit": "iter/sec",
            "range": "stddev: 0.009886028199392183",
            "extra": "mean: 271.9586657999969 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.3658144300960487,
            "unit": "iter/sec",
            "range": "stddev: 0.12521375781641175",
            "extra": "mean: 2.733626444800001 sec\nrounds: 5"
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
          "id": "101e0fbcc34faf5ca680c666b025a1e72246610c",
          "message": "always use n dependency in dependencies kwarg",
          "timestamp": "2024-09-06T10:35:53+02:00",
          "tree_id": "9128a525aad58fe68626a5f762685bfd38a784f5",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/101e0fbcc34faf5ca680c666b025a1e72246610c"
        },
        "date": 1725611949450,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.5963575897566304,
            "unit": "iter/sec",
            "range": "stddev: 0.010244933395204974",
            "extra": "mean: 278.059112599999 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04725895809675009,
            "unit": "iter/sec",
            "range": "stddev: 1.1820229932011",
            "extra": "mean: 21.160009451599997 sec\nrounds: 5"
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
          "id": "a3ba52c323f9889d8ddaa90fed0f0e1f5a0f1ba0",
          "message": "clone submodules in actions",
          "timestamp": "2024-09-06T18:19:16+02:00",
          "tree_id": "8c1b4ecd7b628c715d64f59b36fa21502a574586",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/a3ba52c323f9889d8ddaa90fed0f0e1f5a0f1ba0"
        },
        "date": 1725639791253,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.582091829379965,
            "unit": "iter/sec",
            "range": "stddev: 0.015804767418704613",
            "extra": "mean: 279.16648919999716 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04648593329166835,
            "unit": "iter/sec",
            "range": "stddev: 1.6459407426799584",
            "extra": "mean: 21.511883900999994 sec\nrounds: 5"
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
          "id": "26317a8167b81132ec74a1dd9b28013a2d9c285a",
          "message": "update fastapi submodule to 0.114.0",
          "timestamp": "2024-09-07T00:37:29+02:00",
          "tree_id": "8c68f30dcaa850e11ebc0128f064cc508197d3b9",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/26317a8167b81132ec74a1dd9b28013a2d9c285a"
        },
        "date": 1725662562249,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.705781532664107,
            "unit": "iter/sec",
            "range": "stddev: 0.0011264241876809736",
            "extra": "mean: 269.8486111999955 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04661426359496045,
            "unit": "iter/sec",
            "range": "stddev: 1.998246663129695",
            "extra": "mean: 21.45266111440001 sec\nrounds: 5"
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
          "id": "754e133cadb064cd6bc068bf5e0c4fe4dbaba421",
          "message": "remove redundant pre-commit hooks",
          "timestamp": "2024-09-07T00:43:03+02:00",
          "tree_id": "4624b84e53384523bf3b26e85f294c82c8d467c9",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/754e133cadb064cd6bc068bf5e0c4fe4dbaba421"
        },
        "date": 1725662802196,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.7011042564324423,
            "unit": "iter/sec",
            "range": "stddev: 0.0008023889991712748",
            "extra": "mean: 270.18963280000037 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.046893165459635094,
            "unit": "iter/sec",
            "range": "stddev: 2.0362776898072363",
            "extra": "mean: 21.3250692334 sec\nrounds: 5"
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
          "id": "b27fb88bd9b4b532cc621bc59a7d29c90dbed115",
          "message": "fix pre-commit issues",
          "timestamp": "2024-09-07T01:04:46+02:00",
          "tree_id": "8eb8075d973f89f1c4c41a764fce23a01b5db895",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/b27fb88bd9b4b532cc621bc59a7d29c90dbed115"
        },
        "date": 1725664101894,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.6865799875128444,
            "unit": "iter/sec",
            "range": "stddev: 0.0011991137016679567",
            "extra": "mean: 271.25411720000443 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04708771601704336,
            "unit": "iter/sec",
            "range": "stddev: 1.9213034263692501",
            "extra": "mean: 21.236961241400003 sec\nrounds: 5"
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
          "id": "e05d8f98bcfc287415018ace8d66ad98429a03fa",
          "message": "Update dependency fastapi to >=0.114.0 (#12)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-09-07T01:30:50+02:00",
          "tree_id": "ef73e70e171ed04d5e07b4a91387dc75d3088238",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/e05d8f98bcfc287415018ace8d66ad98429a03fa"
        },
        "date": 1725665662274,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.7303865925339923,
            "unit": "iter/sec",
            "range": "stddev: 0.0009960605748625983",
            "extra": "mean: 268.0687309999996 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.0468778946247339,
            "unit": "iter/sec",
            "range": "stddev: 1.9552600867526064",
            "extra": "mean: 21.332016038800003 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "2f8785a191babc69bef8cdd6fdfe9658f70022b3",
          "message": "Update all non-major dependencies",
          "timestamp": "2024-09-16T04:22:53Z",
          "tree_id": "01cc39c71e5b3448f7226ed5b477ac609e6209d5",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/2f8785a191babc69bef8cdd6fdfe9658f70022b3"
        },
        "date": 1726460794542,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.610134476072487,
            "unit": "iter/sec",
            "range": "stddev: 0.01759494235785373",
            "extra": "mean: 276.9979917999933 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04625104062688425,
            "unit": "iter/sec",
            "range": "stddev: 1.8934978901005168",
            "extra": "mean: 21.621135145199997 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "be3f59f435205f1bf058a3b11220b5727bfea157",
          "message": "Update all non-major dependencies",
          "timestamp": "2024-09-23T03:36:54Z",
          "tree_id": "77728c3775564cf9dc29a3f68f3893eaa8b78cb1",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/be3f59f435205f1bf058a3b11220b5727bfea157"
        },
        "date": 1727062836008,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.49002779873437,
            "unit": "iter/sec",
            "range": "stddev: 0.02348424590843867",
            "extra": "mean: 286.5306690000125 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04621389942543176,
            "unit": "iter/sec",
            "range": "stddev: 1.7177014284017575",
            "extra": "mean: 21.638511626000003 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "b087c61247b37b817433756d019a2c2c677f92ee",
          "message": "Update dependency ruff to >=0.6.8",
          "timestamp": "2024-09-30T03:46:19Z",
          "tree_id": "ec25ae6a70c82f6d5806fe716b83fc99ba72f386",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/b087c61247b37b817433756d019a2c2c677f92ee"
        },
        "date": 1727668197689,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.7061399169336147,
            "unit": "iter/sec",
            "range": "stddev: 0.0004865071366104341",
            "extra": "mean: 269.82251680000786 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04670312612787816,
            "unit": "iter/sec",
            "range": "stddev: 1.96063861248133",
            "extra": "mean: 21.411842908800004 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "9c727ac409e67af3ae81eeb3fe8ce9f8010639aa",
          "message": "Lock file maintenance",
          "timestamp": "2024-10-01T20:26:06Z",
          "tree_id": "1d16e189b8a5f72c9767982e283fa303901daed5",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/9c727ac409e67af3ae81eeb3fe8ce9f8010639aa"
        },
        "date": 1727814575314,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.717000394300839,
            "unit": "iter/sec",
            "range": "stddev: 0.0015611893144924609",
            "extra": "mean: 269.0341388000036 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04750821710786222,
            "unit": "iter/sec",
            "range": "stddev: 1.1746423345652108",
            "extra": "mean: 21.048990277399998 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "dbde50ad836c1814660d3da16348df91717fef79",
          "message": "Update dependency ruff to >=0.6.9",
          "timestamp": "2024-10-07T03:09:19Z",
          "tree_id": "00d3f0ef18a84a6fe6ba2160119043707d15ef4d",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/dbde50ad836c1814660d3da16348df91717fef79"
        },
        "date": 1728270781972,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.466836174431844,
            "unit": "iter/sec",
            "range": "stddev: 0.02178444911953451",
            "extra": "mean: 288.44743440000684 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04552556251527856,
            "unit": "iter/sec",
            "range": "stddev: 1.9293352482670352",
            "extra": "mean: 21.965681361200005 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "df8eb99f724dc3a3b2e7ea10b69994e70f111d06",
          "message": "Update all non-major dependencies",
          "timestamp": "2024-10-12T15:20:50Z",
          "tree_id": "688ff6134ac76febe7c7576cb519ea9db0d6b890",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/df8eb99f724dc3a3b2e7ea10b69994e70f111d06"
        },
        "date": 1728746674089,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.471888057818645,
            "unit": "iter/sec",
            "range": "stddev: 0.023899235676644363",
            "extra": "mean: 288.02771960000655 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04561175297820625,
            "unit": "iter/sec",
            "range": "stddev: 1.9076770351545573",
            "extra": "mean: 21.924173808399996 sec\nrounds: 5"
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
          "id": "d03b21ffbc5d29f3cd149b3c66edee4548be6e28",
          "message": "fix: compatibility with fastapi 0.115.2",
          "timestamp": "2024-10-12T18:22:57+02:00",
          "tree_id": "c9387d974ce569f6b339626ab12efdd791f8b693",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/d03b21ffbc5d29f3cd149b3c66edee4548be6e28"
        },
        "date": 1728750416244,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.513171821282738,
            "unit": "iter/sec",
            "range": "stddev: 0.012234592011501474",
            "extra": "mean: 284.64306640000245 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.046000064860533055,
            "unit": "iter/sec",
            "range": "stddev: 1.3871180565718737",
            "extra": "mean: 21.7390997824 sec\nrounds: 5"
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
          "id": "969d3a639036b9e6226c470300ab055e5e50b47a",
          "message": "Update dependency pre-commit to v4 (#19)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-10-14T21:22:03+02:00",
          "tree_id": "60e55db5413591b861f59ed59a7df916f4ac7872",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/969d3a639036b9e6226c470300ab055e5e50b47a"
        },
        "date": 1728933942388,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.559471328381849,
            "unit": "iter/sec",
            "range": "stddev: 0.010783197853844458",
            "extra": "mean: 280.9405970000057 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04650015543361435,
            "unit": "iter/sec",
            "range": "stddev: 1.3913126914129599",
            "extra": "mean: 21.505304459200005 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "b345fefe53a75c569d1f3847beac29bb88247172",
          "message": "chore(deps): update all non-major dependencies",
          "timestamp": "2024-10-21T03:27:06Z",
          "tree_id": "bc26703f703c8734b2854de1e33676aea9d6f6ed",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/b345fefe53a75c569d1f3847beac29bb88247172"
        },
        "date": 1729481441026,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.612084768226054,
            "unit": "iter/sec",
            "range": "stddev: 0.02019177425543881",
            "extra": "mean: 276.84843080000974 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04734040204327943,
            "unit": "iter/sec",
            "range": "stddev: 1.7766314572351452",
            "extra": "mean: 21.123605986399998 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "8c2225214ce13a5357589d4058258e6d167a0ad0",
          "message": "chore(deps): update all non-major dependencies",
          "timestamp": "2024-10-28T04:32:06Z",
          "tree_id": "df67d975f9b4f327e7f0bfe68dfaa84e1cd3d8e0",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/8c2225214ce13a5357589d4058258e6d167a0ad0"
        },
        "date": 1730090147702,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.671154033761139,
            "unit": "iter/sec",
            "range": "stddev: 0.01494066220705048",
            "extra": "mean: 272.3939095999981 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.046271512534695435,
            "unit": "iter/sec",
            "range": "stddev: 1.9223354087203182",
            "extra": "mean: 21.611569305199982 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "89b69bc5f7c718ba115c3ad9252a193d45a2f3da",
          "message": "chore(deps): lock file maintenance",
          "timestamp": "2024-11-01T03:33:48Z",
          "tree_id": "6dae09597e502e21bae2e59385f0ecd2a395f9f8",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/89b69bc5f7c718ba115c3ad9252a193d45a2f3da"
        },
        "date": 1730432250637,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.6828222624286835,
            "unit": "iter/sec",
            "range": "stddev: 0.014498799749565016",
            "extra": "mean: 271.53088820000164 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04529894933425661,
            "unit": "iter/sec",
            "range": "stddev: 1.964125900388664",
            "extra": "mean: 22.075567197400005 sec\nrounds: 5"
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
            "email": "29139614+renovate[bot]@users.noreply.github.com",
            "name": "renovate[bot]",
            "username": "renovate[bot]"
          },
          "distinct": true,
          "id": "737aa17625b7c71cf72ad29cb9a602d8a35ed256",
          "message": "chore(deps): update all non-major dependencies",
          "timestamp": "2024-11-04T03:17:39Z",
          "tree_id": "9d14b604e2b9b10363a4261bb7225f020067d5f2",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/737aa17625b7c71cf72ad29cb9a602d8a35ed256"
        },
        "date": 1730690490075,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.609611962057737,
            "unit": "iter/sec",
            "range": "stddev: 0.022046565160826613",
            "extra": "mean: 277.0380889999956 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04598800403201789,
            "unit": "iter/sec",
            "range": "stddev: 1.554080150953203",
            "extra": "mean: 21.744801085600006 sec\nrounds: 5"
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
          "id": "b96582942eef8baf54691ae2335e7117377a1266",
          "message": "chore(deps): update dependency ruff to >=0.7.3 (#24)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-11-11T04:07:39Z",
          "tree_id": "7e59d094d92330fecbac568a5f4d29761f2311c7",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/b96582942eef8baf54691ae2335e7117377a1266"
        },
        "date": 1731298277350,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.287660502673451,
            "unit": "iter/sec",
            "range": "stddev: 0.02516103428503738",
            "extra": "mean: 304.16765939999664 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.046239369136258215,
            "unit": "iter/sec",
            "range": "stddev: 1.4265441707989686",
            "extra": "mean: 21.626592634799994 sec\nrounds: 5"
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
          "id": "b576e5dcdc295b09cf0d3a53fc59e23ffb8ba25b",
          "message": "fix(deps): update all non-major dependencies (#25)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-11-18T04:09:02Z",
          "tree_id": "d55fb68de4cf2249cb6c835a9c8b2810659353de",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/b576e5dcdc295b09cf0d3a53fc59e23ffb8ba25b"
        },
        "date": 1731903163938,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.5851360780202155,
            "unit": "iter/sec",
            "range": "stddev: 0.018165415477488026",
            "extra": "mean: 278.9294403999918 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.046118375138618536,
            "unit": "iter/sec",
            "range": "stddev: 1.5130196773728863",
            "extra": "mean: 21.683331144999975 sec\nrounds: 5"
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
          "id": "98ec1118f893c77d2ca518e9a55eb8490bdc1682",
          "message": "chore(deps): update dependency ruff to >=0.8.0 (#26)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-11-25T03:53:42Z",
          "tree_id": "296cbc7cba52f7a5ef690aeea2a22e707897e593",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/98ec1118f893c77d2ca518e9a55eb8490bdc1682"
        },
        "date": 1732507046209,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.6674101947199693,
            "unit": "iter/sec",
            "range": "stddev: 0.017389870128093076",
            "extra": "mean: 272.67198020001047 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.04573994939099641,
            "unit": "iter/sec",
            "range": "stddev: 1.4960527055289319",
            "extra": "mean: 21.862726419999994 sec\nrounds: 5"
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
          "id": "46f9b2ddffba8f7c9ce087fa9110b70500f20aea",
          "message": "chore(deps): lock file maintenance (#27)\n\nCo-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>",
          "timestamp": "2024-12-01T03:37:08Z",
          "tree_id": "d31dfcf7ac1ca61a912d6cf220e6b44ee5a5637e",
          "url": "https://github.com/jvllmr/fastapi-deferred-init/commit/46f9b2ddffba8f7c9ce087fa9110b70500f20aea"
        },
        "date": 1733024448681,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/test_lib.py::test_basic[True]",
            "value": 3.6276224276607634,
            "unit": "iter/sec",
            "range": "stddev: 0.017477210704971935",
            "extra": "mean: 275.6626467999979 msec\nrounds: 5"
          },
          {
            "name": "tests/test_lib.py::test_basic[False]",
            "value": 0.047134937281216635,
            "unit": "iter/sec",
            "range": "stddev: 1.6635885473557175",
            "extra": "mean: 21.21568538500001 sec\nrounds: 5"
          }
        ]
      }
    ]
  }
}