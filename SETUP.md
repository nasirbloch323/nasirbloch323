# 🚀 GitHub 3D Profile README - Setup Guide

## 📁 Files Included

```
nasirbloch323-github-profile/
├── README.md                          # Main 3D Profile README
├── .github/
│   └── workflows/
│       ├── 3d-contrib.yml            # 3D Contribution Graph (Daily Auto)
│       ├── snake.yml                 # Snake Animation (Daily Auto)
│       └── update-readme.yml         # Auto-Update Stats & Projects (Daily Auto)
└── scripts/
    └── update_readme.py              # Python script for fetching latest data
```

---

## ⚡ Quick Setup Steps

### Step 1: Create Profile Repository
1. Go to [GitHub](https://github.com/new)
2. Create a **new public repository**
3. Name it exactly: **`nasirbloch323`** (same as your username)
4. ✅ Initialize with a README (optional - you'll replace it)

### Step 2: Upload All Files
1. Clone your new repo:
```bash
git clone https://github.com/nasirbloch323/nasirbloch323.git
cd nasirbloch323
```

2. Copy ALL files from this folder into the repo
3. Commit & Push:
```bash
git add .
git commit -m "🚀 Initial 3D Profile Setup"
git push origin main
```

### Step 3: Enable GitHub Actions
1. Go to your repo → **Actions** tab
2. Click **"I understand my workflows, go ahead and enable them"**
3. Run each workflow manually first time:
   - Click on each workflow name
   - Click **"Run workflow"** button

### Step 4: Generate GitHub Token (For Private Repo Stats)
1. Go to Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click **Generate new token**
3. Select scopes: `repo`, `read:user`, `read:packages`
4. Copy the token
5. Go to your profile repo → Settings → Secrets and variables → Actions
6. Click **New repository secret**
7. Name: `GITHUB_TOKEN` (already exists by default, but if needed create `PAT_TOKEN`)
8. Paste your token

---

## 🎨 3D Features Included

| Feature | Tool/Service | Auto-Update |
|---------|-------------|-------------|
| 🌌 3D Contribution Graph | `github-profile-3d-contrib` | ✅ Daily |
| 🐍 Snake Animation | `Platane/snk` | ✅ Daily |
| 📊 GitHub Stats | `github-readme-stats` | ✅ Live |
| 🔥 Streak Stats | `streak-stats` | ✅ Live |
| 🏆 Trophies | `github-profile-trophy` | ✅ Live |
| 📦 Latest Repos | Custom Python Script | ✅ Daily |
| ⚡ Recent Activity | GitHub API | ✅ Daily |
| 🛠️ Skill Icons | `skillicons.dev` | ✅ Live |
| ✍️ Typing Animation | `readme-typing-svg` | ✅ Live |

---

## ⏰ Auto-Update Schedule

| Workflow | Cron | Time (PKT) |
|----------|------|-----------|
| Snake Animation | `0 2 * * *` | 7:00 AM |
| 3D Contribution Graph | `0 3 * * *` | 8:00 AM |
| README Auto-Update | `0 4 * * *` | 9:00 AM |

All workflows also support **manual trigger** via `workflow_dispatch`.

---

## 🛠️ Customization Tips

### Change Colors/Theme
Edit `README.md` and replace `theme=radical` with:
- `dark`, `radical`, `merko`, `gruvbox`, `tokyonight`, `onedark`, `cobalt`, `synthwave`, `highcontrast`, `dracula`

### Add More Projects
Edit `scripts/update_readme.py` → `project_mapping` dictionary to add your project descriptions.

### Change 3D Graph Style
Edit `.github/workflows/3d-contrib.yml` and change:
- `profile-night-rainbow.svg` → `profile-green-animate.svg`
- Other options: `profile-season-animate.svg`, `profile-night-view.svg`, `profile-gitblock.svg`

### Add WakaTime Stats
1. Sign up at [wakatime.com](https://wakatime.com)
2. Add this to README:
```markdown
<img src="https://github-readme-stats.vercel.app/api/wakatime?username=nasirbloch323&theme=radical&hide_border=true" />
```

---

## 🔥 Pro Tips

1. **Star your own repo** to get it trending!
2. **Pin your best 6 repos** on your GitHub profile for maximum visibility
3. **Update your GitHub bio** to match your README branding
4. **Enable GitHub Sponsors** if you want to receive donations
5. **Add a profile picture** that matches the DevOps theme

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| 3D graph not showing | Run the workflow manually first time |
| Snake not animating | Check if `output` branch exists after first run |
| Stats not loading | GitHub API rate limit - add a PAT token |
| Workflow failing | Check Actions logs for specific errors |
| Images broken | Ensure raw URLs are correct in README |

---

## 📞 Need Help?

- GitHub Profile README Docs: https://docs.github.com/en/account-and-profile
- 3D Contrib Repo: https://github.com/yoshi389111/github-profile-3d-contrib
- GitHub Readme Stats: https://github.com/anuraghazra/github-readme-stats

---

**Made with ❤️ for Nasir Mehmood | DevOps Engineer**
