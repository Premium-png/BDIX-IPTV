# 🤖 IPTV Auto Update

Generated: **2026-09-13 08:19 UTC**

## Changes

- New backup streams: **0**
- New channels automatically added: **0**
- New Adult channels automatically added: **0**
- Known bad V1 entries removed: **10**
- Existing channel categories corrected: **0**
- Existing metadata fields repaired: **25**
- Alternative labels normalized: **8**
- Wrapper/proxy URLs resolved: **640**
- Blocked/expired URLs skipped without a clean replacement: **28**
- Duplicate URLs removed: **0**
- Confirmed dead streams deleted: **0**
- Current HTTP 404/410 results: **6**
- Uncertain remote failures ignored: **19**
- Restricted/reachable responses preserved: **10**
- Supported playlist categories: **11**

## Category policy

- The updater uses only the categories already present in the current playlist:
  Bangladesh, Indian Bangla, Indian Movies, Indian Music, Indian Entertainment, International Movies, International Music, Documentary & Wildlife, Kids, Religious, Sports
- Non-Bangladeshi news channels are excluded.
- Bangladesh entries require an exact verified channel name; source group labels are not trusted.
- Bangladesh news channels remain inside the Bangladesh category.
- Backups for existing channels inherit the primary channel's current category.
- Adult channels and user-rejected stream URLs are excluded permanently.
- Sports, Indian Entertainment, Documentary & Wildlife, and Kids use major-channel allowlists.
- Non-Islamic religious channels are excluded.
- VOD, geo-blocked, and explicitly not-24/7 entries are not auto-added.

## Current 404/410 streaks

- `2/5` — HTTP 404 — https://cdn.ghuddi.live/Bangla_TV/Bangla_TV_BD/playlist.m3u8
- `1/5` — HTTP 404 — http://103.190.133.68:1935/news21live/live/playlist.m3u8
- `1/5` — HTTP 404 — https://cdn-4.pishow.tv/live/1293/master.m3u8
- `1/5` — HTTP 404 — https://server.zillarbarta.com/ZBCINEMA/index.m3u8
- `1/5` — HTTP 404 — https://tvsen6.aynaott.com/opREbXLqJ2HFYPCXTJBa/index.m3u8
- `1/5` — HTTP 404 — https://video1.getstreamhosting.com:1936/eycqczsxka/eycqczsxka/playlist.m3u8

## Cleaned V1 entries

- Removed **Aristanis SuperTv** — https://video2.azotosolutions.com:1936/supertvoristano/supertvoristano/playlist.m3u8
- Removed **Asian** — https://mtlivestream.com/hls/asian/ytlive/index.m3u8
- Removed **AzStarTV** — http://live.azstartv.com/azstar/smil:azstar.smil/playlist.m3u8
- Removed **LaC News 24** — https://f5842579ff984c1c98d63b8d789673eb.msvdn.net/live/S27391994/HVvPMzy/playlist.m3u8
- Removed **News 24 Ⓢ** — https://tv.balkanweb.com/news24/livestream/playlist.m3u8
- Removed **Rtv 38 Toscana** — https://845d8509d2cb4f249dd0b2ae5755b6c2.msvdn.net/rtv38/rtv38_live_main/mainabr/playlist_dvr.m3u8
- Removed **RTV HB Ⓢ** — https://prd-hometv-live-open.spectar.tv/ERO_1_083/playlist.m3u8
- Removed **RTV Noord** — https://media.rtvnoord.nl/live/rtvnoord/tv/playlist.m3u8
- Removed **RTV ZE Ⓢ** — https://stream.rtvze.ba/live/123/123.m3u8
- Removed **Supertv** — http://wms.shared.streamshow.it:1935/supertv/supertv/live.m3u8

## Metadata repairs

- **Aristanis SuperTv** — tvg-id
- **Asian** — tvg-id
- **AzStarTV** — tvg-id
- **Bangla 1** — tvg-id
- **BTV** — tvg-id
- **Channel 1** — tvg-id
- **Channel 16** — tvg-id
- **Ekushe TV** — tvg-id
- **EP TV** — tvg-id
- **Independent** — tvg-id
- **LaC News 24** — tvg-id
- **News 21 Bangla TV** — tvg-id
- **News 24 Ⓢ** — tvg-id
- **Rtv 38 Toscana** — tvg-id
- **RTV HB Ⓢ** — tvg-id
- **RTV Noord** — tvg-id
- **RTV ZE Ⓢ** — tvg-id
- **Supertv** — tvg-id
- **Akash Bangla** — tvg-id
- **Khusbo Bangla** — tvg-id
- **R Plus Gold** — tvg-id
- **Ruposhi Bangla** — tvg-id
- **Persiana Kore** — tvg-id
- **Sangeet Bhojpuri** — tvg-id
- **Star Sports SL 2** — tvg-id

## Adult expansion sources


## Safety

- Unclassified new channels skipped: 381
- Non-Adult new channels without logos skipped: 0
- Adult candidates skipped because daily cap was reached: 0
- Adult candidates strictly tested this run: **0** / 40
- Adult candidates validated as live HLS: **0**
- Adult candidates rejected by strict validation: **0**
- Adult additions/backups skipped by quality gate: 0
- Adult candidates skipped for weak metadata: 0
- Adult candidates skipped by name policy (VOD/geo/not-24x7): 0
- Candidates skipped by the owner's curated policy: 89
- Dedicated Adult source feeds configured: 0
- Channels already at the backup limit skipped: 7

> A stream is deleted only after repeated HTTP 404/410 responses. Timeouts, DNS/connect failures, 401/403/405/451, and other uncertain responses do not trigger deletion. This reduces false deletion of BDIX, ISP-specific, geo-restricted, or temporarily unavailable streams.
