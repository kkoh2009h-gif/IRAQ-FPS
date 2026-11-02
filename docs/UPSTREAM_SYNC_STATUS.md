# IRAQ FPS — upstream source sync status

Last source snapshot checked: **VCFG v2.36** (upstream main).

## Imported into this repository
- VCFG launcher sources and selected assets under `upstream/vcfg/launcher/`
- Plugin runtime sources under `upstream/vcfg/plugin/source/` and `plugin/common/`
- New-engine shader IR under `upstream/vcfg/plugin/shaders/`
- Classic-engine sources, shader IR, and shader generator under `upstream/vcfg/classic/`
- Overlay sources and shader inputs under `upstream/vcfg/overlay/`
- ELF/shader validation helper under `upstream/vcfg/tools/elf_arrays.py`
- Upstream MIT license and attribution

## Not yet release-ready
- The upstream build environment/dependencies have not been fully reproduced in this repository's GitHub Actions.
- The experimental PKG workflow in the project has not been validated against the upstream v2.36 build scripts.
- No IRAQ FPS PKG has been verified on a PS4; do not treat workflow artifacts as install-ready.
- Launcher branding and package metadata still need a complete pass, followed by a clean build and hardware testing.

## Safe next build sequence
1. Configure the OpenOrbis toolchain and GoldHEN Plugins SDK as required by upstream.
2. Build the new plugin and classic plugin using the upstream scripts.
3. Run the upstream shader-array and regression checks.
4. Build the launcher PKG using the upstream packaging script, with IRAQ FPS branding changes reviewed.
5. Install only after the PKG is reproducibly built; test on GoldHEN 9.00 with backups and one plugin instance.

Upstream reference: https://github.com/Melnikoff07/vcfg
