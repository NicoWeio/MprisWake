This is a small Python script to keep your computer awake while Spotify is playing.

## Installation (not tested)
- `pip install pydbus`
- Setup as a user service
  - `ln -s /path/to/mpriswake.service ~/.config/systemd/user/mpriswake.service`
  - `systemctl --user daemon-reload`
  - `systemctl --user enable --now mpriswake.service`

## To do
- Make it work with other MPRIS players, don't just hard-code Spotify
- Try to get rid of polling and use signals instead
