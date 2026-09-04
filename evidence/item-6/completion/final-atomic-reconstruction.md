# Item 6 final atomic reconstruction

## Scope and identity

- Source branch content commit: `7da1923e655e65046734ae5e9f7cf8df330b8362`.
- Reconstructed content commit: `d7f7974fedbb702af2a846f3dddde1a7b50710dd`.
- Source and reconstructed content tree: `bb96e412439ed1c43e82a994719353217c6deba6`.
- Recovery ref: `codex/item-6-completion-pre-final-atomic-rewrite` at the source commit.
- Source commits: 76. Reconstructed content commits: 105.
- Result: exact tree equality before this evidence-only receipt. This receipt is the only intentional post-source tree addition.

## Verification scenarios

| Scenario | Invocation | Binary observable | Captured result |
|---|---|---|---|
| Exact content parity | `git rev-parse d7f7974^{tree} 7da1923^{tree}` | Both tree hashes are identical | `bb96e412439ed1c43e82a994719353217c6deba6` for both |
| Full regression | `uv run pytest -q` | Exit 0 | 629 passed |
| Item 6 regression | `uv run pytest -q tests/item6` | Exit 0 | 502 passed |
| Changed Python formatting | `uv run ruff format --check <52 changed Python files>` | Exit 0 | 52 files already formatted |
| Changed Python lint | `uv run ruff check <52 changed Python files>` | Exit 0 | All checks passed |
| Static typing | `uv run basedpyright src tests tools/freeze_item6_config.py` | Exit 0 | 0 errors, 0 warnings, 0 notes |
| Real validation CLI | `uv run python tools/freeze_item6_config.py validate --root evidence/item-6/frozen --manifest evidence/item-6/generated-config-manifest.json --audit evidence/item-6/config-audit.json` | Exit 0 | Validated Item 6 frozen configuration and audit |
| Patch hygiene | `git diff --check origin/main..d7f7974` | Exit 0 | No whitespace errors |
| OMO exclusion | `test -z "$(git ls-files '.omo/**')"` | Exit 0 | No tracked `.omo` paths |
| Credential redaction | Parse the committed resourceful config and sanitization receipt, then assert the sentinel and one bound redaction | Exit 0 | Secret-safe scan passed |

## Old-to-new commit map

Patch-identical rows have the same stable patch ID. Split rows partition one former combined patch into independently validatable commits. The AdoraBuild ordering-only commit is an extracted partition of that source patch.

