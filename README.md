# river-dotfiles

A River configuration

## Structure

```bash
.
├── autostart
├── config
├── config.json
├── init
├── LICENSE
├── mappings
├── README.md
├── rules
├── scripts
│   ├── border
│   ├── layout_changer
│   └── tmp
│       └── river_tags
└── variables
```

The structure of the configuration is as follows, in order of execution:

- `init`: the main file, the one that `river` will execute on start. It only sources the other executable files and notifies the user when finished loading.
- `variables`: some variables that are used in the other files.
- `mappings`: self-explanatory, just the keybindings.
- `config`: contains some `riverctl` commands with settings.
- `rules`: defines the window rules, for example which windows should float.
- `autostart`: contains the programs that should be started on login.

This is all about river itself, but here I also store some scripts and other files:

- `scripts`: contains some useful scripts, for instance:
  - `border`: a script that toggles the border of the focused window; allows `on` and `off` arguments, and if none is provided it just toggles the border width.
  - `layout_changer`: a script that calls rofi to change the layout of the current tag. I actually use [river-luatile](https://github.com/MaxVerevkin/river-luatile) with my personal [layout](https://github.com/pabloavi/river-luatile-layout). In reality, it is a pack of layouts, with a lot of features, like storing per-tag layout or changing settings on the fly. Those settings are defined in `config.json`.
