# Count It

Recursive Python script that queries the Reddit API to count keyword occurrences across all hot article titles in a given subreddit.

## Requirements

- Python 3.4.3+
- `requests` module

## Usage

```bash
python3 0-main.py <subreddit> '<list of keywords>'
```

### Examples

```bash
python3 0-main.py programming 'react python java javascript scala'
# java: 27
# javascript: 20
# python: 17
# react: 17
# scala: 4

python3 0-main.py programming 'JavA java'
# java: 54

python3 0-main.py not_a_valid_subreddit 'python java'
# (no output)
```

## Behavior

- Keywords are **case-insensitive** (`Java`, `JAVA`, `java` all count as `java`)
- Duplicate keywords in the list are summed (`java java` counts all occurrences together)
- Punctuation-attached words are ignored (`java.`, `java!` do not count as `java`)
- Results are sorted by count descending; ties are sorted alphabetically
- Words with zero matches are not printed
- Invalid or redirected subreddits print nothing

## File

| File | Description |
|------|-------------|
| `0-count.py` | Recursive function `count_words(subreddit, word_list)` |
