# Baobab Insight Partners — Tovuti ya Kampuni ya Utafiti

Mfumo huu umejengwa kwa **Django** (Python), umewekewa ulinzi wa hali ya juu dhidi ya
wadukuzi, na umetengenezwa tayari kwa ajili ya **GitHub + Render**. Hauhitaji kompyuta
ya kawaida (local PC) — kila kitu kinafanyika kwenye kivinjari (browser).

---

## SEHEMU YA 1 — Kuweka Mradi kwenye GitHub (bila kompyuta ya kawaida)

Kwa kuwa hauko kwenye kompyuta yako binafsi, njia bora zaidi ni **GitHub Codespaces**
— mazingira kamili ya uandishi wa code yanayofanya kazi ndani ya kivinjari chako tu.

### Hatua 1: Unda Akaunti na Repository mpya GitHub
1. Ingia kwenye [github.com](https://github.com) na akaunti yako.
2. Bonyeza **"New repository"**.
3. Jina la repo: `baobab-insight-website` (au jina lolote unalotaka).
4. Chagua **Private** (kwa usalama, hadi utakapokuwa tayari kuifanya public).
5. **USICHAGUE** "Add a README file" — acha itupu kabisa.
6. Bonyeza **Create repository**.

### Hatua 2: Fungua GitHub Codespaces
1. Kwenye ukurasa wa repo yako mpya, bonyeza kitufe cha kijani **"Code"**.
2. Chagua tab ya **"Codespaces"**.
3. Bonyeza **"Create codespace on main"**.
4. Subiri dakika 1-2 — itafungua VS Code kamili ndani ya kivinjari chako (bure kwa
   masaa fulani kwa mwezi kwenye akaunti ya kawaida ya GitHub).

### Hatua 3: Pakia Faili za Mradi kwenye Codespace
Nitakupa faili zote kama **ZIP** moja. Ndani ya Codespace:

1. Kwenye VS Code (ndani ya kivinjari), bonyeza kwenye eneo la faili upande wa kushoto.
2. Buruta (drag & drop) faili ya ZIP niliyokupa moja kwa moja kwenye eneo hilo la faili,
   AU tumia terminal iliyo chini ya Codespace na uandike:
   ```bash
   # Kama umepakia ZIP kwenye Codespace tayari:
   unzip baobab_insight.zip -d .
   mv baobab_insight/* .
   mv baobab_insight/.* . 2>/dev/null
   rmdir baobab_insight
   ```
3. Hakikisha faili zote zimeonekana upande wa kushoto (manage.py, config/, core/ n.k.)

### Hatua 4: Tuma (Push) Code kwenda GitHub
Kwenye terminal ya Codespace (chini ya skrini), andika amri hizi mfululizo:

```bash
git add .
git commit -m "Mwanzo wa mradi wa Baobab Insight Partners"
git push
```

Hongera — code yako sasa iko GitHub! Unaweza kuifungua tena wakati wowote kutoka
kivinjari chochote bila kuhitaji kompyuta maalum.

---

## SEHEMU YA 2 — Kujaribu Mradi Kabla ya Kuipeleka Render (Hiari)

Bado ukiwa ndani ya Codespace, unaweza kujaribu tovuti kabla ya kui-deploy:

```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Codespace itaonyesha arifa "Open in Browser" — bonyeza hiyo kuona tovuti yako ikifanya
kazi moja kwa moja kwenye kivinjari, kabla hata haujaipeleka Render.

---

## SEHEMU YA 3 — Kui-Deploy kwenye Render

### Hatua 1: Unda Akaunti Render
Nenda [render.com](https://render.com) na uunde akaunti (unaweza kutumia GitHub
kuingia moja kwa moja — "Sign in with GitHub").

### Hatua 2: Unganisha Repo na Deploy kwa "Blueprint"
Mradi huu una faili ya `render.yaml` iliyowekwa tayari (inaitwa "Render Blueprint"),
hivyo Render itaweza kuunda **Web Service** na **Database** kwa wakati mmoja bila
kuweka mipangilio mingi kwa mkono.

1. Kwenye Render Dashboard, bonyeza **"New +"** → **"Blueprint"**.
2. Chagua repo yako `baobab-insight-website` kutoka GitHub (utahitaji kuipa Render
   ruhusa ya kuisoma repo yako mara ya kwanza).
3. Render itasoma `render.yaml` na kuonyesha itakachounda: Web Service moja +
   PostgreSQL Database moja. Bonyeza **"Apply"**.
4. Subiri dakika 3-5 wakati Render inajenga (build) na kuanzisha mfumo wako.

### Hatua 3: Ongeza Environment Variables za Ziada
`render.yaml` inaunda baadhi ya mipangilio moja kwa moja (SECRET_KEY, DATABASE_URL),
lakini bado unahitaji kuongeza hizi kwa mkono kwenye **Render Dashboard → Environment**:

| Jina | Thamani ya Mfano | Maelezo |
|---|---|---|
| `PROPOSAL_NOTIFY_EMAIL` | `wewe@barua-pepe-yako.com` | Barua pepe itakayopokea taarifa za RFP mpya |
| `DEFAULT_FROM_EMAIL` | `no-reply@baobabinsight.com` | Barua pepe ya "kutoka" |
| `ADMIN_URL_PATH` | `admin-siri-yako-2026/` | **BADILISHA** hii na jina lako la siri (angalia sehemu ya usalama chini) |
| `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` | (kutoka Gmail/SendGrid) | Ili barua pepe za taarifa zitume kweli (bila hizi, arifa zitaonekana kwenye logs pekee) |

Baada ya kuongeza, Render itafanya "redeploy" moja kwa moja.

### Hatua 4: Unda Akaunti ya Admin (Superuser)
1. Kwenye Render Dashboard, fungua Web Service yako.
2. Bonyeza tab ya **"Shell"** (inakupa terminal moja kwa moja kwenye server yako).
3. Andika:
   ```bash
   python manage.py createsuperuser
   ```
4. Jaza username, email, na nywila madhubuti (angalau herufi 12, mchanganyiko).

### Hatua 5: Ingia Kwenye Admin Panel Yako
Fungua: `https://JINA-LA-APP-YAKO.onrender.com/ADMIN_URL_PATH_YAKO/`
(Tumia thamani uliyoweka kwenye `ADMIN_URL_PATH`, si `/admin/` ya kawaida).

Kuanzia hapo unaweza kuongeza: Sekta, Huduma, Takwimu za Impact, Timu, Ripoti/PDF,
Makala za Blog, na kufuatilia Maombi ya RFP yanayoingia.

---

## SEHEMU YA 4 — Usalama Uliowekwa Tayari (na Unachopaswa Kufanya)

### Tayari Umewekewa (Built-in)
- **HTTPS ya kulazimishwa** — trafiki yote inasukumwa kwenda HTTPS (SSL) kiotomatiki.
- **HSTS** — kivinjari kinakumbuka kutumia HTTPS pekee kwa mwaka mzima.
- **Content Security Policy (CSP)** — inazuia uwekaji wa JavaScript/CSS hatarishi.
- **django-axes** — akaunti inafungwa kiotomatiki baada ya majaribio 5 ya nywila
  isiyo sahihi (kinga dhidi ya "brute-force attacks").
- **Honeypot field** — fomu ya RFP ina uwanja wa uwongo unaonasa "bots" za spam
  moja kwa moja bila kuathiri watumiaji halisi.
- **Rate limiting** — mtu mmoja (IP) hawezi kutuma zaidi ya maombi 5 ya RFP kwa saa.
- **File upload validation** — nyaraka za ToR zinazopakiwa lazima ziwe PDF/DOC pekee,
  chini ya 5MB, kuzuia mashambulizi ya kupitia faili hatarishi.
- **Admin URL iliyofichwa** — sio `/admin/` ya kawaida, hivyo bots za kiotomatiki
  haziwezi kuikuta kwa urahisi.
- **Secure cookies** — session na CSRF cookies zinatumwa kwa HTTPS pekee.
- **Nywila madhubuti** — mfumo unalazimisha nywila za angalau herufi 12.
- **Siri zote (secrets) ziko nje ya code** — SECRET_KEY, database password, na email
  password zote ziko kwenye Render Environment Variables, sio kwenye GitHub.

### Lazima Ufanye Mwenyewe (Muhimu Sana)
1. **BADILISHA `ADMIN_URL_PATH`** kutoka default kabla ya kwenda "live" — tumia neno
   la kipekee lisilotabirika (mfano: `mgt-baobab-x7k2/`).
2. **Usiwahi kuweka faili ya `.env`** kwenye GitHub — `.gitignore` tayari inaizuia,
   lakini kagua mara mbili kabla ya `git push` ya kwanza.
3. **Tumia nywila tofauti na dhabiti** kwa kila akaunti ya admin — usitumie nywila
   uliyotumia mahali pengine.
4. **Kagua Render Logs mara kwa mara** (Dashboard → Logs) — utaona maonyo endapo
   kuna majaribio ya kuingia bila ruhusa (`django.security` na `axes` warnings).
5. **Sasisha maktaba (dependencies) mara kwa mara** — kila baada ya miezi 2-3,
   angalia toleo jipya la Django na maktaba nyingine kwenye `requirements.txt`
   kwa masuala ya usalama (security patches).
6. **Weka akaunti ya Render na GitHub na 2FA (Two-Factor Authentication)** — hii ni
   ulinzi wa nje ya mfumo lakini muhimu sana, kwani mtu akiingia GitHub yako
   anaweza kubadilisha code moja kwa moja.
7. **Usimpe mtu yeyote ufikiaji wa Admin Panel** isipokuwa watu unaowaamini kikamilifu.

---

## SEHEMU YA 5 — Kuongeza Domain Yako Mwenyewe (Hiari)

1. Nunua domain (mfano `baobabinsight.com` au `baobabinsight.co.tz`) kutoka
   Namecheap, GoDaddy, au msajili wa ndani.
2. Render Dashboard → Web Service yako → **Settings → Custom Domains** → ongeza
   domain yako.
3. Render itakupa DNS records za kuongeza kwenye msajili wa domain yako
   (kawaida CNAME au A record).
4. Baada ya DNS kusambaa (dakika hadi masaa 24), ongeza domain hiyo pia kwenye
   `ALLOWED_HOSTS` na `CSRF_TRUSTED_ORIGINS` kwenye Render Environment Variables.
5. Render itatoa cheti cha SSL (HTTPS) bure kiotomatiki kwa domain yako mpya.

---

## Muundo wa Mradi

```
baobab_insight/
├── config/          → Mipangilio kuu ya Django (settings, urls)
├── core/            → Homepage, About, Team, Testimonials, Impact Stats
├── sectors/         → Sekta za utafiti (Afya, Elimu, Uchumi, n.k.)
├── services/        → Huduma zinazotolewa
├── insights/        → Ripoti (PDF), Blog/Makala
├── proposals/       → Fomu ya RFP + ulinzi wa spam/rate-limit
├── templates/       → HTML templates zote
├── static/css/      → Muundo wa mwonekano (Navy/Teal theme)
├── render.yaml       → Blueprint ya kui-deploy Render
├── build.sh          → Script ya build kwenye Render
└── requirements.txt  → Maktaba zote zinazohitajika
```

Kila swali au tatizo ukikutana nalo njiani, niletee ujumbe wa hitilafu (error) uliopata
na nitakusaidia kulitatua hatua kwa hatua.
