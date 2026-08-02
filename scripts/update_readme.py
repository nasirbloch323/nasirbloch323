#!/usr/bin/env python3
"""
Auto-Update GitHub Profile README
"""

import os
import re
import sys
import requests
from datetime import datetime, timezone
from pathlib import Path

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "nasirbloch323")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
README_PATH = Path("README.md")

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "nasirbloch323-profile-updater"
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"


def fetch_github_api(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        if response.status_code == 403:
            print(f"Rate limited on {url}")
            return []
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []


def get_latest_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated&direction=desc&per_page=6"
    repos = fetch_github_api(url)
    
    if not repos:
        return ""
    
    repo_cards = []
    for repo in repos:
        name = repo.get("name", "")
        url = repo.get("html_url", "")
        
        repo_cards.append(
            f'<a href="{url}">\n'
            f'  <img src="https://github-readme-stats.vercel.app/api/pin/?'
            f'username={GITHUB_USERNAME}&repo={name}&theme=radical&hide_border=true&'
            f'bg_color=0D1117&title_color=00F0FF&icon_color=00F0FF" />\n'
            f'</a>'
        )
    
    return "\n".join(repo_cards)


def get_recent_activity():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/events/public?per_page=5"
    events = fetch_github_api(url)
    
    if not events:
        return "- No recent public activity to display"
    
    activity_lines = []
    for event in events:
        event_type = event.get("type", "")
        repo_name = event.get("repo", {}).get("name", "")
        
        if event_type == "PushEvent":
            msg = f"Pushed code to **{repo_name}**"
        elif event_type == "CreateEvent":
            msg = f"Created new repository **{repo_name}**"
        elif event_type == "ForkEvent":
            msg = f"Forked **{repo_name}**"
        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "")
            msg = f"{action.capitalize()} issue in **{repo_name}**"
        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action", "")
            msg = f"{action.capitalize()} PR in **{repo_name}**"
        elif event_type == "WatchEvent":
            msg = f"Starred **{repo_name}**"
        elif event_type == "ReleaseEvent":
            msg = f"Released new version in **{repo_name}**"
        else:
            msg = f"{event_type.replace('Event', '')} in **{repo_name}**"
        
        activity_lines.append(f"- {msg}")
    
    return "\n".join(activity_lines)


def get_featured_projects():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated&direction=desc&per_page=6"
    repos = fetch_github_api(url)
    
    if not repos:
        return "| Project | Tech Stack | Description |\n|---------|-----------|-------------|"
    
    project_mapping = {
        "flask-Todo-App-Helm": ("Full CI/CD with GitOps deployment", "Jenkins, Helm, ArgoCD, AWS EKS, Docker, Flask"),
        "jenkins-shared-lib": ("Reusable pipeline components", "Groovy, Jenkins, CI/CD"),
        "Kubernetes-Setup-on-AWS-EC2-KIND-": ("Local K8s cluster on cloud VMs", "Kubernetes, KIND, AWS EC2, Docker"),
        "100-days-of-code-python": ("Complete Python learning journey", "Python, Jupyter, ML"),
        "Recommendation-System": ("ML-based recommendation engine", "Python, ML, Data Science"),
        "Jenkins-installation-": ("Automated Jenkins setup scripts", "Shell, Jenkins, DevOps"),
        "AI-BankApp-DevOps": ("Containerized financial platform", "Docker, K8s, Spring Boot, Java 21"),
    }
    
    rows = []
    for repo in repos:
        name = repo.get("name", "")
        url = repo.get("html_url", "")
        
        if name in project_mapping:
            desc, tech = project_mapping[name]
        else:
            desc = repo.get("description") or "DevOps Project"
            tech = repo.get("language") or "DevOps"
        
        tech_badges = " ".join([f"`{t.strip()}`" for t in tech.split(",")])
        rows.append(f"| **[{name}]({url})** | {tech_badges} | {desc} |")
    
    header = "| Project | Tech Stack | Description |\n|---------|-----------|-------------|"
    return header + "\n" + "\n".join(rows)


def replace_section(content, start_marker, end_marker, new_content):
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        re.DOTALL,
    )
    replacement = start_marker + "\n" + new_content + "\n" + end_marker
    
    if pattern.search(content):
        return pattern.sub(replacement, content)
    else:
        print(f"Marker not found: {start_marker}")
        return content


def update_timestamp(content):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return replace_section(
        content,
        "<!-- LAST_UPDATED:START -->",
        "<!-- LAST_UPDATED:END -->",
        now
    )


def main():
    print("Starting README auto-update...")
    
    if not README_PATH.exists():
        print(f"README.md not found at {README_PATH.absolute()}!")
        sys.exit(1)
    
    content = README_PATH.read_text(encoding="utf-8")
    
    print("Fetching latest projects...")
    try:
        projects_content = get_featured_projects()
        content = replace_section(
            content,
            "<!-- PROJECTS:START -->",
            "<!-- PROJECTS:END -->",
            f'\n<div align="center">\n\n{projects_content}\n\n</div>\n'
        )
        print("Projects updated!")
    except Exception as e:
        print(f"Error updating projects: {e}")
    
    print("Fetching latest repo cards...")
    try:
        repos_content = get_latest_repos()
        content = replace_section(
            content,
            "<!-- REPOS:START -->",
            "<!-- REPOS:END -->",
            f'\n<div align="center">\n\n{repos_content}\n\n</div>\n'
        )
        print("Repo cards updated!")
    except Exception as e:
        print(f"Error updating repos: {e}")
    
    print("Fetching recent activity...")
    try:
        activity_content = get_recent_activity()
        content = replace_section(
            content,
            "<!-- ACTIVITY:START -->",
            "<!-- ACTIVITY:END -->",
            f'\n<div align="center">\n\n{activity_content}\n\n</div>\n'
        )
        print("Activity updated!")
    except Exception as e:
        print(f"Error updating activity: {e}")
    
    print("Updating timestamp...")
    content = update_timestamp(content)
    
    README_PATH.write_text(content, encoding="utf-8")
    print("README.md updated successfully!")


if __name__ == "__main__":
    main()
