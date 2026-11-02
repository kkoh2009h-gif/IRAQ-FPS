# IRAQ FPS

**IRAQ FPS** is a community rebrand/derivative project based on the VCFG PS4 frame-generation homebrew project.

## Current status
- Public web UI prototype: https://kkoh2009h-gif.github.io/IRAQ-FPS/
- Imported VCFG launcher source: upstream/vcfg/launcher/src/
- Branding pass applied to the launcher header.
- Native PS4 PKG build and runtime integration are **not yet validated**. The separate prototype build workflow is experimental and should not be treated as a confirmed working PKG pipeline.

## Upstream project and license
- Upstream: https://github.com/Melnikoff07/vcfg
- License: MIT; see upstream/vcfg/LICENSE
- Upstream documentation and compatibility information remain authoritative for the frame-generation engine.
- This project is independent and is not affiliated with Sony or game publishers.

## Important
Frame generation depends on the upstream GoldHEN plugin and game-specific compatibility. Rebranding the launcher does not itself implement or improve FPS. Do not install experimental plugins on a console without backups and understanding the risk.

## Planned work
1. Integrate the complete upstream build layout and dependencies with attribution.
2. Rebrand launcher title, icon, package metadata, and menus as IRAQ FPS.
3. Build a reproducible PS4 PKG in CI using the upstream-supported toolchain.
4. Test on PS4 GoldHEN 9.00 before claiming compatibility.
