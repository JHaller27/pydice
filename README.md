# pydice
Python script to roll dice

## Usage
roll <dice> [<dice> [<dice> [...]]]
  
<dice> format is as follows:
  `WdX[(d|k)(h|l)Y][+|-Z]` where...
  * W = number of dice to roll (required)
  * X = number of sides on each die (required)
  * Y = number of dice to drop/keep (optional)
    * dh/dl/kh/kl = **d**rop/**k**eep **h**ighest/**l**owest
    * Note: `WdXdlY` has the same effect as `WdXkh[W-Y]`
  * Z = amount to add/subtract (optional)

## Examples
| Command | Description |
|:-------:|:------------|
| `roll 1d20` | Roll a single 20-sided die |
| `roll 1d20kh1` | Roll 2 20-sided dice and keep only the highest roll (i.e. roll with advantage) |
| `roll 1d20dl1` | Roll 2 20-sided dice and drop only the lowest roll (equivalent to the previous command) |
| `roll 1d20+3` | Roll 1 20-sided die then add 3 |
| `roll 4d6kh3+2` | Roll 4 6-sided dice, keep only the highest 3 rolls, then add 2 to the summation |
