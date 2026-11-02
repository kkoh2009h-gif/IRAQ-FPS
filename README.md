# IRAQ FPS

**IRAQ FPS** is a community-branded PS4 homebrew launcher/build project based on the VCFG frame-generation project.

## Build status
- **CI build:** successful for upstream VCFG **v2.36**.
- **Artifact:** `IRAQ-FPS-build-2.36` (GitHub Actions artifact; contains the PKG and plugin binaries).
- **Package:** `IRAQ-FPS_v2.36.pkg`.
- **Runtime status:** not yet tested on a physical PS4. A successful CI build confirms compilation and packaging, not in-game compatibility or performance gains.
- **Web UI:** prototype only; settings shown on the site do not change console/game settings.

## Download the build
Open [GitHub Actions](https://github.com/kkoh2009h-gif/IRAQ-FPS/actions/workflows/build-ps4.yml), select the latest successful **Build IRAQ FPS PS4 PKG** run, and download the `IRAQ-FPS-build-2.36` artifact. Extract the ZIP to access the PKG and PRX files.

## Upstream and license
- Upstream project: https://github.com/Melnikoff07/vcfg
- Pinned source: VCFG v2.36
- License: MIT; upstream license and attribution are retained in this repository.
- This is an independent community project and is not affiliated with Sony or game publishers.

## Important compatibility notes
- Frame generation and performance behavior depend on the upstream plugin, GoldHEN, and game-specific compatibility.
- The PKG is the launcher package; `.prx` files are plugin binaries and are not installed as PKG files.
- Do not load multiple copies of the plugin at once.
- Back up console data before testing. Stop if a game or system becomes unstable.
- Do not assume a universal FPS increase or 60 FPS support.

## Next milestones
1. Complete branding review (including launcher icon and package metadata).
2. Test installation and launcher startup on PS4 with GoldHEN 9.00.
3. Confirm the correct PRX loading path and configuration on-device.
4. Test supported games individually and document results, crashes, and limitations.
5. Only then publish a release marked as hardware-tested.

## Project links
- Web prototype: https://kkoh2009h-gif.github.io/IRAQ-FPS/
- Source repository: https://github.com/kkoh2009h-gif/IRAQ-FPS
- Build workflow: https://github.com/kkoh2009h-gif/IRAQ-FPS/actions/workflows/build-ps4.yml