| Original commit | Original subject | Reconstructed commit or commits | Disposition |
|---|---|---|---|
| `be6039219a14f1913680e768459fb63cd213c8b3` | fix(item6): account for every frozen config file | `163debbd6deba59131b71caa74cdcc434822e220`<br>`f4043bf6e1bb15ce8a21977f1db7af902df61575`<br>`16e8c8922564aaad96c99ec558c73c6737d6fdef` | split |
| `c53b3d3a7f618a64f77ba6d5233d4b0625d905e5` | fix(item6): audit YUNG replacement defaults | `22eb8119146e63472ff52ce209acf4218fb08e4d` | patch-identical replay |
| `8b4173f80da250a787420dc211900ff71fbce56e` | fix(item6): audit Better Desert Temples placement | `cac16769d510d9de4d8dd6d2a6fcade70f1b85ab` | patch-identical replay |
| `6e18b70a04b4ae22b1a549b906c2446070ffd670` | fix(item6): audit Better Dungeons placement | `7a2c15b73240d8abb2237c4e3de0ebc66ebf9122` | patch-identical replay |
| `26a6d6fcf80823fd5c97bad9427c10b5cfcd452f` | fix(item6): audit Better Nether Fortresses placement | `77355fc334dcf6b5cbb122905540a42b8c64012e` | patch-identical replay |
| `4b52609efe6fcc82c8144bba17cb485fd10901ca` | fix(item6): audit Better Jungle Temples placement | `bde7ce8c63a16a1639300920dc0eacbf225a12dc` | patch-identical replay |
| `4bc0e69ca88ee696be5fe51b3c01c50d68840ca3` | fix(item6): audit Better Mineshafts placement | `c9b8c79a3047dbef1c8c15f042a38c047c435019` | patch-identical replay |
| `ba154748ff40cf78c2031939fc60780d8e706cfd` | fix(item6): audit Better Ocean Monuments placement | `255b205d65906af04ab68bf61a2e28536bd70643` | patch-identical replay |
| `ffc3149487da58af4f3ab83388d31958b6ca9e52` | fix(item6): audit Better Strongholds placement | `fb0902305b52503eceb428da93ab43939e1315e8` | patch-identical replay |
| `f05bb3f02a5af10aa5fdea7dd3959dc0c3ffe400` | fix(item6): audit Better Witch Huts placement | `f5d83bddefab6b2954e54acd396664f30a2c506c` | patch-identical replay |
| `08e84113c91e8152f80c1224adcdde417891522f` | docs(item6): classify auxiliary YUNG surfaces | `afc8561fd67084f639ea6d0d91cab49596a4ca5d` | patch-identical replay |
| `5d24ded7c19c861d1a77bb8e28ab9998a5cb0a56` | fix(item6): bind audit values to frozen sources | `5c678a1947f8149c6da96343b510a3a119feb910` | patch-identical replay |
| `2fac6d0e65d3a91d7b4738a4d0294689423122be` | fix(item6): reject repeated wildcard source lines | `f2eea2bad9f973e242730c7568f079da4278ebde` | patch-identical replay |
| `5b68f5cf2954bc9bfe0389de73c94cd07e00a356` | test(item6): retain worktree isolation receipts | `6d27d754ad44a3bfb06806cc43e97286920e71ce` | patch-identical replay |
| `46238b4992c86af276bd6e8c62483789409d31b9` | test(item6): retain accounting closure receipts | `4979b72294c2a72662488c7f2238da963eec5b05` | patch-identical replay |
| `d33ceb121aeb4311a53c1a14496ef48f513264e5` | test(item6): retain value-binding verification receipts | `4aab6c456808dfbb4bb985da8a43e3e57db991b5`<br>`fc48adc3a741142caa4cb9717624f62f97703cba`<br>`33a5946a840f078801137d2a99ef2f9ef5de23f8`<br>`a82d5b2ddb6aeef0dee54b77549ddfaa08b6e4db` | split |
| `9c565b8ecf8be69011794d479b551029086c9c55` | test(item6): record provider-split rewrite verification | `738bd0248bdd8195142028172d376defd4b5af6d` | patch-identical replay |
| `7e21079d9b5e67e23599d96e73483dcb5263ba15` | test(item6): characterize validator facade | `3a448a7b715832ee35f98ebf3cc9901e8ad0f907` | patch-identical replay |
| `2e699fde284d70ab54ea09b1d46e395d748f9779` | refactor(item6): extract configuration capture | `111f7b261bbc68a252295cfd44e5545e1c5e71c9` | patch-identical replay |
| `5a4c6b631137a519b94db6757e9c2d0f7962a274` | refactor(item6): extract audit validation | `a067208229be337edad3e05f6c7941237c3c8afc` | patch-identical replay |
| `b3dc73f000add0ba57239637f17b7ba98a7e9ce2` | test(item6): record validator split review | `dfc71bc6ff9b3cbf7c555167c6263b6372929a83` | patch-identical replay |
| `f01524ebf2098422531a37e3aa62f2f0a4946922` | refactor(item6): extract manifest inventory validation | `cda76459eee2c0b4bb08b6c36e01d55d6977fdaf` | patch-identical replay |
| `522745ede2ec060d85c519573d3d23ed37dc170c` | fix(item6): enforce manifest capture contract | `fa20c8c393e7b53ac3702d005a69f5c013659873` | patch-identical replay |
| `b07c646f4819c023e0c42204925a140cc26b4e19` | fix(item6): bind repository evidence references | `8d8895eb87d2947fb7380a0d9623f88d149bd7cd` | patch-identical replay |
| `f0811416f0454da16b6f6fb8ba7ae56f45f785dd` | fix(item6): bind lifecycle receipt | `748cd179f0e3462a5929dbac82c0af74026968ce` | patch-identical replay |
| `93cdc722e0aa98ed5db05e24dc5ce03838b987bd` | fix(item6): bind materialization receipt | `f7b4bb01689773456353905bfaaf5d838298cf7d` | patch-identical replay |
| `a6e70aa2da98efd3c5b9707f331f1e3fa39d7287` | fix(item6): preflight capture sources | `c3c541fa5e294c7975bd25060b7a9bdf18e5e1b3` | patch-identical replay |
| `24056c2ba691af1d6063f52a079f1ab998dbd297` | fix(item6): reject nested capture symlinks | `ef3bb68da448be5837b9a357e45eebcf25a0ec1d` | patch-identical replay |
| `e1b2b7f50e3583ce38f2e3be6ef284b55a04a3e2` | test(item6): record capture final gates | `654aafbe5bfbf327f3669c8752b199624af3fced` | patch-identical replay |
| `a86f364849490ae6bcb1109120e6116fc42fbd0e` | docs: define atomic delivery workflow | `8179d23dec8826124115b18ab957727ee4ec899c` | patch-identical replay |
| `8725081924e24bf93e032a37bcd5acb8ba628b6f` | docs(item6): synchronize frozen configuration audit | `f15081d45e9bd3c8af7e4492493bea3e18f7cbf0` | patch-identical replay |
| `524baef6e65e1d52939fe0df72fed5829325b929` | docs(item6): close retained-stack audit ledger | `59b145d4e32f53a45ef5bd17051cee9623bb9118` | patch-identical replay |
| `bc51c7dcaf28ea51fa551c7a5970ffea2e8a2e68` | fix(item6): forbid unknown manifest fields | `2ef9c9fc9c106a3cffc6f98ce619f8d5e5adc1fc` | patch-identical replay |
| `2fa6a9e61bace2fb2535b4d9a8713f1c0172a404` | fix(item6): forbid unknown audit fields | `3aabb1fe9637aa8bd2019d2e93cd3b1cc7496c16` | patch-identical replay |
| `78223638ca3eeb880963e5f4d98da77a61c174c3` | fix(item6): confine frozen manifest paths | `b532490de5aa2315eb029b1ce0c94b0bf9376efa` | patch-identical replay |
| `e54daf516f3a0e96b29008301423091df67e22a6` | fix(item6): add grouped setting surface contract | `bf06b60b99cb1d786bd24c651f8bba6549559484` | patch-identical replay |
| `22e1224c5111a278656a9bd76cf599f9f46705ab` | fix(item6): complete WDA setting surfaces | `43b7f1f7a337c6758170d5cdae53be3754bcde1c`<br>`0266ac376dfdae3eca0e9fe20e57d1fe35041558` | split |
| `b0c84b0d199feca6579beb7af52a91f6c45c5c9e` | fix(item6): complete Seven Seas setting surfaces | `f5f8946c06d3fe0badcabdb98eef9c0c412ae53a`<br>`f1d5885a4129aa9b29e5056481a993bf78dcf490` | split |
| `c9b74611e5877e70ac76cf16c500bc0593dc66ac` | fix(item6): complete IDAS setting surfaces | `3d93b6f1c293182ee635d908109dc2a541bf6693`<br>`d33c2e049f2b9c0029f70c9c4947a9ca207c8b84`<br>`c2e638d99cc2bc2c2d10e70b4cd30dc6a83e7565` | split |
| `7e26ac82e276b3b18d44bbf745bc62c1373d33a7` | fix(item6): complete integrated setting surfaces | `e1f1eb3d862a68029adedda47ac5e9e771605e56`<br>`f92594bfedfe2dde18f8ac7b46bfa98afc647a10`<br>`d58ce3aa7477db9483e5ed1f2cf9bd5614c20c10`<br>`393c74e7efcf832e38e62d8ddce4a41faa05cecc`<br>`6d0ed974704d8a867bd048952d09b6b928a3827c` | split |
| `62b3b0273f49c8264d6904f432893fe1bb62f2fd` | fix(item6): complete MES setting surfaces | `9a21c65728853c8964fb0e3060188788b832e802`<br>`8574d4a5512ff0ac9ad84b1967c009ef85c159f1` | split |
| `8496e050d4fff0c17e3df73ce76488189fe125d5` | fix(item6): complete MNS setting surfaces | `021769748158b6e0bb9189986ac4f3cd1291b6a0`<br>`9a340e6d2c0be683328502cce8db3ce72c0afa24` | split |
| `f5cacb74d88e8ebf270552cf977353caa80f3779` | fix(item6): complete MSS setting surfaces | `75808196d8eb6215149682fd2e0d52ad456dbf6e`<br>`4df0431d3fc491c7d04ff0c8530cebdffce79393` | split |
| `daf781ffa577b18cec1e49d087e3e7e0926e823b` | fix(item6): complete MVS setting surfaces | `a819c7806ae3d78f38191b11da1c4b6c0036535f`<br>`d33cf08dd6c3b29edcb3c518f7bd2ca54166deea` | split |
| `8ba90fee9b075d06cb881b3bed3b48d048790cbf` | fix(item6): complete Repurposed Structures surfaces | `ca373c47461f36353c3a79825b468b5bbada78ce`<br>`e8a3db46d629d205b1c0e4d40581dc3d099ec783` | split |
| `ced2675e66f97b73752d6bcb350d1819a58af4b9` | fix(item6): audit Repurposed Structures loot controls | `640dab61e3f1faf81d547ea0487dbe93875f1738` | patch-identical replay |
| `17491911f0e4d84f5eb2487e2fa660953f657251` | fix(item6): complete AdoraBuild setting surfaces | `05252535911be56d3a62feffc834b09c7f1000a7`<br>`52c45ceec103c8759b6e5f04a5745c041588c3ea`<br>`5fcced1452a146587f8e936dc62cd22f37be884a` | split |
| `646401048b8e87f44201ba35e05f0ef14ebd812b` | fix(item6): complete Aether setting surfaces | `8cf2cb01324b3d80e9f497e73464080ca50e2ac2`<br>`8a2a7a8cac21ffadbc35a97e3b67e07812ee039c` | split |
| `6cc388c0664dc92c839db976299bb825fe01a87a` | fix(item6): complete BetterEnd setting surfaces | `9d8cd34b23c569d592502db092e3f77246eed710`<br>`db75e0d3d7e849215099c1cb33328b37f1c262dc` | split |
| `5b5d3202b6bbb46ca660d60c67cc140e27c93243` | fix(item6): complete Creating Space setting surfaces | `9e50fe473d41faa520797a81a9d9a836cbbf9d30`<br>`22deaa00c500705c2875b343b510720a42f5f8bc` | split |
| `08f95e2fe2313874d6b1b7291bebcfdaeb3e2f09` | fix(item6): complete Deep Aether setting surfaces | `95c710b8beb3e0ac9733e78d3f3da119bc6bafa5`<br>`02b5444a26612ff8562b785a99f6f3870cf705a8` | split |
| `d07d0a03cb5c677933faa06e956184fe8d22ce33` | fix(item6): complete Explorations setting surfaces | `539898800be84baee9ef09124604f4c6b0094f9d`<br>`53666020bf5d1857f37b86ac95ba68c3f4a827fd` | split |
| `0f51343f43a34d76b7a476156ccc2e9a3b1d25dd` | fix(item6): complete Explorify setting surfaces | `fd10b955c0df97e9f1af963ac49e75cf2136f20a`<br>`a269971f529a8f41b895a5ac071a7ad51d944f6f` | split |
| `f0786fd543efbdd8599055c1d74d20fa9e085b4b` | fix(item6): complete Illager Invasion setting surfaces | `e30d8134b8a7d3f4fc0a24959e841c334b143ed0`<br>`1f514023813aa124f8d50c86b5b22c3498d734e0` | split |
| `df5271bd8dfa522064c49cd2ca2fd9ec0f6a6b14` | fix(item6): complete Supplementaries setting surfaces | `e0540e1a5eb9c84e52a2a971ac9e82ed5236b0e1`<br>`4bf9ca863b39de2de2d8168a6ffcb5a9dc1acd31` | split |
| `43326e4baee152b8872c26c515c447a86138e06f` | fix(item6): complete Terralith setting surfaces | `67961e4b8eb24d543b76deb8ccbf06a87933e825`<br>`7635fb2ba7ff533e3aab9195214fd4c148e23222` | split |
| `19eb6f09e73ea6bfd69578d849cad7a021f593b4` | docs(ledger): close Items 3 through 5 | `2e622c0ebd7b42c94fa1c2bd4dc35815eaefff7d` | patch-identical replay |
| `f7fff7f1a5dc68c01a2cd603107973bbce071015` | fix(item6): bind Towns and Towers defaults | `bda1ba2764dd803ca21e9b5d7101e8aff1d46c12` | patch-identical replay |
| `ad06ebf9d8b96b44d66002309141765f56c1c611` | fix(item6): require file-accounting rationales | `d627cfa01302ed36cbf93d71b670eed305d61542` | patch-identical replay |
| `6aef58247085574d358318769d49fcb6a0c2a2c1` | fix(item6): redact generated capture credential | `6d44feec65b414e64f3ed7692c277b0f922e783e` | patch-identical replay |
| `865b4f9e745cbef70f1bb275ba355e2df0335206` | fix(item6): validate sanitization receipts | `b223d673a9e1da274a7f107cedfda86ca9e285c4` | patch-identical replay |
| `df3090141fed0e253fd3338baecb4f6dd082cdc6` | fix(item6): bind sanitized frozen identity | `0722636e2b17f76ea006307e81c6824f72cca601` | patch-identical replay |
| `b170ce7aad70322ecbaee27d113df880f91b56fb` | docs: consolidate durable engineering rules | `885b9a690b95c76d8d6fcc8604ade6a70d3cf6e6` | patch-identical replay |
| `de0a86c124e073dfc8a528876a2566b426198390` | fix(item6): seal audit semantics | `b2dceaa6a94dcf01c742a8242cc129d7369855a9` | patch-identical replay |
| `08fca3538a0ab19cb18826ce80876cc300cfe85e` | docs: add anti-overengineering decision gates | `a2f30fd0989b46be2ddb5c6cf17d0faf796b04de` | patch-identical replay |
| `eeb6b38e6c6331629fdc51169aada6a82dab4dbe` | docs(item6): synchronize audit counts and sanitization | `4bd8fb39fe5ef20d8b47128ac381c8f37ec1e57f` | patch-identical replay |
| `3ad06e63f5152dbc5b018f778d42441658254e48` | style(item6): format audit validation files | `b14a2bc4b5cb06137accd8b8c8a5f8b95a59f58d` | patch-identical replay |
| `16c9a9b993f351927b812b830e32a23e30f6601e` | fix(item6): bind Towns and Towers defaults | `2afeb618dbbea57c6fa32183c2ff1ef43e17ea7c` | patch-identical replay |
| `a5e118f8e0b24b8581ca217b033dab6382fb6b1d` | fix(item6): reject linked capture output parents | `563dbd61fb736cae0e988c0ef3507faed04fb6cb` | patch-identical replay |
| `1b72ef62d031671b3a9549e40070f789b75dbaee` | refactor(item6): split audit validation concerns | `dfb1446196ed43be5c7d77efaba5b2ecb63f4684` | patch-identical replay |
| `10dd7b3312d949a0794be5446fffc89e319ad810` | fix(item6): audit Towns and Towers toggles | `366f5760b692ba8e4180dd7991f2e87eebcf1b0c` | patch-identical replay |
| `ada7decd5fa4672ebdb3d4dceee71d821075d38e` | fix(item6): preserve captured config bytes | `695e55260bc2ddd390749dbb9e96e956cd78ee9f` | patch-identical replay |
| `8291b75352aefa239e61b8ad2cb52d92634b3765` | fix(item6): audit vanilla structure placement | `bd3aaa6acd6451974b302cb29fac5723c23c81d0` | patch-identical replay |
| `b621e9ec27b2f5b88ebd45cf5666bf0200d90f38` | fix(item6): audit vanilla structure toggles | `2a5fa02c187e42400f426fbbde70231d715281a6` | patch-identical replay |
| `76baf1d96a3537b1a61c28247c6bab13f058685e` | fix(item6): audit Naturalist mob removals | `ca086ce639b8da3643c18addd2c2fefeae86199f` | patch-identical replay |
| `7da1923e655e65046734ae5e9f7cf8df330b8362` | docs(item6): sync final audit counts | `d7f7974fedbb702af2a846f3dddde1a7b50710dd` | patch-identical replay |

## Reviewability boundary

Each CristelLib source file now lands in its own commit. Direct TOML controls remain separate from grouped JSON5 placement and toggle surfaces. The two historical receipt bundles are partitioned by characterization, failure, success, CLI, and cleanup purpose. The indivisible typed audit migration and sanitized identity migration remain isolated.
