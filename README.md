
# taga

A simple role-giving bot for discord.

## Requires

* **python3** (version 3.6 and above, tested with versions 3.6.9 and 3.8.5)
* **discord.py** (tested with version 1.3.4)

## Usage

```
python3 start.py
```

## settings.json example
```
{
	"token": "key with many numbers, letters and punctuation here",
	"server_id": "123123123",
	"channel_id": "456456456",
	"role_id": "789789789",
	"commands": {
		"marking": {"name":"mark", "aliases":["iamhere"]},
		"barking": {"name":"bark"}
	},
	"command_prefix": "%%"
}
```
