#!/usr/bin/env python3
"""Prefer exactly named repository PNGs; otherwise preserve existing tvg-logo.

This intentionally changes ONLY the tvg-logo attribute on #EXTINF lines. No
stream URLs, channel names, groups, header, ordering, or extra directives change.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / 'IPTV Playlist.m3u'
LOGOS = ROOT / 'logos'
RAW_BASE = 'https://raw.githubusercontent.com/saeidsujon-rahman/BDIX-IPTV/main/logos/'
LOGO_ATTRIBUTE = re.compile(r'(?<!\S)tvg-logo="[^"]*"')
BACKUP_SUFFIX = re.compile(r'\s*\[(?:backup\s*\d+|primary)\]\s*$', re.I)


def slug(name):
    clean = BACKUP_SUFFIX.sub('', name)
    return re.sub(r'[^a-z0-9]+', '-', clean.casefold()).strip('-')[:85] or 'unnamed-channel'


def main():
    if not PLAYLIST.is_file() or not LOGOS.is_dir():
        raise SystemExit('Playlist or logos directory missing')
    available = {p.name for p in LOGOS.iterdir() if p.is_file() and p.suffix.lower() == '.png'}
    # Keep bytes exactly as-is except for explicitly replaced/added logo metadata.
    original = PLAYLIST.read_bytes()
    text = original.decode('utf-8-sig')
    newline = '\r\n' if '\r\n' in text else '\n'
    parts = text.splitlines(keepends=True)
    updated = []
    replaced = added = fallback = 0
    for line in parts:
        if not line.startswith('#EXTINF:'):
            updated.append(line)
            continue
        header = line.rstrip('\r\n')
        left, sep, channel_name = header.rpartition(',')
        if not sep:
            updated.append(line)
            continue
        filename = slug(channel_name.strip()) + '.png'
        if filename not in available:
            fallback += 1
            updated.append(line)
            continue
        url = RAW_BASE + filename
        existing = LOGO_ATTRIBUTE.search(left)
        if existing:
            new_left = left[:existing.start()] + 'tvg-logo="' + url + '"' + left[existing.end():]
            if new_left != left:
                replaced += 1
        else:
            new_left = left + ' tvg-logo="' + url + '"'
            added += 1
        ending = line[len(header):]
        updated.append(new_left + ',' + channel_name + ending)
    result = ''.join(updated).encode('utf-8')
    if original.startswith(b'\xef\xbb\xbf'):
        result = b'\xef\xbb\xbf' + result
    if result != original:
        PLAYLIST.write_bytes(result)
    print(f'Repository logos updated: {replaced}; inserted: {added}; external/unchanged fallback: {fallback}')
    print(f'Changed playlist: {result != original}')


if __name__ == '__main__':
    main()
