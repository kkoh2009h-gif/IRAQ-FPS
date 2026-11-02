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

## Build workflow
- GitHub Actions now checks out the pinned upstream v2.36 source and uses the upstream Docker build scripts (including pinned OpenOrbis/GoldHEN dependencies and regression checks).
- The workflow applies launcher string branding and sets the package title to IRAQ FPS in `param.sfo`; the upstream package/content ID is intentionally retained for now. The icon remains upstream-branded and needs a separate asset review.
- The latest workflow run has not yet been confirmed successful; check Actions before treating its artifact as usable.

## Not yet release-ready
- The upstream build environment is provisioned in CI from the upstream Docker scripts; this has not yet been confirmed end-to-end for this fork.
- The workflow was corrected to use the upstream v2.36 output filename and publish it as `IRAQ-FPS_v2.36.pkg`; a successful run is still required to validate it end-to-end.
- No IRAQ FPS PKG has been verified on a PS4; do not treat workflow artifacts as install-ready.
- Launcher icon branding still needs a complete pass, followed by a clean build and hardware testing.

## Safe next build sequence
1. Configure the OpenOrbis toolchain and GoldHEN Plugins SDK as required by upstream.
2. Build the new plugin and classic plugin using the upstream scripts.
3. Run the upstream shader-array and regression checks.
4. Build the launcher PKG using the upstream packaging script, with IRAQ FPS branding changes reviewed.
5. Install only after the PKG is reproducibly built; test on GoldHEN 9.00 with backups and one plugin instance.

Upstream reference: https://github.com/Melnikoff07/vcfg
