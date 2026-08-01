# WordleFetch
## Get the answers you want


Default output when only running the command:
```bash
$ wordlefetch
```
```text
- Todays Wordle -
Answer • pshaw
Date • 2026-07-15
Editor • Tracy Bennett
```
Example of using flags to customise the output:
```bash
$ wordlefetch -H -A -D -H
```
```text
- Todays Wordle -
Answer • pshaw
Date • 2026-07-15
- Todays Wordle -
```

## Display Flags
These flags control which information is displayed in the output and can be used more than once.

| Flag | Long Form | Description |
| :--- | :--- | :--- |
| -H | --header | Adds showing the header. |
| -A | --answer | Adds showing the Wordle answer. |
| -D | --date-display | Adds showing the date. |
| -E | --editor | Adds showing the Wordle editor. |
| -I | --id | Adds showing the Wordle ID. |
| -L | --launch | Adds showing days since Wordle launch. |

### Advanced Configuration & Miscellaneous Flags

| Flag | Long Form | Description |
| :--- | :--- | :--- |
| -u | --url | Allows fetching data from a separate API endpoint |
| -d | --customdate | Allows fetching a different date instead of today's date |
| -V | --version | Shows installed WordleFetch package version and exits |



## Links
[PyPi - WordleFetch](https://pypi.org/project/WordleFetch/)




---

# This project is licensed under the MIT license, see [LICENSE](LICENSE)