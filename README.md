# Spotify Top 100

A Python script that scrapes the current **Billboard Hot 100** chart and builds a private **Spotify playlist** from it.

---

## ⚙️ How it works

1. **Scrape** — BeautifulSoup pulls the chart titles from billboard.com and saves them to `Top_Songs.txt`
2. **Authenticate** — Spotipy handles the Spotify OAuth flow (first run opens your browser)
3. **Create + fill** — a private playlist is created and each song is searched and added automatically

---

## 🛠️ Setup

Install dependencies

```
pip install -r requirements.txt
```

Get Spotify API credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) — create an app and add a redirect URI (e.g. `https://localhost:8080/`).

Create a `.env` file

```
SPOTIPY_CLIENT_ID=your-client-id
SPOTIPY_CLIENT_SECRET=your-client-secret
SPOTIPY_REDIRECT_URI=https://localhost:8080/
```

---

## ▶️ Usage

```
python main.py
```

Songs that can't be matched on Spotify are printed as "Not Found" and skipped.
