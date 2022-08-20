from sdk import Patch, Mod
from os import getcwd, sep

mod = Mod()
patches = [
    Patch(0x67a70, b"\x00\x20\x00\xbf"), # movs r0, #0 nop
    # Minecraft::_reloadInput()
    Patch(0x6946c, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Button::render(Minecraft*, int, int)
    Patch(0x6d32c, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Button::renderBg(Minecraft*, int, int)
    Patch(0x6d228, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Screen::updateTabButtonSelection()
    Patch(0x73232, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # GameRenderer::pick(float)
    Patch(0x85b3e, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Gui::render(float, bool, int, int)
    Patch(0x71aa2, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
]

for patch in patches:
    mod.add_patch(patch)

mod.save(getcwd() + sep + "xperia_ui.mod")

